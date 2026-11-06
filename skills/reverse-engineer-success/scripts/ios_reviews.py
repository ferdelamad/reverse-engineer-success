#!/usr/bin/env python3
"""Print recent US App Store reviews rated 1-2 stars. The feed returns few reviews, so treat it as a sample.

Usage: ios_reviews.py <track_id> [<track_id> ...]
"""
import json
import sys
import urllib.request

for track in sys.argv[1:]:
    url = f"https://itunes.apple.com/us/rss/customerreviews/id={track}/sortby=mostrecent/json"
    feed = json.load(urllib.request.urlopen(url, timeout=30))["feed"]
    entries = feed.get("entry", [])
    entries = entries if isinstance(entries, list) else [entries]
    reviews = [e for e in entries if "im:rating" in e]
    print(f"== {track}: {len(reviews)} recent reviews")
    for e in reviews:
        if int(e["im:rating"]["label"]) <= 2:
            print(" ", e["im:rating"]["label"], e["content"]["label"][:200].replace("\n", " "))
