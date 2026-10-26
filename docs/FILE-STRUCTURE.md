# File structure

| Path | What it is |
|---|---|
| `index.html` | The page: intro, one card per app, footer back to the portfolio |
| `styles.css` | All styles; light and dark palettes as CSS variables at the top |
| `favicon.svg` | Site icon: four rounded app tiles |
| `images/favicon-32.png`, `images/apple-touch-icon.png` | PNG versions of the site icon |
| `images/og.png` | Link-preview image (1200 × 630) for Open Graph and social cards |
| `images/icons/` | Each app's icon from its own repo, 128 px WebP |
| `images/shots/` | Each app's screenshot, cropped 3:2, at 480 and 960 px WebP |
| `fonts/` | Newsreader and Inter (Latin), with their SIL Open Font Licences |
| `tests/check_site.py` | Checks images, alt text and links |
| `docs/` | Instructions, system design, this file, and `images/page.webp` for the README |
| `UsefulApps.md` | The project spec |
| `.nojekyll` | Tells GitHub Pages to serve the files as they are |
