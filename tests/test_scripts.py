from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import tempfile
import threading
import unittest

from scripts.fetch_rules import fetch_rules, html_to_text
from scripts.tz import convert_deadline


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


class FetchRulesTests(unittest.TestCase):
    def test_html_removes_scripts_and_keeps_rule_boundaries(self):
        self.assertEqual(html_to_text('<h1>Rules</h1><script>wrong deadline</script>'
                                     '<p>Submit <b>Nov 7</b> &amp; include a demo.</p>'),
                         'Rules\nSubmit Nov 7 & include a demo.\n')

    def test_fetch_saves_text_and_provenance(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "rules.html").write_text("<p>Deadline: 23:59 UTC.</p>", encoding="utf-8")
            server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=folder))
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                url = f"http://127.0.0.1:{server.server_port}/rules.html"
                target = fetch_rules(url, root / "output", "sample")
                self.assertEqual(target.read_text(), "Deadline: 23:59 UTC.\n")
                self.assertIn(url, target.with_suffix(".source.json").read_text())
                with self.assertRaises(FileExistsError):
                    fetch_rules(url, root / "output", "sample")
            finally:
                server.shutdown()
                server.server_close()
                thread.join()

    def test_rejects_non_web_url_and_path_traversal(self):
        for url, slug in [("file:///etc/hosts", "rules"), ("https://example.com", "../rules")]:
            with self.subTest(url=url, slug=slug), self.assertRaises(ValueError):
                fetch_rules(url, ".", slug)


class DeadlineTests(unittest.TestCase):
    def test_explicit_ist_to_utc(self):
        result = convert_deadline("2026-11-07T23:59:00+05:30")
        self.assertEqual(result["UTC"].isoformat(), "2026-11-07T18:29:00+00:00")
        self.assertEqual(result["IST"].isoformat(), "2026-11-07T23:59:00+05:30")

    def test_utc_crosses_calendar_day_in_ist(self):
        self.assertEqual(convert_deadline("2026-11-07T23:59:00Z")["IST"].isoformat(),
                         "2026-11-08T05:29:00+05:30")

    def test_iana_zone(self):
        self.assertEqual(convert_deadline("2026-11-07T23:59:00", "Asia/Kolkata")["UTC"].hour, 18)

    def test_rejects_missing_zone_and_conflicting_zone(self):
        for value, zone in [("2026-11-07T23:59:00", None), ("2026-11-07T23:59:00Z", "Asia/Kolkata")]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                convert_deadline(value, zone)

    def test_rejects_ambiguous_and_nonexistent_dst_times(self):
        for value in ["2026-11-01T01:30:00", "2026-03-08T02:30:00"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                convert_deadline(value, "America/New_York")


if __name__ == "__main__":
    unittest.main()
