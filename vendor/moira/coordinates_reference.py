"""Moira coordinate transforms, vendored as a deliberately narrowed source extract.

Original: https://github.com/TheDaniel166/moira/blob/1bb9f66cde48f91cb13ebc5a715dec030d592b44/moira/coordinates.py
Original Git blob: 45d1665c089547d87acfef1188bea059e9e2efac
Copyright 2026 TheDaniel166; MIT license at vendor/moira/LICENSE.

Selected definitions below are unmodified excerpts; file imports, module surface
and dependencies are narrowed. This module provides a comparison/reference
implementation, never observed Digicomp DR-70 behaviour.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from .constants import DEG2RAD, RAD2DEG

@dataclass(frozen=True, slots=True)


@dataclass(frozen=True, slots=True)


def _clamp_unit(x: float) -> float:
    """Clamp to the closed unit interval [-1, +1] for inverse trig safety."""
    return max(-1.0, min(1.0, x))


def _require_finite_coordinate(name: str, value: float) -> float:
    """Return one finite coordinate value or fail before trigonometry."""

    result = float(value)
    if not math.isfinite(result):
        raise ValueError(f"{name} must be finite, got {value!r}")
    return result


def _require_latitude(name: str, value: float) -> float:
    """Return one physical latitude/declination in the closed degree domain."""

    result = _require_finite_coordinate(name, value)
    if not -90.0 <= result <= 90.0:
        raise ValueError(f"{name} must be within [-90, 90] degrees, got {value!r}")
    return result


def normalize_degrees(angle: float) -> float:
    """Reduce an angle to [0, 360)."""
    result = angle % 360.0
    # IEEE 754: a tiny negative value added to 360.0 may not underflow the
    # representable floor, leaving result == 360.0.  Clamp it back to 0.
    return 0.0 if result >= 360.0 else result


def angular_distance(a: float, b: float) -> float:
    """Shortest unsigned arc between two longitudes (0–180°).

    Reduce the magnitude of the difference before folding at 180 degrees.
    A negative remainder would first add 360 and then subtract it again,
    introducing avoidable rounding at closed aspect-orb boundaries.
    """
    diff = abs(a - b) % 360.0
    return diff if diff <= 180.0 else 360.0 - diff


def signed_angular_distance(from_deg: float, to_deg: float) -> float:
    """Signed difference to_deg − from_deg in (−180, +180]."""
    diff = (to_deg - from_deg) % 360.0
    if diff > 180.0:
        diff -= 360.0
    return diff


def equatorial_to_horizontal(
    ra_deg: float,
    dec_deg: float,
    lst_deg: float,
    lat_deg: float,
) -> tuple[float, float]:
    """
    Convert equatorial (RA, Dec) to horizontal (Azimuth, Altitude).

    Parameters
    ----------
    ra_deg  : Right Ascension in degrees
    dec_deg : Declination in degrees
    lst_deg : Local Sidereal Time in degrees
    lat_deg : Geographic latitude in degrees (north positive)

    Returns
    -------
    (azimuth, altitude) in degrees
    Azimuth is measured from North, clockwise (0=N, 90=E, 180=S, 270=W).
    """
    truth = equatorial_to_horizontal_with_truth(
        ra_deg,
        dec_deg,
        lst_deg,
        lat_deg,
    )
    return truth.azimuth_deg, truth.altitude_deg


def equatorial_to_horizontal_with_truth(
    ra_deg: float,
    dec_deg: float,
    lst_deg: float,
    lat_deg: float,
) -> HorizontalCoordinatesTruth:
    """Convert equatorial coordinates and disclose singular azimuth geometry."""

    ra_deg = _require_finite_coordinate("ra_deg", ra_deg)
    dec_deg = _require_latitude("dec_deg", dec_deg)
    lst_deg = _require_finite_coordinate("lst_deg", lst_deg)
    lat_deg = _require_latitude("lat_deg", lat_deg)

    ha = (lst_deg - ra_deg) % 360.0   # Hour Angle
    ha_r  = ha  * DEG2RAD
    dec_r = dec_deg * DEG2RAD
    lat_r = lat_deg * DEG2RAD

    sin_alt = (math.sin(dec_r) * math.sin(lat_r)
               + math.cos(dec_r) * math.cos(lat_r) * math.cos(ha_r))
    alt = math.asin(max(-1.0, min(1.0, sin_alt))) * RAD2DEG

    # Resolve the singularity from the horizontal projection itself.  Testing
    # ``cos(alt)`` after ``asin`` is too noisy near an exact zenith and can
    # manufacture a plausible-looking azimuth for a direction that has none.
    east = -math.cos(dec_r) * math.sin(ha_r)
    north = (
        math.sin(dec_r) * math.cos(lat_r)
        - math.cos(dec_r) * math.sin(lat_r) * math.cos(ha_r)
    )
    horizontal_norm = math.hypot(east, north)
    if abs(math.cos(lat_r)) < 1e-12 or horizontal_norm < 1e-12:
        # Object is at the zenith or the observer is at a geographic pole.
        # Azimuth is undefined; return 0.0 by convention.
        return HorizontalCoordinatesTruth(
            right_ascension_deg=ra_deg,
            declination_deg=dec_deg,
            local_sidereal_time_deg=lst_deg,
            observer_latitude_deg=lat_deg,
            hour_angle_deg=ha,
            azimuth_deg=0.0,
            altitude_deg=alt,
            azimuth_defined=False,
        )
    denom_az = math.cos(lat_r) * math.cos(alt * DEG2RAD)
    cos_az = (math.sin(dec_r) - math.sin(lat_r) * sin_alt) / denom_az
    # clamp for numerical safety
    cos_az = max(-1.0, min(1.0, cos_az))
    az = math.acos(cos_az) * RAD2DEG

    if math.sin(ha_r) > 0:
        az = 360.0 - az

    return HorizontalCoordinatesTruth(
        right_ascension_deg=ra_deg,
        declination_deg=dec_deg,
        local_sidereal_time_deg=lst_deg,
        observer_latitude_deg=lat_deg,
        hour_angle_deg=ha,
        azimuth_deg=az,
        altitude_deg=alt,
        azimuth_defined=True,
    )


def ecliptic_to_equatorial(
    lon_deg: float,
    lat_deg: float,
    obliquity_deg: float,
) -> tuple[float, float]:
    """
    Convert ecliptic longitude/latitude to equatorial RA/Dec.

    Returns
    -------
    (right_ascension, declination) in degrees
    """
    truth = ecliptic_to_equatorial_with_truth(lon_deg, lat_deg, obliquity_deg)
    return truth.right_ascension_deg, truth.declination_deg


def ecliptic_to_equatorial_with_truth(
    lon_deg: float,
    lat_deg: float,
    obliquity_deg: float,
) -> EquatorialCoordinatesTruth:
    """Convert ecliptic coordinates with explicit input and frame truth."""

    lon_deg = _require_finite_coordinate("lon_deg", lon_deg)
    lat_deg = _require_latitude("lat_deg", lat_deg)
    obliquity_deg = _require_finite_coordinate("obliquity_deg", obliquity_deg)

    eps = obliquity_deg * DEG2RAD
    lon = lon_deg * DEG2RAD
    lat = lat_deg * DEG2RAD

    sin_dec = (math.sin(lat) * math.cos(eps)
               + math.cos(lat) * math.sin(eps) * math.sin(lon))
    dec = math.asin(max(-1.0, min(1.0, sin_dec))) * RAD2DEG

    y = math.sin(lon) * math.cos(eps) - math.tan(lat) * math.sin(eps)
    x = math.cos(lon)
    ra = normalize_degrees(math.atan2(y, x) * RAD2DEG)

    return EquatorialCoordinatesTruth(
        ecliptic_longitude_deg=lon_deg,
        ecliptic_latitude_deg=lat_deg,
        obliquity_deg=obliquity_deg,
        right_ascension_deg=ra,
        declination_deg=dec,
    )


def equatorial_to_ecliptic(
    ra_deg: float,
    dec_deg: float,
    obliquity_deg: float,
) -> tuple[float, float]:
    """
    Convert equatorial RA/Dec to ecliptic longitude/latitude.

    Returns
    -------
    (longitude, latitude) in degrees
    """
    eps = obliquity_deg * DEG2RAD
    ra  = ra_deg  * DEG2RAD
    dec = dec_deg * DEG2RAD

    sin_lat = (math.sin(dec) * math.cos(eps)
               - math.cos(dec) * math.sin(eps) * math.sin(ra))
    lat = math.asin(max(-1.0, min(1.0, sin_lat))) * RAD2DEG

    y = math.sin(ra) * math.cos(eps) + math.tan(dec) * math.sin(eps)
    x = math.cos(ra)
    lon = normalize_degrees(math.atan2(y, x) * RAD2DEG)

    return lon, lat
