#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Story of Nature - Dedicated Product Detail Pages (PDP) Generator
Generates standalone, high-converting product pages for all 6 items:
- pure-essence.html
- golden-immunity.html
- gece-masali.html
- saf-bebek-kolajeni.html
- rosemary-elixir.html
- 14-gunluk-paket.html
And a universal dynamic product.html template.
"""

import os

SITE_DIR = "/Users/emre/.gemini/antigravity/scratch/story-of-nature/site"

PRODUCTS_DATA = {
    "no01": {
        "filename": "pure-essence.html",
        "title": "Pure Essence İlikli Kemik Suyu (300 ml)",
        "subtitle": "No. 01 • The Pure Bone Broth Chapter",
        "price": 220,
        "old_price": 260,
        "vol": "300 ml Cam Kavanoz",
        "badge": "✦ ÇOK SATAN #1",
        "badge_color": "#163824",
        "badge_bg": "#EBF3EC",
        "category_name": "İlikli Kemik Suları",
        "rating": "5.0",
        "review_count": 142,
        "lead": "Acıbadem Sağlık rehberi standartlarında; seçilmiş dana kaval kemikleri, organik elma sirkesi ve taze sebzelerle 28 saat boyunca kısık ateşte ağır ağır demlendi. Sıfır ilave tuz, sıfır koruyucu ve buzdolabında taş jöle kıvamı.",
        "slides": [
            {"src": "assets/gallery_no01_01_hero.jpg", "label": "1 / 6 • Ürün Görünümü & Onay Rozetleri", "thumb": "Ürün"},
            {"src": "assets/gallery_no01_02_ingredients.jpg", "label": "2 / 6 • Öne Çıkan Standartlar (Dairesel Rozetler)", "thumb": "Standartlar"},
            {"src": "assets/gallery_no01_03_who_can_use.jpg", "label": "3 / 6 • Özellikleri ve Etkileri (Cosmed Checklist)", "thumb": "Özellikler"},
            {"src": "assets/gallery_no01_04_clinical.jpg", "label": "4 / 6 • Acıbadem Klinik Raporu & Aktif İçerik", "thumb": "Klinik"},
            {"src": "assets/gallery_no01_05_texture.jpg", "label": "5 / 6 • Reddit #1 Kalite Testi: Jöle Kanıtı", "thumb": "Jöle Testi"},
            {"src": "assets/gallery_no01_06_how_to_use.jpg", "label": "6 / 6 • Nasıl Tüketilir? 3 Adımlı Rutin", "thumb": "Kullanım"}
        ],
        "highlights": [
            "Çift Ön Haşlama ile Sıfır Ağır Koku (Kokusuz & Kadifemsi)",
            "3 Kademeli Soğuk Filtrasyon ile <%0.2 Yağ Oranı",
            "Buzdolabında (+4°C) Kaşıkla Kalkan Doğal Taş Jöle",
            "Acıbadem Standardında 7.800 mg Tip 1 & 3 Biyoaktif Kolajen",
            "121°C Otoklav Basınçlı Sterilizasyon ile 6 Ay Koruyucusuz Raf Ömrü"
        ],
        "table": [
            ("Protein (100 ml)", "12.4 g Saf Biyoaktif Protein"),
            ("Doğal Kolajen (Tip 1 & 3)", "7.800 mg Konsantrasyon"),
            ("Glisin & Prolin Aminoasitleri", "Zengin Bağırsak Bariyeri & Mukoza Desteği"),
            ("İlave Tuz / Bulyon / Şeker", "%0.0 (Tamamen Katkısız)"),
            ("Yağ Oranı", "<%0.2 (Doymuş Yağdan Arındırılmış)"),
            ("Sterilizasyon", "121°C Otoklav Basınçlı Cam Kapama"),
            ("Raf Ömrü", "Kapak Açılmadan 6 Ay (Oda Sıcaklığında)")
        ],
        "recipe_title": "Lokanta Usulü İlikli Sarı Mercimek Çorbası",
        "recipe_desc": "Mercimek ve sebzeler tencereye konur; 1 kavanoz No. 01 kemik suyu ve 3 bardak suyla 20 dakika kısık ateşte pişirilip blenderdan geçirilir. 1 kasede 14g protein!",
        "recipe_time": "⏱ 25 Dakika • Kolay"
    },
    "no02": {
        "filename": "golden-immunity.html",
        "title": "Golden Immunity İlikli Kemik Suyu (300 ml)",
        "subtitle": "No. 02 • Turmeric & Ginger Elixir",
        "price": 240,
        "old_price": 280,
        "vol": "300 ml Cam Kavanoz",
        "badge": "✦ BAĞIŞIKLIK KÜRÜ",
        "badge_color": "#9C6B18",
        "badge_bg": "#FCF4E6",
        "category_name": "İlikli Kemik Suları",
        "rating": "4.9",
        "review_count": 89,
        "lead": "28 saatlik saf ilikli kemik suyumuza taze rendelenmiş zencefil, altın kök zerdeçal, tane karabiber ve taze sıkılmış limon ilave edildi. Karabiberdeki piperin sayesinde zerdeçalın emilimi 20 kat artar.",
        "slides": [
            {"src": "assets/gallery_no02_01_hero.jpg", "label": "1 / 4 • Golden Immunity Görünüm", "thumb": "Ürün"},
            {"src": "assets/gallery_no02_02_ingredients.jpg", "label": "2 / 4 • Zerdeçal & Zencefil Formülü", "thumb": "İçerik"},
            {"src": "assets/gallery_no01_05_texture.jpg", "label": "3 / 4 • Doğal Jelatin Doku Kanıtı", "thumb": "Jöle Testi"},
            {"src": "assets/gallery_no01_06_how_to_use.jpg", "label": "4 / 4 • Sabah Aç Karnına Rutin", "thumb": "Kullanım"}
        ],
        "highlights": [
            "Taze Kök Zerdeçal & Zencefil ile Güçlü Antioksidan Kalkan",
            "Tane Karabiber (Piperin) ile %2000 Artırılmış Kurkumin Emilimi",
            "Taze Limon ile Doğal C Vitamini Katalizörü",
            "Mevsim Geçişlerinde Doğal Bağışıklık ve Eklem Desteği",
            "Sıfır İlave Tuz, Koruyucusuz ve Kokusuz"
        ],
        "table": [
            ("Aktif Bileşenler", "Taze Kök Zerdeçal, Zencefil, Tane Karabiber, Limon"),
            ("Protein (100 ml)", "11.8 g"),
            ("Piperin Katalizörü", "Zerdeçal Emilimini 20 Kat Artırır"),
            ("İlave Tuz / Şeker", "%0.0 (Sıfır Katkı)"),
            ("Kullanım Önerisi", "Sabahları fincanda ısıtılarak aç karnına"),
            ("Net Miktar", "300 ml Cam Kavanoz")
        ],
        "recipe_title": "Altın Sabah İksiri (Limon & Karabiberli)",
        "recipe_desc": "150 ml No. 02 kemik suyu 60°C'de ılıtılır, 1/4 taze limon suyu ve taze çekilmiş tane karabiber eklenerek sabah aç karnına içilir. Kafeinsiz zindelik!",
        "recipe_time": "⏱ 3 Dakika • Zahmetsiz"
    },
    "no03": {
        "filename": "gece-masali.html",
        "title": "Night Story Sakinleşme Çayı (75 gr)",
        "subtitle": "No. 03 • Deep Sleep & Restore Botanical Tea",
        "price": 240,
        "old_price": 270,
        "vol": "75 gr Işık Geçirmez Kraft Doypack",
        "badge": "✦ DERİN REM UYKUSU",
        "badge_color": "#5C527F",
        "badge_bg": "#F2EFF9",
        "category_name": "Fonksiyonel Botanik Çaylar",
        "rating": "5.0",
        "review_count": 114,
        "lead": "Geceleri zihni yavaşlatmak, kortizolü düşürmek ve kesintisiz uyku mimarisini desteklemek için organik Fransız lavantası, tıbbi papatya ve melisa yaprağı ile harmanlandı. Kemik suyundaki glisin ile mükemmel ikili.",
        "slides": [
            {"src": "assets/gallery_no03_01_hero.jpg", "label": "1 / 3 • Gece Masalı Çay Paketi", "thumb": "Paket"},
            {"src": "assets/product_no03_night_tea.jpg", "label": "2 / 3 • Demleme ve Çiçek Harmanı", "thumb": "Harman"},
            {"src": "assets/gallery_no01_03_who_can_use.jpg", "label": "3 / 3 • Derin REM Uykusu & Glisin", "thumb": "Fayda"}
        ],
        "highlights": [
            "Organik Fransız Lavantası, Tıbbi Papatya ve Melisa Yaprağı",
            "%100 Kafeinsiz Akşam Ritüeli",
            "Kemik Suyundaki Glisin ile Birleştiğinde Üst Düzey Uyku Kalitesi",
            "Işık ve Nem Geçirmez Kilitli Kraft Doypack",
            "Hiçbir Yapay Aroma veya Katkı İçermez"
        ],
        "table": [
            ("Harman Bileşenleri", "Tıbbi Papatya, Melisa Yaprağı, Fransız Lavantası"),
            ("Kafein Oranı", "%0.0 (Tamamen Kafeinsiz)"),
            ("Demleme Şekli", "90°C sıcak suda 6-8 dakika kapalı demlik"),
            ("Ambalaj", "75 g Işık Geçirmez Kilitli Kraft Paket"),
            ("Tüketim Zamanı", "Uykudan 40 dakika önce 1 fincan")
        ],
        "recipe_title": "Gece Masalı & Kolajenli Mukoza Onarım Kürü",
        "recipe_desc": "No. 03 çayı demlenir; içerisine 1 yemek kaşığı saf ilikli kemik suyu (doğal glisin kaynağı) ve bal ilave edilip ılık yudumlanır.",
        "recipe_time": "⏱ 6 Dakika • Zahmetsiz"
    },
    "no04": {
        "filename": "saf-bebek-kolajeni.html",
        "title": "Saf Bebek Kolajeni Kemik Suyu (300 ml)",
        "subtitle": "No. 04 • Baby First Nutrition (6. Aydan İtibaren)",
        "price": 210,
        "old_price": 250,
        "vol": "300 ml Cam Kavanoz",
        "badge": "✦ BEBEK EK GIDA • SIFIR TUZ",
        "badge_color": "#237443",
        "badge_bg": "#EBF3EC",
        "category_name": "Bebek Ek Gıda Serisi",
        "rating": "5.0",
        "review_count": 96,
        "lead": "Bebeklerin narin sindirim ve böbrek sistemine özel olarak sıfır tuz, sıfır baharat ve sadece taze dana kaval kemiği iliğinden 28 saatte süzüldü. Pediatristlerin ek gıda önerileriyle %100 uyumludur.",
        "slides": [
            {"src": "assets/gallery_no04_01_hero.jpg", "label": "1 / 4 • Saf Bebek Kolajeni Görünüm", "thumb": "Ürün"},
            {"src": "assets/gallery_no04_02_baby_safety.jpg", "label": "2 / 4 • Sıfır Tuz & Pediatrik Güvenlik", "thumb": "Güvenlik"},
            {"src": "assets/gallery_no01_05_texture.jpg", "label": "3 / 4 • Doğal Jelatin Doku Kanıtı", "thumb": "Jöle Testi"},
            {"src": "assets/gallery_no01_06_how_to_use.jpg", "label": "4 / 4 • Çorba ve Püre Hazırlama", "thumb": "Kullanım"}
        ],
        "highlights": [
            "0 mg İlave Tuz • Bebek Böbreklerini Kesinlikle Yormaz",
            "0 Baharat, 0 Soğan/Sarımsak • Gaz ve Alerji Yapmaz",
            "6. Aydan İtibaren Ek Gıda Çorba ve Pürelerine Uygun",
            "Kemik, Diş ve Kıkırdak Gelişimi İçin Saf Kalsiyum Deposu",
            "121°C Otoklav Basınçlı Sterilizasyon ile %100 Güvenli"
        ],
        "table": [
            ("Uygunluk Dönemi", "6. Aydan İtibaren Ek Gıdaya Geçiş"),
            ("İlave Tuz & Baharat", "%0.0 (Kesinlikle İçermez)"),
            ("Protein (100 ml)", "12.0 g Kolay Sindirilebilir"),
            ("Kullanım Şekli", "Sebze çorbası, balkabağı püresi veya mamaya 2-3 kaşık"),
            ("Ambalaj", "300 ml Cam Kavanoz (BPA İçermez)")
        ],
        "recipe_title": "Balkabaklı & İlikli Bebek Ek Gıda Püresi",
        "recipe_desc": "Buharda pişen balkabağı ve havuç çatalla ezilir; içerisine 2-3 yemek kaşığı ılık No. 04 kemik suyu ve zeytinyağı eklenir.",
        "recipe_time": "⏱ 12 Dakika • Çok Kolay"
    },
    "no05": {
        "filename": "rosemary-elixir.html",
        "title": "Rosemary Collagen Elixir (300 ml)",
        "subtitle": "No. 05 • Wild Rosemary & Mountain Thyme Infusion",
        "price": 230,
        "old_price": 260,
        "vol": "300 ml Cam Kavanoz",
        "badge": "✦ GURME AKDENİZ AROMASI",
        "badge_color": "#C86D51",
        "badge_bg": "#FCF2EE",
        "category_name": "Gurme Kemik Suları",
        "rating": "4.9",
        "review_count": 67,
        "lead": "Taze Ege yayla biberiyesi, dağ kekiği ve defne yaprağıyla demlendi. Akdeniz şifasını ve nefis gurme aromayı sofranıza taşır; pilavlarda, makarnalarda ve sıcak çorbalarda eşsiz bir lezzet katar.",
        "slides": [
            {"src": "assets/gallery_no05_01_hero.jpg", "label": "1 / 4 • Rosemary Collagen Elixir", "thumb": "Ürün"},
            {"src": "assets/gallery_no01_02_ingredients.jpg", "label": "2 / 4 • Akdeniz Bitkisel İnfüzyon", "thumb": "İçerik"},
            {"src": "assets/gallery_no01_05_texture.jpg", "label": "3 / 4 • Doğal Jelatin Doku Kanıtı", "thumb": "Jöle Testi"},
            {"src": "assets/gallery_no01_06_how_to_use.jpg", "label": "4 / 4 • Gurme Yemek Rutini", "thumb": "Kullanım"}
        ],
        "highlights": [
            "Taze Yabani Biberiye, Dağ Kekiği ve Defne Yaprağı İnfüzyonu",
            "Yüksek Antioksidan Değeri ile Hücresel Koruma",
            "Gurme Yemeklerde ve Pilavlarda Lokanta Lezzeti",
            "Buzdolabında Taş Jöle, Isıtıldığında Kadifemsi Aromatik İksir",
            "Katkısız, Koruyucusuz ve 121°C Otoklav Güvencesi"
        ],
        "table": [
            ("Bitkisel İnfüzyon", "Yabani Biberiye, Dağ Kekiği, Kereviz Sapı, Defne"),
            ("Protein (100 ml)", "12.2 g"),
            ("Kullanım Alanı", "Pilav, makarna sosları, güveç ve gurme çorbalar"),
            ("Tuz / Koruyucu", "%0.0 (Sıfır Katkı)"),
            ("Net Miktar", "300 ml Cam Kavanoz")
        ],
        "recipe_title": "Biberiyeli & İlikli Tereyağlı Siyez Pilavı",
        "recipe_desc": "Tereyağında kavrulan siyez bulguruna 1 kavanoz No. 05 kemik suyu ve 1 bardak su eklenerek kısık ateşte demlendirilir.",
        "recipe_time": "⏱ 30 Dakika • Kolay"
    },
    "bundle": {
        "filename": "14-gunluk-paket.html",
        "title": "14 Günlük Lüks Hücresel Yenilenme Kiti",
        "subtitle": "The Complete 14-Day Wellness Reset Box",
        "price": 980,
        "old_price": 1250,
        "vol": "Özel Hediye Kutusunda Full Set",
        "badge": "✦ EN ÇOK SATAN WELLNESS SETİ (%20 İNDİRİM)",
        "badge_color": "#163824",
        "badge_bg": "#FCF4E6",
        "category_name": "Kür Paketleri",
        "rating": "5.0",
        "review_count": 188,
        "lead": "Hücresel yenilenme, bağırsak geçirgenliği (Leaky Gut) onarımı ve cilt elastikiyeti için tasarlandı. 4 kavanoz ilikli kemik suyu, 1 paket Night Story botanik çayı, el yapımı zeytin ağacı dozaj kaşığı ve 14 günlük kullanım takvimi tek bir kutuda.",
        "slides": [
            {"src": "assets/gallery_bundle_01_hero.jpg", "label": "1 / 4 • 14 Günlük Lüks Yenilenme Kiti", "thumb": "Set"},
            {"src": "assets/bundle_14day_box.jpg", "label": "2 / 4 • Açık Kutu İçeriği & Kaşık", "thumb": "Kutu"},
            {"src": "assets/gallery_no01_05_texture.jpg", "label": "3 / 4 • Yoğun Kolajen Doku Kanıtı", "thumb": "Jöle Testi"},
            {"src": "assets/gallery_no01_04_clinical.jpg", "label": "4 / 4 • Acıbadem Klinik Raporu", "thumb": "Klinik"}
        ],
        "highlights": [
            "4 Kavanoz Pure Essence İlikli Kemik Suyu (300 ml x 4)",
            "1 Paket Night Story Sakinleşme Çayı (75 gr)",
            "Hediye: El Yapımı Zeytin Ağacı Dozaj Kaşığı",
            "Hediye: 14 Günlük Hücresel Yenilenme Rehber Kitapçığı",
            "ÜCRETSİZ ZIRHLI SOĞUK ZİNCİR KARGO (Kırılmaya Karşı Sigortalı)"
        ],
        "table": [
            ("Kutu İçeriği", "4x Pure Essence Kemik Suyu + 1x Night Story Çayı"),
            ("Aksesuarlar", "El Yapımı Zeytin Ağacı Kaşık + 14 Günlük Rehber"),
            ("Kullanım Süresi", "14 Günlük Kesintisiz Hücresel Kür"),
            ("Fayda Alanı", "Bağırsak bariyeri onarımı, cilt elastikiyeti, kaliteli uyku"),
            ("Kargo Durumu", "Ücretsiz Zırhlı Strafor Kargo (Sigortalı)")
        ],
        "recipe_title": "14 Günlük Dönüşüm Programı",
        "recipe_desc": "Her sabah aç karnına 100 ml ılık kemik suyu + limon; her gece uykudan 40 dk önce lavanta-papatya çayı + 1 kaşık kemik suyu.",
        "recipe_time": "⏱ 14 Günlük Rutin"
    }
}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title} | Story of Nature</title>
  <meta name="description" content="{meta_desc}">
  <link rel="canonical" href="https://storyofnature.com.tr/{filename}">
  
  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🌿</text></svg>">

  <!-- Google Fonts: Cormorant Garamond & Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <style>
    :root {{
      --bg-canvas: #FAF7F2;
      --bg-surface: #ffffff;
      --bg-card: #F3EFE6;
      --color-dark: #14281D;
      --color-dark-hover: #1E3D2C;
      --text-main: #141D17;
      --text-muted: #556258;
      --gold-champagne: #C5A059;
      --gold-hover: #A8833E;
      --gold-tint: rgba(197, 160, 89, 0.12);
      --color-trust-green: #237443;
      --color-terracotta: #C86D51;
      --border-subtle: #E8E4DA;
      --font-serif: 'Cormorant Garamond', Georgia, serif;
      --font-sans: 'Inter', -apple-system, sans-serif;
      --radius-sm: 8px;
      --radius-md: 16px;
      --radius-lg: 24px;
      --radius-full: 9999px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: var(--font-sans);
      background: var(--bg-canvas);
      color: var(--text-main);
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
    }}

    /* Top Ticker */
    .top-banner {{
      background: var(--color-dark);
      color: #fff;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 1px;
      padding: 10px 16px;
      text-align: center;
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 12px;
    }}

    /* Header */
    header {{
      background: rgba(250, 247, 242, 0.94);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-subtle);
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .header-container {{
      max-width: 1240px;
      margin: 0 auto;
      padding: 14px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .brand-mark {{
      text-decoration: none;
      color: var(--color-dark);
      display: flex;
      flex-direction: column;
    }}
    .brand-mark .sub {{ font-size: 10px; font-weight: 800; letter-spacing: 2px; color: var(--gold-champagne); text-transform: uppercase; }}
    .brand-mark .title {{ font-family: var(--font-serif); font-size: 26px; font-weight: 700; line-height: 1; }}

    .nav-links {{
      display: flex;
      gap: 24px;
      align-items: center;
    }}
    @media (max-width: 860px) {{ .nav-links {{ display: none; }} }}
    .nav-links a {{
      text-decoration: none;
      color: var(--text-main);
      font-size: 13.5px;
      font-weight: 600;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{ color: var(--gold-champagne); }}

    .header-right {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .btn-header-cart {{
      background: var(--color-dark);
      color: #fff;
      border: none;
      padding: 10px 18px;
      border-radius: var(--radius-full);
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: background 0.2s;
    }}
    .btn-header-cart:hover {{ background: var(--color-dark-hover); }}

    /* Breadcrumbs */
    .breadcrumbs {{
      max-width: 1240px;
      margin: 20px auto 0;
      padding: 0 24px;
      font-size: 12px;
      color: var(--text-muted);
      display: flex;
      gap: 8px;
      align-items: center;
    }}
    .breadcrumbs a {{ color: var(--text-muted); text-decoration: none; }}
    .breadcrumbs a:hover {{ color: var(--color-dark); }}

    /* Main Product Layout (2:3 Cosmed Portrait Gallery & Buy Box) */
    .product-pdp-section {{
      max-width: 1240px;
      margin: 24px auto 60px;
      padding: 0 24px;
      display: grid;
      grid-template-columns: 1.05fr 1fr;
      gap: 50px;
      align-items: start;
    }}
    @media (max-width: 900px) {{
      .product-pdp-section {{ grid-template-columns: 1fr; gap: 32px; }}
    }}

    /* Gallery (2:3 Aspect Ratio) */
    .pdp-gallery {{
      display: flex;
      flex-direction: column;
      gap: 14px;
      position: sticky;
      top: 90px;
    }}
    .gallery-viewport {{
      position: relative;
      width: 100%;
      aspect-ratio: 2 / 3;
      max-height: 560px;
      border-radius: var(--radius-md);
      overflow: hidden;
      background: #fff;
      border: 1px solid var(--border-subtle);
      box-shadow: 0 10px 30px rgba(0,0,0,0.06);
    }}
    .gallery-viewport img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: opacity 0.2s ease;
    }}
    .gallery-badge-floating {{
      position: absolute;
      bottom: 14px;
      left: 14px;
      background: rgba(20, 40, 29, 0.88);
      backdrop-filter: blur(8px);
      color: #fff;
      font-size: 11px;
      font-weight: 700;
      padding: 6px 14px;
      border-radius: 20px;
    }}
    .gallery-arrow {{
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.92);
      border: 1px solid var(--border-subtle);
      color: var(--color-dark);
      font-size: 18px;
      font-weight: bold;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .gallery-arrow:hover {{ background: var(--color-dark); color: #fff; }}
    .gallery-arrow.prev {{ left: 12px; }}
    .gallery-arrow.next {{ right: 12px; }}

    .gallery-thumbs-row {{
      display: flex;
      gap: 10px;
      overflow-x: auto;
      padding-bottom: 6px;
    }}
    .gallery-thumb-item {{
      flex: 0 0 74px;
      height: 74px;
      border-radius: 10px;
      overflow: hidden;
      cursor: pointer;
      border: 2px solid transparent;
      background: #fff;
      position: relative;
    }}
    .gallery-thumb-item img {{ width: 100%; height: 100%; object-fit: cover; }}
    .gallery-thumb-item.active {{
      border-color: var(--gold-champagne);
      box-shadow: 0 0 0 2px rgba(197, 160, 89, 0.3);
    }}
    .gallery-thumb-title {{
      position: absolute;
      bottom: 0; left: 0; right: 0;
      background: rgba(20, 40, 29, 0.85);
      color: #fff;
      font-size: 9px;
      font-weight: 700;
      text-align: center;
      padding: 2px 0;
    }}

    /* Buy Box */
    .pdp-buy-box {{
      display: flex;
      flex-direction: column;
      gap: 18px;
    }}
    .pdp-badge-pill {{
      display: inline-block;
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 1px;
      padding: 6px 14px;
      border-radius: 12px;
      width: fit-content;
      text-transform: uppercase;
    }}
    .pdp-title {{
      font-family: var(--font-serif);
      font-size: 38px;
      font-weight: 600;
      line-height: 1.15;
      color: var(--color-dark);
    }}
    .pdp-subtitle {{
      font-size: 13px;
      color: var(--gold-champagne);
      font-weight: 700;
      letter-spacing: 1.5px;
      text-transform: uppercase;
    }}
    .pdp-reviews-row {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 13px;
    }}
    .pdp-stars {{ color: #E2B755; font-size: 16px; }}
    .pdp-price-row {{
      display: flex;
      align-items: baseline;
      gap: 14px;
      margin: 6px 0;
    }}
    .pdp-price {{
      font-family: var(--font-serif);
      font-size: 38px;
      font-weight: 700;
      color: var(--gold-champagne);
    }}
    .pdp-old-price {{
      font-size: 18px;
      color: var(--text-muted);
      text-decoration: line-through;
    }}
    .pdp-installment {{
      font-size: 12px;
      color: var(--color-trust-green);
      font-weight: 700;
      background: #e8f5e9;
      padding: 4px 10px;
      border-radius: 8px;
    }}
    .pdp-lead {{
      font-size: 15px;
      line-height: 1.65;
      color: var(--text-muted);
    }}

    /* Bullets */
    .pdp-highlights {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      background: #fff;
      padding: 18px;
      border-radius: 16px;
      border: 1px solid var(--border-subtle);
    }}
    .pdp-highlight-item {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 13px;
      font-weight: 600;
      color: var(--color-dark);
    }}
    .pdp-highlight-item span.check {{
      color: var(--color-trust-green);
      font-weight: bold;
    }}

    /* Qty & Add to Cart */
    .pdp-action-box {{
      display: flex;
      align-items: center;
      gap: 14px;
      margin-top: 10px;
    }}
    .pdp-qty-stepper {{
      display: flex;
      align-items: center;
      background: #fff;
      border-radius: 12px;
      border: 1px solid var(--border-subtle);
      overflow: hidden;
    }}
    .pdp-qty-btn {{
      background: none;
      border: none;
      width: 40px;
      height: 44px;
      cursor: pointer;
      font-size: 18px;
      font-weight: bold;
      color: var(--color-dark);
    }}
    .pdp-qty-btn:hover {{ background: var(--bg-card); }}
    .pdp-qty-val {{
      width: 40px;
      text-align: center;
      font-weight: 700;
      font-size: 15px;
    }}
    .pdp-btn-add {{
      flex: 1;
      background: var(--color-dark);
      color: #fff;
      padding: 15px 24px;
      border-radius: var(--radius-full);
      font-size: 15px;
      font-weight: 700;
      border: none;
      cursor: pointer;
      transition: background 0.2s;
    }}
    .pdp-btn-add:hover {{ background: var(--color-dark-hover); }}

    .pdp-btn-whatsapp {{
      width: 100%;
      background: #25D366;
      color: #fff;
      padding: 13px;
      border-radius: var(--radius-full);
      font-size: 14px;
      font-weight: 700;
      border: none;
      cursor: pointer;
      text-align: center;
      text-decoration: none;
      display: block;
    }}

    /* Guarantee bar */
    .pdp-guarantee-bar {{
      font-size: 12px;
      color: var(--color-trust-green);
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    /* Deep Dive Tabs */
    .pdp-details-section {{
      max-width: 1240px;
      margin: 40px auto 80px;
      padding: 0 24px;
    }}
    .pdp-tabs-nav {{
      display: flex;
      gap: 12px;
      border-bottom: 2px solid var(--border-subtle);
      margin-bottom: 28px;
      overflow-x: auto;
    }}
    .pdp-tab-btn {{
      background: none;
      border: none;
      padding: 12px 20px;
      font-size: 15px;
      font-weight: 700;
      color: var(--text-muted);
      cursor: pointer;
      border-bottom: 3px solid transparent;
      margin-bottom: -2px;
      transition: all 0.2s;
    }}
    .pdp-tab-btn.active {{
      color: var(--color-dark);
      border-bottom-color: var(--gold-champagne);
    }}
    .pdp-tab-pane {{
      display: none;
      background: #fff;
      padding: 34px;
      border-radius: 20px;
      border: 1px solid var(--border-subtle);
    }}
    .pdp-tab-pane.active {{ display: block; }}

    .pdp-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 14px;
    }}
    .pdp-table th, .pdp-table td {{
      padding: 14px 18px;
      text-align: left;
      border-bottom: 1px solid var(--border-subtle);
    }}
    .pdp-table th {{ background: var(--bg-card); color: var(--text-muted); font-weight: 700; width: 35%; }}

    /* Footer */
    footer {{
      background: var(--color-dark);
      color: #fff;
      padding: 60px 24px 30px;
      margin-top: 80px;
    }}
    .footer-inner {{
      max-width: 1240px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 20px;
    }}
    .footer-copy {{ font-size: 13px; color: #8C9990; }}
  </style>
</head>
<body>

  <!-- Top Banner -->
  <div class="top-banner">
    <span>🚚 750 TL ve Üzeri Siparişlerde <strong>ÜCRETSİZ ZIRHLI SOĞUK ZİNCİR KARGO</strong> • Kırılmaya Karşı %100 Sigortalı</span>
  </div>

  <!-- Header -->
  <header>
    <div class="header-container">
      <a href="index.html" class="brand-mark">
        <span class="sub">Artisanal Wellness</span>
        <span class="title">Story of Nature</span>
      </a>

      <nav class="nav-links">
        <a href="index.html#katalog">Koleksiyon</a>
        <a href="index.html#tarifler" style="color: var(--gold-champagne); font-weight: 700;">Yemek Tarifleri</a>
        <a href="index.html#neden-kokusuz">Neden Kokusuz?</a>
        <a href="index.html#jole-testi">Jöle Testi</a>
        <a href="index.html#faydalar">Klinik Rapor</a>
      </nav>

      <div class="header-right">
        <button class="btn-header-cart" onclick="window.location.href='index.html#katalog'">
          <span>Sepet</span>
          <span>→</span>
        </button>
      </div>
    </div>
  </header>

  <!-- Breadcrumbs -->
  <div class="breadcrumbs">
    <a href="index.html">Ana Sayfa</a>
    <span>/</span>
    <a href="index.html#katalog">{category_name}</a>
    <span>/</span>
    <strong>{title}</strong>
  </div>

  <!-- Main Product Section -->
  <section class="product-pdp-section">
    <!-- Left: 2:3 Cosmed Gallery -->
    <div class="pdp-gallery">
      <div class="gallery-viewport">
        <button class="gallery-arrow prev" onclick="prevSlide()">‹</button>
        <img id="mainImg" src="{main_slide_src}" alt="{title}">
        <button class="gallery-arrow next" onclick="nextSlide()">›</button>
        <div class="gallery-badge-floating" id="slideBadge">{main_slide_label}</div>
      </div>

      <div class="gallery-thumbs-row">
        {thumbs_html}
      </div>
    </div>

    <!-- Right: Buy Box -->
    <div class="pdp-buy-box">
      <span class="pdp-badge-pill" style="color: {badge_color}; background: {badge_bg};">{badge}</span>
      <div class="pdp-subtitle">{subtitle}</div>
      <h1 class="pdp-title">{title}</h1>

      <div class="pdp-reviews-row">
        <span class="pdp-stars">★★★★★</span>
        <strong>{rating}</strong>
        <span style="color: var(--text-muted);">({review_count} Doğrulanmış Müşteri Değerlendirmesi)</span>
      </div>

      <div class="pdp-price-row">
        <span class="pdp-price" id="totalPrice">{price} TL</span>
        <span class="pdp-old-price">{old_price} TL</span>
        <span class="pdp-installment">Vade farksız 3 taksit x {installment3} TL</span>
      </div>

      <p class="pdp-lead">{lead}</p>

      <div class="pdp-highlights">
        {highlights_html}
      </div>

      <!-- Action Box -->
      <div class="pdp-action-box">
        <div class="pdp-qty-stepper">
          <button class="pdp-qty-btn" onclick="updateQty(-1)">−</button>
          <span class="pdp-qty-val" id="qtyVal">1</span>
          <button class="pdp-qty-btn" onclick="updateQty(1)">+</button>
        </div>
        <button class="pdp-btn-add" onclick="handleAddToCart()">
          <span>Sepete Ekle ({price} TL)</span>
        </button>
      </div>

      <a href="https://wa.me/905330849027?text=Merhaba,%20{encoded_title}%20sipari%C5%9Fi%20vermek%20istiyorum." target="_blank" class="pdp-btn-whatsapp">
        WhatsApp ile Hızlı Sipariş Ver ↗
      </a>

      <div class="pdp-guarantee-bar">
        <span>🚚</span>
        <span>750 TL üzerine <strong>Ücretsiz Soğuk Zincir Kargo</strong> • Kırılmaya Karşı %100 Sigortalı</span>
      </div>
    </div>
  </section>

  <!-- Deep Dive Tabs -->
  <section class="pdp-details-section">
    <div class="pdp-tabs-nav">
      <button class="pdp-tab-btn active" onclick="switchTab('tab-analiz', this)">Acıbadem Bilimsel Besin Analizi</button>
      <button class="pdp-tab-btn" onclick="switchTab('tab-kullanim', this)">Nasıl Tüketilir?</button>
      <button class="pdp-tab-btn" onclick="switchTab('tab-tarif', this)">Mutfak Tarif Eşleşmesi</button>
    </div>

    <!-- Tab 1: Analiz -->
    <div id="tab-analiz" class="pdp-tab-pane active">
      <h3 style="font-family: var(--font-serif); font-size: 26px; margin-bottom: 16px; color: var(--color-dark);">Laboratuvar Onaylı Besin Değerleri</h3>
      <table class="pdp-table">
        {table_rows_html}
      </table>
      <div style="margin-top: 18px; font-size: 13px; color: var(--text-muted);">
        * Değerler Acıbadem Sağlık Grubu ve bağımsız akredite gıda laboratuvarı analiz raporları doğrultusunda hazırlanmıştır.
      </div>
    </div>

    <!-- Tab 2: Kullanım -->
    <div id="tab-kullanim" class="pdp-tab-pane">
      <h3 style="font-family: var(--font-serif); font-size: 26px; margin-bottom: 16px; color: var(--color-dark);">3 Adımlı Günlük Tüketim Rutini</h3>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
        <div style="background: var(--bg-card); padding: 22px; border-radius: 16px;">
          <div style="font-weight: 800; font-size: 12px; color: var(--gold-champagne); margin-bottom: 6px;">1. ADIM: SABAH AÇ KARNINA</div>
          <p style="font-size: 13.5px; color: var(--text-main);">Cezvede hafifçe ılıtıp (kaynatmadan) içerisine taze limon suyu ve tane karabiber ekleyerek için. Bağırsak mukozasını güne hazırlar.</p>
        </div>
        <div style="background: var(--bg-card); padding: 22px; border-radius: 16px;">
          <div style="font-weight: 800; font-size: 12px; color: var(--gold-champagne); margin-bottom: 6px;">2. ADIM: BEBEK & YEMEKLER</div>
          <p style="font-size: 13.5px; color: var(--text-main);">Bebeklerin sebze çorbasına veya aile yemeklerine 2-3 yemek kaşığı ilave edin. Besin değerini ve kolajen miktarını katlar.</p>
        </div>
        <div style="background: var(--bg-card); padding: 22px; border-radius: 16px;">
          <div style="font-weight: 800; font-size: 12px; color: var(--gold-champagne); margin-bottom: 6px;">3. ADIM: SAKLAMA KOŞULLARI</div>
          <p style="font-size: 13.5px; color: var(--text-main);">Kapak açıldıktan sonra buzdolabında (+4°C) 4-5 gün saklayın. Kalanını buz kalıplarında dondurarak 6 ay kullanabilirsiniz.</p>
        </div>
      </div>
    </div>

    <!-- Tab 3: Tarif -->
    <div id="tab-tarif" class="pdp-tab-pane">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
        <h3 style="font-family: var(--font-serif); font-size: 26px; color: var(--color-dark);">{recipe_title}</h3>
        <span style="font-size: 12px; font-weight: 700; color: var(--gold-champagne);">{recipe_time}</span>
      </div>
      <p style="font-size: 15px; color: var(--text-main); line-height: 1.6; margin-bottom: 18px;">{recipe_desc}</p>
      <a href="index.html#tarifler" style="display: inline-block; background: var(--color-dark); color: #fff; padding: 10px 22px; border-radius: var(--radius-full); text-decoration: none; font-size: 13px; font-weight: 700;">
        Tüm Mutfak Tariflerini Gör →
      </a>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <div class="footer-inner">
      <div>
        <div style="font-family: var(--font-serif); font-size: 24px; font-weight: 700;">Story of Nature</div>
        <div class="footer-copy">© 2026 Story of Nature Artisanal Wellness. Tüm hakları saklıdır.</div>
      </div>
      <div>
        <a href="index.html" style="color: #fff; text-decoration: none; font-size: 13px; font-weight: 600;">← Ana Sayfaya Dön</a>
      </div>
    </div>
  </footer>

  <script>
    const SLIDES = {slides_json};
    let currentSlide = 0;
    const basePrice = {price};
    let qty = 1;

    function renderSlide(idx) {{
      if (idx < 0) idx = SLIDES.length - 1;
      if (idx >= SLIDES.length) idx = 0;
      currentSlide = idx;

      const img = document.getElementById('mainImg');
      const badge = document.getElementById('slideBadge');
      if (img) {{
        img.style.opacity = '0.4';
        setTimeout(() => {{
          img.src = SLIDES[idx].src;
          img.style.opacity = '1';
        }}, 80);
      }}
      if (badge) badge.innerText = SLIDES[idx].label;

      document.querySelectorAll('.gallery-thumb-item').forEach((t, i) => {{
        if (i === idx) t.classList.add('active');
        else t.classList.remove('active');
      }});
    }}

    function prevSlide() {{ renderSlide(currentSlide - 1); }}
    function nextSlide() {{ renderSlide(currentSlide + 1); }}

    function updateQty(delta) {{
      qty = Math.max(1, qty + delta);
      document.getElementById('qtyVal').innerText = qty;
      document.getElementById('totalPrice').innerText = (basePrice * qty) + ' TL';
    }}

    function handleAddToCart() {{
      // Store in localStorage for seamless cart sync with index.html
      let cart = JSON.parse(localStorage.getItem('son_cart') || '{{}}');
      const itemTitle = "{title}";
      if (!cart[itemTitle]) {{
        cart[itemTitle] = {{ price: basePrice, qty: qty }};
      }} else {{
        cart[itemTitle].qty += qty;
      }}
      localStorage.setItem('son_cart', JSON.stringify(cart));
      alert(qty + ' adet {title} sepete eklendi! Ana sayfadaki sepetinizden siparişi tamamlayabilirsiniz.');
      window.location.href = 'index.html#katalog';
    }}

    function switchTab(tabId, btn) {{
      document.querySelectorAll('.pdp-tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.pdp-tab-pane').forEach(p => p.classList.remove('active'));
      btn.classList.add('active');
      document.getElementById(tabId).classList.add('active');
    }}
  </script>
</body>
</html>
"""

