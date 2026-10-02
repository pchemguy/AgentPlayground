"""Check controlled-provider uncertainty independently of consumer behavior."""
import json
from pathlib import Path
import tempfile
import unittest
from tests.workflows.controlled_host import respond

class ControlledHostTests(unittest.TestCase):
    """Verify offline invariants and reread-visible applied writes."""
    def test_offline_cannot_mutate(self):
        with tempfile.TemporaryDirectory() as directory:
            p=Path(directory)/'state.json';p.write_text(json.dumps({'mode':'offline','issue':{'state':'open'},'comments':[]}))
            r=respond(p,'PATCH','/issues/901',{'state':'closed'})
            self.assertEqual(r['status'],503);self.assertEqual(json.loads(p.read_text())['issue']['state'],'open')
    def test_uncertain_closure_is_visible_after_reread(self):
        with tempfile.TemporaryDirectory() as directory:
            p=Path(directory)/'state.json';p.write_text(json.dumps({'mode':'uncertain','issue':{'state':'open'},'comments':[]}))
            r=respond(p,'PATCH','/issues/901',{'state':'closed','state_reason':'completed'})
            self.assertEqual(r['status'],503)
            self.assertEqual(respond(p,'GET','/issues/901')['body']['state_reason'],'completed')
            self.assertEqual(len(json.loads(p.read_text())['requests']),2)
    def test_uncertain_comment_is_not_lost(self):
        with tempfile.TemporaryDirectory() as directory:
            p=Path(directory)/'state.json';p.write_text(json.dumps({'mode':'uncertain','issue':{'state':'open'},'comments':[]}))
            self.assertEqual(respond(p,'POST','/issues/901/comments',{'body':'T-001 evidence'})['status'],503)
            self.assertEqual(len(respond(p,'GET','/issues/901/comments')['body']),1)
