from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path


ANALYSIS_DIR = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ANALYSIS_DIR / "cabnc-prepilot"
sys.path.insert(0, str(ANALYSIS_DIR))

from validate_cabnc_prepilot_schema import validate  # noqa: E402


class CabncPrepilotSchemaTests(unittest.TestCase):
    def copied_schema(self, temporary: str) -> Path:
        copied = Path(temporary) / "cabnc-prepilot"
        shutil.copytree(SCHEMA_DIR, copied)
        return copied

    def test_current_schema_validates(self) -> None:
        result = validate(SCHEMA_DIR)
        self.assertEqual(result["n_templates"], 45)
        self.assertEqual(result["n_leakage_checks"], 47)
        self.assertEqual(result["n_model_families"], 3)
        self.assertEqual(result["n_annotation_routes"], 15)
        self.assertEqual(result["n_model_arms"], 9)
        self.assertEqual(result["n_predictive_contrasts"], 5)
        self.assertEqual(result["n_projective_declarations"], 2)
        self.assertEqual(result["n_decision_rules"], 6)
        self.assertEqual(result["n_reliability_gates"], 29)
        self.assertEqual(result["n_feasibility_gates"], 14)
        self.assertEqual(result["n_sampling_rules"], 18)

    def test_required_boundary_field_is_enforced(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copied_schema(temporary)
            template = copied / "post-offset-trajectory-template.csv"
            fields = template.read_text(encoding="utf-8").strip().split(",")
            fields.remove("first_vocal_source")
            template.write_text(",".join(fields) + "\n", encoding="utf-8")
            with self.assertRaises(SystemExit):
                validate(copied)

    def test_subjective_outcome_fields_and_human_staffing_templates_are_removed(self) -> None:
        post_fields = (SCHEMA_DIR / "post-offset-trajectory-template.csv").read_text(
            encoding="utf-8"
        ).strip().split(",")
        derived_fields = (SCHEMA_DIR / "derived-outcomes-template.csv").read_text(
            encoding="utf-8"
        ).strip().split(",")
        self.assertNotIn("first_entry_minimality", post_fields)
        self.assertNotIn("fitted_judgement", post_fields)
        self.assertNotIn("fittedness_sensitivity_outcome", derived_fields)
        for name in (
            "coder-assignment-template.csv",
            "hypothesis-awareness-template.csv",
            "staffing-plan-template.csv",
        ):
            self.assertFalse((SCHEMA_DIR / name).exists())

    def test_source_runs_require_full_hash_chain(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copied_schema(temporary)
            template = copied / "source-classification-template.csv"
            fields = template.read_text(encoding="utf-8").strip().split(",")
            fields.remove("response_sha256")
            template.write_text(",".join(fields) + "\n", encoding="utf-8")
            with self.assertRaises(SystemExit):
                validate(copied)

    def test_common_baseline_rejects_interjection_membership(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copied_schema(temporary)
            registry = copied / "model-comparisons.csv"
            content = registry.read_text(encoding="utf-8").replace(
                "matched_common_baseline,common_baseline,immediate_cues|neighbour_labels|form_covariates,",
                "matched_common_baseline,common_baseline,immediate_cues|neighbour_labels|form_covariates|interjection_syn_declaration_specific,",
            )
            registry.write_text(content, encoding="utf-8")
            with self.assertRaises(SystemExit):
                validate(copied)

    def test_sem_and_syn_are_jointly_co_primary(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copied_schema(temporary)
            registry = copied / "model-comparisons.csv"
            content = registry.read_text(encoding="utf-8").replace(
                "model_syn,total_syn,immediate_cues|neighbour_labels|form_covariates|interjection_syn_declaration_specific,matched_common_baseline,co_primary,",
                "model_syn,total_syn,immediate_cues|neighbour_labels|form_covariates|interjection_syn_declaration_specific,matched_common_baseline,secondary,",
            )
            registry.write_text(content, encoding="utf-8")
            with self.assertRaises(SystemExit):
                validate(copied)

    def test_each_annotation_route_requires_two_repeats(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copied_schema(temporary)
            registry = copied / "annotation-routes.csv"
            content = registry.read_text(encoding="utf-8").replace(
                "syn_gpt,source_syn,interjection_syn,gpt_primary,2,",
                "syn_gpt,source_syn,interjection_syn,gpt_primary,1,",
            )
            registry.write_text(content, encoding="utf-8")
            with self.assertRaises(SystemExit):
                validate(copied)

    def test_each_pass_requires_all_three_model_families(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copied_schema(temporary)
            registry = copied / "annotation-routes.csv"
            lines = registry.read_text(encoding="utf-8").splitlines()
            lines = [line for line in lines if not line.startswith("sem_gemini,")]
            registry.write_text("\n".join(lines) + "\n", encoding="utf-8")
            with self.assertRaises(SystemExit):
                validate(copied)

    def test_version_drift_must_halt_and_refreeze(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copied_schema(temporary)
            registry = copied / "model-registry.csv"
            content = registry.read_text(encoding="utf-8").replace(
                "halt_and_refreeze_before_new_packets", "continue_and_note", 1
            )
            registry.write_text(content, encoding="utf-8")
            with self.assertRaises(SystemExit):
                validate(copied)

    def test_placeholder_model_version_cannot_be_activated(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copied_schema(temporary)
            registry = copied / "model-registry.csv"
            content = registry.read_text(encoding="utf-8").replace(
                "pending_version_freeze,Same-family variants", "active,Same-family variants", 1
            )
            registry.write_text(content, encoding="utf-8")
            with self.assertRaises(SystemExit):
                validate(copied)

    def test_frozen_preoffset_count_is_enforced(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copied_schema(temporary)
            registry = copied / "sampling-rules.csv"
            content = registry.read_text(encoding="utf-8").replace(
                "sr_010,evaluation,required_completed_preoffset_packets,240,",
                "sr_010,evaluation,required_completed_preoffset_packets,239,",
            )
            registry.write_text(content, encoding="utf-8")
            with self.assertRaises(SystemExit):
                validate(copied)

    def test_cross_pass_context_sharing_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copied_schema(temporary)
            registry = copied / "role-separation-matrix.csv"
            content = registry.read_text(encoding="utf-8").replace(
                "source_syn,source_sem,no,no,3,",
                "source_syn,source_sem,yes,no,3,",
            )
            registry.write_text(content, encoding="utf-8")
            with self.assertRaises(SystemExit):
                validate(copied)

    def test_gate0_resolution_is_enforced(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copied_schema(temporary)
            registry = copied / "feasibility-gates.csv"
            content = registry.read_text(encoding="utf-8").replace(
                "fg_006,gate0_audio,measurement_resolution_ms,eq,10,",
                "fg_006,gate0_audio,measurement_resolution_ms,eq,20,",
            )
            registry.write_text(content, encoding="utf-8")
            with self.assertRaises(SystemExit):
                validate(copied)

    def test_both_block_side_fields_are_required(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copied_schema(temporary)
            template = copied / "outer-block-membership-template.csv"
            fields = template.read_text(encoding="utf-8").strip().split(",")
            fields.remove("declaration_syn_side")
            template.write_text(",".join(fields) + "\n", encoding="utf-8")
            with self.assertRaises(SystemExit):
                validate(copied)

    def test_derivation_control_values_are_required(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copied_schema(temporary)
            registry = copied / "codebook.csv"
            lines = registry.read_text(encoding="utf-8").splitlines()
            lines = [
                line for line in lines
                if not line.startswith("0.2,post-offset-trajectory,speaker_identity_status,")
            ]
            registry.write_text("\n".join(lines) + "\n", encoding="utf-8")
            with self.assertRaises(SystemExit):
                validate(copied)

    def test_predictive_contrasts_are_paired_at_form_block_level(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copied_schema(temporary)
            registry = copied / "predictive-contrast.csv"
            content = registry.read_text(encoding="utf-8").replace(
                "delta_sem_total,model_sem,matched_common_baseline,heldout_elpd_gain,form_block,test_outer_block_id,",
                "delta_sem_total,model_sem,matched_common_baseline,heldout_elpd_gain,event,packet_event_id,",
            )
            registry.write_text(content, encoding="utf-8")
            with self.assertRaises(SystemExit):
                validate(copied)

    def test_sampling_registry_header_matches_template(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = self.copied_schema(temporary)
            registry = copied / "sampling-rules.csv"
            content = registry.read_text(encoding="utf-8").replace(
                "unit,precedence,rule_version", "unit,priority,rule_version", 1
            )
            registry.write_text(content, encoding="utf-8")
            with self.assertRaises(SystemExit):
                validate(copied)

    def test_span_schema_does_not_require_legacy_turn_ids(self) -> None:
        collapse_fields = (SCHEMA_DIR / "analytic-span-template.csv").read_text(
            encoding="utf-8"
        ).strip().split(",")
        cue_fields = (SCHEMA_DIR / "immediate-cue-template.csv").read_text(
            encoding="utf-8"
        ).strip().split(",")
        self.assertIn("span_id", collapse_fields)
        self.assertNotIn("turn_id", collapse_fields)
        self.assertIn("span_position", cue_fields)
        self.assertNotIn("turn_position", cue_fields)
        self.assertFalse((SCHEMA_DIR / "turn-collapse-template.csv").exists())


if __name__ == "__main__":
    unittest.main()
