# Subtle Motion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add restrained dynamic effects to the profile cover and desk view while preserving the editorial, non-template visual direction.

**Architecture:** Motion in the README cover is implemented with internal SVG CSS. Motion in the desk view uses native CSS transitions, CSS custom properties, and a small inline script for pointer state, coordinates, keyboard selection, and idle detection. No external runtime dependency is introduced.

**Tech Stack:** SVG, CSS, HTML, vanilla JavaScript, Python unittest

## Global Constraints

- No gradients, glow effects, particle fields, fake terminal copy, or cyberpunk status language.
- No external JavaScript or animation library.
- Respect `prefers-reduced-motion: reduce`.
- Preserve all existing public links and keyboard navigation.

---

### Task 1: Motion regression tests

**Files:**
- Modify: `tests/test_profile.py`

- [ ] Add assertions for SVG keyframes, reduced-motion handling, radar sweep, desk-view coordinate output, crosshair elements, idle state, and absence of external scripts.
- [ ] Run `python -m unittest discover -s tests -v` and confirm the new assertions fail against the current static implementation.

### Task 2: Animated README cover

**Files:**
- Modify: `assets/noxen-index.svg`

- [ ] Add internal CSS keyframes for intro, sweep, scan, blink, and staggered labels.
- [ ] Add reduced-motion rules that disable every animation.
- [ ] Keep the existing monochrome/red geometry and avoid gradients and filters.
- [ ] Run the profile tests and confirm the SVG assertions pass.

### Task 3: Interactive desk view

**Files:**
- Modify: `docs/index.html`

- [ ] Add crosshair guides, coordinate readout, entrance state, pointer parallax, and idle drift.
- [ ] Keep J/K, arrow-key, and Enter navigation unchanged.
- [ ] Disable non-essential motion for reduced-motion users and small touch screens.
- [ ] Run `node --check` on the extracted inline script.
- [ ] Run `python -m unittest discover -s tests -v` and confirm all tests pass.

### Task 4: Integration

**Files:**
- Verify: `README.md`, `assets/noxen-index.svg`, `docs/index.html`, `tests/test_profile.py`

- [ ] Compare the branch against `main` and confirm only motion-related files and documentation changed.
- [ ] Open and merge a pull request after verification.