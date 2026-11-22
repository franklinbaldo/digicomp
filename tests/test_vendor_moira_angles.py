"""Tests for the isolated MIT-licensed Moira ascendant research reference.

These tests compare mathematical invariants only. They are NOT DR-70 fidelity
tests, and they use no historical DR-70 input/output observations.
"""

import math
import unittest

from vendor.moira._angles import _asc_from_armc, _sin_hour_angle
from vendor.moira.constants import DEG2RAD


class VendoredMoiraAscendantTests(unittest.TestCase):
    def test_simple_zero_obliquity_equator(self):
        # With ecliptic and celestial equator coincident, rising longitude
        # leads ARMC by 90 degrees.
        for armc, expected in [(0.0, 90.0), (90.0, 180.0),
                               (180.0, 270.0), (270.0, 0.0)]:
            with self.subTest(armc=armc):
                self.assertAlmostEqual(
                    _asc_from_armc(armc, 0.0, 0.0), expected, places=9
                )

    def test_longitudes_are_finite_normalized(self):
        for armc in (0.0, 5.0, 90.0, 180.0, 270.0, 359.9999):
            for latitude in (-89.0, -45.0, 0.0, 40.0, 89.0):
                result = _asc_from_armc(armc, 23.44, latitude)
                with self.subTest(armc=armc, latitude=latitude):
                    self.assertTrue(math.isfinite(result))
                    self.assertGreaterEqual(result, 0.0)
                    self.assertLess(result, 360.0)

    def test_rising_branch_for_nonpolar_cases(self):
        # The selected root must be on the rising branch, not setting.
        for armc, latitude in ((0.0, 40.0), (34.0, -30.0),
                               (95.0, 10.0), (220.0, -45.0)):
            result = _asc_from_armc(armc, 23.44, latitude)
            with self.subTest(armc=armc, latitude=latitude):
                self.assertLess(
                    _sin_hour_angle(result, armc * DEG2RAD, 23.44 * DEG2RAD),
                    0.0,
                )

    def test_repeatable_without_external_ephemeris(self):
        a = _asc_from_armc(37.25, 23.43928, -8.761)
        b = _asc_from_armc(37.25, 23.43928, -8.761)
        self.assertEqual(a, b)

    def test_polar_tie_is_numerical_not_physical(self):
        for latitude in (-90.0, 90.0):
            x = _asc_from_armc(113.0, 23.44, latitude)
            self.assertTrue(math.isfinite(x))
            self.assertGreaterEqual(x, 0.0)
            self.assertLess(x, 360.0)


if __name__ == "__main__":
    unittest.main()
