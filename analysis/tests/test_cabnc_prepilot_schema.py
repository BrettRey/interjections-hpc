from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path


ANALYSIS_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ANALYSIS_DIR))

from validate_cabnc_prepilot_schema import validate  # noqa: E402


class CabncPrepilotSchemaTests(unittest.TestCase):
    def test_current_schema_validates(self) -> None:
        result = validate(ANALYSIS_DIR / "cabnc-prepilot")
        self.assertGreaterEqual(result["n_templates"], 25)
        self.assertGreaterEqual(result["n_leakage_checks"], 15)

    def test_missing_required_field_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = Path(temporary) / "cabnc-prepilot"
            shutil.copytree(ANALYSIS_DIR / "cabnc-prepilot", copied)
            source = copied / "post-offset-trajectory-template.csv"
            fields = source.read_text(encoding="utf-8").strip().split(",")
            fields.remove("timing_source")
            source.write_text(",".join(fields) + "\n", encoding="utf-8")
            with self.assertRaises(SystemExit):
                validate(copied)

    def test_coder_entered_trajectory_is_not_required(self) -> None:
        fields = (
            ANALYSIS_DIR
            / "cabnc-prepilot"
            / "post-offset-trajectory-template.csv"
        ).read_text(encoding="utf-8").strip().split(",")
        self.assertNotIn("post_offset_trajectory", fields)

        derived_fields = (
            ANALYSIS_DIR
            / "cabnc-prepilot"
            / "derived-outcomes-template.csv"
        ).read_text(encoding="utf-8").strip().split(",")
        self.assertIn("post_offset_trajectory", derived_fields)


if __name__ == "__main__":
    unittest.main()
