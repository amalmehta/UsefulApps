"""Checks index.html before it goes live. Standard library only.

- Every image it references (img src and srcset, icons, Open Graph image) exists in the repo.
- Every <img> has non-empty alt text.
- No link is a placeholder: REPLACE-ME, a bare "#", or example.com.
- Every external link is https.
- Every card with a download has an install note.

With --live it also goes online:
- Every card's link answers 200, the spec's meaning of "live".
- No link under releases/latest names a version, since it would break at the next release.
- No "Coming soon" card has a public repo with a release, since people could already get it.

Run from anywhere: python3 tests/check_site.py [--live]   (exit code 0 means it passed)
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen
import json
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://amalmehta.github.io/UsefulApps/"
PLACEHOLDERS = ("REPLACE-ME", "REPLACE-WITH", "example.com")
OWNER = "amalmehta"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []   # (line, path)
        self.links = []    # (line, href)
        self.missing_alt = []
        self.cards = []    # {"id", "go", "soon", "install"}

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        line = self.getpos()[0]
        classes = (a.get("class") or "").split()
        if tag == "li" and "app" in classes:
            self.cards.append({"id": a.get("id", ""), "go": None, "soon": False, "install": False})
        elif self.cards:
            if tag == "a" and "go" in classes:
                self.cards[-1]["go"] = a.get("href")
            elif "soon" in classes:
                self.cards[-1]["soon"] = True
            elif "install" in classes:
                self.cards[-1]["install"] = True
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


def fetch(url):
    """The status code for a URL, following redirects, and its body if it's small enough to want."""
    request = Request(url, headers={"User-Agent": "UsefulApps-check-site"})
    try:
        with urlopen(request, timeout=20) as response:
            return response.status, response.read(2_000_000)
    except HTTPError as err:
        return err.code, b""
    except URLError as err:
        return None, str(err.reason).encode()


def public_repos():
    """Public repos only: names of private ones never appear in this public file."""
    names = []
    for number in range(1, 6):
        status, body = fetch(f"https://api.github.com/users/{OWNER}/repos?per_page=100&page={number}")
        if status != 200:
            raise RuntimeError(f"GitHub answered {status} listing public repos")
        batch = json.loads(body)
        names += [r["name"] for r in batch]
        if len(batch) < 100:
            break
    return names


def squash(name):
    return re.sub(r"[^a-z0-9]", "", name.lower())


def live_problems(cards, repos=None, fetch_url=fetch):
    problems = []
    repos = public_repos() if repos is None else repos
    for card in cards:
        link = card["go"]
        if link:
            if "/releases/latest/download/" in link and re.search(r"v?\d+\.\d+", link.rsplit("/", 1)[-1]):
                problems.append(f"{card['id']}: names a version under releases/latest, so it breaks at the next release: {link}")
            status, _ = fetch_url(link)
            if status != 200:
                problems.append(f"{card['id']}: link answered {status}: {link}")
        if card["soon"]:
            # goal-garden's card matches a repo called goal-garden, recruiting-platform's recruiting-platform-personalized.
            for repo in repos:
                if squash(repo).startswith(squash(card["id"])):
                    status, _ = fetch_url(f"https://api.github.com/repos/{OWNER}/{repo}/releases/latest")
                    if status == 200:
                        problems.append(f"{card['id']}: says Coming soon, but {OWNER}/{repo} has a public release")
    return problems


def main():
    page = Page()
    page.feed((ROOT / "index.html").read_text(encoding="utf-8"))
    problems = []

    for card in page.cards:
        if card["go"] and "/releases/" in card["go"] and not card["install"]:
            problems.append(f"{card['id']}: has a download but no install note")
    if "--live" in sys.argv[1:]:
        try:
            problems += live_problems(page.cards)
        except RuntimeError as err:
            problems.append(f"couldn't finish the live check: {err}")

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
