# Subtle Motion Design

## Goal

Add motion to the Noxen GitHub profile without returning to cyberpunk, fake-terminal, neon, particle, or template-heavy presentation.

## Visual behavior

- The README cover uses only CSS motion inside the existing monochrome SVG.
- Motion is limited to title entry, red rule reveal, slow radar rotation, and one quiet target blink.
- No gradients, glow filters, external images, GIFs, canvas, or JavaScript are used in the README artwork.

## Desk view behavior

- The page enters with restrained typography and row transitions.
- Pointer position creates a maximum seven-pixel parallax shift and updates a small coordinate readout.
- Clicking empty space produces one short crosshair trace; clicking links does not.
- Existing J/K, arrow-key, and Enter navigation remains unchanged.
- Pressing X briefly replaces the Noxen wordmark with its hexadecimal form.

## Accessibility and performance

- `prefers-reduced-motion: reduce` disables animations, parallax, cursor decoration, coordinates, and click traces.
- The page remains dependency-free and contains no external scripts.
- All effects use CSS transforms, opacity, or short-lived DOM elements.

## Success criteria

- The profile feels active but not theatrical.
- Existing content and project links remain unchanged.
- Automated tests reject old AI/cyberpunk motifs and verify the motion boundaries.
