#!/usr/bin/env python3
"""Audit articles: word count, schema types, headings, store links and internal links.

Usage: article_audit.py <url> [<url> ...]
"""
import re,sys,urllib.request,html
UA={'User-Agent':'Mozilla/5.0 (Macintosh) AppleWebKit/537.36 Chrome/120 Safari/537.36'}
for u in sys.argv[1:]:
    h=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=20).read().decode('utf8','ignore')
    body=re.sub(r'<(script|style)[^>]*>.*?</\1>','',h,flags=re.S)
    heads=[re.sub('<[^>]+>','',x).strip() for x in re.findall(r'<h[12][^>]*>(.*?)</h[12]>',body,re.S)]
    text=html.unescape(re.sub(r'<[^>]+>',' ',body)); words=len(text.split())
    print('\n==',u,'words',words,'jsonld',sorted(set(re.findall(r'"@type"\s*:\s*"(\w+)"',h)))[:10])
    print('emdash',text.count('—'),'store_links',len(re.findall('apps.apple.com|play.google.com',h)),'internal_blog_links',len(set(re.findall(r'href="(/blog/[^"]+)"',h))))
    print('heads',heads[:14])
    print('start:',' '.join(text.split())[:420])
