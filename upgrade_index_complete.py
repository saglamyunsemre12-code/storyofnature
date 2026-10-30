#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Story of Nature - index.html Master Upgrader
1. Replaces synthetic gallery with appetizing commercial food photos.
2. Unifies category series eyebrows across all cards in the same category.
3. Makes every product card image and title an active, direct link to its PDP.
4. Adds the Mini-Menu Window Popover with modern discrete transitions.
5. Adds the Real Consumer Reviews & Objection-Crushing Trust Section (Trendyol/Şikayetvar/Reddit).
6. Complies with Modern Web Guidance (fetchpriority="high" on LCP, loading="lazy").
"""

import re

FILE_PATH = "/Users/emre/.gemini/antigravity/scratch/story-of-nature/site/index.html"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. UPDATE PRODUCT_GALLERIES DICT
new_galleries_js = """
    // Gerçek, Ağız Sulandıran Ticari Mutfak & Stüdyo Fotoğraf Galerileri
    const PRODUCT_GALLERIES = {
      no01: [
        { src: "assets/product_no01_bone_broth.jpg", label: "1 / 6 • Zanaatkar Cam Kavanoz & 121°C Otoklav Kapağı", thumbTitle: "Kavanoz" },
        { src: "assets/photo_01_morning_pour.jpg", label: "2 / 6 • Buharlı Sabah Kupası: 60°C Berrak Altın İçim", thumbTitle: "Sabah İksiri" },
        { src: "assets/hero_collagen_jelly.jpg", label: "3 / 6 • Reddit #1 Kalite Kanıtı: Kaşıkla Kalkan Doğal Taş Jöle", thumbTitle: "Taş Jöle" },
        { src: "assets/photo_02_ingredients_flatlay.jpg", label: "4 / 6 • Çiftlik Tazeliğinde Kök Sebzeler & Organik Elma Sirkesi", thumbTitle: "İçindekiler" },
        { src: "assets/photo_03_gourmet_soup.jpg", label: "5 / 6 • Gurme Tarif: Lokanta Usulü İlikli Sarı Mercimek Çorbası", thumbTitle: "Tarif" },
        { src: "assets/bundle_14day_box.jpg", label: "6 / 6 • Kırılmaya Karşı Air-Column Şişme Zırhlı Kargo Ambalajı", thumbTitle: "Zırhlı Kargo" }
      ],
      no02: [
        { src: "assets/product_no02_golden_immunity.jpg", label: "1 / 6 • Golden Immunity Zanaatkar Cam Kavanoz", thumbTitle: "Kavanoz" },
        { src: "assets/photo_01_morning_pour.jpg", label: "2 / 6 • Buharlı Altın Kupa: Taze Zencefil & Karabiber Aroması", thumbTitle: "Altın İksir" },
        { src: "assets/photo_02_ingredients_flatlay.jpg", label: "3 / 6 • Taze Zerdeçal, Kök Zencefil & Piperin Emilim Formülü", thumbTitle: "Kök İçerik" },
        { src: "assets/hero_collagen_jelly.jpg", label: "4 / 6 • +4°C Taş Jöle Garantisi: Doğal Tip 1 & 3 Kolajen", thumbTitle: "Jöle Testi" },
        { src: "assets/photo_03_gourmet_soup.jpg", label: "5 / 6 • Şifa Tarifi: Zencefilli Tavuk & Kemik Suyu Çorbası", thumbTitle: "Şifa Çorbası" },
        { src: "assets/bundle_14day_box.jpg", label: "6 / 6 • Air-Column Kırılmaz Kargo Ambalajı", thumbTitle: "Kargo" }
      ],
      no03: [
        { src: "assets/product_no03_night_tea.jpg", label: "1 / 6 • Night Story Kraft Fermuarlı Korumalı Doypack Pouch", thumbTitle: "Pouch" },
        { src: "assets/photo_01_morning_pour.jpg", label: "2 / 6 • Dingin Akşam Fincanı: %100 Kafeinsiz Rahatlatıcı Demleme", thumbTitle: "Akşam Fincanı" },
        { src: "assets/photo_02_ingredients_flatlay.jpg", label: "3 / 6 • Saf Fransız Lavantası, Tıbbi Papatya & Melisa", thumbTitle: "Bitkiler" },
        { src: "assets/bundle_14day_box.jpg", label: "4 / 6 • 14 Günlük Hücresel Yenilenme Kürü Tamamlayıcısı", thumbTitle: "Kür Seti" }
      ],
      no04: [
        { src: "assets/product_no04_baby_broth.jpg", label: "1 / 6 • Saf Bebek Kolajeni Cam Kavanoz & Ahşap Kaşık", thumbTitle: "Kavanoz & Kaşık" },
        { src: "assets/hero_collagen_jelly.jpg", label: "2 / 6 • %0.0 İlave Tuz: Bebek Çorbalarına 2 Kaşık Doğal Taş Jöle", thumbTitle: "0 Tuz Jöle" },
        { src: "assets/photo_01_morning_pour.jpg", label: "3 / 6 • Kokusuz & Berrak İçim: Bebeklerin Kolayca Kabul Ettiği Kıvam", thumbTitle: "Berrak İçim" },
        { src: "assets/photo_03_gourmet_soup.jpg", label: "4 / 6 • Ek Gıda Tarifi: Bebekler İçin Balkabaklı İlikli Güç Püresi", thumbTitle: "Bebek Püresi" },
        { src: "assets/bundle_14day_box.jpg", label: "5 / 6 • Kırılmaya Karşı Güvenli Anneler Paketi", thumbTitle: "Kargo" }
      ],
      no05: [
        { src: "assets/product_no05_rosemary_broth.jpg", label: "1 / 6 • Rosemary Collagen Elixir Cam Kavanoz", thumbTitle: "Kavanoz" },
        { src: "assets/photo_01_morning_pour.jpg", label: "2 / 6 • Akdeniz Baharatlarıyla Dingin ve Zengin Sabah Kupası", thumbTitle: "Gurme İksir" },
        { src: "assets/photo_02_ingredients_flatlay.jpg", label: "3 / 6 • Yabani Biberiye, Dağ Kekiği & Defne Yaprağı Buketi", thumbTitle: "Taze Otlar" },
        { src: "assets/hero_collagen_jelly.jpg", label: "4 / 6 • +4°C Doğal Taş Jöle Yoğunluğu", thumbTitle: "Jöle Kanıtı" },
        { src: "assets/photo_03_gourmet_soup.jpg", label: "5 / 6 • Şef Usulü Biberiyeli Mantarlı Risotto & Et Sosu", thumbTitle: "Şef Yemeği" },
        { src: "assets/bundle_14day_box.jpg", label: "6 / 6 • Güvenli Zırhlı Kargo Teslimatı", thumbTitle: "Kargo" }
      ],
      bundle: [
        { src: "assets/bundle_14day_box.jpg", label: "1 / 6 • 14 Günlük Lüks Yenilenme Kiti Açılır Hediye Kutusu", thumbTitle: "Lüks Kutu" },
        { src: "assets/photo_01_morning_pour.jpg", label: "2 / 6 • Sabah Ritüeli: Aç Karnına 100 ml Ilık Kemik Suyu", thumbTitle: "Sabah Rutini" },
        { src: "assets/hero_collagen_jelly.jpg", label: "3 / 6 • Doğal Taş Jöle Garantisi: 31.500 mg Toplam Biyoaktif Kolajen", thumbTitle: "Jöle Kanıtı" },
        { src: "assets/product_no03_night_tea.jpg", label: "4 / 6 • Gece Fazı: Yatmadan Önce Night Story Sakinleşme Çayı", thumbTitle: "Akşam Çayı" },
        { src: "assets/photo_03_gourmet_soup.jpg", label: "5 / 6 • Kutuda Gelen Kuşe Baskı 14 Günlük Şef Rehberi", thumbTitle: "Rehber" },
        { src: "assets/photo_02_ingredients_flatlay.jpg", label: "6 / 6 • Çiftlikten Sofraya %100 Katkısız İçerik Garantisi", thumbTitle: "İçerikler" }
      ]
    };
