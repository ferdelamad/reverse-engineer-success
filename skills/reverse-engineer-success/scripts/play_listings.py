#!/usr/bin/env python3
"""Print title, install band and rating for Google Play packages as CSV.

Usage: play_listings.py <package> [<package> ...]
"""
import csv
import html
import re
import sys
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Macintosh) AppleWebKit/537.36 Chrome/120 Safari/537.36"}

out = csv.writer(sys.stdout)
out.writerow(["package", "title", "installs", "rating", "rating_count"])
for package in sys.argv[1:]:
    url = f"https://play.google.com/store/apps/details?id={package}&hl=en&gl=US"
    try:
        page = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20).read().decode("utf8", "ignore")
    except Exception as e:
        out.writerow([package, f"ERROR {e}", "", "", ""])
        continue
    title = re.findall(r"<title[^>]*>(.*?) - Apps on", page)
    installs = re.findall(r">([0-9.,]+[KM]?\+)<", page)
    rating = re.findall(r'"ratingValue":"([\d.]+)","ratingCount":"(\d+)"', page)
    out.writerow([
        package,
        html.unescape(title[0]) if title else "",
        installs[0] if installs else "",
        round(float(rating[0][0]), 2) if rating else "",
        rating[0][1] if rating else "",
    ])
