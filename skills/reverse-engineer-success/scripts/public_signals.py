#!/usr/bin/env python3
"""Look for public first-party signals: stats pages, pricing, sitemap sections, npm and GitHub traction.

Usage: public_signals.py <hostname> [--npm <package>] [--github <owner/repo>]
"""
import argparse
import collections
import json
import re
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Macintosh) AppleWebKit/537.36 Chrome/120 Safari/537.36"}
PATHS = ["/stats", "/api/stats", "/open", "/open-startup", "/metrics", "/transparency", "/pricing", "/llms.txt"]


def fetch(url, limit=2_000_000):
    try:
        response = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=15)
        return response.status, response.geturl(), response.read(limit).decode("utf8", "ignore")
    except Exception as e:
        return getattr(e, "code", 0), url, ""


def fetch_json(url):
    status, _, body = fetch(url, 20_000_000)
    try:
        return json.loads(body) if status == 200 else None
    except ValueError:
        return None


parser = argparse.ArgumentParser()
parser.add_argument("host")
parser.add_argument("--npm")
parser.add_argument("--github")
args = parser.parse_args()

print(f"== Candidate pages on {args.host}")
for path in PATHS:
    status, final, body = fetch(f"https://{args.host}{path}")
    kind = "json" if body.lstrip()[:1] in ("{", "[") else "html/text"
    moved = f" -> {final}" if final.rstrip("/") != f"https://{args.host}{path}".rstrip("/") else ""
    print(f"{status or 'ERR'} {path} {kind} {len(body)} bytes{moved}")

status, _, sitemap = fetch(f"https://{args.host}/sitemap.xml", 6_000_000)
urls = re.findall(r"<url>\s*<loc>\s*([^<\s]+)", sitemap)
if not urls:
    for child in re.findall(r"<sitemap>\s*<loc>\s*([^<\s]+)", sitemap)[:10]:
        urls += re.findall(r"<url>\s*<loc>\s*([^<\s]+)", fetch(child, 6_000_000)[2])
sections = collections.Counter(u.split("/", 4)[3] or "root" if u.count("/") > 2 else "root" for u in urls)
print(f"\n== Sitemap: {len(urls)} URLs")
print(sections.most_common(15))

if args.npm:
    print(f"\n== npm: {args.npm}")
    month = fetch_json(f"https://api.npmjs.org/downloads/point/last-month/{args.npm}")
    year = fetch_json(f"https://api.npmjs.org/downloads/range/last-year/{args.npm}")
    print("last month:", month.get("downloads") if month else "unavailable")
    if year:
        totals = collections.Counter()
        for day in year["downloads"]:
            totals[day["day"][:7]] += day["downloads"]
        print("by month:", dict(sorted(totals.items())))

if args.github:
    print(f"\n== GitHub: {args.github}")
    repo = fetch_json(f"https://api.github.com/repos/{args.github}")
    if repo:
        print({k: repo.get(k) for k in ["stargazers_count", "forks_count", "open_issues_count", "created_at", "pushed_at", "homepage"]},
              "license:", (repo.get("license") or {}).get("spdx_id"))
    else:
        print("unavailable")
