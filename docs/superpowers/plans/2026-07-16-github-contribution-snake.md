# GitHub Contribution Snake Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a daily generated, theme-adaptive GitHub contribution snake below the profile checks card without changing the existing GitHub Pages deployment.

**Architecture:** A dedicated GitHub Actions workflow generates light and dark SVG files with `Platane/snk/svg-only@v3`, then publishes only the generated `dist` directory to the orphan `snake-output` branch with `crazy-max/ghaction-github-pages@v3.1.0`. The README embeds both raw branch assets through a `<picture>` element selected by `prefers-color-scheme`.

**Tech Stack:** GitHub Actions YAML, Platane/snk, crazy-max GitHub Pages action, HTML in Markdown, Python `unittest`.

## Global Constraints

- Generate SVG only; no GIF output.
- Use GitHub green `#3fb950` for the snake in light and dark themes.
- Write generated assets only to `snake-output`; do not commit generated files to `main`.
- Grant only `contents: write` to the snake workflow.
- Run manually with `workflow_dispatch` and daily with cron.
- Do not modify the existing Pages workflow or anything under `docs/`.
- Keep the signature cover, tagline, project table, checks SVG, and footer unchanged.

---

### Task 1: Add contribution-snake regression tests

**Files:**
- Modify: `tests/test_profile.py`

**Interfaces:**
- Consumes: `README.md` and `.github/workflows/snake.yml`.
- Produces: `ProfileTests.test_contribution_snake_workflow_and_readme_embedding`.

- [ ] **Step 1: Extend the test fixture**

Add:

```python
SNAKE_WORKFLOW_PATH = ROOT / ".github/workflows/snake.yml"
SNAKE_WORKFLOW = SNAKE_WORKFLOW_PATH.read_text(encoding="utf-8")
```

- [ ] **Step 2: Add the failing test**

```python
def test_contribution_snake_workflow_and_readme_embedding(self):
    self.assertTrue(SNAKE_WORKFLOW_PATH.exists())
    self.assertIn("workflow_dispatch:", SNAKE_WORKFLOW)
    self.assertIn("schedule:", SNAKE_WORKFLOW)
    self.assertIn("permissions:\n  contents: write", SNAKE_WORKFLOW)
    self.assertIn("Platane/snk/svg-only@v3", SNAKE_WORKFLOW)
    self.assertIn("crazy-max/ghaction-github-pages@v3.1.0", SNAKE_WORKFLOW)
    self.assertIn("target_branch: snake-output", SNAKE_WORKFLOW)
    self.assertIn("dist/github-snake.svg?palette=github-light&color_snake=%233fb950", SNAKE_WORKFLOW)
    self.assertIn("dist/github-snake-dark.svg?palette=github-dark&color_snake=%233fb950", SNAKE_WORKFLOW)
    self.assertEqual(README.count("<picture>"), 1)
    self.assertIn('(prefers-color-scheme: dark)', README)
    self.assertIn('(prefers-color-scheme: light)', README)
    self.assertIn("snake-output/github-snake-dark.svg", README)
    self.assertIn("snake-output/github-snake.svg", README)
```

- [ ] **Step 3: Verify the test fails before implementation**

Run:

```bash
python -m unittest tests.test_profile.ProfileTests.test_contribution_snake_workflow_and_readme_embedding -v
```

Expected: failure because `.github/workflows/snake.yml` does not exist.

- [ ] **Step 4: Commit the regression test**

```bash
git add tests/test_profile.py
git commit -m "test: define contribution snake integration"
```

---

### Task 2: Add the isolated generation workflow

**Files:**
- Create: `.github/workflows/snake.yml`

**Interfaces:**
- Consumes: `${{ github.repository_owner }}` and `${{ secrets.GITHUB_TOKEN }}`.
- Produces on `snake-output`: `github-snake.svg` and `github-snake-dark.svg`.

- [ ] **Step 1: Create the workflow**

