# Subtle Motion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add restrained motion to the profile cover and GitHub Pages desk view while preserving the minimal editorial design.

**Architecture:** The README remains static Markdown and embeds one self-contained SVG with CSS keyframes. The GitHub Pages page remains a single dependency-free HTML file whose CSS handles transitions and whose inline JavaScript handles pointer coordinates, limited parallax, click traces, keyboard navigation, and the hexadecimal wordmark easter egg.

**Tech Stack:** SVG, CSS animations, vanilla JavaScript, Python `unittest`, Node.js syntax check.

## Global Constraints

- No gradients, glow effects, particles, canvas, Three.js, GIFs, or external script dependencies.
- Preserve all existing project links and README copy.
- Support `prefers-reduced-motion: reduce`.
- Limit README SVG to no more than four CSS keyframe definitions.
- Keep page parallax at or below seven pixels per axis.

---

### Task 1: Define motion regression tests

**Files:**
- Modify: `tests/test_profile.py`

**Interfaces:**
- Consumes: `README.md`, `assets/noxen-index.svg`, `docs/index.html`.
- Produces: five regression tests executed by Python `unittest`.

- [ ] Add assertions for CSS keyframes, reduced-motion handling, coordinate UI, parallax variables, click trace cleanup, and the X-key easter egg.
- [ ] Run `python -m unittest discover -s tests -v` against the old implementation.
- [ ] Confirm the SVG and page-motion tests fail because motion is not implemented.
- [ ] Commit with `test: define restrained motion behavior`.

### Task 2: Add restrained README cover motion

**Files:**
- Modify: `assets/noxen-index.svg`

**Interfaces:**
- Consumes: the existing monochrome cover geometry.
- Produces: a self-contained animated SVG with `prefers-reduced-motion` fallback.

- [ ] Add four CSS keyframes: title entry, red-rule reveal, radar rotation, and target blink.
- [ ] Apply animation classes only to existing title, metadata, rule, radar arm, and target elements.
- [ ] Keep the artwork free of SVG animation tags, gradients, and filters.
- [ ] Run `python -m unittest discover -s tests -v` and confirm the SVG test passes.
- [ ] Commit with `feat: animate profile cover subtly`.

### Task 3: Add controlled desk-view interaction

**Files:**
- Modify: `docs/index.html`

**Interfaces:**
- Consumes: existing project links and keyboard selection behavior.
- Produces: pointer parallax, coordinates, click traces, entry transitions, and `showHex()`.

- [ ] Add CSS variables `--mx` and `--my` and limit motion-layer translation to seven pixels.
- [ ] Add entry animations for the wordmark, metadata, rule, addresses, and project rows.
- [ ] Add a coordinate readout and update it from pointer movement.
- [ ] Add a short-lived `.trace` element on empty-space clicks and remove it on `animationend`.
- [ ] Add `showHex()` and trigger it when the X key is pressed.
- [ ] Disable decorative motion under `prefers-reduced-motion: reduce`.
- [ ] Run `python -m unittest discover -s tests -v` and confirm five tests pass.
- [ ] Extract the inline script and run `node --check` against it.
- [ ] Commit with `feat: add restrained desk view motion`.

### Task 4: Verify and integrate

**Files:**
- Verify: `README.md`, `assets/noxen-index.svg`, `docs/index.html`, `tests/test_profile.py`

**Interfaces:**
- Consumes: the completed feature branch.
- Produces: a reviewed pull request merged into `main`.

- [ ] Re-run the complete Python test suite.
- [ ] Re-run the Node.js syntax check.
- [ ] Compare the feature branch against `main` and confirm only expected files changed.
- [ ] Open a pull request with verification evidence.
- [ ] Merge only after GitHub reports the pull request as mergeable.
