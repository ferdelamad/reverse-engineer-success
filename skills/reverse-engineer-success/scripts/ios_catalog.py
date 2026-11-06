#!/usr/bin/env python3
"""List an App Store developer's US catalogue as CSV.

Usage: ios_catalog.py <artist_id>
"""
import csv
import json
import sys
import urllib.request

artist = sys.argv[1]
url = f"https://itunes.apple.com/lookup?id={artist}&entity=software&limit=200"
data = json.load(urllib.request.urlopen(url, timeout=30))
apps = [r for r in data["results"] if r.get("wrapperType") == "software"]
apps.sort(key=lambda r: r.get("userRatingCount", 0), reverse=True)

out = csv.writer(sys.stdout)
out.writerow(["app", "track_id", "seller", "genre", "released", "us_ratings", "us_avg_rating", "site"])
for r in apps:
    out.writerow([
        r.get("trackName"),
        r.get("trackId"),
        r.get("sellerName"),
        r.get("primaryGenreName"),
        r.get("releaseDate", "")[:10],
        r.get("userRatingCount", 0),
        round(r.get("averageUserRating", 0), 2),
        r.get("sellerUrl") or "",
    ])
