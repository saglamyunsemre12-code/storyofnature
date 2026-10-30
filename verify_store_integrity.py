#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

SITE_DIR = "/Users/emre/.gemini/antigravity/scratch/story-of-nature/site"
HTML_FILES = [
    "index.html",
    "pure-essence.html",
    "golden-immunity.html",
    "gece-masali.html",
    "saf-bebek-kolajeni.html",
    "rosemary-elixir.html",
    "14-gunluk-paket.html",
    "product.html"
]

print("=== VERIFYING STORE INTEGRITY & ASSET REFERENCES ===")

all_ok = True

for f in HTML_FILES:
    path = os.path.join(SITE_DIR, f)
    if not os.path.exists(path):
        print(f"❌ Missing file: {f}")
        all_ok = False
        continue
    
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Check image sources
    img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    missing_imgs = []
    for src in img_srcs:
        if src.startswith("http") or src.startswith("data:"):
            continue
        asset_path = os.path.join(SITE_DIR, src)
        if not os.path.exists(asset_path):
            missing_imgs.append(src)
    
    # Check internal links
    links = re.findall(r'href=["\']([^"\'#]+\.html[^"\']*)["\']', content)
    missing_links = []
    for link in links:
        target = link.split("?")[0].split("#")[0]
        if not target.startswith("http"):
            target_path = os.path.join(SITE_DIR, target)
            if not os.path.exists(target_path):
                missing_links.append(link)
                
    print(f"📄 {f:24} | Size: {len(content):6} B | Images: {len(img_srcs):2} ({'OK' if not missing_imgs else 'MISSING: ' + str(missing_imgs)}) | Links: {len(links):2} ({'OK' if not missing_links else 'BROKEN: ' + str(missing_links)})")
    if missing_imgs or missing_links:
        all_ok = False

if all_ok:
    print("\n✅ ALL 8 HTML FILES, INTERNAL LINKS, AND ASSETS ARE 100% HEALTHY AND VERIFIED!")
else:
    print("\n❌ SOME ASSETS OR LINKS ARE BROKEN!")
