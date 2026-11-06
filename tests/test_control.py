import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from control.engine import Engine


class ControlTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / "project"
        self.repo.mkdir()
        self.git("init", "-b", "main")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "user.name", "Test")
        (self.repo / "README.md").write_text("# Fixture\n\nA sample project for checking actual missing files.\n\n## Setup\n\npython3 -m pip install -r requirements.txt\npython3 app.py\n")
        self.git("add", ".")
        self.git("commit", "-m", "fixture")
        self.engine = Engine(self.repo, self.root / "state.sqlite3")

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.repo), *args], stderr=subprocess.DEVNULL)

    def test_evidence_and_restart_persistence(self):
        state = self.engine.audit()
        check = next(c for c in state["run"]["checks"] if c["id"] == "references")
        self.assertEqual(check["status"], "blocked")
        self.assertIn("requirements.txt", check["evidence"])
        self.assertEqual(Engine(self.repo, self.root / "state.sqlite3").state()["run"]["id"], state["run"]["id"])

    def test_approval_is_bound_to_repository_bytes(self):
        run = self.engine.audit()["run"]
        self.engine.decide(run["id"], "setup-reference", "approved", "owner")
        (self.repo / "README.md").write_text("Changed after review")
        with self.assertRaisesRegex(ValueError, "changed"):
            self.engine.decide(run["id"], "setup-reference", "approved", "owner")
        with self.assertRaisesRegex(ValueError, "stale"):
            self.engine.create_pr(run["id"])

    def test_no_approval_no_pr(self):
        run = self.engine.audit()["run"]
        with self.assertRaisesRegex(ValueError, "Approve"):
            self.engine.create_pr(run["id"])
        with self.assertRaisesRegex(ValueError, "Unknown"):
            self.engine.decide(run["id"], "not-a-fix", "approved", "owner")

    def test_generated_draft_does_not_count_as_complete(self):
        run = self.engine.audit()["run"]
        proposal = next(c["proposal"] for c in run["checks"] if c["id"] == "submission")
        (self.repo / "SUBMISSION.md").write_text(proposal["after"])
        updated = self.engine.audit()["run"]
        self.assertEqual(next(c["status"] for c in updated["checks"] if c["id"] == "submission"), "blocked")

    def test_recheck_changes_score_and_resets_decisions(self):
        run = self.engine.audit()["run"]
        self.engine.decide(run["id"], "setup-reference", "rejected", "owner")
        (self.repo / "requirements.txt").write_text("")
        updated = self.engine.audit("Repository changed")["run"]
        self.assertGreater(updated["score"], run["score"])
        self.assertNotEqual(updated["id"], run["id"])

    def test_pr_contains_only_approved_change(self):
        run = self.engine.audit()["run"]
        self.engine.decide(run["id"], "submission-brief", "approved", "owner")
        original = subprocess.check_output
        calls = []
        def execute(args, **kwargs):
            calls.append(args)
            if args[:2] == ("git", "push"):
                return "pushed"
            if args[:3] == ("gh", "pr", "create"):
                checkout = Path(kwargs["cwd"])
                self.assertTrue((checkout / "SUBMISSION.md").exists())
                self.assertEqual((checkout / "README.md").read_text(), (self.repo / "README.md").read_text())
                return "https://github.com/example/project/pull/1"
            return original(args, **kwargs)
        with patch("control.engine.subprocess.check_output", side_effect=execute):
            result = self.engine.create_pr(run["id"])
        self.assertTrue(result["url"].endswith("/1"))
        self.assertFalse((self.repo / "SUBMISSION.md").exists())
        with patch("control.engine.subprocess.check_output", side_effect=execute):
            self.assertEqual(self.engine.create_pr(run["id"]), result)
        self.assertEqual(sum(args[:3] == ("gh", "pr", "create") for args in calls), 1)