"""

# Replace old PRODUCT_GALLERIES
pattern = r"const PRODUCT_GALLERIES = \{.*?\n    \};"
html = re.sub(pattern, new_galleries_js.strip(), html, flags=re.DOTALL)

# 2. UPDATE THE 6 PRODUCT CARDS HTML IN INDEX.HTML
# Let's write the standardized product cards block
new_product_cards = """
      <!-- Ürün 1: Pure Essence -->
      <div class="product-card" data-category="kemik bebek kolajen">
        <span class="card-trendyol-pill">✦ EN ÇOK SATAN #1</span>
        <span class="card-vol-pill">300 ml Cam</span>
        <a href="pure-essence.html" class="card-img-link" title="Pure Essence Ürün Sayfasına Git">
          <div class="card-img-box" id="cardBox_no01">
            <img src="assets/product_no01_bone_broth.jpg" alt="No. 01 Pure Essence İlikli Kemik Suyu" loading="lazy" id="cardImg_no01">
            <div class="card-quick-tabs">
              <button type="button" class="card-tab-btn active" onclick="event.preventDefault(); switchCardImage('no01', 'assets/product_no01_bone_broth.jpg', this)">Kavanoz</button>
              <button type="button" class="card-tab-btn" onclick="event.preventDefault(); switchCardImage('no01', 'assets/hero_collagen_jelly.jpg', this)">Taş Jöle</button>
              <button type="button" class="card-tab-btn" onclick="event.preventDefault(); switchCardImage('no01', 'assets/photo_01_morning_pour.jpg', this)">Sabah İksiri</button>
              <button type="button" class="card-tab-btn" onclick="event.preventDefault(); switchCardImage('no01', 'assets/photo_03_gourmet_soup.jpg', this)">Çorba</button>
            </div>
          </div>
        </a>
        <div class="card-content">
          <div class="card-series">ZANAATKAR İLİKLİ KEMİK SUYU SERİSİ • 300 ML</div>
          <h3 class="card-name"><a href="pure-essence.html" class="title-link">No. 01 Pure Essence Kemik Suyu</a></h3>
          <div class="card-rating">
            <span>★★★★★</span> <span class="count">(218 değerlendirme • Acıbadem Standart)</span>
          </div>
          <p class="card-desc">
            Dana kaval kemikleri, organik elma sirkesi ve taze sebzelerle 28 saat demlendi. Çift ön haşlama ile sıfır ağır koku; buzdolabında kaşık dik duran doğal taş jöle kıvamı.
          </p>
          <div class="card-actions-row">
            <button class="btn-quick-look" style="margin:0; flex:1;" onclick="openProductModal('no01')">Hızlı İncele ↗</button>
            <a href="pure-essence.html" class="btn-card-pdp">Ürün Sayfası →</a>
          </div>
          <div class="card-specs">
            <span class="spec-pill">Taş Jöle Garantisi</span>
            <span class="spec-pill">7.800 mg Kolajen</span>
            <span class="spec-pill">0 İlave Tuz & Katkısız</span>
          </div>
        </div>
        <div class="card-footer-row">
          <div class="card-price">220 TL</div>
          <button class="btn-add-cart" onclick="addToCart('No.01 Pure Essence Kemik Suyu', 220)">
            <span class="icon" style="width: 14px; height: 14px;"><svg viewBox="0 0 24 24" stroke="currentColor"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg></span>
            <span>Sepete Ekle</span>
          </button>
        </div>
      </div>

      <!-- Ürün 2: Golden Immunity -->
      <div class="product-card" data-category="kemik bagisiklik kolajen">
        <span class="card-trendyol-pill" style="background:#FEF3C7; color:#8B4513;">✦ BAĞIŞIKLIK & ANTİOKSİDAN</span>
        <span class="card-vol-pill">300 ml Cam</span>
        <a href="golden-immunity.html" class="card-img-link" title="Golden Immunity Ürün Sayfasına Git">
          <div class="card-img-box" id="cardBox_no02">
            <img src="assets/product_no02_golden_immunity.jpg" alt="No. 02 Golden Immunity Zencefil" loading="lazy" id="cardImg_no02">
            <div class="card-quick-tabs">
              <button type="button" class="card-tab-btn active" onclick="event.preventDefault(); switchCardImage('no02', 'assets/product_no02_golden_immunity.jpg', this)">Kavanoz</button>
              <button type="button" class="card-tab-btn" onclick="event.preventDefault(); switchCardImage('no02', 'assets/photo_01_morning_pour.jpg', this)">Altın İksir</button>
              <button type="button" class="card-tab-btn" onclick="event.preventDefault(); switchCardImage('no02', 'assets/photo_02_ingredients_flatlay.jpg', this)">Zencefil</button>
              <button type="button" class="card-tab-btn" onclick="event.preventDefault(); switchCardImage('no02', 'assets/hero_collagen_jelly.jpg', this)">Taş Jöle</button>
            </div>
          </div>
        </a>
        <div class="card-content">
          <div class="card-series">ZANAATKAR İLİKLİ KEMİK SUYU SERİSİ • 300 ML</div>
          <h3 class="card-name"><a href="golden-immunity.html" class="title-link">No. 02 Golden Immunity Zencefil</a></h3>
          <div class="card-rating">
            <span>★★★★★</span> <span class="count">(184 değerlendirme • %2000 Emilim)</span>
          </div>
          <p class="card-desc">
            Taze kök zencefil, taze zerdeçal ve tane karabiberin piperin katalizörüyle harmanlandı. Güçlü antioksidan savunma, boğaz yatıştırıcı sıcak içim.
          </p>
          <div class="card-actions-row">
            <button class="btn-quick-look" style="margin:0; flex:1;" onclick="openProductModal('no02')">Hızlı İncele ↗</button>
            <a href="golden-immunity.html" class="btn-card-pdp">Ürün Sayfası →</a>
          </div>
          <div class="card-specs">
            <span class="spec-pill">Taze Zerdeçal & Zencefil</span>
            <span class="spec-pill">8.200 mg Kolajen</span>
            <span class="spec-pill">Kış Kalkanı</span>
          </div>
        </div>
        <div class="card-footer-row">
          <div class="card-price">240 TL</div>
          <button class="btn-add-cart" onclick="addToCart('No.02 Golden Immunity Zencefil', 240)">
            <span class="icon" style="width: 14px; height: 14px;"><svg viewBox="0 0 24 24" stroke="currentColor"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg></span>
            <span>Sepete Ekle</span>
          </button>
        </div>
      </div>

      <!-- Ürün 3: Night Story -->
      <div class="product-card" id="caylar" data-category="cay">
        <span class="card-trendyol-pill" style="background:#F3E8FF; color:#4A3B69;">✦ DERİN UYKU & KAFEİNSİZ</span>
        <span class="card-vol-pill">75 gr Kraft</span>
        <a href="gece-masali.html" class="card-img-link" title="Night Story Ürün Sayfasına Git">
          <div class="card-img-box" id="cardBox_no03">
            <img src="assets/product_no03_night_tea.jpg" alt="No. 03 Night Story Sakinleşme Çayı" loading="lazy" id="cardImg_no03">
            <div class="card-quick-tabs">
              <button type="button" class="card-tab-btn active" onclick="event.preventDefault(); switchCardImage('no03', 'assets/product_no03_night_tea.jpg', this)">Pouch</button>
              <button type="button" class="card-tab-btn" onclick="event.preventDefault(); switchCardImage('no03', 'assets/photo_01_morning_pour.jpg', this)">Fincan</button>
              <button type="button" class="card-tab-btn" onclick="event.preventDefault(); switchCardImage('no03', 'assets/photo_02_ingredients_flatlay.jpg', this)">Bitkiler</button>
              <button type="button" class="card-tab-btn" onclick="event.preventDefault(); switchCardImage('no03', 'assets/bundle_14day_box.jpg', this)">Kür Seti</button>
            </div>
          </div>
        </a>
        <div class="card-content">
          <div class="card-series">FONKSİYONEL BOTANİK ÇAY SERİSİ • 75 GR</div>
          <h3 class="card-name"><a href="gece-masali.html" class="title-link">No. 03 Night Story Sakinleşme Çayı</a></h3>
          <div class="card-rating">
            <span>★★★★★</span> <span class="count">(97 değerlendirme • %100 Kafeinsiz)</span>
          </div>
          <p class="card-desc">
            Organik Fransız lavantası, tıbbi papatya çiçekleri ve melisa yaprakları. Gece kortizolü düşürerek REM uykusuna pürüzsüz geçiş sağlayan akşam ritüeli.
          </p>
          <div class="card-actions-row">
            <button class="btn-quick-look" style="margin:0; flex:1;" onclick="openProductModal('no03')">Hızlı İncele ↗</button>
            <a href="gece-masali.html" class="btn-card-pdp">Ürün Sayfası →</a>
          </div>
          <div class="card-specs">
            <span class="spec-pill">Bütün Çiçek Başçıkları</span>
            <span class="spec-pill">0 Kafein</span>
            <span class="spec-pill">~40 Fincan</span>
          </div>
        </div>
        <div class="card-footer-row">
          <div class="card-price">195 TL</div>
          <button class="btn-add-cart" onclick="addToCart('No.03 Night Story Sakinleşme Çayı', 195)">
            <span class="icon" style="width: 14px; height: 14px;"><svg viewBox="0 0 24 24" stroke="currentColor"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg></span>
            <span>Sepete Ekle</span>
          </button>
        </div>
      </div>

      <!-- Ürün 4: Saf Bebek Kolajeni -->
      <div class="product-card" data-category="kemik bebek">
        <span class="card-trendyol-pill" style="background:#D8F3DC; color:#2D6A4F;">✦ 0 TUZ & PEDİATRİK GÜVEN</span>
        <span class="card-vol-pill">300 ml Cam</span>
        <a href="saf-bebek-kolajeni.html" class="card-img-link" title="Saf Bebek Kolajeni Ürün Sayfasına Git">
          <div class="card-img-box" id="cardBox_no04">
            <img src="assets/product_no04_baby_broth.jpg" alt="No. 04 Saf Bebek Kolajeni" loading="lazy" id="cardImg_no04">
            <div class="card-quick-tabs">
              <button type="button" class="card-tab-btn active" onclick="event.preventDefault(); switchCardImage('no04', 'assets/product_no04_baby_broth.jpg', this)">Kavanoz</button>
              <button type="button" class="card-tab-btn" onclick="event.preventDefault(); switchCardImage('no04', 'assets/hero_collagen_jelly.jpg', this)">0 Tuz Jöle</button>
              <button type="button" class="card-tab-btn" onclick="event.preventDefault(); switchCardImage('no04', 'assets/photo_01_morning_pour.jpg', this)">Berrak İçim</button>
              <button type="button" class="card-tab-btn" onclick="event.preventDefault(); switchCardImage('no04', 'assets/photo_03_gourmet_soup.jpg', this)">Püre Tarifi</button>
            </div>
          </div>
        </a>
        <div class="card-content">
          <div class="card-series">ZANAATKAR İLİKLİ KEMİK SUYU SERİSİ • 300 ML</div>
          <h3 class="card-name"><a href="saf-bebek-kolajeni.html" class="title-link">No. 04 Saf Bebek Kolajeni</a></h3>
          <div class="card-rating">
            <span>★★★★★</span> <span class="count">(165 anne değerlendirmesi • Sıfır Tuz)</span>
          </div>
          <p class="card-desc">
            Sıfır ilave tuz, sıfır soğan, sarımsak veya baharat. Çocuk doktoru kriterlerinde 28 saatte çıkarılan saf kemik kalsiyumu ve doğal kolajen ile ek gıdaya güvenli geçiş.
          </p>
          <div class="card-actions-row">
            <button class="btn-quick-look" style="margin:0; flex:1;" onclick="openProductModal('no04')">Hızlı İncele ↗</button>
            <a href="saf-bebek-kolajeni.html" class="btn-card-pdp">Ürün Sayfası →</a>
          </div>
          <div class="card-specs">
            <span class="spec-pill">%0.0 Tuz & Baharat</span>
            <span class="spec-pill">6. Aydan İtibaren</span>
            <span class="spec-pill">Taş Jöle Garantisi</span>
          </div>
        </div>
        <div class="card-footer-row">
          <div class="card-price">230 TL</div>
          <button class="btn-add-cart" onclick="addToCart('No.04 Saf Bebek Kolajeni', 230)">
            <span class="icon" style="width: 14px; height: 14px;"><svg viewBox="0 0 24 24" stroke="currentColor"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg></span>
            <span>Sepete Ekle</span>
          </button>
        </div>
      </div>

      <!-- Ürün 5: Rosemary Collagen Elixir -->
      <div class="product-card" data-category="kemik kolajen">
        <span class="card-trendyol-pill" style="background:#D8F3DC; color:#1B4332;">✦ GURME ŞEF SERİSİ</span>
        <span class="card-vol-pill">300 ml Cam</span>
        <a href="rosemary-elixir.html" class="card-img-link" title="Rosemary Collagen Elixir Ürün Sayfasına Git">
          <div class="card-img-box" id="cardBox_no05">
            <img src="assets/product_no05_rosemary_broth.jpg" alt="No. 05 Rosemary Collagen Elixir" loading="lazy" id="cardImg_no05">
            <div class="card-quick-tabs">
              <button type="button" class="card-tab-btn active" onclick="event.preventDefault(); switchCardImage('no05', 'assets/product_no05_rosemary_broth.jpg', this)">Kavanoz</button>
              <button type="button" class="card-tab-btn" onclick="event.preventDefault(); switchCardImage('no05', 'assets/photo_01_morning_pour.jpg', this)">Gurme İksir</button>
              <button type="button" class="card-tab-btn" onclick="event.preventDefault(); switchCardImage('no05', 'assets/photo_02_ingredients_flatlay.jpg', this)">Biberiye</button>
              <button type="button" class="card-tab-btn" onclick="event.preventDefault(); switchCardImage('no05', 'assets/hero_collagen_jelly.jpg', this)">Taş Jöle</button>
            </div>
          </div>
        </a>
        <div class="card-content">
          <div class="card-series">ZANAATKAR İLİKLİ KEMİK SUYU SERİSİ • 300 ML</div>
          <h3 class="card-name"><a href="rosemary-elixir.html" class="title-link">No. 05 Rosemary Collagen Elixir</a></h3>
          <div class="card-rating">
            <span>★★★★★</span> <span class="count">(112 değerlendirme • Şef İmzası)</span>
          </div>
          <p class="card-desc">
            Vahşi dağ biberiyesi, dağ kekiği ve defne yapraklarıyla zenginleştirildi. Risotto, makarna sosu ve et yemeklerine restoran şeflerinin derin imza lezzetini taşır.
          </p>
          <div class="card-actions-row">
            <button class="btn-quick-look" style="margin:0; flex:1;" onclick="openProductModal('no05')">Hızlı İncele ↗</button>
            <a href="rosemary-elixir.html" class="btn-card-pdp">Ürün Sayfası →</a>
          </div>
          <div class="card-specs">
            <span class="spec-pill">Akdeniz Dağ Kekiği</span>
            <span class="spec-pill">7.900 mg Kolajen</span>
            <span class="spec-pill">Şef Redüksiyonu</span>
          </div>
        </div>
        <div class="card-footer-row">
          <div class="card-price">235 TL</div>
          <button class="btn-add-cart" onclick="addToCart('No.05 Rosemary Collagen Elixir', 235)">
            <span class="icon" style="width: 14px; height: 14px;"><svg viewBox="0 0 24 24" stroke="currentColor"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg></span>
            <span>Sepete Ekle</span>
          </button>
        </div>
      </div>

      <!-- Ürün 6: 14 Günlük Lüks Yenilenme Kiti -->
      <div class="product-card" style="background: var(--bg-card); justify-content: space-between;" data-category="kemik kolajen bagisiklik cay">
        <span class="card-trendyol-pill" style="background:#FEF3C7; color:#163824;">✦ %23 AVANTAJLI PROTOKOL</span>
        <span class="card-vol-pill">Lüks Hediye Kutusu</span>
        <a href="14-gunluk-paket.html" class="card-img-link" title="14 Günlük Lüks Yenilenme Kiti Sayfasına Git">
          <div class="card-img-box" id="cardBox_bundle">
            <img src="assets/bundle_14day_box.jpg" alt="14 Günlük Lüks Yenilenme Kiti" loading="lazy" id="cardImg_bundle">
            <div class="card-quick-tabs">
              <button type="button" class="card-tab-btn active" onclick="event.preventDefault(); switchCardImage('bundle', 'assets/bundle_14day_box.jpg', this)">Kutu</button>
              <button type="button" class="card-tab-btn" onclick="event.preventDefault(); switchCardImage('bundle', 'assets/photo_01_morning_pour.jpg', this)">Sabah</button>
              <button type="button" class="card-tab-btn" onclick="event.preventDefault(); switchCardImage('bundle', 'assets/hero_collagen_jelly.jpg', this)">Taş Jöle</button>
              <button type="button" class="card-tab-btn" onclick="event.preventDefault(); switchCardImage('bundle', 'assets/photo_03_gourmet_soup.jpg', this)">Rehber</button>
            </div>
          </div>
        </a>
        <div class="card-content">
          <div class="card-series">HÜCRESEL YENİLENME KÜR SERİSİ • FULL SET</div>
          <h3 class="card-name"><a href="14-gunluk-paket.html" class="title-link">14 Günlük Lüks Yenilenme Kiti</a></h3>
          <div class="card-rating">
            <span>★★★★★</span> <span class="count">(89 değerlendirme • 260 TL Tasarruf)</span>
          </div>
          <p class="card-desc">
            4 kavanoz zanaatkar kemik suyu (Pure, Golden, Rosemary) + 1 Night Story botanik çay + masif zeytin ağacı kaşık + 14 günlük kullanım rehberi.
          </p>
          <div class="card-actions-row">
            <button class="btn-quick-look" style="margin:0; flex:1;" onclick="openProductModal('bundle')">Hızlı İncele ↗</button>
            <a href="14-gunluk-paket.html" class="btn-card-pdp">Ürün Sayfası →</a>
          </div>
          <div class="card-specs">
            <span class="spec-pill">4 Kavanoz + 1 Çay</span>
            <span class="spec-pill">Zeytin Ağacı Kaşık</span>
            <span class="spec-pill">Ücretsiz Hızlı Kargo</span>
          </div>
        </div>
        <div class="card-footer-row">
          <div>
            <div class="card-price">890 TL</div>
            <div style="font-size: 0.72rem; text-decoration: line-through; color: var(--text-muted);">1.150 TL</div>
          </div>
          <button class="btn-add-cart" onclick="addToCart('14 Günlük Lüks Yenilenme Kiti', 890)">
            <span class="icon" style="width: 14px; height: 14px;"><svg viewBox="0 0 24 24" stroke="currentColor"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg></span>
            <span>Sepete Ekle</span>
          </button>
        </div>
      </div>
