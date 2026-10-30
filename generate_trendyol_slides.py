#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Story of Nature - Trendyol / Cosmed Style Infographic Slide Generator
Generates ultra-high resolution (1200x1200) e-commerce visual assets mimicking
the exact infographic visual architecture of bestseller products like Cosmed Atopia on Trendyol.
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ASSETS_DIR = "/Users/emre/.gemini/antigravity/scratch/story-of-nature/site/assets"
OUTPUT_DIR = ASSETS_DIR

# Color Palette (Aesop / Apple / Cosmed Luxury Natural E-Commerce)
BG_COLOR = (248, 246, 240)        # #F8F6F0 Luxury Bone/Ivory
DARK_GREEN = (26, 56, 38)          # #1A3826 Signature Forest Green
DEEP_OBSIDIAN = (22, 30, 24)       # #161E18 Text Primary
GOLD_ACCENT = (197, 160, 89)       # #C5A059 Luxury Gold
LIGHT_SAGE = (235, 242, 235)       # #EBF2EB Pill Tint
WHITE = (255, 255, 255)
MUTED_TEXT = (110, 118, 112)       # Soft grey-green
BORDER_COLOR = (226, 222, 212)
CARD_BG = (255, 255, 255)
AMBER_TINT = (249, 243, 230)

# Fonts
FONT_HELVETICA_BOLD = "/System/Library/Fonts/HelveticaNeue.ttc"
FONT_HELVETICA_REG = "/System/Library/Fonts/HelveticaNeue.ttc"
FONT_GEORGIA = "/System/Library/Fonts/Supplemental/Georgia.ttf"

def get_font(size, bold=False, serif=False):
    if serif and os.path.exists(FONT_GEORGIA):
        return ImageFont.truetype(FONT_GEORGIA, size)
    index = 1 if bold else 0
    return ImageFont.truetype(FONT_HELVETICA_BOLD, size, index=index)

def draw_pill(draw, xy, text, font, bg_color, text_color, border_color=None, padding_x=24, padding_y=12):
    bbox = font.getbbox(text)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x, y = xy
    rect = [x, y, x + w + padding_x * 2, y + h + padding_y * 2]
    radius = (rect[3] - rect[1]) // 2
    draw.rounded_rectangle(rect, radius=radius, fill=bg_color, outline=border_color, width=1)
    text_x = x + padding_x
    text_y = y + padding_y - bbox[1]
    draw.text((text_x, text_y), text, font=font, fill=text_color)
    return rect[2], rect[3]

def draw_centered_text(draw, y, text, font, fill_color, img_width=1200):
    bbox = font.getbbox(text)
    w = bbox[2] - bbox[0]
    x = (img_width - w) // 2
    draw.text((x, y - bbox[1]), text, font=font, fill=fill_color)
    return y + (bbox[3] - bbox[1])

def add_header(img, draw, title, subtitle=None):
    # Top brand bar
    draw.text((60, 48), "STORY OF NATURE", font=get_font(20, bold=True), fill=GOLD_ACCENT)
    draw.text((1200 - 60 - 240, 48), "ARTISANAL WELLNESS", font=get_font(18, bold=False), fill=MUTED_TEXT)
    draw.line([(60, 84), (1140, 84)], fill=BORDER_COLOR, width=1)
    
    # Title & Subtitle
    y = 108
    y = draw_centered_text(draw, y, title, get_font(38, bold=True), DARK_GREEN)
    if subtitle:
        y += 8
        draw_centered_text(draw, y, subtitle, get_font(22, bold=False), MUTED_TEXT)
    return y + 36

