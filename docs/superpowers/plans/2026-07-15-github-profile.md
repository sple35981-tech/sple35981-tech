# GitHub Profile Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish a concise, personal GitHub profile README for Noxen without profile-generator styling.

**Architecture:** Use one root `README.md` as the complete profile surface. Keep all presentation in native GitHub Markdown so it works in light and dark themes without external rendering services.

**Tech Stack:** GitHub Markdown, GitHub profile repository convention

## Global Constraints

- Repository must be public and named exactly `sple35981-tech`.
- Do not add animated typing text, trophies, visitor counters, contribution snakes, or badge walls.
- Link only to repositories that currently exist and are public.
- Keep claims factual and wording direct.

---

### Task 1: Create the profile README

**Files:**
- Create: `README.md`

**Interfaces:**
- Consumes: public repository URL `https://github.com/sple35981-tech/claude-cc-switch-bat`
- Produces: the complete profile page rendered by GitHub

- [ ] **Step 1: Write the README**

Create `README.md` with the approved name, positioning, current focus, selected work, working environment, private-research note, and contact section.

- [ ] **Step 2: Validate the copy**

Confirm that the README contains none of these phrases or patterns:

```text
passionate about
cutting-edge
leveraging AI
guru
expert
visitor counter
trophy
contribution snake
```

Expected: no matches.

- [ ] **Step 3: Validate public links**

Confirm that the selected project link points to:

```text
https://github.com/sple35981-tech/claude-cc-switch-bat
```

Expected: repository exists and is public.

- [ ] **Step 4: Commit**

```bash
git add README.md
git commit -m "feat: add personal GitHub profile"
```

### Task 2: Activate the GitHub profile repository

**Files:**
- No file changes

**Interfaces:**
- Consumes: completed root `README.md`
- Produces: visible profile content on `https://github.com/sple35981-tech`

- [ ] **Step 1: Rename the repository**

Open repository settings for `sple35981-tech/blog` and change the repository name to:

```text
sple35981-tech
```

Expected full name:

```text
sple35981-tech/sple35981-tech
```

- [ ] **Step 2: Confirm visibility**

Verify the repository is public.

Expected: GitHub displays a special-profile-repository notice and renders the root README on the account profile.

- [ ] **Step 3: Verify the final profile**

Open:

```text
https://github.com/sple35981-tech
```

Expected: the README appears above the pinned repositories, all headings render correctly, and the selected project link opens successfully.
