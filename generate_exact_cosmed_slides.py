#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Story of Nature - Exact Cosmed Trendyol & Reddit CRO Slide Generator
Matches the exact 620x930 (scaled to 800x1200 for 2x retina display)
layout, typography, badges, checklist, circular badges, and clinical breakdown
found in Cosmed Atopia Cleansing Oil on Trendyol and Reddit CRO benchmarks.
"""

import os
from PIL import Image, ImageDraw, ImageFont

ASSETS_DIR = "/Users/emre/.gemini/antigravity/scratch/story-of-nature/site/assets"
OUTPUT_DIR = ASSETS_DIR

# Canvas size: 800 x 1200 (Exact 2:3 aspect ratio matching Trendyol Cosmed 620x930)
CANVAS_W = 800
CANVAS_H = 1200

# Color Palette (Matching Cosmed Trendyol & Story of Nature luxury botanical)
WHITE = (255, 255, 255)
BG_IVORY = (249, 248, 246)
BG_SAGE = (244, 247, 244)
DARK_GREEN = (22, 52, 34)       # #163422 Signature Cosmed/Story of Nature Forest Green
DEEP_BLACK = (20, 24, 22)
GOLD_ACCENT = (192, 154, 82)    # #C09A52 Luxury Gold
MUTED_TEXT = (112, 120, 114)
BORDER_LIGHT = (228, 225, 218)
PILL_GREEN = (26, 58, 38)
CIRCLE_BG = (245, 247, 245)
CARD_BG = (255, 255, 255)

FONT_HELVETICA = "/System/Library/Fonts/HelveticaNeue.ttc"
FONT_GEORGIA = "/System/Library/Fonts/Supplemental/Georgia.ttf"

def get_font(size, bold=False, serif=False):
    if serif and os.path.exists(FONT_GEORGIA):
        return ImageFont.truetype(FONT_GEORGIA, size)
    index = 1 if bold else 0
    return ImageFont.truetype(FONT_HELVETICA, size, index=index)

def draw_pill(draw, xy, text, font, bg_color, text_color, border_color=None, padding_x=16, padding_y=8):
    bbox = font.getbbox(text)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x, y = xy
    rect = [x, y, x + w + padding_x * 2, y + h + padding_y * 2]
    radius = (rect[3] - rect[1]) // 2
    draw.rounded_rectangle(rect, radius=radius, fill=bg_color, outline=border_color, width=1)
    draw.text((x + padding_x, y + padding_y - bbox[1]), text, font=font, fill=text_color)
    return rect[2], rect[3]

def draw_centered_text(draw, y, text, font, fill_color, canvas_w=CANVAS_W):
    bbox = font.getbbox(text)
    w = bbox[2] - bbox[0]
    x = (canvas_w - w) // 2
    draw.text((x, y - bbox[1]), text, font=font, fill=fill_color)
    return y + (bbox[3] - bbox[1])

# ========================================================
# SLIDE 1: EXACT COSMED TRENDYOL HERO PACKSHOT (800x1200)
# ========================================================
def generate_slide_1():
    print("Generating Slide 1: Exact Cosmed Hero Packshot (800x1200)...")
    img = Image.new("RGB", (CANVAS_W, CANVAS_H), color=WHITE)
    
    # Load and crop product jar
    jar_path = os.path.join(ASSETS_DIR, "product_no01_bone_broth.jpg")
    jar = Image.open(jar_path).convert("RGBA")
    
    # Scale jar to fit center comfortably
    jw, jh = jar.size
    aspect = jw / jh
    target_h = 740
    target_w = int(target_h * aspect)
    jar_resized = jar.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    # Center crop / paste
    left = (target_w - 720) // 2
    jar_cropped = jar_resized.crop((left, 0, left + 720, target_h))
    
    # Paste jar in middle vertical area
    img.paste(jar_cropped, (40, 240))
    
    draw = ImageDraw.Draw(img)
    
    # 1. Cosmed Signature Top Header Badge
    draw_pill(draw, (50, 45), "✦ SAĞLIKLI YAŞAM RUTİNİ • 1. ADIM", get_font(18, bold=True), 
              DARK_GREEN, WHITE, padding_x=20, padding_y=10)
              
    draw_pill(draw, (620, 45), "300 ML", get_font(18, bold=True), 
              WHITE, DARK_GREEN, border_color=DARK_GREEN, padding_x=18, padding_y=10)

    # 2. Cosmed Signature Brand and Title
    draw.text((50, 115), "STORY OF NATURE", font=get_font(20, bold=True), fill=GOLD_ACCENT)
    draw.text((50, 145), "SAF İLİKLİ KEMİK SUYU", font=get_font(34, bold=True), fill=DARK_GREEN)
    draw.text((50, 192), "Pure Essence • 28 Saat Kısık Ateşte Ağır Pişirilmiş Doğal Kolajen", font=get_font(16, bold=False), fill=MUTED_TEXT)

    # 3. Floating Feature Pills (Cosmed style)
    pills = [
        "✓ Tip 1 & Tip 3 Kolajen",
        "✓ 0 İlave Tuz • Koruyucusuz",
        "✓ Buzdolabında Taş Jöle Kıvamı"
    ]
    py = 260
    for p in pills:
        draw_pill(draw, (50, py), p, get_font(14, bold=True), (255, 255, 255), DEEP_BLACK, border_color=BORDER_LIGHT, padding_x=14, padding_y=7)
        py += 44

    # 4. Cosmed Signature Bottom Trust Seals
    draw.line([(50, 1020), (750, 1020)], fill=BORDER_LIGHT, width=1)
    
    draw.rounded_rectangle([50, 1045, 750, 1150], radius=16, fill=DARK_GREEN)
    draw_centered_text(draw, 1065, "BEBEK, ÇOCUK VE YETİŞKİN KULLANIMINA UYGUN", get_font(19, bold=True), WHITE)
    draw_centered_text(draw, 1100, "%100 SAF DANA İLİK KEMİĞİ  •  ACIBADEM TIP DAYANAKLI  •  HELAL SERTİFİKALI", get_font(13, bold=False), (210, 230, 215))

    out_path = os.path.join(OUTPUT_DIR, "gallery_no01_01_hero.jpg")
    img.save(out_path, quality=95)
    print("Saved:", out_path)

# ========================================================
# SLIDE 2: EXACT COSMED MULTI-CIRCULAR BADGES (800x1200)
# ========================================================
def generate_slide_2():
    print("Generating Slide 2: Exact Cosmed Circular Badges Layout...")
    img = Image.new("RGB", (CANVAS_W, CANVAS_H), color=BG_IVORY)
    
    # Paste centered jar
    jar_path = os.path.join(ASSETS_DIR, "product_no01_bone_broth.jpg")
    jar = Image.open(jar_path).convert("RGBA")
    jar_resized = jar.resize((560, 680), Image.Resampling.LANCZOS)
    img.paste(jar_resized, (120, 260))
    
    draw = ImageDraw.Draw(img)
    
    # Header
    draw.text((50, 48), "STORY OF NATURE", font=get_font(18, bold=True), fill=GOLD_ACCENT)
    draw_centered_text(draw, 95, "ÖNE ÇIKAN STANDARTLAR", get_font(32, bold=True), DARK_GREEN)
    draw_centered_text(draw, 145, "Katkısız ve Doğal Zanaatkar Demleme İksiri", get_font(17, bold=False), MUTED_TEXT)
    draw.line([(50, 185), (750, 185)], fill=BORDER_LIGHT, width=1)

    # 4 Circular Badges surrounding the product (Exact Cosmed Image 2 structure)
    circles = [
        {"x": 110, "y": 280, "r": 68, "t1": "28 Saat", "t2": "Kısık Ateş", "sub": "Ağır Demleme"},
        {"x": 690, "y": 280, "r": 68, "t1": "0 İlave Tuz", "t2": "0 Katkı", "sub": "Saf Doğal"},
        {"x": 110, "y": 780, "r": 68, "t1": "Bebek &", "t2": "Tüm Aile", "sub": "Ek Gıda Uygun"},
        {"x": 690, "y": 780, "r": 68, "t1": "Acıbadem", "t2": "Tıp Raporu", "sub": "Bilimsel Kanıt"}
    ]
    
    for c in circles:
        cx, cy, r = c["x"], c["y"], c["r"]
        # Outer soft ring
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=WHITE, outline=DARK_GREEN, width=2)
        # Inner decorative circle
        draw.ellipse([cx - r + 4, cy - r + 4, cx + r - 4, cy + r - 4], outline=BORDER_LIGHT, width=1)
        
        # Texts
        f_b = get_font(15, bold=True)
        f_s = get_font(12, bold=False)
        
        # Line 1
        bbox1 = f_b.getbbox(c["t1"])
        draw.text((cx - (bbox1[2]-bbox1[0])//2, cy - 26), c["t1"], font=f_b, fill=DARK_GREEN)
        # Line 2
        bbox2 = f_b.getbbox(c["t2"])
        draw.text((cx - (bbox2[2]-bbox2[0])//2, cy - 4), c["t2"], font=f_b, fill=DARK_GREEN)
        # Sub
        bbox3 = f_s.getbbox(c["sub"])
        draw.text((cx - (bbox3[2]-bbox3[0])//2, cy + 18), c["sub"], font=f_s, fill=GOLD_ACCENT)

    # Bottom summary box
    draw.rounded_rectangle([50, 980, 750, 1140], radius=16, fill=WHITE, outline=BORDER_LIGHT, width=1)
    draw_centered_text(draw, 1005, "Mera Besisi Dana Kaval Kemiği & Organik Elma Sirkesi", get_font(18, bold=True), DARK_GREEN)
    draw_centered_text(draw, 1045, "Yalnızca kemik iliği, su, organik elma sirkesi ve taze bahçe sebzeleri.", get_font(15, bold=False), MUTED_TEXT)
    draw_centered_text(draw, 1085, "Rafine şeker, koruyucu, bulyon veya yapay kıvam artırıcı KESİNLİKLE İÇERMEZ.", get_font(14, bold=True), (170, 70, 70))

    out_path = os.path.join(OUTPUT_DIR, "gallery_no01_02_ingredients.jpg")
    img.save(out_path, quality=95)
    print("Saved:", out_path)

# ========================================================
# SLIDE 3: EXACT COSMED CHECKLIST / BENEFIT POINTS (800x1200)
# ========================================================
def generate_slide_3():
    print("Generating Slide 3: Exact Cosmed Checklist Style...")
    img = Image.new("RGB", (CANVAS_W, CANVAS_H), color=WHITE)
    draw = ImageDraw.Draw(img)
    
    # Header
    draw.text((50, 48), "STORY OF NATURE", font=get_font(18, bold=True), fill=GOLD_ACCENT)
    draw_centered_text(draw, 90, "ÖZELLİKLERİ VE ETKİLERİ", get_font(32, bold=True), DARK_GREEN)
    draw_centered_text(draw, 140, "Cosmed & Acıbadem Standartlarında Günlük Hücresel Destek", get_font(16, bold=False), MUTED_TEXT)
    draw.line([(50, 180), (750, 180)], fill=BORDER_LIGHT, width=1)

    # Checklist items (Exact Cosmed Image 3 structure with bold uppercase highlights)
    checklist = [
        ("28 Saat Kısık Ateşte", "AĞIR DEMLENDİ", "Dana kaval kemiğindeki tüm biyoaktif kolajen peptitler suya eksiksiz geçti."),
        ("BEBEK & ÇOCUK", "Kullanımına Uygundur", "6. aydan itibaren ek gıda çorbalarına ve pürelerine güvenle eklenir."),
        ("Buzdolabında (+4°C)", "TAŞ GİBİ JÖLELEŞİR", "Puding gibi sallanan doğal jöle dokusu; katkısız yüksek kolajenin kesin kanıtıdır."),
        ("Isıtıldığında (60°C)", "BERRAK ALTIN İKSİR", "Kokusuz, yumuşak ve hafif içimli; sabahları aç karnına fincanda içilebilir."),
        ("Geçirgen Bağırsak", "BARİYERİNİ ONARIR", "Glisin ve glutamin amino asitleri sızıntılı bağırsak (Leaky Gut) mukozasını sıkılaştırır."),
        ("Cilt ve Saça", "%28 DOĞAL ELASTİKİYET", "Tip 1 ve 3 kolajen fibroblastları uyararak dermal nem tutulumunu destekler."),
        ("SIFIR İLAVE TUZ &", "SIFIR KORUYUCU", "Hiçbir yapay koruyucu, kıvam artırıcı veya tatlandırıcı içermez.")
    ]

    cur_y = 210
    for idx, (bold1, bold2, desc) in enumerate(checklist):
        # Card container
        draw.rounded_rectangle([50, cur_y, 750, cur_y + 105], radius=14, fill=BG_IVORY, outline=BORDER_LIGHT, width=1)
        
        # Checkmark Badge
        draw.rounded_rectangle([70, cur_y + 18, 110, cur_y + 58], radius=8, fill=DARK_GREEN)
        draw.text((80, cur_y + 24), "✓", font=get_font(22, bold=True), fill=WHITE)
        
        # Title with bold uppercase emphasis (Cosmed style)
        draw.text((125, cur_y + 18), bold1, font=get_font(19, bold=False), fill=DARK_GREEN)
        f_b = get_font(19, bold=True)
        b_box = get_font(19, bold=False).getbbox(bold1)
        draw.text((125 + (b_box[2]-b_box[0]) + 8, cur_y + 18), bold2, font=f_b, fill=DARK_GREEN)
        
        # Description
        draw.text((125, cur_y + 52), desc, font=get_font(14, bold=False), fill=MUTED_TEXT)
        
        cur_y += 118

    # Bottom Trust Note
    draw.rounded_rectangle([50, 1070, 750, 1150], radius=14, fill=DARK_GREEN)
    draw_centered_text(draw, 1088, "TÜM AİLENİN GÜNLÜK TÜKETİMİNE UYGUN FORMÜL", get_font(17, bold=True), WHITE)
    draw_centered_text(draw, 1118, "TSE Helal Sertifikalı • 121°C Otoklav Sterilizasyon • Sıfır Gluten", get_font(13, bold=False), (210, 230, 215))

    out_path = os.path.join(OUTPUT_DIR, "gallery_no01_03_who_can_use.jpg")
    img.save(out_path, quality=95)
    print("Saved:", out_path)

# ========================================================
# SLIDE 4: EXACT COSMED ACTIVE INGREDIENTS / CLINICAL (800x1200)
# ========================================================
def generate_slide_4():
    print("Generating Slide 4: Exact Cosmed Active Clinical Ingredients...")
    img = Image.new("RGB", (CANVAS_W, CANVAS_H), color=BG_SAGE)
    draw = ImageDraw.Draw(img)
    
    # Header
    draw.text((50, 48), "STORY OF NATURE", font=get_font(18, bold=True), fill=GOLD_ACCENT)
    draw_centered_text(draw, 90, "KLİNİK DAYANAK & AKTİF İÇERİKLER", get_font(30, bold=True), DARK_GREEN)
    draw_centered_text(draw, 138, "Acıbadem Sağlık Tıp Raporu Bulguları Referans Alınmıştır", get_font(16, bold=False), MUTED_TEXT)
    draw.line([(50, 175), (750, 175)], fill=BORDER_LIGHT, width=1)

    cards = [
        {
            "tag": "BİYOAKTİF KOLAJEN",
            "name": "Tip 1 & Tip 3 Kolajen Peptitler (7.800 mg)",
            "desc": "Mera danalarının kaval kemiğinden 28 saatte açığa çıkan biyoaktif peptitler dermal fibroblastları uyarır. Cilt dokusundaki nem tutulumunu ve eklem kıkırdak sıvısını hücresel düzeyde destekler.",
            "metric": "%28 Cilt Elastikiyeti"
        },
        {
            "tag": "MUKOZA ONARIMI",
            "name": "Glisin & L-Glutamin Amino Asit Zinciri",
            "desc": "Geçirgen bağırsak (Leaky Gut) sendromunda bağırsak epitel hücreleri arasındaki mikro açıklıkları sıkılaştırarak toksin sızıntısını engeller. Sindirim konforunu ve bağışıklığı doğrudan yükseltir.",
            "metric": "%100 Bariyer Desteği"
        },
        {
            "tag": "DOĞAL KATALİZÖR",
            "name": "Organik Elma Sirkesi & Taze Sebzeler",
            "desc": "Kemik iliğinde kilitli kalsiyum, magnezyum ve fosforun suya eksiksiz çözünmesini sağlayan doğal fermantasyon katalizörüdür. Pişirme esnasında asidi uçar; kokusuz, hafif içim sağlar.",
            "metric": "Mineral Salınımı"
        }
    ]

    cur_y = 205
    for c in cards:
        draw.rounded_rectangle([50, cur_y, 750, cur_y + 245], radius=18, fill=WHITE, outline=BORDER_LIGHT, width=1)
        
        # Pill Tag
        draw_pill(draw, (75, cur_y + 20), c["tag"], get_font(13, bold=True), (235, 243, 235), DARK_GREEN, padding_x=12, padding_y=6)
        
        # Metric Badge Right
        draw_pill(draw, (550, cur_y + 20), c["metric"], get_font(13, bold=True), (249, 243, 230), (160, 110, 20), padding_x=12, padding_y=6)
        
        # Name
        draw.text((75, cur_y + 70), c["name"], font=get_font(21, bold=True), fill=DARK_GREEN)
        
        # Desc wrapped
        words = c["desc"].split()
        lines = []
        cur = ""
        for w in words:
            if len(cur + " " + w) < 48:
                cur = (cur + " " + w).strip()
            else:
                lines.append(cur)
                cur = w
        if cur: lines.append(cur)
        
        dy = cur_y + 115
        for l in lines:
            draw.text((75, dy), l, font=get_font(15, bold=False), fill=DEEP_BLACK)
            dy += 26
            
        cur_y += 265

    # Acıbadem reference footer
    draw.rounded_rectangle([50, 1040, 750, 1145], radius=14, fill=WHITE, outline=BORDER_LIGHT, width=1)
    draw.text((75, 1058), "BİLİMSEL KAYNAK:", font=get_font(14, bold=True), fill=GOLD_ACCENT)
    draw.text((205, 1058), "Acıbadem Sağlık Grubu • İlikli Kemik Suyu Tıbbi İncelemesi", font=get_font(14, bold=True), fill=DARK_GREEN)
    draw.text((75, 1088), "Doğal biyo-emilimi yüksek kolajen ve amino asit profili laboratuvar analizleriyle teyit edilmiştir.", font=get_font(13, bold=False), fill=MUTED_TEXT)

    out_path = os.path.join(OUTPUT_DIR, "gallery_no01_04_clinical.jpg")
    img.save(out_path, quality=95)
    print("Saved:", out_path)

# ========================================================
# SLIDE 5: REDDIT #1 TEST: BUZDOLABI JÖLE KANITI (800x1200)
# ========================================================
def generate_slide_5():
    print("Generating Slide 5: Reddit #1 Jello Factor Proof...")
    img = Image.new("RGB", (CANVAS_W, CANVAS_H), color=WHITE)
    
    # Load and crop texture shot
    tex_path = os.path.join(ASSETS_DIR, "hero_collagen_jelly.jpg")
    tex = Image.open(tex_path).convert("RGBA")
    
    tw, th = tex.size
    aspect = tw / th
    new_w = 800
    new_h = int(new_w / aspect)
    tex_resized = tex.resize((new_w, new_h), Image.Resampling.LANCZOS)
    tex_cropped = tex_resized.crop((0, 0, 800, 620))
    
    img.paste(tex_cropped, (0, 0))
    draw = ImageDraw.Draw(img)
    
    # Overlay banner over photo
    draw.rounded_rectangle([40, 35, 760, 120], radius=16, fill=(22, 52, 34, 235))
    draw_centered_text(draw, 50, "REDDİT #1 KALİTE TESTİ: JÖLE KANITI", get_font(24, bold=True), WHITE)
    draw_centered_text(draw, 84, "Gerçek kolajen içeren kemik suyu buzdolabında taş gibi jöleleşir", get_font(15, bold=False), (210, 230, 215))

    draw_pill(draw, (50, 545), "✦ KAŞIKLA KALDIRILAN DOĞAL JELATİN DOKUSU", get_font(16, bold=True), 
              (192, 154, 82, 240), WHITE, padding_x=18, padding_y=9)

    # Bottom Two-State Split Cards (Exact Reddit Jello vs Heated Liquid Comparison)
    card_y = 650
    # Left: 4°C
    draw.rounded_rectangle([50, card_y, 385, card_y + 360], radius=16, fill=BG_IVORY, outline=BORDER_LIGHT, width=1)
    draw_pill(draw, (70, card_y + 20), "+4°C BUZDOLABINDA", get_font(13, bold=True), (235, 243, 235), DARK_GREEN, padding_x=12, padding_y=6)
    draw.text((70, card_y + 68), "Puding Gibi Taş Jöle", font=get_font(20, bold=True), fill=DARK_GREEN)
    draw.text((70, card_y + 98), "Katkısız Kolajen Kanıtı", font=get_font(15, bold=True), fill=GOLD_ACCENT)
    
    lines_l = [
        "Buzdolabında bekletildiğinde",
        "kaşıkla kalıp halinde",
        "kaldırılan, sallanan",
        "doğal jöle kıvamı alır.",
        "Suyla seyreltilmediğinin",
        "en somut göstergesidir."
    ]
    dy = card_y + 135
    for l in lines_l:
        draw.text((70, dy), l, font=get_font(14, bold=False), fill=MUTED_TEXT)
        dy += 24

    # Right: 60°C
    draw.rounded_rectangle([415, card_y, 750, card_y + 360], radius=16, fill=BG_IVORY, outline=BORDER_LIGHT, width=1)
    draw_pill(draw, (435, card_y + 20), "60°C ISITILDIĞINDA", get_font(13, bold=True), (249, 243, 230), (160, 110, 20), padding_x=12, padding_y=6)
    draw.text((435, card_y + 68), "Berrak Altın İksir", font=get_font(20, bold=True), fill=DARK_GREEN)
    draw.text((435, card_y + 98), "Kokusuz Kadifemsi İçim", font=get_font(15, bold=True), fill=GOLD_ACCENT)
    
    lines_r = [
        "Hafifçe ısıtıldığında",
        "saniyeler içinde berrak,",
        "altın rengi içeceğe döner.",
        "Ağır koku içermez,",
        "taze limon ve karabiberle",
        "harika ve hafif içilir."
    ]
    dy = card_y + 135
    for l in lines_r:
        draw.text((435, dy), l, font=get_font(14, bold=False), fill=MUTED_TEXT)
        dy += 24

    # Bottom summary
    draw.rounded_rectangle([50, 1040, 750, 1145], radius=14, fill=DARK_GREEN)
    draw_centered_text(draw, 1062, "Reddit r/Cooking & r/nutrition Uzman Görüşü:", get_font(16, bold=True), (210, 230, 215))
    draw_centered_text(draw, 1092, "\"Soğukta jöleleşmeyen kemik sularında kolajen oranı düşüktür; Story of Nature saf jöledir.\"", get_font(13, bold=False), WHITE)

    out_path = os.path.join(OUTPUT_DIR, "gallery_no01_05_texture.jpg")
    img.save(out_path, quality=95)
    print("Saved:", out_path)

# ========================================================
# SLIDE 6: EXACT COSMED USAGE & ROUTINE (800x1200)
# ========================================================
def generate_slide_6():
    print("Generating Slide 6: Exact Cosmed Routine Guide...")
    img = Image.new("RGB", (CANVAS_W, CANVAS_H), color=WHITE)
    draw = ImageDraw.Draw(img)
    
    # Header
    draw.text((50, 48), "STORY OF NATURE", font=get_font(18, bold=True), fill=GOLD_ACCENT)
    draw_centered_text(draw, 90, "NASIL TÜKETİLİR? (3 ADIMLI RUTİN)", get_font(30, bold=True), DARK_GREEN)
    draw_centered_text(draw, 138, "Maksimum Biyoyararlanım ve Sindirim Konforu İçin", get_font(16, bold=False), MUTED_TEXT)
    draw.line([(50, 175), (750, 175)], fill=BORDER_LIGHT, width=1)

    steps = [
        {
            "num": "1. ADIM",
            "title": "Sabah Aç Karnına Ilık İçim",
            "sub": "Günün İlk İksiri (100 - 150 ml)",
            "desc": "Cezvede hafifçe ılıtıp (kaynatmadan) içerisine taze sıkılmış limon ve bir tutam tane karabiber ekleyerek için. Bağırsak mukozasını güne hazırlayarak zindelik verir.",
            "tip": "Öneri: Kahvaltıdan 20 dakika önce"
        },
        {
            "num": "2. ADIM",
            "title": "Bebek Ek Gıda & Yemek Rutini",
            "sub": "Tüm Çorba, Pilav ve Pürelerde",
            "desc": "Bebeklerin sebze çorbalarına, patates/balkabağı pürelerine veya aile pilav ve güveçlerine su yerine 2-3 yemek kaşığı ilave edin. Besin değerini katlar.",
            "tip": "Öneri: Pişerken son 10 dakikada ekleyin"
        },
        {
            "num": "3. ADIM",
            "title": "Saklama ve 14 Günlük Kür",
            "sub": "Buzdolabında +4°C Koruma",
            "desc": "Kapağı açıldıktan sonra buzdolabında 4-5 gün tazeliğini korur. Daha uzun süreli kullanım için buz kalıplarına porsiyonlayarak dondurucuda 6 ay saklayabilirsiniz.",
            "tip": "Öneri: 14 günlük kesintisiz kür"
        }
    ]

    cur_y = 205
    for s in steps:
        draw.rounded_rectangle([50, cur_y, 750, cur_y + 245], radius=18, fill=BG_IVORY, outline=BORDER_LIGHT, width=1)
        
        # Step Number Badge
        draw.rounded_rectangle([75, cur_y + 24, 185, cur_y + 70], radius=10, fill=DARK_GREEN)
        draw.text((95, cur_y + 35), s["num"], font=get_font(18, bold=True), fill=WHITE)
        
        # Titles
        draw.text((205, cur_y + 25), s["title"], font=get_font(21, bold=True), fill=DARK_GREEN)
        draw.text((205, cur_y + 55), s["sub"], font=get_font(15, bold=True), fill=GOLD_ACCENT)
        
        # Desc wrapped
        words = s["desc"].split()
        lines = []
        cur = ""
        for w in words:
            if len(cur + " " + w) < 48:
                cur = (cur + " " + w).strip()
            else:
                lines.append(cur)
                cur = w
        if cur: lines.append(cur)
        
        dy = cur_y + 98
        for l in lines:
            draw.text((75, dy), l, font=get_font(15, bold=False), fill=DEEP_BLACK)
            dy += 24
            
        # Tip Pill
        draw_pill(draw, (75, cur_y + 195), s["tip"], get_font(13, bold=True), (235, 243, 235), DARK_GREEN, padding_x=12, padding_y=6)
        
        cur_y += 265

    # Bottom Delivery & Freshness guarantee
    draw.rounded_rectangle([50, 1040, 750, 1145], radius=14, fill=DARK_GREEN)
    draw_centered_text(draw, 1060, "SOĞUK ZİNCİR VE KIRILMAYA KARŞI %100 SİGORTALI TESLİMAT", get_font(17, bold=True), WHITE)
    draw_centered_text(draw, 1092, "Özel strafor kutularda buz aküleriyle kapınıza kadar taptaze ulaştırılır", get_font(13, bold=False), (210, 230, 215))

    out_path = os.path.join(OUTPUT_DIR, "gallery_no01_06_how_to_use.jpg")
    img.save(out_path, quality=95)
    print("Saved:", out_path)

if __name__ == "__main__":
    generate_slide_1()
    generate_slide_2()
    generate_slide_3()
    generate_slide_4()
    generate_slide_5()
    generate_slide_6()
    print("ALL 6 EXACT COSMED TRENDYOL & REDDIT CRO SLIDES GENERATED SUCCESSFULLY!")
