#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("/Users/emre/.gemini/antigravity/scratch/story-of-nature/site/generate_product_pages.py", "r", encoding="utf-8") as f:
    code = f.read()

# Replace the format call with safe token replacement
old_format = """        html_out = PDP_TEMPLATE.format(
            title=p["title"],
            category_eyebrow=p["category_eyebrow"],
            subtitle=p["subtitle"],
            price=p["price"],
            old_price=p["old_price"],
            vol=p["vol"],
            rating=p["rating"],
            review_count=p["review_count"],
            category_name=p["category_name"],
            lead=p["lead"],
            filename=p["filename"],
            first_image=first_slide["src"],
            first_pill=first_slide["pill"],
            first_label=first_slide["label"],
            thumbnails_html=thumbnails_html,
            highlights_html=highlights_html,
            table_rows_html=table_rows_html,
            objections_html=objections_html,
            recipe_title=p["recipe_title"],
            recipe_desc=p["recipe_desc"],
            recipe_time=p["recipe_time"],
            slides_json=json.dumps(p["slides"], ensure_ascii=False)
        )"""

new_format = """        html_out = PDP_TEMPLATE
        replacements = {
            "{title}": str(p["title"]),
            "{category_eyebrow}": str(p["category_eyebrow"]),
            "{subtitle}": str(p["subtitle"]),
            "{price}": str(p["price"]),
            "{old_price}": str(p["old_price"]),
            "{vol}": str(p["vol"]),
            "{rating}": str(p["rating"]),
            "{review_count}": str(p["review_count"]),
            "{category_name}": str(p["category_name"]),
            "{lead}": str(p["lead"]),
            "{filename}": str(p["filename"]),
            "{first_image}": str(first_slide["src"]),
            "{first_pill}": str(first_slide["pill"]),
            "{first_label}": str(first_slide["label"]),
            "{thumbnails_html}": str(thumbnails_html),
            "{highlights_html}": str(highlights_html),
            "{table_rows_html}": str(table_rows_html),
            "{objections_html}": str(objections_html),
            "{recipe_title}": str(p["recipe_title"]),
            "{recipe_desc}": str(p["recipe_desc"]),
            "{recipe_time}": str(p["recipe_time"]),
            "{slides_json}": json.dumps(p["slides"], ensure_ascii=False)
        }
        for k, v in replacements.items():
            html_out = html_out.replace(k, v)"""

if old_format in code:
    code = code.replace(old_format, new_format)
    with open("/Users/emre/.gemini/antigravity/scratch/story-of-nature/site/generate_product_pages.py", "w", encoding="utf-8") as f:
        f.write(code)
    print("Safely replaced format call with string replace dictionary!")
else:
    print("Warning: old_format not found exactly. Searching...")
