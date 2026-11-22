"""Independent invariants for Moira MIT geometry and UT1/TT reference modules.

Synthetic numeric tests only. NOT Digicomp DR-70 instrumental evidence.
"""
import math
import unittest

from vendor.moira._house_quality import (
    house_cycle_verdict,
    house_distortion_profile,
    stable_true_flags,
    strictly_ordered_cusp_cycle,
)
from vendor.moira.coordinates_reference import (
    angular_distance,
    signed_angular_distance,
    ecliptic_to_equatorial,
    equatorial_to_ecliptic,
    equatorial_to_horizontal,
    equatorial_to_horizontal_with_truth,
    normalize_degrees,
)
from vendor.moira.sidereal_time_reference import (
    earth_rotation_angle,
    greenwich_mean_sidereal_time,
    local_mean_sidereal_time,
)

J2000 = 2451545.0


class HouseQualityTests(unittest.TestCase):
    def test_equal_12_houses(self):
        cusps = tuple((15 + 30 * i) % 360 for i in range(12))
        self.assertTrue(strictly_ordered_cusp_cycle(cusps))
        verdict, profile = house_cycle_verdict(cusps, rho_max=7)
        self.assertEqual(verdict, "practically_admissible")
        self.assertIsNotNone(profile)
        self.assertAlmostEqual(profile.distortion_ratio, 1.0)
        self.assertEqual(profile.widths, (30.0,) * 12)

    def test_unordered_and_duplicate_cusps(self):
        original = tuple((15 + 30 * i) % 360 for i in range(12))
        self.assertFalse(strictly_ordered_cusp_cycle(original[::-1]))
        self.assertEqual(house_cycle_verdict(original[::-1], rho_max=7),
                         ("unordered", None))
        cusps = list(original)
        cusps[1] = cusps[0]
        self.assertFalse(strictly_ordered_cusp_cycle(cusps))

    def test_uneven_but_ordered(self):
        widths = [10.0] + [350.0 / 11.0] * 11
        cusps = [0.0]
        for width in widths[:-1]:
            cusps.append(cusps[-1] + width)
        verdict, profile = house_cycle_verdict(cusps, rho_max=2)
        self.assertEqual(verdict, "ordered_but_impractical")
        self.assertGreater(profile.distortion_ratio, 3)
        self.assertAlmostEqual(sum(profile.widths), 360, places=7)

    def test_invalid_length_or_rho(self):
        with self.assertRaises(ValueError):
            strictly_ordered_cusp_cycle((0, 30))
        with self.assertRaises(ValueError):
            house_distortion_profile((0, 30))
        with self.assertRaises(ValueError):
            house_cycle_verdict(tuple(range(12)), rho_max=0.5)

    def test_stability_neighborhood(self):
        self.assertEqual(
            stable_true_flags([True] * 7, radius=2),
            (False, False, True, True, True, False, False),
        )
        with self.assertRaises(ValueError):
            stable_true_flags([True] * 7, radius=-1)


class CoordinateTests(unittest.TestCase):
    def test_wrap_and_circular_difference(self):
        self.assertEqual(normalize_degrees(-1e-15), 0.0)
        self.assertEqual(normalize_degrees(360.0), 0.0)
        self.assertEqual(angular_distance(350, 10), 20)
        self.assertEqual(signed_angular_distance(350, 10), 20)
        self.assertEqual(signed_angular_distance(10, 350), -20)
        self.assertEqual(signed_angular_distance(0, 180), 180)

    def test_ecliptic_equatorial_cardinal(self):
        ra, dec = ecliptic_to_equatorial(90, 0, 23.4392911)
        self.assertAlmostEqual(ra, 90, places=9)
        self.assertAlmostEqual(dec, 23.4392911, places=8)
        lon, lat = equatorial_to_ecliptic(ra, dec, 23.4392911)
        self.assertAlmostEqual(lon, 90, places=8)
        self.assertAlmostEqual(lat, 0, places=8)

    def test_ecliptic_equatorial_roundtrip_off_axis(self):
        for lon, lat in ((5, 12), (123, -35), (265, 45)):
            ra, dec = ecliptic_to_equatorial(lon, lat, 23.44)
            new_lon, new_lat = equatorial_to_ecliptic(ra, dec, 23.44)
            with self.subTest(lon=lon, lat=lat):
                self.assertAlmostEqual(
                    signed_angular_distance(lon, new_lon), 0, places=7
                )
                self.assertAlmostEqual(new_lat, lat, places=7)

    def test_horizon_east_and_west(self):
        west_az, west_alt = equatorial_to_horizontal(0, 0, 90, 0)
        east_az, east_alt = equatorial_to_horizontal(0, 0, 270, 0)
        self.assertAlmostEqual(west_az, 270, places=8)
        self.assertAlmostEqual(east_az, 90, places=8)
        self.assertAlmostEqual(west_alt, 0, places=8)
        self.assertAlmostEqual(east_alt, 0, places=8)

    def test_zenith_azimuth_undefined(self):
        truth = equatorial_to_horizontal_with_truth(0, 0, 0, 0)
        self.assertFalse(truth.azimuth_defined)
        self.assertAlmostEqual(truth.altitude_deg, 90, places=8)

    def test_reject_invalid_declination(self):
        with self.assertRaises(ValueError):
            equatorial_to_horizontal(0, 95, 0, 0)
        with self.assertRaises(ValueError):
            ecliptic_to_equatorial(0, float("nan"), 23.4)


class ClockTests(unittest.TestCase):
    def test_era_and_gmst_j2000_numeric_reference(self):
        # IAU 2000 ERA / IAU 2006 GMST with UT1=TT at this synthetic instant.
        self.assertAlmostEqual(earth_rotation_angle(J2000), 280.46061837504, places=8)
        self.assertAlmostEqual(
            greenwich_mean_sidereal_time(J2000, J2000),
            280.4606224044844, places=8,
        )

    def test_clock_longitude_offset_and_wrap(self):
        gmst = greenwich_mean_sidereal_time(J2000, J2000)
        self.assertAlmostEqual(local_mean_sidereal_time(J2000, J2000, 0), gmst)
        self.assertAlmostEqual(
            local_mean_sidereal_time(J2000, J2000, 90),
            (gmst + 90) % 360,
        )
        self.assertAlmostEqual(
            local_mean_sidereal_time(J2000, J2000, -90),
            (gmst - 90) % 360,
        )

    def test_ut1_tt_not_conflated(self):
        first = greenwich_mean_sidereal_time(J2000, J2000)
        second = greenwich_mean_sidereal_time(J2000, J2000 + 10)
        self.assertNotEqual(first, second)

    def test_no_implicit_clock_or_nutation(self):
        with self.assertRaises(TypeError):
            greenwich_mean_sidereal_time(J2000)
        with self.assertRaises(ValueError):
            greenwich_mean_sidereal_time(J2000, float("nan"))
        with self.assertRaises(ValueError):
            local_mean_sidereal_time(J2000, J2000, float("inf"))
        with self.assertRaises(ValueError):
            local_mean_sidereal_time(J2000, J2000, 1000)


if __name__ == "__main__":
    unittest.main()
