# Subtle Motion Design

## Goal
Add motion to the Noxen profile without returning to cyberpunk, fake-terminal, particle, or template-heavy visuals.

## README cover
- Keep the current monochrome cover and muted red accent.
- Add a slow radar sweep, one horizontal scan pass, a softly blinking target point, and staggered address labels.
- Motion must be CSS-only inside the SVG and stop when `prefers-reduced-motion: reduce` is active.
- Do not add gradients, glow filters, typing effects, or continuously moving background decoration.

## Desk view
- Preserve the editorial/debugger layout and all current project links.
- Add a short entrance transition, subtle pointer parallax, live pointer coordinates, project-row selection motion, and a quiet idle drift after inactivity.
- Add crosshair guide lines that follow the pointer at low opacity.
- Keep keyboard navigation using J/K, arrow keys, and Enter.
- Use no external JavaScript or animation library.

## Accessibility and performance
- Disable non-essential transitions, pointer guides, and idle drift for reduced-motion users.
- Avoid animation loops driven by `requestAnimationFrame`; pointer movement should update CSS variables only.
- Keep all effects readable in both light and dark color schemes and usable on mobile.

## Verification
- Parse the SVG and HTML successfully.
- Confirm motion hooks and reduced-motion handling are present.
- Confirm old cyberpunk motifs and external scripts remain absent.
- Confirm every local asset referenced by README and HTML exists.