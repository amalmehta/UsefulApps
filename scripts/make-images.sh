#!/bin/sh
# Rebuilds the PNGs that index.html declares:
#   images/favicon-32.png        32 × 32    from favicon.svg
#   images/apple-touch-icon.png  180 × 180  from favicon.svg
#   images/og.png                1200 × 630 from scripts/og.html
#
# Needs rsvg-convert (brew install librsvg) and Google Chrome. Chrome renders the card
# because it reads the WebP icons and the woff2 Newsreader font as the live page does.
#
# Run from anywhere: sh scripts/make-images.sh
set -eu

ROOT=$(cd "$(dirname "$0")/.." && pwd)
CHROME=${CHROME:-"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"}

rsvg-convert -w 32 -h 32 "$ROOT/favicon.svg" -o "$ROOT/images/favicon-32.png"
rsvg-convert -w 180 -h 180 "$ROOT/favicon.svg" -o "$ROOT/images/apple-touch-icon.png"

"$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
  --window-size=1200,630 --virtual-time-budget=2000 \
  --screenshot="$ROOT/images/og.png" "file://$ROOT/scripts/og.html" 2>/dev/null

# Fail loudly if any size drifts from what index.html declares.
for spec in favicon-32.png:32x32 apple-touch-icon.png:180x180 og.png:1200x630; do
  file=${spec%%:*}; want=${spec#*:}
  got=$(sips -g pixelWidth -g pixelHeight "$ROOT/images/$file" | awk '/pixelWidth/{w=$2} /pixelHeight/{h=$2} END{print w "x" h}')
  [ "$got" = "$want" ] || { echo "images/$file is $got, expected $want" >&2; exit 1; }
  echo "images/$file $got"
done
