# Noxen Profile Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the cyberpunk profile with a compact editorial index and dependency-free desk view.

**Architecture:** GitHub README renders a static SVG cover and concise table. GitHub Pages uses one self-contained HTML file for layout and keyboard interaction. A Python unittest suite validates forbidden motifs, parsing, local assets and dependency constraints.

**Tech Stack:** Markdown, SVG, HTML, CSS, vanilla JavaScript, Python unittest.

## Global Constraints
- No biography section.
- No gradients, glow, particles, planets, fake terminals, binary text, typing animations, badges, counters or skill bars.
- No external JavaScript dependency.
- Support responsive layouts and reduced motion.

---

### Task 1: Define regression checks
**Files:**
- Create: `tests/test_profile.py`

- [x] Add checks for banned cyberpunk language and effects.
- [x] Add checks for compact README structure and local asset references.
- [x] Add SVG parse and static-artwork checks.
- [x] Add HTML dependency, keyboard-navigation and reduced-motion checks.

### Task 2: Replace README and cover
**Files:**
- Modify: `README.md`
- Create: `assets/noxen-index.svg`

- [x] Replace the identity-node copy with a three-destination work index.
- [x] Create a static monochrome SVG cover with one muted red accent.

### Task 3: Replace the interactive page
**Files:**
- Modify: `docs/index.html`

- [x] Remove Three.js and the 3D scene.
- [x] Add editorial project layout, J/K navigation, pointer detail and responsive behavior.

### Task 4: Verify
- [x] Run `python -m unittest discover -s tests -v`.
- [x] Confirm five tests pass with zero failures.
