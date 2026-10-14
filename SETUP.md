# GitHub Profile Setup Guide — Rafi741088

## What's included

- `README.md` — profile README ready to commit.
- `assets/github-banner.gif` — genuinely animated 1600×400 banner (36 frames, infinite loop).
- `assets/github-banner.png` — static fallback/preview.
- `assets/section-divider.gif` and `.svg` — animated and static separators.
- `generate_assets.py` — reproducible Pillow-based asset generator.
- `.github/workflows/snake.yml` — optional GitHub Actions workflow for contribution-snake SVGs.

## Install locally (Windows PowerShell)

1. Install Python 3.10+ if needed.
2. Extract this ZIP.
3. Open PowerShell in the extracted folder.
4. Run:

   ```powershell
   python -m pip install Pillow
   python generate_assets.py
   ```

5. Check that the `assets` directory contains the banner and divider assets.

The delivered GIF/PNG are already generated; rerun the script only if you want to regenerate them.

## Put it on GitHub

Your profile repository already exists: `Rafi741088/Rafi741088`.

1. Download/clone it:

   ```powershell
   git clone https://github.com/Rafi741088/Rafi741088.git
   cd Rafi741088
   ```

2. Copy this kit's `README.md`, `assets` directory, and `.github` directory into the cloned repository. Review/merge with any existing files you want to keep.
3. Commit and push:

   ```powershell
   git add README.md assets .github
   git commit -m "Refresh animated GitHub profile"
   git push origin main
   ```

Do not overwrite files you want to preserve without reviewing the diff first.

## Contribution snake workflow

The workflow is optional. Copy `.github/workflows/snake.yml` into the profile repository. Then open **Actions** on GitHub and enable workflows if GitHub prompts you. Run **Generate contribution snake** manually once. When it succeeds, the workflow publishes SVGs to the `output` branch and the README image should load. The scheduled run is daily.

The generator uses actual GitHub contribution data. It does not create commits or fake contribution activity.

## Third-party embeds used by README

- Typing headline: `https://readme-typing-svg.demolab.com/` — third-party hosted animation; may be unavailable.
- GitHub stats: `https://github-readme-stats.vercel.app/` — public stats card service; may be cached, rate-limited, or unavailable.
- Streak card: `https://streak-stats.demolab.com/` — public streak card service; may be cached or unavailable.
- Technology icons: `https://skillicons.dev/` — external technology icon image service.
- Badges: `https://img.shields.io/` — badge rendering service.
- Contribution snake action: `Platane/snk@v3` and `crazy-max/ghaction-github-pages@v4`; external GitHub Actions maintained by their respective authors.

The README still has ordinary headings, links, and explanatory text if these services fail. External providers can change their behavior; no external embed is guaranteed permanently available.

## Before pushing

- Confirm your LinkedIn URL is correct.
- If your portfolio has a verified public deployment, add its URL; this version intentionally does not guess one.
- Review the featured-project descriptions and technology claims before publishing.
- Preview the README on GitHub after the commit.
- Verify that `assets/github-banner.gif` animates and the PNG fallback is readable.
- Check mobile rendering, external image loading, and workflow run status.
