"""Synthetic-only negative and branch controls; no DR-70 firmware or output."""

from __future__ import annotations

import copy
import unittest

from scripts.reconstruction_gate import evaluate


FAKE_FIRMWARE = {
    "evidence_id": "FAKE-ROM-1", "locator": "fake:test:offset-0",
    "sha256": "a" * 64, "custody_reviewed": True, "analysis_permitted": True,
}
FAKE_ARCHITECTURE = {
    "evidence_id": "FAKE-BOARD-1", "isa": "FAKE-ISA",
    "address_mapping": "FAKE mapping", "byte_order": "FAKE order",
    "peripheral_evidence_id": "FAKE-LED-1", "independently_corroborated": True,
}
FAKE_IO = {
    "id": "FAKE-IO-1", "evidence_id": "FAKE-PHOTO-1",
    "locator": "fake:frame:1", "input_literal": "FAKE INPUT",
    "keys_literal": "FAKE KEYS", "output_literal": "FAKE OUTPUT",
    "directness": "device_observation", "source_reviewed": True,
    "synthetic": False,
}


class ReconstructionTriageTests(unittest.TestCase):
    def test_no_evidence_is_documentation(self) -> None:
        self.assertEqual(evaluate({})["track"], "C_DOCUMENTATION")

    def test_missing_cpu_is_not_emulator(self) -> None:
        self.assertEqual(evaluate({"firmware": FAKE_FIRMWARE})["track"], "C_DOCUMENTATION")

    def test_missing_rom_is_not_emulator(self) -> None:
        self.assertEqual(evaluate({"architecture": FAKE_ARCHITECTURE})["track"], "C_DOCUMENTATION")

    def test_uncorroborated_isa_not_accepted(self) -> None:
        a = copy.deepcopy(FAKE_ARCHITECTURE)
        a["independently_corroborated"] = False
        self.assertEqual(evaluate({"firmware": FAKE_FIRMWARE, "architecture": a})["track"], "C_DOCUMENTATION")

    def test_wrong_hash_not_accepted(self) -> None:
        f = {**FAKE_FIRMWARE, "sha256": "not-a-hash"}
        self.assertEqual(evaluate({"firmware": f, "architecture": FAKE_ARCHITECTURE})["track"], "C_DOCUMENTATION")

    def test_rights_not_cleared_not_accepted(self) -> None:
        f = {**FAKE_FIRMWARE, "analysis_permitted": False}
        self.assertEqual(evaluate({"firmware": f, "architecture": FAKE_ARCHITECTURE})["track"], "C_DOCUMENTATION")

    def test_full_synthetic_metadata_only_suggests_study(self) -> None:
        a = evaluate({"firmware": FAKE_FIRMWARE, "architecture": FAKE_ARCHITECTURE})
        self.assertEqual(a["track"], "A_INSTRUCTION_STUDY")
        self.assertFalse(a["approved_for_emulation"])
        self.assertFalse(a["approved_as_authentic_dr70"])

    def test_observed_io_suggests_behavior_study_only(self) -> None:
        a = evaluate({"observations": [FAKE_IO]})
        self.assertEqual(a["track"], "B_BEHAVIOR_STUDY")
        self.assertFalse(a["approved_for_emulation"])

    def test_software_generated_output_is_not_observation(self) -> None:
        x = {**FAKE_IO, "synthetic": True}
        self.assertEqual(evaluate({"observations": [x]})["track"], "C_DOCUMENTATION")

    def test_secondary_retelling_not_observation(self) -> None:
        x = {**FAKE_IO, "directness": "secondary_report"}
        self.assertEqual(evaluate({"observations": [x]})["track"], "C_DOCUMENTATION")

    def test_unhashable_directness_is_not_observation(self) -> None:
        for malformed in (["device_observation"], {"value": "device_observation"}):
            with self.subTest(directness=malformed):
                x = {**FAKE_IO, "directness": malformed}
                self.assertEqual(evaluate({"observations": [x]})["track"], "C_DOCUMENTATION")

    def test_unreviewed_output_not_observation(self) -> None:
        x = {**FAKE_IO, "source_reviewed": False}
        self.assertEqual(evaluate({"observations": [x]})["track"], "C_DOCUMENTATION")

    def test_missing_keys_not_replayable(self) -> None:
        x = {**FAKE_IO, "keys_literal": ""}
        self.assertEqual(evaluate({"observations": [x]})["track"], "C_DOCUMENTATION")

    def test_no_approval_even_when_both_paths_have_metadata(self) -> None:
        a = evaluate({"firmware": FAKE_FIRMWARE, "architecture": FAKE_ARCHITECTURE, "observations": [FAKE_IO]})
        self.assertEqual(a["track"], "A_INSTRUCTION_STUDY")
        self.assertFalse(a["approved_as_authentic_dr70"])

    def test_nonlist_observations_is_error(self) -> None:
        with self.assertRaisesRegex(ValueError, "observations must be a list"):
            evaluate({"observations": {}})

    def test_nonobject_input_is_error(self) -> None:
        with self.assertRaisesRegex(ValueError, "JSON object"):
            evaluate([])


if __name__ == "__main__":
    unittest.main()
