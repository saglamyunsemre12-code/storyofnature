#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

FILE_PATH = "/Users/emre/.gemini/antigravity/scratch/story-of-nature/site/index.html"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    html = f.read()

m = re.search(r'<div class="catalog-grid">', html)
if not m:
    print("catalog-grid not found!")
    exit(1)

start_idx = m.end()

bundle_pos = html.find('id="cardBox_bundle"', start_idx)
if bundle_pos == -1:
    print("cardBox_bundle not found!")
    exit(1)

# Find the end of Card 6, which ends right before </div>\n    </div>\n  </section>
end_idx = html.find('</div>\n    </div>\n  </section>', bundle_pos)
if end_idx == -1:
    end_idx = html.find('</div>\n      </div>\n    </div>', bundle_pos)
    if end_idx != -1:
        end_idx += len('</div>\n      </div>')

print(f"Replacing catalog-grid from index {start_idx} to {end_idx}")

NEW_CARDS = """
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

html = html[:start_idx] + "\n" + NEW_CARDS.strip() + "\n    " + html[end_idx:]

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("catalog-grid successfully updated with direct links, unified series taxonomy, and authentic culinary photography!")
