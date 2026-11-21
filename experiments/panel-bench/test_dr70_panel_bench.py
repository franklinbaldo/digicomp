"""Standalone tests for the experimental panel, no hardware fidelity asserted."""

import unittest

from dr70_panel_bench import Panel


class PanelTest(unittest.TestCase):
    def test_starts_off_without_fake_output(self):
        self.assertFalse(Panel().power_on)
        self.assertIsNone(Panel().snapshot()["observed_dr70_output"])

    def test_power_switch(self):
        panel = Panel()
        panel.apply("power", "on")
        self.assertTrue(panel.power_on)
        panel.apply("power", "off")
        self.assertFalse(panel.power_on)

    def test_latching_shift(self):
        panel = Panel()
        panel.apply("power", "on")
        panel.apply("shift")
        self.assertTrue(panel.shift_latched)
        self.assertTrue(panel.shift_lamp)
        panel.apply("shift")
        self.assertFalse(panel.shift_latched)
        self.assertFalse(panel.shift_lamp)

    def test_lamp_assumption_is_explicit(self):
        panel = Panel()
        panel.apply("shift")
        self.assertTrue(panel.shift_latched)
        self.assertFalse(panel.shift_lamp)
        self.assertIn("shift_lamp_hypothesis", panel.snapshot())

    def test_key_is_recorded_without_invented_behavior(self):
        panel = Panel()
        panel.apply("key", "UNKNOWN_KEY_1")
        self.assertIsNone(panel.snapshot()["observed_dr70_output"])
        self.assertEqual(panel.events[0]["value"], "UNKNOWN_KEY_1")

    def test_deterministic_replay(self):
        panel = Panel()
        for action, value in [("power", "on"), ("shift", ""), ("key", "x"), ("power", "off")]:
            panel.apply(action, value)
        self.assertEqual(Panel.replay(panel.events).snapshot(), panel.snapshot())

    def test_invalid_key_does_not_modify_state(self):
        panel = Panel()
        before = panel.snapshot()
        with self.assertRaises(ValueError):
            panel.apply("key", "\x00")
        self.assertEqual(panel.snapshot(), before)

    def test_invalid_power_does_not_modify_state(self):
        panel = Panel()
        with self.assertRaises(ValueError):
            panel.apply("power", "maybe")
        self.assertEqual(panel.events, [])

    def test_replay_rejects_extra_fields(self):
        with self.assertRaises(ValueError):
            Panel.replay([{"action": "key", "value": "a", "guessed_output": "42"}])

    def test_replay_rejects_non_string_fields(self):
        with self.assertRaises(ValueError):
            Panel.replay([{"action": "key", "value": 12}])

    def test_snapshot_is_detached_from_event_history(self):
        panel = Panel()
        panel.apply("power", "on")
        panel.apply("key", "V")
        exported = panel.snapshot()
        exported["events"][0]["value"] = "off"
        exported["events"].append({"action": "key", "value": "FORGED"})
        exported["sources"].clear()
        self.assertTrue(panel.power_on)
        self.assertEqual(panel.events, [
            {"action": "power", "value": "on"},
            {"action": "key", "value": "V"},
        ])
        self.assertEqual(len(panel.snapshot()["sources"]), 2)

    def test_replay_rejects_non_mapping_event(self):
        with self.assertRaises(ValueError):
            Panel.replay([None])
        with self.assertRaises(ValueError):
            Panel.replay(["key"])

    def test_direct_key_type_rejected_without_event(self):
        panel = Panel()
        with self.assertRaises(ValueError):
            panel.apply("key", 12)
        self.assertEqual(panel.events, [])

    def test_replay_detaches_input_event_dicts(self):
        input_events = [{"action": "power", "value": "on"}]
        replayed = Panel.replay(input_events)
        input_events[0]["value"] = "off"
        self.assertTrue(replayed.power_on)
        self.assertEqual(replayed.events[0]["value"], "on")

    def test_event_cannot_have_unrecognized_action(self):
        panel = Panel()
        with self.assertRaises(ValueError):
            panel.apply("compute", "natal")
        self.assertEqual(panel.events, [])


if __name__ == "__main__":
    unittest.main()
