# yogic-tools: working notes for Claude

Static GitHub Pages site (no build, no scripts, no tests, no CI) for Yogic Approach's public
browser tools. Every page here is **live and public**: change it through a branch and a PR.

## Facts to start from (checked 2026-11-09)

- Pages serves `main` at `/`: <http://yogicapproach.com/yogic-tools/>. The repo has no CNAME of
  its own; it sits under the org's `yogicapproach.com` domain.
- Tracked content: `index.html`, `syp/index.html`, `syp/syp-companion/{index,privacy}.html`,
  `syp/syp-companion/assets/*.png`, `syp/notes/*.html`, `README.md`, this file.
- The extension source is **not here**. It is in the `syp-companion` repo
  (`C:\Users\kaanchan\Projects\Yoga\Ashram\SYP\SYP-Unofficial\github\syp-companion`; its
  `docs/EXTENSION-PUBLISHING.md` is the store-submission playbook). Read it, do not edit it from here.
- Releases (zips + `SHA256SUMS`, tag `syp-companion-v<version>`) are published **on this repo's**
  Releases page. Latest at the time of writing: `syp-companion-v0.8.3`.

## Rules

1. **The privacy page and the store listings change together.** `syp/syp-companion/privacy.html`
   is the policy URL both store listings point to. If a new extension version stores or sends
   anything new, update it, and the date on it, in a PR that is merged *before* the store upload.
   To find what a version stores, grep its source for `chrome.storage` and `fetch(`.
2. **The install page hard-codes the store versions** (`syp/syp-companion/index.html`, two
   "(version X)" mentions). Update them once the stores actually serve the new version, not before.
3. **The notes page is deliberately unlisted**: `<meta name="robots" content="noindex,nofollow">`
   and no link to it from any other page. Do not add links, a sitemap entry, or remove the meta.
4. **Each page carries its own colour tokens** (inline `<style>`). Do not restyle or extract a shared
   stylesheet until the site-root design is settled; it would be done twice.
5. Do not push to `main` or merge; open a draft PR. A change to the privacy page or an install
   link is "ready to test" for KA, not self-closed.
6. `graphify-out/` and `.gh-offline-sync/` are ignored by `.gitignore`.

## Checking a change

There is no test suite. Open the changed file in a browser, and after merge check the live URL
(`curl -sI http://yogicapproach.com/yogic-tools/<path>` should be `200`).
