"""Minimal Moira constants adapter for the vendored _angles.py module.

Adapted from TheDaniel166/moira/moira/constants.py at
1bb9f66cde48f91cb13ebc5a715dec030d592b44 (MIT).
Only units consumed by _angles.py are retained. Original Moira package is
not imported or executed; this is an intentionally narrow research adapter.
"""

import math

DEG2RAD = math.pi / 180.0
RAD2DEG = 180.0 / math.pi
