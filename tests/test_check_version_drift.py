import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import check_version_drift as c  # noqa: E402

PAGE_083 = '<p><a href="x">Install from Firefox Add-ons</a> (version 0.8.3).</p><p>Chrome (version 0.8.3).</p>'


class StaleInstallPage(unittest.TestCase):
    """NAMED FAILURE: stores serve 0.11.x but the hard-coded install page still says 0.8.3."""

    def test_page_at_083_against_0110_tag_fails(self):
        code, msg = c.check(PAGE_083, "syp-companion-v0.11.0")
        self.assertEqual(code, 1)
        self.assertIn("0.8.3", msg)

    def test_matching_versions_pass(self):
        self.assertEqual(c.check(PAGE_083, "syp-companion-v0.8.3")[0], 0)

    def test_one_stale_mention_among_two_fails(self):
        page = PAGE_083.replace("Chrome (version 0.8.3)", "Chrome (version 0.11.0)")
        self.assertEqual(c.check(page, "syp-companion-v0.11.0")[0], 1)

    def test_unreadable_tag_or_page_is_an_error_not_a_pass(self):
        self.assertEqual(c.check(PAGE_083, "latest")[0], 2)
        self.assertEqual(c.check("<p>no version here</p>", "syp-companion-v0.8.3")[0], 2)

    def test_real_install_page_is_parseable(self):
        self.assertTrue(c.page_versions(c.DEFAULT_PAGE.read_text(encoding="utf-8")))

    def test_cli_exit_code_on_drift(self):
        self.assertEqual(c.main(["--tag", "syp-companion-v0.11.0"]), 1)


if __name__ == "__main__":
    unittest.main()
