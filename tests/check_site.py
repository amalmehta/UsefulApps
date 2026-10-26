"""Checks index.html before it goes live. Standard library only.

- Every image it references (img src and srcset, icons, Open Graph image) exists in the repo.
- Every <img> has non-empty alt text.
- No link is a placeholder: REPLACE-ME, a bare "#", or example.com.
- Every external link is https.

Run from anywhere: python3 tests/check_site.py   (exit code 0 means it passed)
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import sys

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://amalmehta.github.io/UsefulApps/"
PLACEHOLDERS = ("REPLACE-ME", "REPLACE-WITH", "example.com")


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []   # (line, path)
        self.links = []    # (line, href)
        self.missing_alt = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        line = self.getpos()[0]
        if tag == "img":
            if not (a.get("alt") or "").strip():
                self.missing_alt.append((line, a.get("src")))
            if a.get("src"):
                self.images.append((line, a["src"]))
            for part in (a.get("srcset") or "").split(","):
                if part.strip():
                    self.images.append((line, part.split()[0]))
        elif tag == "a":
            self.links.append((line, a.get("href") or ""))
        elif tag == "link":
            if a.get("rel") in ("icon", "apple-touch-icon", "stylesheet", "preload"):
                self.images.append((line, a.get("href", "")))
            elif a.get("href"):
                self.links.append((line, a["href"]))
        elif tag == "meta" and a.get("property") == "og:image":
            self.images.append((line, a.get("content", "")))


def local_path(ref):
    """Map a reference to a file in the repo, or None if it points somewhere else."""
    if ref.startswith(SITE):
        ref = ref[len(SITE):]
    if urlparse(ref).scheme:
        return None
    return ROOT / ref.split("#")[0].split("?")[0]


def main():
    page = Page()
    page.feed((ROOT / "index.html").read_text(encoding="utf-8"))
    problems = []

    for line, ref in page.images:
        path = local_path(ref)
        if path is None:
            problems.append(f"line {line}: file is not in this repo: {ref}")
        elif not path.is_file():
            problems.append(f"line {line}: missing file: {ref}")
    for line, src in page.missing_alt:
        problems.append(f"line {line}: image without alt text: {src}")
    for line, href in page.links:
        if href in ("", "#") or any(p.lower() in href.lower() for p in PLACEHOLDERS):
            problems.append(f"line {line}: placeholder link: {href!r}")
        elif href.startswith("#"):
            continue  # in-page anchor, checked below
        elif urlparse(href).scheme and urlparse(href).scheme != "https":
            problems.append(f"line {line}: external link is not https: {href}")
        elif not urlparse(href).scheme and not local_path(href).exists():
            problems.append(f"line {line}: missing local page: {href}")

    print(f"{len(page.images)} image and asset references, {len(page.links)} links checked")
    if problems:
        print("\n".join(problems))
        print(f"FAILED: {len(problems)} problem(s)")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
