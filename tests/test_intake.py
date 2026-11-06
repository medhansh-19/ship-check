import json
import tempfile
import unittest
from pathlib import Path
from control.intake import discover, validate


class IntakeTests(unittest.TestCase):
    def test_validates_repository_not_arbitrary_url(self):
        self.assertEqual(validate('https://github.com/team/project','main'),'team/project')
        for repository in ('https://evil.invalid/team/project','../private','owner/repo/extra'):
            with self.assertRaises(ValueError):validate(repository,'main')
        with self.assertRaises(ValueError):validate('owner/repo','--upload-pack=bad')

    def test_monorepo_detects_multiple_stacks_and_preserves_commands(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            (root/'web').mkdir();(root/'service').mkdir()
            (root/'web/package.json').write_text(json.dumps({'scripts':{'test':'vitest run'},'packageManager':'pnpm@9'}))
            (root/'service/go.mod').write_text('module sample')
            result=discover(root)
            self.assertEqual({item['stack'] for item in result},{'Go','JavaScript/TypeScript'})
            self.assertEqual(next(i for i in result if i['stack']=='JavaScript/TypeScript')['commands']['test'],'vitest run')

    def test_unknown_stack_never_claims_pass(self):
        with tempfile.TemporaryDirectory() as temp:
            (Path(temp)/'unknown.custom').write_text('anything')
            self.assertEqual(discover(temp),[])
