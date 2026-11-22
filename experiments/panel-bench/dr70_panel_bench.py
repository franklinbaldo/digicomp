"""Experimental DR-70 front-panel event recorder, not a DR-70 emulator.

Only the existence of a key switch, an illuminated latching shift key and an
LED-labelled display is reported in the cited sources. All implemented state
transitions are experimental test-harness conventions, not recovered firmware.

Sources:
- https://www.calcuseum.com/scrapbook/BONUS/10925/1.htm (DR-70 L606)
- https://deskthority.net/viewtopic.php?t=20346 (owner's keyboard report)
"""

from __future__ import annotations

from dataclasses import dataclass, field
import json
import sys
from typing import Literal

SOURCE_CALCUSEUM = "F1-L606"
SOURCE_DESKTHORITY = "F2-OWNER-REPORT"


@dataclass
class Panel:
    power_on: bool = False
    shift_latched: bool = False
    events: list[dict[str, object]] = field(default_factory=list)

    @property
    def shift_lamp(self) -> bool:
        """Hypothesis: latch lamp is lit only when power and latch are active."""
        return self.power_on and self.shift_latched

    def apply(self, action: Literal["power", "shift", "key"], value: str = "") -> None:
        if not isinstance(action, str) or not isinstance(value, str):
            raise ValueError("action and value must be strings")
        if action == "power":
            if value not in ("on", "off"):
                raise ValueError("power requires on/off")
            self.power_on = value == "on"
        elif action == "shift":
            if value:
                raise ValueError("shift takes no value")
            self.shift_latched = not self.shift_latched
        elif action == "key":
            if not value or not value.isprintable() or len(value) > 64:
                raise ValueError("key label must contain 1..64 printable characters")
            # The electrical effect and calculator semantics of this key are unknown.
        else:
            raise ValueError(f"unknown action: {action}")
        self.events.append({"action": action, "value": value})

    @classmethod
    def replay(cls, events: list[dict[str, object]]) -> "Panel":
        panel = cls()
        for item in events:
            if not isinstance(item, dict) or set(item) != {"action", "value"}:
                raise ValueError("unsupported event fields")
            action, value = item["action"], item["value"]
            if not isinstance(action, str) or not isinstance(value, str):
                raise ValueError("event fields must be strings")
            panel.apply(action, value)  # type: ignore[arg-type]
        return panel

    def snapshot(self) -> dict[str, object]:
        """Export a detached view, not a mutable reference to the live event log."""
        return {
            "kind": "EXPERIMENTAL_PANEL_NOT_ORIGINAL_DR70",
            "power_on": self.power_on,
            "shift_latched": self.shift_latched,
            "shift_lamp_hypothesis": self.shift_lamp,
            "observed_dr70_output": None,
            "events": [item.copy() for item in self.events],
            "sources": [SOURCE_CALCUSEUM, SOURCE_DESKTHORITY],
        }


def run_cli() -> None:
    panel = Panel()
    print("DR-70 experimental panel recorder (NOT firmware, no astrology calculations)")
    print("Commands: power on | power off | shift | key LABEL | status | quit")
    for line in sys.stdin:
        command = line.strip()
        if command == "quit":
            break
        if command == "status":
            print(json.dumps(panel.snapshot(), ensure_ascii=False, sort_keys=True))
            continue
        words = command.split(maxsplit=1)
        if not words:
            continue
        try:
            panel.apply(words[0], words[1] if len(words) == 2 else "")  # type: ignore[arg-type]
            print(json.dumps(panel.snapshot(), ensure_ascii=False, sort_keys=True))
        except ValueError as exc:
            print(f"INVALID: {exc}")


if __name__ == "__main__":
    run_cli()
