# Instructions

## See it locally

Open `index.html` in a browser. There is no build step. To see it as GitHub Pages serves it:

```sh
python3 -m http.server 8000   # then open http://localhost:8000/
```

## Edit an app

Each app is one `<li class="app">` in `index.html`, with:

1. **Icon:** `images/icons/<app>.webp`, 128 × 128, from the app's own repo. Give it alt text.
2. **Name and pitch:** one line on what it does for whom.
3. **Screenshot:** `images/shots/<app>-480.webp` and `-960.webp`, cropped to 3:2 from the top.
4. **Bullets:** two or three, short.
5. **Badges:** Mac, iPhone, Web.
6. **Price:** copy it from the app's own config. While the app isn't on sale, keep the `planned` tag.
7. **Action:** a link only when it's public and live, otherwise `<span class="soon">Coming soon</span>`.

When an app goes on sale, swap its "Coming soon" for `<a class="go" href="…">Buy … →</a>` (or "Open …"), and remove the `planned` tag from its price.

## Add an app

Copy an existing `<li class="app">` block and change every field. Make the images like this (needs `magick` and `cwebp`):

```sh
# icon: trim any transparent margin, then 128 px
magick icon.png -trim +repage -resize 128x128 -strip /tmp/i.png && cwebp -q 85 /tmp/i.png -o images/icons/my-app.webp
# screenshot: crop 3:2 from the top, then two widths
magick shot.png -gravity North -crop 1200x800+0+0 +repage -strip /tmp/s.png
for w in 480 960; do magick /tmp/s.png -resize ${w}x /tmp/s$w.png && cwebp -q 80 /tmp/s$w.png -o images/shots/my-app-$w.webp; done
```

If there is no screenshot, use the large-icon panel (`<div class="shot shot-icon">`), as Messaging Graph does.

## Check

```sh
python3 tests/check_site.py
```

It fails if an image is missing or has no alt text, a link is a placeholder (`REPLACE-ME`, `#`, `example.com`), or an external link isn't https.

## Deploy

GitHub Pages serves the `main` branch root. Run the check, commit, and push to `main`; the site updates within a minute or two at <https://amalmehta.github.io/UsefulApps/>.

The Open Graph image (`images/og.png`, 1200 × 630) and the README screenshot (`docs/images/page.webp`) were rendered with headless Chrome. Re-render them if the apps change.
