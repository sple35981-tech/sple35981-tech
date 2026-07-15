# GitHub Contribution Snake Design

## Goal

Add a theme-adaptive animated GitHub contribution snake below the existing GitHub Actions-style checks card and above the `Noxen / 2026` footer in the profile README.

## Scope

This change adds one isolated GitHub Actions workflow, one generated-output branch, and one README `<picture>` block. It must not modify the existing GitHub Pages deployment, signature cover, typewriter tagline, project table, or Actions checks SVG.

## Architecture

- Workflow file: `.github/workflows/snake.yml`
- Generator: `Platane/snk/svg-only@v3`
- Input account: `${{ github.repository_owner }}`
- Generated files:
  - `dist/github-snake.svg` using the GitHub light palette
  - `dist/github-snake-dark.svg` using the GitHub dark palette
- Publishing action: push only generated files to an orphan `snake-output` branch
- README source URLs: raw files from the `snake-output` branch

The separate output branch keeps generated assets out of `main` and avoids coupling the snake workflow to the repository's existing Pages content.

## Workflow Triggers

The workflow runs:

1. On `workflow_dispatch` so it can be generated immediately and re-run manually.
2. Once per day using a UTC cron schedule.

Only one workflow run may publish at a time. New runs cancel older in-progress runs for the same workflow.

## Permissions and Security

- Set workflow-level `permissions: contents: write`; no broader permissions are granted.
- Use the repository-provided `GITHUB_TOKEN`; no personal token or secret is required.
- Pin actions to stable major versions supported by their maintainers.
- The workflow writes only to `snake-output`.

## Theme Adaptation

The README uses a `<picture>` element:

- Dark scheme selects `github-snake-dark.svg`.
- Light scheme selects `github-snake.svg`.
- The fallback `<img>` uses the light SVG.

The snake remains GitHub green in both themes while contribution cells use the corresponding GitHub palette.

## README Placement

The new block appears directly after:

```html
<img src="./assets/noxen-github-actions-checks.svg" ... />
```

and directly before:

```html
<p align="right">
  <sub>Noxen / 2026</sub>
</p>
```

The image is centered, uses `width="100%"`, and has descriptive alt text.

## Failure Handling

- If contribution retrieval or SVG generation fails, publishing does not run.
- If publishing fails, the existing files on `snake-output` remain available, so the README keeps showing the previous successful animation.
- The workflow does not alter `main` during scheduled runs.

## Verification

Before merging:

1. Validate the workflow YAML structure.
2. Confirm `permissions` contains only `contents: write`.
3. Confirm both light and dark output paths are generated.
4. Confirm the publishing step targets `snake-output` only.
5. Confirm the README contains exactly one theme-adaptive `<picture>` block.
6. Confirm existing Pages workflow files are unchanged.
7. Merge the workflow and README change, then manually dispatch the workflow.
8. Verify the first run succeeds and both SVG files are reachable from `snake-output`.
9. Verify the profile renders the correct asset in light and dark modes.

## Non-Goals

- No custom JavaScript animation.
- No GIF output.
- No changes to GitHub Pages.
- No red or cyberpunk color variants.
- No generated files committed to `main`.
