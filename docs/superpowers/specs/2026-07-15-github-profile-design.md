# GitHub Profile Design

## Goal

Turn the empty public repository into a restrained, personal GitHub profile README for Noxen. The page should feel written by a real developer rather than assembled from a profile generator.

## Voice

- Direct, calm, and specific.
- English-first because GitHub is an international platform, with a short Chinese line for context.
- No exaggerated claims such as "expert", "guru", or "full-stack everything".
- No generic AI copy such as "passionate about leveraging cutting-edge technology".

## Visual Direction

- Native GitHub Markdown and a small amount of HTML alignment only.
- No generated banner, animated typing text, visitor counter, trophy wall, contribution snake, or autoplay media.
- No large badge wall. Tools are written as plain text so the page remains readable in light and dark mode.
- Strong hierarchy through spacing, short headings, and concise paragraphs.

## Information Architecture

1. Name and one-line positioning.
2. A short, human introduction describing the kind of problems Noxen works on.
3. Current focus, limited to three concrete areas.
4. Selected public work with an accurate description of `claude-cc-switch-bat`.
5. Working environment and tools as plain text.
6. A short note that some research repositories remain private while documentation and reproducibility are being improved.
7. Contact information.

## Content Constraints

- Mention reverse engineering, security tooling, CTF, automation, and practical agent workflows.
- Avoid presenting private or unfinished repositories as publicly available projects.
- Only link to repositories that currently exist and are public.
- Keep the complete README short enough to scan in under one minute.
- Do not publish sensitive research details, exploit code, credentials, or operational security information.

## Repository Constraint

GitHub only renders a profile README when the public repository name exactly matches the account login: `sple35981-tech/sple35981-tech`. The current writable empty repository is `sple35981-tech/blog`; after the content is prepared, it must be renamed to `sple35981-tech` in repository settings.

## Success Criteria

- The README renders cleanly in GitHub light and dark themes.
- Every public link resolves.
- The wording sounds personal and specific rather than templated.
- A visitor can understand Noxen's focus and find the main public project in less than one minute.