```yaml
name: Generate contribution snake

on:
  workflow_dispatch:
  schedule:
    - cron: "17 0 * * *"

permissions:
  contents: write

concurrency:
  group: contribution-snake
  cancel-in-progress: true

jobs:
  generate:
    runs-on: ubuntu-latest
    timeout-minutes: 5
    steps:
      - name: Generate light and dark SVGs
        uses: Platane/snk/svg-only@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: |
            dist/github-snake.svg?palette=github-light&color_snake=%233fb950
            dist/github-snake-dark.svg?palette=github-dark&color_snake=%233fb950

      - name: Publish generated SVGs
        uses: crazy-max/ghaction-github-pages@v3.1.0
        with:
          target_branch: snake-output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

- [ ] **Step 2: Validate the workflow structure**

Run:

```bash
python - <<'PY'
from pathlib import Path
import yaml
path = Path('.github/workflows/snake.yml')
data = yaml.safe_load(path.read_text())
assert data['permissions'] == {'contents': 'write'}
assert data['concurrency']['group'] == 'contribution-snake'
assert data['jobs']['generate']['timeout-minutes'] == 5
print('snake workflow structure: passed')
PY
```

Expected: `snake workflow structure: passed`.

- [ ] **Step 3: Run the focused regression test**

Run:

```bash
python -m unittest tests.test_profile.ProfileTests.test_contribution_snake_workflow_and_readme_embedding -v
```

Expected: still fails because the README `<picture>` block is not present.

- [ ] **Step 4: Commit the workflow**

```bash
git add .github/workflows/snake.yml
git commit -m "ci: generate contribution snake daily"
```

---

### Task 3: Embed the theme-adaptive snake in the README

**Files:**
- Modify: `README.md:35-41`

**Interfaces:**
- Consumes: raw SVG files from the `snake-output` branch.
- Produces: one centered `<picture>` element with dark, light, and fallback sources.

- [ ] **Step 1: Add the README block after the checks SVG**

```html
<br>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/sple35981-tech/sple35981-tech/snake-output/github-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/sple35981-tech/sple35981-tech/snake-output/github-snake.svg" />
    <img src="https://raw.githubusercontent.com/sple35981-tech/sple35981-tech/snake-output/github-snake.svg" alt="GitHub contribution snake animation" width="100%" />
  </picture>
</p>
```

Keep the `Noxen / 2026` footer immediately after this block.

- [ ] **Step 2: Run the focused test**

Run:

```bash
python -m unittest tests.test_profile.ProfileTests.test_contribution_snake_workflow_and_readme_embedding -v
```

Expected: pass.

- [ ] **Step 3: Run the complete profile suite**

Run:

```bash
python -m unittest discover -s tests -v
```

Expected: all tests pass with zero failures.

- [ ] **Step 4: Commit the README integration**

```bash
git add README.md
git commit -m "feat: show theme-adaptive contribution snake"
```

---

### Task 4: Review, merge, and generate the first assets

**Files:**
- Verify: `.github/workflows/snake.yml`
- Verify: `README.md`
- Verify: `tests/test_profile.py`
- Verify unchanged: `docs/`

**Interfaces:**
- Consumes: completed feature branch.
- Produces: merged workflow on `main`, a successful manual run, and two files on `snake-output`.

- [ ] **Step 1: Compare the branch against `main`**

Expected changed files:

```text
.github/workflows/snake.yml
README.md
docs/superpowers/plans/2026-07-16-github-contribution-snake.md
docs/superpowers/specs/2026-07-16-github-contribution-snake-design.md
tests/test_profile.py
```

No existing file under `docs/` may be modified.

- [ ] **Step 2: Open and merge a pull request**

The PR description must include the test result, workflow permission scope, target branch, and confirmation that Pages files are unchanged.

- [ ] **Step 3: Manually dispatch the workflow from `main`**

Expected: the `generate` job succeeds within five minutes and creates/updates `snake-output`.

- [ ] **Step 4: Verify generated files**

Confirm these URLs return SVG content:

```text
https://raw.githubusercontent.com/sple35981-tech/sple35981-tech/snake-output/github-snake.svg
https://raw.githubusercontent.com/sple35981-tech/sple35981-tech/snake-output/github-snake-dark.svg
```

- [ ] **Step 5: Verify the profile rendering**

Confirm the README contains one contribution snake and switches source under light and dark color schemes.