# ==========================================
# SLIDE 1: HERO PACKSHOT & TRENDYOL BADGES
# ==========================================
def generate_slide_1():
    print("Generating Slide 1: Hero Packshot with Trendyol Badges...")
    # Load base image
    base_path = os.path.join(ASSETS_DIR, "product_no01_bone_broth.jpg")
    base_img = Image.open(base_path).convert("RGBA")
    
    # Target size: 1200x1200
    # Crop/fit base image neatly
    w, h = base_img.size
    aspect = w / h
    new_h = 1200
    new_w = int(new_h * aspect)
    base_resized = base_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Crop center to 1200x1200
    left = (new_w - 1200) // 2
    canvas = base_resized.crop((left, 0, left + 1200, 1200)).convert("RGBA")
    
    # Overlay layer with transparency
    overlay = Image.new("RGBA", (1200, 1200), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Subtle top & bottom vignette gradient for text contrast
    for y in range(220):
        alpha = int(180 * (1 - y / 220))
        draw.line([(0, y), (1200, y)], fill=(248, 246, 240, alpha))
    for y in range(980, 1200):
        alpha = int(190 * ((y - 980) / 220))
        draw.line([(0, y), (1200, y)], fill=(22, 30, 24, alpha))
    
    # Top Floating Badges (Cosmed Trendyol Signature Layout)
    # Badge 1: Bebek & Tüm Aile
    font_badge = get_font(22, bold=True)
    draw_pill(draw, (60, 50), "✦ BEBEK, ÇOCUK VE YETİŞKİN KULLANIMINA UYGUN", font_badge, 
              (26, 56, 38, 235), WHITE, padding_x=22, padding_y=12)
              
    # Badge 2: Hacim
    draw_pill(draw, (940, 50), "300 ml • CAM KAVANOZ", font_badge, 
              (255, 255, 255, 230), DARK_GREEN, border_color=(26, 56, 38), padding_x=20, padding_y=12)

    # Trust Callout Left Ribbon
    font_pill_small = get_font(18, bold=True)
    features = [
        "✓ Tip 1 & Tip 3 Biyoaktif Kolajen",
        "✓ 0 İlave Tuz • Koruyucusuz",
        "✓ Buzdolabında Taş Jöle Kıvamı",
        "✓ Acıbadem Tıp Raporu Dayanaklı"
    ]
    cur_y = 140
    for feat in features:
        draw_pill(draw, (60, cur_y), feat, font_pill_small, (255, 255, 255, 220), DEEP_OBSIDIAN, border_color=(220, 215, 205), padding_x=16, padding_y=8)
        cur_y += 48

    # Bottom Banner (Trendyol e-commerce signature footer)
    draw.rounded_rectangle([60, 1020, 1140, 1140], radius=18, fill=(26, 56, 38, 240), outline=(197, 160, 89), width=2)
    font_footer_title = get_font(28, bold=True)
    font_footer_sub = get_font(19, bold=False)
    
    draw.text((90, 1042), "NO. 01 • PURE ESSENCE İLİKLİ KEMİK SUYU", font=font_footer_title, fill=WHITE)
    draw.text((90, 1085), "28 Saat Kısık Ateşte Ağır Pişirilmiş • %100 Doğal Jelatin & Kolajen Deposu", font=font_footer_sub, fill=(220, 230, 220))
    
    # Gold Seal on right
    draw.rounded_rectangle([920, 1040, 1115, 1120], radius=12, fill=(197, 160, 89, 240))
    draw.text((935, 1052), "ORİJİNAL FORMÜL", font=get_font(15, bold=True), fill=WHITE)
    draw.text((945, 1076), "%100 SAF VE DOĞAL", font=get_font(14, bold=False), fill=(26, 56, 38))

    final = Image.alpha_composite(canvas, overlay).convert("RGB")
    out_path = os.path.join(OUTPUT_DIR, "gallery_no01_01_hero.jpg")
    final.save(out_path, quality=95)
    print(f"Saved: {out_path}")

# ==========================================
# SLIDE 2: AKTİF BİLEŞENLER & FORMÜL
# ==========================================
def generate_slide_2():
    print("Generating Slide 2: Active Ingredients Infographic...")
    img = Image.new("RGB", (1200, 1200), color=BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    start_y = add_header(img, draw, "AKTİF BİLEŞENLER VE DOĞAL FORMÜL", 
                         "Yalnızca 4 Saf Doğal Bileşen • Sıfır Koruyucu • Sıfır İlave Tuz")
    
    # 4 Ingredient Cards in 2x2 Grid
    cards = [
        {
            "num": "01",
            "title": "Dana Kaval Kemiği & İlik",
            "subtitle": "Tip 1 & Tip 3 Biyoaktif Kolajen",
            "desc": "Mera besisi genç danaların kaval ve eklem kemiklerinden 28 saatte çıkarılan yoğun kolajen, kalsiyum, magnezyum ve fosfor deposu.",
            "badge": "%100 Doğal Kolajen"
        },
        {
            "num": "02",
            "title": "Organik Elma Sirkesi",
            "subtitle": "Mineral Çözücü Doğal Katalizör",
            "desc": "Kemik dokusundaki minerallerin ve kolajen peptitlerin suya eksiksiz salınmasını sağlar. Pişirme esnasında asiditesi tamamen uçar.",
            "badge": "Fermantasyon Doğal"
        },
        {
            "num": "03",
            "title": "Taze Kereviz Sapı & Defne",
            "subtitle": "Alkali Denge & Hafif Aroma",
            "desc": "Doğal alkali mineral dengesini korur, kemik suyunun kokusuz, hafif ve kadifemsi içimli olmasını sağlar. Sindirimi rahatlatır.",
            "badge": "Bahçe Tazeliği"
        },
        {
            "num": "04",
            "title": "Glisin, Prolin & Glutamin",
            "subtitle": "Biyoyararlanımı Yüksek Amino Asitler",
            "desc": "Bağırsak epitel hücrelerini sıkılaştırarak Leaky Gut sendromunu onaran, cilt fibroblastlarını besleyen temel amino asit zinciri.",
            "badge": "Hücresel Onarım"
        }
    ]
    
    positions = [
        (80, start_y + 20, 560, start_y + 390),
        (640, start_y + 20, 1120, start_y + 390),
        (80, start_y + 420, 560, start_y + 790),
        (640, start_y + 420, 1120, start_y + 790),
    ]
    
    for i, c in enumerate(cards):
        x1, y1, x2, y2 = positions[i]
        # Card background
        draw.rounded_rectangle([x1, y1, x2, y2], radius=20, fill=WHITE, outline=BORDER_COLOR, width=1)
        
        # Number badge
        draw.rounded_rectangle([x1 + 30, y1 + 30, x1 + 80, y1 + 80], radius=12, fill=LIGHT_SAGE)
        draw.text((x1 + 42, y1 + 42), c["num"], font=get_font(22, bold=True), fill=DARK_GREEN)
        
        # Pill badge
        draw_pill(draw, (x2 - 200, y1 + 30), c["badge"], get_font(15, bold=True), AMBER_TINT, (150, 100, 20), padding_x=12, padding_y=6)
        
        # Title & Subtitle
        draw.text((x1 + 30, y1 + 100), c["title"], font=get_font(26, bold=True), fill=DARK_GREEN)
        draw.text((x1 + 30, y1 + 140), c["subtitle"], font=get_font(18, bold=True), fill=GOLD_ACCENT)
        
        # Description (wrapped text)
        words = c["desc"].split()
        lines = []
        cur = ""
        for w in words:
            if len(cur + " " + w) < 38:
                cur = (cur + " " + w).strip()
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
            
        desc_y = y1 + 185
        for line in lines:
            draw.text((x1 + 30, desc_y), line, font=get_font(17, bold=False), fill=MUTED_TEXT)
            desc_y += 28

    # Bottom Safety & Purity Bar
    bar_y = 1040
    draw.rounded_rectangle([80, bar_y, 1120, bar_y + 90], radius=16, fill=DARK_GREEN)
    purity_text = "0 İLAVE TUZ  •  0 KORUYUCU  •  0 KATKI MADDESİ  •  0 GLUTEN  •  0 RAFİNE ŞEKER"
    draw_centered_text(draw, bar_y + 32, purity_text, get_font(20, bold=True), (220, 240, 220))
    
    out_path = os.path.join(OUTPUT_DIR, "gallery_no01_02_ingredients.jpg")
    img.save(out_path, quality=95)
    print(f"Saved: {out_path}")

# ==========================================
# SLIDE 3: KİMLER KULLANABİLİR? (AUDIENCE)
# ==========================================
def generate_slide_3():
    print("Generating Slide 3: Who Can Use It Infographic...")
    img = Image.new("RGB", (1200, 1200), color=BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    start_y = add_header(img, draw, "KİMLER GÜVENLE KULLANABİLİR?", 
                         "Bebeklerden Yaşlılara Tüm Aile Bireyleri İçin Özel Formüle Edilmiştir")
    
    audiences = [
        {
            "tag": "6. AYDAN İTİBAREN",
            "title": "Bebekler & Çocuklar",
            "highlight": "Tuzsuz Ek Gıda Kaynağı",
            "bullets": [
                "Bebek çorbalarına ve pürelerine 2 kaşık eklenir",
                "Kemik, diş ve kıkırdak yapısını destekler",
                "Sıfır tuz ve sıfır baharat ile tam güvenli"
            ],
            "accent": (46, 117, 89)
        },
        {
            "tag": "DOĞAL MİNERAL",
            "title": "Hamile & Emzirenler",
            "highlight": "Hücresel Doku Desteği",
            "bullets": [
                "Hamilelikte artan kolajen ihtiyacını karşılar",
                "Doğal kalsiyum, magnezyum ve fosfor deposu",
                "Doğum sonrası doku toparlanmasını hızlandırır"
            ],
            "accent": (197, 160, 89)
        },
        {
            "tag": "PERFORMANS & EKLEM",
            "title": "Sporcular & Aktifler",
            "highlight": "Tendon & Eklem Koruma",
            "bullets": [
                "Ağır antrenman sonrası kas rejenerasyonu",
                "Eklem sıvısı kaybını ve kıkırdak aşınmasını önler",
                "Biyoaktif kolajen peptitleri ile hızlı emilim"
            ],
            "accent": (36, 80, 140)
        },
        {
            "tag": "YAŞ ALMAYANLAR",
            "title": "Yetişkinler & Yaşlılar",
            "highlight": "Cilt & Bağırsak Onarımı",
            "bullets": [
                "Acıbadem verisi: %28 cilt elastikiyeti artışı",
                "Geçirgen bağırsak (Leaky Gut) duvarını onarır",
                "Glisin amino asidi ile derin ve kaliteli uyku"
            ],
            "accent": (140, 70, 70)
        }
    ]
    
    card_w = 490
    card_h = 370
    coords = [
        (80, start_y + 20),
        (630, start_y + 20),
        (80, start_y + 430),
        (630, start_y + 430),
    ]
    
    for i, a in enumerate(audiences):
        x, y = coords[i]
        draw.rounded_rectangle([x, y, x + card_w, y + card_h], radius=20, fill=WHITE, outline=BORDER_COLOR, width=1)
        
        # Tag pill
        draw_pill(draw, (x + 30, y + 25), a["tag"], get_font(14, bold=True), LIGHT_SAGE, DARK_GREEN, padding_x=12, padding_y=6)
        
        # Title
        draw.text((x + 30, y + 75), a["title"], font=get_font(26, bold=True), fill=DARK_GREEN)
        draw.text((x + 30, y + 115), a["highlight"], font=get_font(18, bold=True), fill=a["accent"])
        draw.line([(x + 30, y + 150), (x + card_w - 30, y + 150)], fill=BORDER_COLOR, width=1)
        
        # Bullets
        by = y + 175
        for b in a["bullets"]:
            draw.text((x + 30, by), "•", font=get_font(20, bold=True), fill=DARK_GREEN)
            draw.text((x + 55, by), b, font=get_font(17, bold=False), fill=DEEP_OBSIDIAN)
            by += 44

    # Bottom Trust Note
    draw_centered_text(draw, 1060, "Tüm aile fertlerinin günlük tüketimine uygundur • Alerjen İçermez • Helal Sertifikalı", 
                      get_font(19, bold=True), MUTED_TEXT)
    
    out_path = os.path.join(OUTPUT_DIR, "gallery_no01_03_who_can_use.jpg")
    img.save(out_path, quality=95)
    print(f"Saved: {out_path}")

# ==========================================
# SLIDE 4: KLİNİK DAYANAK & ACIBADEM SAĞLIK
# ==========================================
def generate_slide_4():
    print("Generating Slide 4: Clinical Claims Infographic...")
    img = Image.new("RGB", (1200, 1200), color=BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    start_y = add_header(img, draw, "KLİNİK DAYANAK VE SAĞLIK RAPORU", 
                         "Acıbadem Sağlık Grubu Bilimsel Bulguları Referans Alınarak Hazırlanmıştır")
    
    claims = [
        {
            "num": "%100",
            "title": "Geçirgen Bağırsak (Leaky Gut) Onarımı",
            "desc": "Glutamin ve glisin amino asitleri bağırsak mukozasındaki mikro delikleri kapatarak toksinlerin kana sızmasını engeller. Sindirimi ve bağışıklığı doğrudan güçlendirir."
        },
        {
            "num": "+%28",
            "title": "Cilt Elastikiyeti & Kırışıklık Azalımı",
            "desc": "Biyoaktif Tip 1 ve Tip 3 kolajen peptitleri dermal fibroblast hücrelerini uyarır. Cilt nem tutma kapasitesini artırır ve doğal sıkılık kazandırır."
        },
        {
            "num": "5 Kat",
            "title": "Eklem Sıvısı & Kıkırdak Dayanıklılığı",
            "desc": "Doğal kondroitin, glukozamin ve hyalüronik asit içeriği ile eklem sürtünmesini azaltır, spor ve yaşa bağlı kıkırdak deformasyonunu frenler."
        },
        {
            "num": "REM",
            "title": "Glisin ile Kaliteli & Derin Uyku",
            "desc": "Yüksek glisin konsantrasyonu merkezi sinir sisteminde gevşetici etki yapar, vücut ısısını düzenleyerek derin dinlendirici uykuya geçişi kolaylaştırır."
        }
    ]
    
    cur_y = start_y + 20
    for c in claims:
        draw.rounded_rectangle([80, cur_y, 1120, cur_y + 175], radius=18, fill=WHITE, outline=BORDER_COLOR, width=1)
        
        # Metric circle/square
        draw.rounded_rectangle([110, cur_y + 25, 230, cur_y + 150], radius=14, fill=LIGHT_SAGE)
        font_num = get_font(32, bold=True)
        # Center number in block
        bbox = font_num.getbbox(c["num"])
        nw = bbox[2] - bbox[0]
        draw.text((110 + (120 - nw) // 2, cur_y + 60), c["num"], font=font_num, fill=DARK_GREEN)
        
        # Title
        draw.text((260, cur_y + 35), c["title"], font=get_font(24, bold=True), fill=DARK_GREEN)
        
        # Desc
        words = c["desc"].split()
        lines = []
        cur = ""
        for w in words:
            if len(cur + " " + w) < 70:
                cur = (cur + " " + w).strip()
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        
        dy = cur_y + 75
        for line in lines:
            draw.text((260, dy), line, font=get_font(17, bold=False), fill=MUTED_TEXT)
            dy += 26
            
        cur_y += 195

    # Acıbadem reference footer
    draw.rounded_rectangle([80, 1040, 1120, 1130], radius=14, fill=WHITE, outline=BORDER_COLOR)
    draw.text((110, 1058), "KAYNAK:", font=get_font(16, bold=True), fill=GOLD_ACCENT)
    draw.text((190, 1058), "Acıbadem Sağlık Grubu • İlikli Kemik Suyu Faydaları Tıbbi Yayını", font=get_font(16, bold=False), fill=DARK_GREEN)
    draw.text((110, 1088), "Doğal biyoyararlanımı yüksek kolajen ve amino asit profili laboratuvar analizleriyle doğrulanmıştır.", font=get_font(15, bold=False), fill=MUTED_TEXT)
    
    out_path = os.path.join(OUTPUT_DIR, "gallery_no01_04_clinical.jpg")
    img.save(out_path, quality=95)
    print(f"Saved: {out_path}")

# ==========================================
# SLIDE 5: DOKU & KIVAM KANITI (JÖLE TESTİ)
# ==========================================
def generate_slide_5():
    print("Generating Slide 5: Texture & Gelatin Proof...")
    # Load texture shot
    tex_path = os.path.join(ASSETS_DIR, "hero_collagen_jelly.jpg")
    tex_img = Image.open(tex_path).convert("RGBA")
    
    # Resize and crop to fill top portion
    w, h = tex_img.size
    aspect = w / h
    new_w = 1200
    new_h = int(new_w / aspect)
    tex_resized = tex_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    tex_cropped = tex_resized.crop((0, 0, 1200, 680))
    
    img = Image.new("RGBA", (1200, 1200), (*BG_COLOR, 255))
    img.paste(tex_cropped, (0, 0))
    
    draw = ImageDraw.Draw(img)
    
    # Top overlay banner
    draw.rounded_rectangle([60, 40, 1140, 130], radius=16, fill=(26, 56, 38, 235))
    draw_centered_text(draw, 60, "DOKU VE KIVAM KANITI: GERÇEK KOLAJEN TESTİ", get_font(28, bold=True), WHITE)
    draw_centered_text(draw, 95, "Yoğun kolajen içeren kemik suyu buzdolabında taş gibi jöleleşir", get_font(18, bold=False), (220, 235, 220))
    
    # Floating tag on texture image
    draw_pill(draw, (80, 580), "✦ KAŞIKLA KALDIRILAN DOĞAL JELATİN BLOKLARI", get_font(20, bold=True), 
              (197, 160, 89, 240), WHITE, padding_x=20, padding_y=10)

    # Bottom Two-State Explanation (Cold vs Warm)
    card_y = 710
    # Left Card: +4°C Soğukta
    draw.rounded_rectangle([80, card_y, 570, card_y + 350], radius=20, fill=WHITE, outline=BORDER_COLOR, width=1)
    draw_pill(draw, (110, card_y + 25), "4°C SOĞUKTA", get_font(15, bold=True), LIGHT_SAGE, DARK_GREEN, padding_x=12, padding_y=6)
    draw.text((110, card_y + 75), "Puding Kıvamında Taş Jöle", font=get_font(24, bold=True), fill=DARK_GREEN)
    draw.text((110, card_y + 115), "Saf Kolajenin Kesin İspatı", font=get_font(18, bold=True), fill=GOLD_ACCENT)
    
    left_desc = [
        "Buzdolabında bekletildiğinde",
        "kaşıkla kalıp halinde kaldırılan,",
        "titreyen doğal jöle dokusu oluşur.",
        "Suyla seyreltilmediğinin kanıtıdır."
    ]
    dy = card_y + 155
    for line in left_desc:
        draw.text((110, dy), line, font=get_font(17, bold=False), fill=MUTED_TEXT)
        dy += 28

    # Right Card: 60°C Isıtıldığında
    draw.rounded_rectangle([630, card_y, 1120, card_y + 350], radius=20, fill=WHITE, outline=BORDER_COLOR, width=1)
    draw_pill(draw, (660, card_y + 25), "60°C ISITILDIĞINDA", get_font(15, bold=True), AMBER_TINT, (160, 110, 20), padding_x=12, padding_y=6)
    draw.text((660, card_y + 75), "Berrak Altın Sarısı İksir", font=get_font(24, bold=True), fill=DARK_GREEN)
    draw.text((660, card_y + 115), "Kokusuz & Kadifemsi İçim", font=get_font(18, bold=True), fill=GOLD_ACCENT)
    
    right_desc = [
        "Isıtıldığında saniyeler içinde",
        "berrak, altın renkli bir içeceğe",
        "dönüşür. Ağır koku barındırmaz,",
        "limon ve karabiberle harika içilir."
    ]
    dy = card_y + 155
    for line in right_desc:
        draw.text((660, dy), line, font=get_font(17, bold=False), fill=MUTED_TEXT)
        dy += 28

    # Bottom summary
    draw_centered_text(draw, 1090, "%100 Katkısız • Nişasta veya Kıvam Artırıcı İçermez • Tamamen Doğal Jelatin", 
                      get_font(18, bold=True), DARK_GREEN)

    final = img.convert("RGB")
    out_path = os.path.join(OUTPUT_DIR, "gallery_no01_05_texture.jpg")
    final.save(out_path, quality=95)
    print(f"Saved: {out_path}")

# ==========================================
# SLIDE 6: NASIL TÜKETİLİR? (3 ADIM RUTİN)
# ==========================================
def generate_slide_6():
    print("Generating Slide 6: How to Use / 3-Step Routine...")
    img = Image.new("RGB", (1200, 1200), color=BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    start_y = add_header(img, draw, "NASIL TÜKETİLİR? (3 ADIMLI GÜNLÜK RUTİN)", 
                         "Maksimum Biyoyararlanım ve Hücresel Emilim İçin Tüketim Rehberi")
    
    steps = [
        {
            "step": "ADIM 1",
            "title": "Sabah Aç Karnına Ilık İçim",
            "subtitle": "Günün İlk İksiri (100 - 150 ml)",
            "desc": "Cezvede hafifçe ılıtıp (kaynatmadan) içerisine taze sıkılmış limon ve bir tutam tane karabiber ekleyerek için. Bağırsak bariyerini ilk adımda uyandırır ve gün boyu koruma sağlar.",
            "tip": "Öneri: Kahvaltıdan 20 dk önce"
        },
        {
            "step": "ADIM 2",
            "title": "Bebek Ek Gıda & Yemek Rutini",
            "subtitle": "Tüm Çorba ve Pürelerin İçine",
            "desc": "Bebeklerin sebze çorbalarına, pilav, güveç, makarna soslarına su yerine 2-3 yemek kaşığı ilave edin. Aile yemeklerinin besin ve kolajen değerini 10 katına çıkarır.",
            "tip": "Öneri: Yemek pişerken son 10 dk ekleyin"
        },
        {
            "step": "ADIM 3",
            "title": "Saklama ve Kür Disiplini",
            "subtitle": "Buzdolabında +4°C Saklama",
            "desc": "Kapağı açıldıktan sonra buzdolabında 4-5 gün tazeliğini korur. Daha uzun süreli kullanım için buz kalıplarına döküp dondurucuya atarak porsiyonluk kullanabilirsiniz.",
            "tip": "Öneri: 14 günlük kesintisiz kür"
        }
    ]
    
    cur_y = start_y + 20
    for s in steps:
        draw.rounded_rectangle([80, cur_y, 1120, cur_y + 230], radius=20, fill=WHITE, outline=BORDER_COLOR, width=1)
        
        # Step Circle
        draw.rounded_rectangle([115, cur_y + 35, 225, cur_y + 145], radius=16, fill=DARK_GREEN)
        draw.text((130, cur_y + 70), s["step"], font=get_font(20, bold=True), fill=WHITE)
        
        # Titles
        draw.text((260, cur_y + 35), s["title"], font=get_font(26, bold=True), fill=DARK_GREEN)
        draw.text((260, cur_y + 72), s["subtitle"], font=get_font(18, bold=True), fill=GOLD_ACCENT)
        
        # Desc
        words = s["desc"].split()
        lines = []
        cur = ""
        for w in words:
            if len(cur + " " + w) < 70:
                cur = (cur + " " + w).strip()
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
            
        dy = cur_y + 110
        for line in lines:
            draw.text((260, dy), line, font=get_font(17, bold=False), fill=MUTED_TEXT)
            dy += 26
            
        # Tip Pill
        draw_pill(draw, (260, cur_y + 175), s["tip"], get_font(14, bold=True), LIGHT_SAGE, DARK_GREEN, padding_x=14, padding_y=6)
        
        cur_y += 250

    # Bottom Delivery & Freshness guarantee
    draw.rounded_rectangle([80, 1045, 1120, 1135], radius=14, fill=DARK_GREEN)
    draw_centered_text(draw, 1065, "SOĞUK ZİNCİR VE KIRILMAYA KARŞI %100 SİGORTALI TESLİMAT", get_font(20, bold=True), WHITE)
    draw_centered_text(draw, 1098, "Özel strafor kutularda buz aküleriyle kapınıza kadar taptaze ulaştırılır", get_font(16, bold=False), (220, 235, 220))
    
    out_path = os.path.join(OUTPUT_DIR, "gallery_no01_06_how_to_use.jpg")
    img.save(out_path, quality=95)
    print(f"Saved: {out_path}")

if __name__ == "__main__":
    generate_slide_1()
    generate_slide_2()
    generate_slide_3()
    generate_slide_4()
    generate_slide_5()
    generate_slide_6()
    print("ALL 6 TRENDYOL INFOGRAPHIC SLIDES GENERATED SUCCESSFULLY!")
