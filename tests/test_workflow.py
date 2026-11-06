import unittest
import test_control


class WorkflowTests(unittest.TestCase):
    setUp=test_control.ControlTests.setUp
    git=test_control.ControlTests.git

    def test_initial_session_empty_despite_static_audit(self):
        self.engine.audit()
        self.assertEqual(self.engine.workflow.state()['activity'],[])
        self.assertEqual(self.engine.workflow.state()['rules'],[])

    def test_owner_can_select_another_repository_without_old_event(self):
        self.engine.workflow.observe('target','owner','@shipcheck-auditor Audit https://github.com/medhansh-19/Afterglow branch main')
        target=self.engine.workflow.state()['target']
        self.assertEqual(target['repository'],'medhansh-19/Afterglow')
        self.assertEqual(target['branch'],'main')
        self.assertIsNone(target['event_url'])

    def test_messages_progress_and_deduplicate(self):
        workflow=self.engine.workflow
        workflow.observe('1','owner','@shipcheck-scout check rules')
        self.assertEqual(workflow.state()['stages']['scout'],'working')
        text='# Rules\n- Primary source: https://example.com\n- [ ] **RULE-01 — MUST — Demo**\n > A demo is required.'
        workflow.observe('2','scout',text)
        workflow.observe('2','scout',text)
        self.assertEqual(len(workflow.state()['rules']),1)
        self.assertEqual(len(workflow.state()['activity']),2)
        workflow.observe('3','auditor','FAIL: Setup is broken. https://github.com/a/b/pull/1')
        self.assertEqual(workflow.state()['stages']['auditor'],'reported')
        self.assertEqual(len(workflow.state()['changes']),1)

    def test_new_session_preserves_history_but_resets_view(self):
        workflow=self.engine.workflow
        workflow.observe('1','auditor','FAIL setup')
        previous=workflow.state()['id']
        workflow.new()
        self.assertNotEqual(workflow.state()['id'],previous)
        self.assertEqual(workflow.state()['findings'],[])
        with self.engine.db() as db:
            self.assertEqual(db.execute('SELECT count(*) FROM workflow_sessions').fetchone()[0],2)
