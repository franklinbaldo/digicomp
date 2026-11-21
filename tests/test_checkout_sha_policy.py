"""Regression guard for literal commit checkouts in DR-70 public workflows.

This validates checkout identity and control placement, not instrument fidelity.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ("validate.yml", "chart-candidates.yml")
EXPRESSION = "$" + "{{ github.event.pull_request.head.sha || github.sha }}"


def _steps(source: str) -> list[str]:
    # Both guarded workflows currently have one job with 6-space step markers.
    return ["      - " + part for part in re.split(r"(?m)^      - ", source)[1:]]


def check_workflow(source: str) -> None:
    steps = _steps(source)
    checkouts = [
        i for i, step in enumerate(steps)
        if re.search(r"(?m)^(?:      - |        )uses: actions/checkout@v4\s*$", step)
    ]
    if len(checkouts) != 1:
        raise AssertionError("expected exactly one checkout step")
    i = checkouts[0]
    checkout = steps[i]
    expected_ref = re.escape(EXPRESSION)
    if not re.search(r"(?m)^\s+ref: " + expected_ref + r"\s*$", checkout):
        raise AssertionError("checkout lacks literal PR HEAD/main ref")
    if not re.search(r"(?m)^\s+persist-credentials: false\s*$", checkout):
        raise AssertionError("checkout persists credentials")
    if i + 1 >= len(steps):
        raise AssertionError("missing immediate checkout verification")
    verify = steps[i + 1]
    if not re.search(r"(?m)^\s+EXPECTED_SHA: " + expected_ref + r"\s*$", verify):
        raise AssertionError("verification does not use the same SHA expression")
    if not re.search(
        r'(?m)^\s+run: test "\$\(git rev-parse HEAD\)" = "\$EXPECTED_SHA"\s*$',
        verify,
    ):
        raise AssertionError("verification does not compare the checked-out HEAD")


class LiteralCheckoutPolicyTests(unittest.TestCase):
    def test_workflows_are_protected(self):
        for name in WORKFLOWS:
            with self.subTest(name=name):
                check_workflow((ROOT / ".github" / "workflows" / name).read_text())

    def test_negative_mutations_fail_closed(self):
        for name in WORKFLOWS:
            original = (ROOT / ".github" / "workflows" / name).read_text()
            check_workflow(original)
            mutants = {
                "remove ref": original.replace(f"          ref: {EXPRESSION}\n", ""),
                "wrong ref": original.replace(f"          ref: {EXPRESSION}", "          ref: main"),
                "remove credential gate": original.replace("          persist-credentials: false\n", ""),
                "remove comparison": original.replace(
                    '        run: test "$(git rev-parse HEAD)" = "$EXPECTED_SHA"\n', ""
                ),
                "mismatched expectation": original.replace(
                    f"          EXPECTED_SHA: {EXPRESSION}",
                    "          EXPECTED_SHA: $" + "{{ github.sha }}",
                ),
                "verification after work": original.replace(
                    "      - name: Verify exact", "      - name: Do work first\n"
                    "        run: echo work\n      - name: Verify exact",
                ),
            }
            for label, mutant in mutants.items():
                self.assertNotEqual(mutant, original, (name, label))
                with self.subTest(name=name, mutation=label):
                    with self.assertRaises(AssertionError):
                        check_workflow(mutant)


if __name__ == "__main__":
    unittest.main()