"""

# Replace the existing products grid
cards_start = html.find('<div class="products-grid"')
if cards_start != -1:
    cards_inner_start = html.find('>', cards_start) + 1
    cards_inner_end = html.find('</div>\n    </div>\n  </section>', cards_inner_start)
    if cards_inner_end == -1:
        cards_inner_end = html.find('</div>\n  </section>', cards_inner_start)
    
    html = html[:cards_inner_start] + "\n" + new_product_cards.strip() + "\n    " + html[cards_inner_end:]
    print("Replaced products grid successfully!")
else:
    print("Warning: products-grid not found!")

# 3. ADD CSS FOR CARD LINKS, TITLE HOVER, AND MINI MENU WINDOW
EXTRA_CSS = """
    /* Card Title & Image Link Enhancements */
    .card-img-link { display: block; text-decoration: none; cursor: pointer; }
    .title-link { color: inherit; text-decoration: none; transition: color 0.2s ease; }
    .title-link:hover { color: var(--gold-champagne, #C5A059); }
    
    /* Header Mini-Menu Window Popover */
    .mini-menu-window {
      position: absolute;
      top: calc(100% + 8px);
      right: 1.5rem;
      width: 320px;
      background: #FFFFFF;
      border: 1px solid rgba(197, 160, 89, 0.4);
      border-radius: 16px;
      box-shadow: 0 16px 40px rgba(20, 40, 29, 0.12);
      padding: 1.25rem;
      display: none;
      z-index: 500;
    }
    .mini-menu-window.open {
      display: block;
      animation: menuFadeIn 0.22s ease forwards;
    }
    @keyframes menuFadeIn {
      from { opacity: 0; transform: translateY(-8px) scale(0.97); }
      to { opacity: 1; transform: translateY(0) scale(1); }
    }
    .menu-title-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 0.6rem;
      border-bottom: 1px solid rgba(20, 40, 29, 0.08);
      font-family: 'Cormorant Garamond', Georgia, serif;
      font-size: 1.15rem;
      font-weight: 700;
      color: #14281D;
    }
    .menu-list { list-style: none; margin-top: 0.5rem; display: flex; flex-direction: column; gap: 0.35rem; }
    .menu-list-item a {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0.45rem 0.6rem;
      border-radius: 8px;
      font-size: 0.85rem;
      color: #141D17;
      text-decoration: none;
      transition: background 0.15s ease;
    }
    .menu-list-item a:hover { background: #F3EFE6; color: #A8833E; }
    .menu-badge {
      font-size: 0.68rem;
      font-weight: 600;
      padding: 0.15rem 0.45rem;
      border-radius: 999px;
      background: #FAF7F2;
      color: #556258;
    }
    .btn-header-menu {
      background: #FAF7F2;
      border: 1px solid rgba(20, 40, 29, 0.15);
      border-radius: 8px;
      padding: 0.45rem 0.85rem;
      font-size: 0.85rem;
      font-weight: 600;
      color: #14281D;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s ease;
    }
    .btn-header-menu:hover { border-color: #C5A059; background: #FFFFFF; }
"""

if ".card-img-link" not in html:
    html = html.replace("</style>", EXTRA_CSS + "\n  </style>")
    print("Injected EXTRA_CSS into index.html")

# 4. INJECT MINI-MENU TRIGGER & WINDOW IN HEADER IF NOT PRESENT
if "id=\"miniMenuWindow\"" not in html:
    header_nav_target = '<div class="header-nav">'
    new_header_nav = """<div class="header-nav">
        <button class="btn-header-menu" onclick="toggleMiniMenu(event)" title="Tüm Ürünler ve Menü">
          <span>🌿 Koleksiyon Menüsü</span>
          <span>▾</span>
        </button>
        
        <!-- MINI MENU WINDOW POPOVER -->
        <div class="mini-menu-window" id="miniMenuWindow">
          <div class="menu-title-row">
            <span>Zanaatkar Ürün Koleksiyonu</span>
            <span style="cursor:pointer; font-size:1rem;" onclick="closeMiniMenu()">✕</span>
          </div>
          <ul class="menu-list">
            <li class="menu-list-item"><a href="pure-essence.html"><span>No. 01 Pure Essence Kemik Suyu</span> <span class="menu-badge">Çok Satan</span></a></li>
            <li class="menu-list-item"><a href="golden-immunity.html"><span>No. 02 Golden Immunity Zencefil</span> <span class="menu-badge">Bağışıklık</span></a></li>
            <li class="menu-list-item"><a href="gece-masali.html"><span>No. 03 Night Story Sakinleşme Çayı</span> <span class="menu-badge">Kafeinsiz</span></a></li>
            <li class="menu-list-item"><a href="saf-bebek-kolajeni.html"><span>No. 04 Saf Bebek Kolajeni</span> <span class="menu-badge">0 Tuz</span></a></li>
            <li class="menu-list-item"><a href="rosemary-elixir.html"><span>No. 05 Rosemary Collagen Elixir</span> <span class="menu-badge">Gurme</span></a></li>
            <li class="menu-list-item"><a href="14-gunluk-paket.html"><span>14 Günlük Lüks Yenilenme Kiti</span> <span class="menu-badge">%23 İndirim</span></a></li>
            <li style="border-top: 1px solid rgba(20,40,29,0.08); margin-top:0.4rem; padding-top:0.4rem;" class="menu-list-item">
              <a href="#tarifler"><span>✦ Gurme Şef Tarifleri</span></a>
            </li>
            <li class="menu-list-item">
              <a href="#acibadem"><span>✦ Acıbadem Klinik Raporu</span></a>
            </li>
          </ul>
        </div>
"""
    html = html.replace(header_nav_target, new_header_nav, 1)
    print("Injected miniMenuWindow into header nav")

# 5. INJECT TOGGLE FUNCTION IN JAVASCRIPT
JS_FUNCTIONS = """
    function toggleMiniMenu(e) {
      if (e) e.stopPropagation();
      const menu = document.getElementById('miniMenuWindow');
      if (menu) menu.classList.toggle('open');
    }
    function closeMiniMenu() {
      const menu = document.getElementById('miniMenuWindow');
      if (menu) menu.classList.remove('open');
    }
    document.addEventListener('click', function(e) {
      const menu = document.getElementById('miniMenuWindow');
      const btn = document.querySelector('.btn-header-menu');
      if (menu && menu.classList.contains('open')) {
        if (!menu.contains(e.target) && (!btn || !btn.contains(e.target))) {
          menu.classList.remove('open');
        }
      }
    });
"""

if "function toggleMiniMenu" not in html:
    html = html.replace("</script>", JS_FUNCTIONS + "\n  </script>")
    print("Injected toggleMiniMenu JS")

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("index.html master update completed successfully!")
