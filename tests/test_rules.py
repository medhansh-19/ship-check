import unittest
from pathlib import Path
import test_control
from control.rules import parse_markdown


class RuleTests(unittest.TestCase):
    setUp = test_control.ControlTests.setUp
    git = test_control.ControlTests.git
    def checklist(self, name="alpha", identifier="EVENT-01", quote="A demo is required."):
        folder = self.repo / "scout/checklists"
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / (name + ".md")
        path.write_text(f"# {name}\n\n- Primary source: https://example.com/{name}\n\n## Submission\n\n- [x] **{identifier} — MUST — Demo requirement**\n  Source: official rules line 4.\n\n  > {quote}\n\n- [ ] **OPTION-01 — OPTIONAL — Bonus**\n\n  > Optional prize evidence.\n")
        return str(path.relative_to(self.repo))

    def test_source_quotes_and_boxes_are_not_proof(self):
        parsed = parse_markdown((Path(__file__).parents[1] / "scout/checklists/flip-the-switch.md").read_text(), "scout/checklists/flip-the-switch.md")
        self.assertGreater(len(parsed["rules"]), 10)
        self.assertTrue(all(r["status"] == "needs_review" for r in parsed["rules"]))
        self.assertTrue(any(r["scored"] for r in parsed["rules"]))

    def test_import_required_rules_and_exclude_optional_score(self):
        selected = self.checklist()
        baseline = self.engine.audit()["run"]
        run = self.engine.select_checklist(selected)["run"]
        self.assertEqual(run["total"], baseline["total"] + 1)
        item = next(c for c in run["checks"] if c["id"] == "event:EVENT-01")
        self.assertEqual(item["quote"], "A demo is required.")
        self.assertEqual(item["status"], "needs_review")
        self.assertEqual(item["source"], "https://example.com/alpha")

    def test_evidence_persists_and_file_changes_invalidate_it(self):
        run = self.engine.select_checklist(self.checklist())["run"]
        with self.assertRaises(ValueError):
            self.engine.review_rule(run["id"], "event:EVENT-01", "passed", "yes", "owner")
        reviewed = self.engine.review_rule(run["id"], "event:EVENT-01", "passed", "Video playback verified at the submitted demo URL.", "owner")["run"]
        self.assertEqual(reviewed["passed"], run["passed"] + 1)
        repeated = self.engine.audit()["run"]
        self.assertEqual(next(c["status"] for c in repeated["checks"] if c["id"] == "event:EVENT-01"), "passed")
        (self.repo / "README.md").write_text("Project changed")
        fresh = self.engine.audit()["run"]
        self.assertEqual(next(c["status"] for c in fresh["checks"] if c["id"] == "event:EVENT-01"), "needs_review")

    def test_switching_event_never_reuses_other_event_verification(self):
        alpha = self.checklist("alpha")
        beta = self.checklist("beta", quote="A different event requirement.")
        run = self.engine.select_checklist(alpha)["run"]
        self.engine.review_rule(run["id"], "event:EVENT-01", "passed", "Owner checked the alpha event requirement.", "owner")
        switched = self.engine.select_checklist(beta)["run"]
        self.assertEqual(switched["event_rules"]["name"], "beta")
        self.assertEqual(next(c["status"] for c in switched["checks"] if c["id"] == "event:EVENT-01"), "needs_review")

    def test_refuse_traversal_and_empty_checklists(self):
        with self.assertRaises(ValueError):
            self.engine.select_checklist("../../README.md")
        path = self.repo / "scout/checklists"
        path.mkdir(parents=True)
        (path / "empty.md").write_text("# Empty")
        with self.assertRaises(ValueError):
            self.engine.select_checklist("scout/checklists/empty.md")

    def test_conditional_prizes_are_not_mandatory_by_default(self):
        text = "# Event\n\n## Optional prizes\n\n- [ ] **CORE-01 — MUST only if entering Core — Open PR**\n\n  > Open a contribution PR.\n"
        item = parse_markdown(text, "test.md")["rules"][0]
        self.assertEqual(item["requirement"], "conditional")
        self.assertFalse(item["scored"])

    def test_missing_quote_cannot_be_verified(self):
        path = self.checklist(quote="")
        run = self.engine.select_checklist(path)["run"]
        with self.assertRaisesRegex(ValueError, "quoted source"):
            self.engine.review_rule(run["id"], "event:EVENT-01", "passed", "Owner recorded some supporting evidence.", "owner")

    def test_duplicate_ids_rejected(self):
        text = "# Event\n- [ ] **DUP-01 — MUST — One**\n> One\n- [ ] **DUP-01 — MUST — Two**\n> Two\n"
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            parse_markdown(text, "test.md")