import json, urllib.parse

for key, p in PRODUCTS_DATA.items():
    # Build thumbs html
    thumbs_html = ""
    for idx, s in enumerate(p["slides"]):
        active_class = "active" if idx == 0 else ""
        thumbs_html += f'''
          <div class="gallery-thumb-item {active_class}" onclick="renderSlide({idx})" title="{s['label']}">
            <img src="{s['src']}" alt="{s['thumb']}" loading="lazy">
            <span class="gallery-thumb-title">{s['thumb']}</span>
          </div>
        '''

    # Build highlights html
    highlights_html = ""
    for h in p["highlights"]:
        highlights_html += f'''
          <div class="pdp-highlight-item">
            <span class="check">✓</span>
            <span>{h}</span>
          </div>
        '''

    # Build table rows html
    table_rows_html = ""
    for row in p["table"]:
        table_rows_html += f'''
          <tr>
            <th>{row[0]}</th>
            <td>{row[1]}</td>
          </tr>
        '''

    installment3 = round((p["price"] / 3), 2)
    encoded_title = urllib.parse.quote(p["title"])

    rendered = HTML_TEMPLATE.format(
        page_title=p["title"],
        meta_desc=p["lead"][:160],
        filename=p["filename"],
        category_name=p["category_name"],
        title=p["title"],
        subtitle=p["subtitle"],
        price=p["price"],
        old_price=p["old_price"],
        installment3=installment3,
        badge=p["badge"],
        badge_color=p["badge_color"],
        badge_bg=p["badge_bg"],
        rating=p["rating"],
        review_count=p["review_count"],
        lead=p["lead"],
        main_slide_src=p["slides"][0]["src"],
        main_slide_label=p["slides"][0]["label"],
        thumbs_html=thumbs_html,
        highlights_html=highlights_html,
        table_rows_html=table_rows_html,
        recipe_title=p["recipe_title"],
        recipe_desc=p["recipe_desc"],
        recipe_time=p["recipe_time"],
        encoded_title=encoded_title,
        slides_json=json.dumps(p["slides"], ensure_ascii=False)
    )

    out_file = os.path.join(SITE_DIR, p["filename"])
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(rendered)
    print("Generated dedicated product page:", p["filename"])

# Also generate universal product.html fallback
product_fallback = os.path.join(SITE_DIR, "product.html")
with open(os.path.join(SITE_DIR, "pure-essence.html"), "r", encoding="utf-8") as f:
    pure_html = f.read()

# Add auto-redirection / routing script in product.html
router_script = """
  <script>
    const params = new URLSearchParams(window.location.search);
    const pid = params.get('id');
    const routes = {
      'no01': 'pure-essence.html',
      'no02': 'golden-immunity.html',
      'no03': 'gece-masali.html',
      'no04': 'saf-bebek-kolajeni.html',
      'no05': 'rosemary-elixir.html',
      'bundle': '14-gunluk-paket.html'
    };
    if (pid && routes[pid]) {
      window.location.replace(routes[pid]);
    }
  </script>
"""
product_html_content = pure_html.replace("<head>", "<head>\n" + router_script)
with open(product_fallback, "w", encoding="utf-8") as f:
    f.write(product_html_content)
print("Generated universal product.html fallback router!")
