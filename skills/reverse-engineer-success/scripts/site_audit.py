#!/usr/bin/env python3
"""Audit public sites: title, tech and payment signals, sitemap size, blog URLs and lastmod by month.

Usage: site_audit.py <hostname> [<hostname> ...]
"""
import re,sys,urllib.request,collections,gzip,ssl
sites=sys.argv[1:]
UA={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36'}
def get(u):
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=15)
        b=r.read(6_000_000)
        if b[:2]==b'\x1f\x8b': b=gzip.decompress(b)
        return r.status,b.decode('utf8','ignore'),r.geturl()
    except Exception as e:
        return 0,'',str(e)[:80]
def locs(u,seen=None,d=0):
    s,b,_=get(u)
    out=re.findall(r'<url>\s*<loc>\s*([^<\s]+)\s*</loc>(?:\s*<lastmod>\s*([^<\s]+))?',b)
    if not out and d<2:
        res=[]
        for sm in re.findall(r'<sitemap>\s*<loc>\s*([^<\s]+)',b)[:10]:
            res+=locs(sm,d=d+1)
        return res
    return out
for host in sites:
    s,h,f=get('https://'+host+'/')
    t=re.findall(r'<title[^>]*>(.*?)</title>',h,re.S)
    gen=re.findall(r'<meta name="generator" content="([^"]+)"',h)
    pay=sorted(set(k for k in ['stripe','paddle','lemonsqueezy','apps.apple.com','play.google.com','revenuecat','posthog','plausible','datafast','gtag','clarity'] if k in h.lower()))
    u=locs('https://'+host+'/sitemap.xml') or locs('https://'+host+'/sitemap-index.xml') or locs('https://'+host+'/sitemap_index.xml')
    blog=[x for x in u if re.search(r'/(blog|guides?|articles?|learn|posts?)/',x[0])]
    months=collections.Counter(x[1][:7] for x in blog if x[1])
    print(f'\n=== {host} status={s} title={t[0].strip()[:70] if t else None} gen={gen[:1]} signals={pay}')
    print(f'sitemap_urls={len(u)} blogish={len(blog)} lastmod_months={sorted(months.items())[-6:]}')
    for x in blog[:5]: print('  ',x[0])
