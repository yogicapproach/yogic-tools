# yogic-tools

Browser tools from [Yogic Approach](https://yogicapproach.com), published as a static site at
<http://yogicapproach.com/yogic-tools/> (GitHub Pages, branch `main`, folder `/`; no build step).

## What is here

| Page | Path in this repo | Live URL |
|---|---|---|
| Tools landing page | `index.html` | <http://yogicapproach.com/yogic-tools/> |
| SYP tools group | `syp/index.html` | <http://yogicapproach.com/yogic-tools/syp/> |
| SYP Companion install page | `syp/syp-companion/index.html` | <http://yogicapproach.com/yogic-tools/syp/syp-companion/> |
| SYP Companion privacy policy | `syp/syp-companion/privacy.html` | <http://yogicapproach.com/yogic-tools/syp/syp-companion/privacy.html> |
| Store listing images | `syp/syp-companion/assets/` | used by the store listings, not by a page |
| Study notes (unlisted, `noindex`) | `syp/notes/` | not linked from anywhere on purpose |

## SYP Companion

A browser extension (Chrome, Edge, Firefox) that adds a bar to the Satyam Yoga Prasad site.
Its **source code is not here**: it lives in the separate `syp-companion` repo. This repo only
publishes the install page, the privacy policy, and the zip builds attached to
[Releases](https://github.com/yogicapproach/yogic-tools/releases) (tags `syp-companion-v<version>`).

People normally install from the stores (Firefox Add-ons, Chrome Web Store; Edge users use the
Chrome listing). The browser updates a store install by itself. A zip from Releases is the
manual alternative and does not update itself.

The Firefox Add-ons and Chrome Web Store listings link to this site for their homepage, support
(this repo's issues) and **privacy policy**.

## Keeping it true

- The install page hard-codes the version it shows. After a new version reaches the stores,
  update `syp/syp-companion/index.html` to match.
- The privacy page describes what the extension stores. A new version that stores or sends
  anything new needs `privacy.html` updated **before** it goes to the stores, and the
  "last updated" date moved.

See `CLAUDE.md` for the working rules.
