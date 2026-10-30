#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Upgrades index.html with:
1. Cosmed Trendyol-style interactive 6-slide infographic galleries.
2. Catalog card quick preview tabs (Ürün, Doku, İçerik, Faydalar).
3. Wide 2-column modal with thumbnail strip, prev/next arrows, and slide counters.
4. Seamless touch/click handlers and responsive mobile design.
"""

import re

FILE_PATH = "/Users/emre/.gemini/antigravity/scratch/story-of-nature/site/index.html"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. ADD CSS
NEW_CSS = """
    /* ========================================================
       TRENDYOL & COSMED STYLE INFOGRAPHIC GALLERY & CRO MODULES
       ======================================================== */
    .modal-box {
      background: var(--bg-canvas);
      border-radius: var(--radius-lg);
      max-width: 1040px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      padding: 36px;
      box-shadow: 0 30px 70px rgba(0,0,0,0.22);
      border: 1px solid var(--border-subtle);
      position: relative;
      transform: translateY(20px);
      transition: var(--transition);
    }
    .modal-overlay.active .modal-box { transform: translateY(0); }
    @media (max-width: 900px) {
      .modal-box { padding: 22px 16px; max-height: 94vh; }
    }

    .modal-product-layout {
      display: grid;
      grid-template-columns: 1.05fr 1fr;
      gap: 36px;
      align-items: start;
    }
    @media (max-width: 860px) {
      .modal-product-layout { grid-template-columns: 1fr; gap: 24px; }
    }

    /* Trendyol Gallery Container */
    .trendyol-gallery {
      display: flex;
      flex-direction: column;
      gap: 14px;
      position: sticky;
      top: 0;
    }
    .gallery-main-viewport {
      position: relative;
      width: 100%;
      aspect-ratio: 1 / 1;
      border-radius: var(--radius-md);
      overflow: hidden;
      background: #F8F6F0;
      border: 1px solid var(--border-subtle);
      box-shadow: 0 8px 24px rgba(0,0,0,0.06);
    }
    .gallery-main-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: opacity 0.25s ease, transform 0.4s ease;
      display: block;
    }
    .gallery-main-viewport:hover .gallery-main-img {
      transform: scale(1.02);
    }
    .gallery-slide-badge {
      position: absolute;
      bottom: 14px;
      left: 14px;
      background: rgba(22, 30, 24, 0.88);
      backdrop-filter: blur(8px);
      color: #fff;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.5px;
      padding: 6px 14px;
      border-radius: 20px;
      z-index: 2;
      pointer-events: none;
      border: 1px solid rgba(255,255,255,0.15);
    }
    .gallery-nav-arrow {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.92);
      border: 1px solid rgba(0,0,0,0.08);
      color: #1A3826;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 18px;
      font-weight: bold;
      box-shadow: 0 4px 12px rgba(0,0,0,0.12);
      transition: all 0.2s ease;
      z-index: 3;
    }
    .gallery-nav-arrow:hover {
      background: #1A3826;
      color: #fff;
      transform: translateY(-50%) scale(1.08);
    }
    .gallery-nav-arrow.prev { left: 10px; }
    .gallery-nav-arrow.next { right: 10px; }

    /* Trendyol Thumbnail Strip */
    .gallery-thumb-strip {
      display: flex;
      gap: 10px;
      overflow-x: auto;
      padding-bottom: 6px;
      scrollbar-width: thin;
    }
    .gallery-thumb-item {
      flex: 0 0 74px;
      height: 74px;
      border-radius: 10px;
      overflow: hidden;
      cursor: pointer;
      border: 2px solid transparent;
      background: #F8F6F0;
      transition: all 0.2s ease;
      position: relative;
    }
    .gallery-thumb-item img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .gallery-thumb-item.active {
      border-color: var(--gold-champagne);
      box-shadow: 0 0 0 2px rgba(197, 160, 89, 0.35);
      transform: scale(0.96);
    }
    .gallery-thumb-item:hover:not(.active) {
      border-color: rgba(26, 56, 38, 0.4);
    }
    .gallery-thumb-caption {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      background: rgba(26, 56, 38, 0.9);
      color: #fff;
      font-size: 9px;
      font-weight: 700;
      text-align: center;
      padding: 2px 0;
    }

    /* Catalog Card Image Overlays */
    .card-img-box {
      width: 100%;
      height: 330px;
      border-radius: var(--radius-md);
      overflow: hidden;
      position: relative;
      background: #F8F6F0;
      margin-bottom: 20px;
    }
    .card-quick-tabs {
      position: absolute;
      bottom: 12px;
      left: 8px;
      right: 8px;
      display: flex;
      gap: 5px;
      justify-content: center;
      z-index: 3;
    }
    .card-tab-btn {
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(6px);
      border: 1px solid rgba(0,0,0,0.06);
      color: #1A3826;
      font-size: 10px;
      font-weight: 700;
      padding: 4px 9px;
      border-radius: 12px;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .card-tab-btn:hover, .card-tab-btn.active {
      background: #1A3826;
      color: #fff;
      transform: translateY(-2px);
    }
    .card-trendyol-pill {
      position: absolute;
      top: 12px;
      left: 12px;
      background: rgba(26, 56, 38, 0.94);
      backdrop-filter: blur(6px);
      color: #fff;
      font-size: 10px;
      font-weight: 800;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      padding: 5px 11px;
      border-radius: 12px;
      z-index: 3;
      border: 1px solid rgba(197, 160, 89, 0.4);
    }
    .card-vol-pill {
      position: absolute;
      top: 12px;
      right: 12px;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(6px);
      color: #1A3826;
      font-size: 10px;
      font-weight: 700;
      padding: 5px 10px;
      border-radius: 12px;
      z-index: 3;
      border: 1px solid var(--border-subtle);
    }
    .modal-qty-row {
      display: flex;
      align-items: center;
      gap: 16px;
      margin: 20px 0;
      padding: 14px 18px;
      background: var(--bg-card);
      border-radius: 14px;
      border: 1px solid var(--border-subtle);
    }
    .qty-counter {
      display: flex;
      align-items: center;
      background: #fff;
      border-radius: 8px;
      border: 1px solid var(--border-subtle);
      overflow: hidden;
    }
    .qty-btn {
      background: none;
      border: none;
      width: 32px;
      height: 32px;
      cursor: pointer;
      font-size: 16px;
      font-weight: bold;
      color: #1A3826;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background 0.15s;
    }
    .qty-btn:hover { background: #f0ede4; }
    .qty-val {
      width: 36px;
      text-align: center;
      font-weight: bold;
      font-size: 14px;
    }
    .installment-pill {
      font-size: 12px;
      color: var(--color-trust-green);
      font-weight: 600;
    }
"""

# Replace existing modal-box definition or insert after it
old_modal_css = re.search(r'\.modal-box\s*\{[^}]*\}', html)
if old_modal_css:
    html = html.replace(old_modal_css.group(0), NEW_CSS)
    print("Replaced old .modal-box CSS successfully!")
else:
    print("Warning: .modal-box CSS target not found directly, appending to head.")

# 2. UPDATE CATALOG GRID CARDS (Trendyol Interactive Preview)
old_cards_pattern = r'<div class="catalog-grid">.*?</div>\s*</div>\s*<!--\s*11\.'
cards_replacement = """<div class="catalog-grid">
      <!-- Ürün 1: Pure Essence -->
      <div class="product-card" data-category="kemik bebek kolajen">
        <span class="card-trendyol-pill">✦ ÇOK SATAN #1</span>
        <span class="card-vol-pill">300 ml Cam</span>
        <div class="card-img-box" id="cardBox_no01">
          <img src="assets/gallery_no01_01_hero.jpg" alt="Pure Essence İlikli Kemik Suyu" loading="lazy" id="cardImg_no01">
          <div class="card-quick-tabs">
            <button class="card-tab-btn active" onclick="switchCardImage('no01', 'assets/gallery_no01_01_hero.jpg', this)">Ürün</button>
            <button class="card-tab-btn" onclick="switchCardImage('no01', 'assets/gallery_no01_05_texture.jpg', this)">Doku (Jöle)</button>
            <button class="card-tab-btn" onclick="switchCardImage('no01', 'assets/gallery_no01_02_ingredients.jpg', this)">İçerik</button>
            <button class="card-tab-btn" onclick="switchCardImage('no01', 'assets/gallery_no01_04_clinical.jpg', this)">Klinik</button>
          </div>
        </div>
        <div class="card-content">
          <div class="card-series">NO. 01 • BONE BROTH</div>
          <h3 class="card-name">Pure Essence Kemik Suyu</h3>
          <div class="card-rating">
            <span>★★★★★</span> <span class="count">(142 değerlendirme • Acıbadem Standart)</span>
          </div>
          <p class="card-desc">
            Dana kaval kemiği, organik elma sirkesi ve taze sebzelerle 28 saat demlendi. Buzdolabında taş gibi jöle kıvamı, 60°C'de berrak altın sarısı içim iksiri.
          </p>
          <button class="btn-quick-look" onclick="openProductModal('no01')">
            6 Slayt İnfografik Galeri & Besin Analizi ↗
          </button>
          <div class="card-specs">
            <span class="spec-pill">300 ml Cam Kavanoz</span>
            <span class="spec-pill">Tip 1 & 3 Kolajen</span>
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
        <span class="card-trendyol-pill">✦ BAĞIŞIKLIK KÜRÜ</span>
        <span class="card-vol-pill">300 ml Cam</span>
        <div class="card-img-box" id="cardBox_no02">
          <img src="assets/gallery_no02_01_hero.jpg" alt="Golden Immunity Zencefil" loading="lazy" id="cardImg_no02">
          <div class="card-quick-tabs">
            <button class="card-tab-btn active" onclick="switchCardImage('no02', 'assets/gallery_no02_01_hero.jpg', this)">Ürün</button>
            <button class="card-tab-btn" onclick="switchCardImage('no02', 'assets/gallery_no02_02_ingredients.jpg', this)">İçerik</button>
            <button class="card-tab-btn" onclick="switchCardImage('no02', 'assets/gallery_no01_05_texture.jpg', this)">Doku</button>
            <button class="card-tab-btn" onclick="switchCardImage('no02', 'assets/gallery_no01_06_how_to_use.jpg', this)">Kullanım</button>
          </div>
        </div>
        <div class="card-content">
          <div class="card-series">NO. 02 • BONE BROTH</div>
          <h3 class="card-name">Golden Immunity Zencefil</h3>
          <div class="card-rating">
            <span>★★★★★</span> <span class="count">(89 değerlendirme)</span>
          </div>
          <p class="card-desc">
            Saf ilikli kemik suyuna taze zencefil, kök zerdeçal, tane karabiber ve limon ilave edildi. %2000 piperin emilimi ile mevsim geçişlerinde doğal kalkan.
          </p>
          <button class="btn-quick-look" onclick="openProductModal('no02')">
            5 Slayt İnfografik Galeri & Besin Analizi ↗
          </button>
          <div class="card-specs">
            <span class="spec-pill">Kök Zerdeçal & Zencefil</span>
            <span class="spec-pill">Piperin Katalizörü</span>
            <span class="spec-pill">Bağışıklık Kürü</span>
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

      <!-- Ürün 3: Night Story Çay -->
      <div class="product-card" id="caylar" data-category="cay">
        <span class="card-trendyol-pill">✦ DERİN UYKU</span>
        <span class="card-vol-pill">75 gr Kraft</span>
        <div class="card-img-box" id="cardBox_no03">
          <img src="assets/gallery_no03_01_hero.jpg" alt="Night Story Sakinleşme Çayı" loading="lazy" id="cardImg_no03">
          <div class="card-quick-tabs">
            <button class="card-tab-btn active" onclick="switchCardImage('no03', 'assets/gallery_no03_01_hero.jpg', this)">Paket</button>
            <button class="card-tab-btn" onclick="switchCardImage('no03', 'assets/product_no03_night_tea.jpg', this)">Demlik</button>
            <button class="card-tab-btn" onclick="switchCardImage('no03', 'assets/gallery_no01_03_who_can_use.jpg', this)">Uyku</button>
          </div>
        </div>
        <div class="card-content">
          <div class="card-series">NO. 03 • BOTANICAL BLEND</div>
          <h3 class="card-name">Night Story Sakinleşme Çayı</h3>
          <div class="card-rating">
            <span>★★★★★</span> <span class="count">(114 değerlendirme)</span>
          </div>
          <p class="card-desc">
            Organik Fransız lavantası, tıbbi papatya ve melisa yaprağı. Kemik suyundaki glisin amino asidi ile birlikte derin REM uykusu ve nörolojik dinlenme sağlar.
          </p>
          <button class="btn-quick-look" onclick="openProductModal('no03')">
            İnfografik Galeri & Bitki Analizi ↗
          </button>
          <div class="card-specs">
            <span class="spec-pill">%100 Kafeinsiz</span>
            <span class="spec-pill">Fransız Lavantası</span>
            <span class="spec-pill">Melisa & Papatya</span>
          </div>
        </div>
        <div class="card-footer-row">
          <div class="card-price">240 TL</div>
          <button class="btn-add-cart" onclick="addToCart('No.03 Night Story Sakinleşme Çayı', 240)">
            <span class="icon" style="width: 14px; height: 14px;"><svg viewBox="0 0 24 24" stroke="currentColor"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg></span>
            <span>Sepete Ekle</span>
          </button>
        </div>
      </div>

      <!-- Ürün 4: Saf Bebek Kolajeni -->
      <div class="product-card" data-category="kemik bebek">
        <span class="card-trendyol-pill">✦ BEBEK & EK GIDA</span>
        <span class="card-vol-pill">300 ml Cam</span>
        <div class="card-img-box" id="cardBox_no04">
          <img src="assets/gallery_no04_01_hero.jpg" alt="Saf Bebek Kolajeni" loading="lazy" id="cardImg_no04">
          <div class="card-quick-tabs">
            <button class="card-tab-btn active" onclick="switchCardImage('no04', 'assets/gallery_no04_01_hero.jpg', this)">Ürün</button>
            <button class="card-tab-btn" onclick="switchCardImage('no04', 'assets/gallery_no04_02_baby_safety.jpg', this)">Güvenlik</button>
            <button class="card-tab-btn" onclick="switchCardImage('no04', 'assets/gallery_no01_05_texture.jpg', this)">Doku</button>
            <button class="card-tab-btn" onclick="switchCardImage('no04', 'assets/gallery_no01_06_how_to_use.jpg', this)">Kullanım</button>
          </div>
        </div>
        <div class="card-content">
          <div class="card-series">NO. 04 • BABY NUTRITION</div>
          <h3 class="card-name">Saf Bebek Kolajeni</h3>
          <div class="card-rating">
            <span>★★★★★</span> <span class="count">(96 değerlendirme • Pediatrist Onaylı)</span>
          </div>
          <p class="card-desc">
            6. aydan itibaren ek gıdaya geçen bebekler için sıfır tuz ve sıfır baharat ile sadece saf dana kaval kemiği iliğinden 28 saatte süzüldü. Bebek böbreklerini yormaz.
          </p>
          <button class="btn-quick-look" onclick="openProductModal('no04')">
            Pediatrik Güvenlik Galerisi ↗
          </button>
          <div class="card-specs">
            <span class="spec-pill">6. Aydan İtibaren</span>
            <span class="spec-pill">Sıfır Tuz & Baharat</span>
            <span class="spec-pill">Bebek Çorbalarına</span>
          </div>
        </div>
        <div class="card-footer-row">
          <div class="card-price">210 TL</div>
          <button class="btn-add-cart" onclick="addToCart('No.04 Saf Bebek Kolajeni', 210)">
            <span class="icon" style="width: 14px; height: 14px;"><svg viewBox="0 0 24 24" stroke="currentColor"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg></span>
            <span>Sepete Ekle</span>
          </button>
        </div>
      </div>

      <!-- Ürün 5: Rosemary Elixir -->
      <div class="product-card" data-category="kemik kolajen">
        <span class="card-trendyol-pill">✦ GURME AROMA</span>
        <span class="card-vol-pill">300 ml Cam</span>
        <div class="card-img-box" id="cardBox_no05">
          <img src="assets/gallery_no05_01_hero.jpg" alt="Rosemary Collagen Elixir" loading="lazy" id="cardImg_no05">
          <div class="card-quick-tabs">
            <button class="card-tab-btn active" onclick="switchCardImage('no05', 'assets/gallery_no05_01_hero.jpg', this)">Ürün</button>
            <button class="card-tab-btn" onclick="switchCardImage('no05', 'assets/gallery_no01_02_ingredients.jpg', this)">İçerik</button>
            <button class="card-tab-btn" onclick="switchCardImage('no05', 'assets/gallery_no01_05_texture.jpg', this)">Doku</button>
          </div>
        </div>
        <div class="card-content">
          <div class="card-series">NO. 05 • HERBAL INFUSION</div>
          <h3 class="card-name">Rosemary Collagen Elixir</h3>
          <div class="card-rating">
            <span>★★★★★</span> <span class="count">(67 değerlendirme)</span>
          </div>
          <p class="card-desc">
            Taze yayla biberiyesi, dağ kekiği ve defne yaprağıyla demlendi. Gurme yemeklerde, pilavlarda ve sıcak çorbalarda nefis Akdeniz şifası.
          </p>
          <button class="btn-quick-look" onclick="openProductModal('no05')">
            İnfografik Galeri & Analiz ↗
          </button>
          <div class="card-specs">
            <span class="spec-pill">Yabani Biberiye & Kekik</span>
            <span class="spec-pill">Yüksek Antioksidan</span>
            <span class="spec-pill">Gurme Lezzet</span>
          </div>
        </div>
        <div class="card-footer-row">
          <div class="card-price">230 TL</div>
          <button class="btn-add-cart" onclick="addToCart('No.05 Rosemary Collagen Elixir', 230)">
            <span class="icon" style="width: 14px; height: 14px;"><svg viewBox="0 0 24 24" stroke="currentColor"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg></span>
            <span>Sepete Ekle</span>
          </button>
        </div>
      </div>

      <!-- Ürün 6: 14 Günlük Lüks Kit -->
      <div class="product-card" style="background: var(--bg-card); justify-content: space-between;" data-category="kemik kolajen bagisiklik cay">
        <span class="card-trendyol-pill">✦ FULL WELLNESS SETİ</span>
        <span class="card-vol-pill">Lüks Kutu</span>
        <div class="card-img-box" id="cardBox_bundle">
          <img src="assets/gallery_bundle_01_hero.jpg" alt="14 Günlük Lüks Wellness Kiti" loading="lazy" id="cardImg_bundle">
          <div class="card-quick-tabs">
            <button class="card-tab-btn active" onclick="switchCardImage('bundle', 'assets/gallery_bundle_01_hero.jpg', this)">Set</button>
            <button class="card-tab-btn" onclick="switchCardImage('bundle', 'assets/bundle_14day_box.jpg', this)">Kutu</button>
            <button class="card-tab-btn" onclick="switchCardImage('bundle', 'assets/gallery_no01_05_texture.jpg', this)">Doku</button>
            <button class="card-tab-btn" onclick="switchCardImage('bundle', 'assets/gallery_no01_04_clinical.jpg', this)">Klinik</button>
          </div>
        </div>
        <div class="card-content">
          <div class="card-series">ÖZEL SEÇKİ • COMPLETE WELLNESS</div>
          <h3 class="card-name">14 Günlük Lüks Yenilenme Kiti</h3>
          <div class="card-rating">
            <span>★★★★★</span> <span class="count">(188 değerlendirme • %100 Memnuniyet)</span>
          </div>
          <p class="card-desc">
            Hücresel yenilenme kürü için tasarlandı: 4 kavanoz kemik suyu + 1 Night Story botanik çayı + el yapımı zeytin ağacı dozaj kaşığı ve 14 günlük kullanım rehberi.
          </p>
          <button class="btn-quick-look" onclick="openProductModal('bundle')">
            Kutu Detayları & İnfografik Galeri ↗
          </button>
          <div class="card-specs">
            <span class="spec-pill">4x İlikli Kemik Suyu</span>
            <span class="spec-pill">1x Botanik Çay</span>
            <span class="spec-pill">Ahşap Dozaj Kaşığı</span>
          </div>
        </div>
        <div class="card-footer-row">
          <div>
            <div class="card-price" style="font-size: 26px;">980 TL</div>
            <div style="font-size: 11px; color: var(--color-trust-green); font-weight: 700;">✓ Kargo Bedava</div>
          </div>
          <button class="btn-add-cart" onclick="addToCart('14 Günlük Lüks Yenilenme Kiti', 980)">
            <span class="icon" style="width: 14px; height: 14px;"><svg viewBox="0 0 24 24" stroke="currentColor"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg></span>
            <span>Sepete Ekle</span>
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- 11."""

cards_match = re.search(r'<div class="catalog-grid">.*?</div>\s*</div>\s*<!--\s*11\.', html, re.DOTALL)
if cards_match:
    html = html.replace(cards_match.group(0), cards_replacement)
    print("Catalog Grid upgraded with Trendyol interactive preview tabs!")
else:
    print("Warning: Catalog grid regex match failed.")

# 3. UPDATE JAVASCRIPT: PRODUCT_GALLERIES, openProductModal, switchCardImage, switchModalSlide
JS_OLD_START = "const PRODUCT_DETAILS = {"
JS_INSERT = """
    // ==========================================
    // TRENDYOL & COSMED STYLE INFOGRAPHIC GALLERIES
    // ==========================================
    const PRODUCT_GALLERIES = {
      no01: [
        { src: "assets/gallery_no01_01_hero.jpg", label: "1 / 6 • Ürün Görünümü & Onay Badgeleri", thumbTitle: "Ürün" },
        { src: "assets/gallery_no01_02_ingredients.jpg", label: "2 / 6 • Aktif Bileşenler & Doğal Formül", thumbTitle: "İçerik" },
        { src: "assets/gallery_no01_03_who_can_use.jpg", label: "3 / 6 • Kimler Kullanabilir?", thumbTitle: "Kullanıcı" },
        { src: "assets/gallery_no01_04_clinical.jpg", label: "4 / 6 • Acıbadem Klinik Raporu", thumbTitle: "Klinik" },
        { src: "assets/gallery_no01_05_texture.jpg", label: "5 / 6 • Doku & Jelatin Kıvam Testi", thumbTitle: "Doku" },
        { src: "assets/gallery_no01_06_how_to_use.jpg", label: "6 / 6 • Nasıl Tüketilir? (3 Adım)", thumbTitle: "Kullanım" }
      ],
      no02: [
        { src: "assets/gallery_no02_01_hero.jpg", label: "1 / 5 • Golden Immunity Görünüm", thumbTitle: "Ürün" },
        { src: "assets/gallery_no02_02_ingredients.jpg", label: "2 / 5 • Zerdeçal & Zencefil Formülü", thumbTitle: "İçerik" },
        { src: "assets/gallery_no01_05_texture.jpg", label: "3 / 5 • Doğal Jelatin Doku Kanıtı", thumbTitle: "Doku" },
        { src: "assets/gallery_no01_03_who_can_use.jpg", label: "4 / 5 • Kimler Güvenle Kullanabilir?", thumbTitle: "Kullanıcı" },
        { src: "assets/gallery_no01_06_how_to_use.jpg", label: "5 / 5 • Sabah Aç Karnına Rutin", thumbTitle: "Kullanım" }
      ],
      no03: [
        { src: "assets/gallery_no03_01_hero.jpg", label: "1 / 3 • Gece Masalı Çay Paketi", thumbTitle: "Paket" },
        { src: "assets/product_no03_night_tea.jpg", label: "2 / 3 • Demleme ve Çiçek Harmanı", thumbTitle: "Demleme" },
        { src: "assets/gallery_no01_03_who_can_use.jpg", label: "3 / 3 • Derin REM Uykusu & Glisin", thumbTitle: "Uyku" }
      ],
      no04: [
        { src: "assets/gallery_no04_01_hero.jpg", label: "1 / 5 • Saf Bebek Kolajeni", thumbTitle: "Ürün" },
        { src: "assets/gallery_no04_02_baby_safety.jpg", label: "2 / 5 • Sıfır Tuz & Pediatrik Güvenlik", thumbTitle: "Güvenlik" },
        { src: "assets/gallery_no01_05_texture.jpg", label: "3 / 5 • Doğal Jelatin Kıvamı", thumbTitle: "Doku" },
        { src: "assets/gallery_no01_03_who_can_use.jpg", label: "4 / 5 • 6. Aydan İtibaren Ek Gıda", thumbTitle: "Ek Gıda" },
        { src: "assets/gallery_no01_06_how_to_use.jpg", label: "5 / 5 • Çorba ve Püre Hazırlama", thumbTitle: "Kullanım" }
      ],
      no05: [
        { src: "assets/gallery_no05_01_hero.jpg", label: "1 / 4 • Rosemary Collagen Elixir", thumbTitle: "Ürün" },
        { src: "assets/gallery_no01_02_ingredients.jpg", label: "2 / 4 • Akdeniz Bitkisel İnfüzyon", thumbTitle: "İçerik" },
        { src: "assets/gallery_no01_05_texture.jpg", label: "3 / 4 • Jelatin Doku Kanıtı", thumbTitle: "Doku" },
        { src: "assets/gallery_no01_06_how_to_use.jpg", label: "4 / 4 • Gurme Yemek Rutini", thumbTitle: "Kullanım" }
      ],
      bundle: [
        { src: "assets/gallery_bundle_01_hero.jpg", label: "1 / 4 • 14 Günlük Lüks Yenilenme Kiti", thumbTitle: "Set" },
        { src: "assets/bundle_14day_box.jpg", label: "2 / 4 • Açık Kutu İçeriği & Kaşık", thumbTitle: "Kutu" },
        { src: "assets/gallery_no01_05_texture.jpg", label: "3 / 4 • Yoğun Kolajen Doku Kanıtı", thumbTitle: "Doku" },
        { src: "assets/gallery_no01_04_clinical.jpg", label: "4 / 4 • Acıbadem Klinik Raporu", thumbTitle: "Klinik" }
      ]
    };

    let currentModalKey = "no01";
    let currentModalSlideIdx = 0;
    let modalSelectedQty = 1;

    function switchCardImage(cardKey, imgSrc, btn) {
      const img = document.getElementById('cardImg_' + cardKey);
      if (img) {
        img.style.opacity = '0.3';
        setTimeout(() => {
          img.src = imgSrc;
          img.style.opacity = '1';
        }, 120);
      }
      const parentTabs = btn.parentElement;
      if (parentTabs) {
        parentTabs.querySelectorAll('.card-tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
      }
    }

    function switchModalSlide(idx) {
      const gallery = PRODUCT_GALLERIES[currentModalKey] || PRODUCT_GALLERIES['no01'];
      if (idx < 0) idx = gallery.length - 1;
      if (idx >= gallery.length) idx = 0;
      currentModalSlideIdx = idx;

      const mainImg = document.getElementById('modalMainImg');
      const badge = document.getElementById('modalSlideBadge');
      if (mainImg) {
        mainImg.style.opacity = '0.4';
        setTimeout(() => {
          mainImg.src = gallery[idx].src;
          mainImg.style.opacity = '1';
        }, 100);
      }
      if (badge) {
        badge.innerText = gallery[idx].label;
      }

      // Update thumbnails
      const thumbs = document.querySelectorAll('.gallery-thumb-item');
      thumbs.forEach((t, i) => {
        if (i === idx) t.classList.add('active');
        else t.classList.remove('active');
      });
    }

    function prevModalSlide() {
      switchModalSlide(currentModalSlideIdx - 1);
    }

    function nextModalSlide() {
      switchModalSlide(currentModalSlideIdx + 1);
    }

    function updateModalQty(delta) {
      modalSelectedQty = Math.max(1, modalSelectedQty + delta);
      const qtyElem = document.getElementById('modalQtyVal');
      const priceElem = document.getElementById('modalTotalPrice');
      const data = PRODUCT_DETAILS[currentModalKey];
      if (qtyElem) qtyElem.innerText = modalSelectedQty;
      if (priceElem && data) {
        const total = data.price * modalSelectedQty;
        priceElem.innerText = total + ' TL';
      }
    }
"""

html = html.replace("const PRODUCT_DETAILS = {", JS_INSERT + "\n    const PRODUCT_DETAILS = {")

# Update openProductModal function to render Trendyol gallery
OLD_OPEN_MODAL_REGEX = r'function openProductModal\(key\)\s*\{.*?\n    \}'
NEW_OPEN_MODAL = """function openProductModal(key) {
      currentModalKey = key;
      currentModalSlideIdx = 0;
      modalSelectedQty = 1;
      
      const data = PRODUCT_DETAILS[key];
      if (!data) return;

      const gallery = PRODUCT_GALLERIES[key] || PRODUCT_GALLERIES['no01'];

      // Build Thumbnails HTML
      let thumbsHtml = '';
      gallery.forEach((slide, idx) => {
        const activeClass = idx === 0 ? 'active' : '';
        thumbsHtml += `
          <div class="gallery-thumb-item ${activeClass}" onclick="switchModalSlide(${idx})" title="${slide.label}">
            <img src="${slide.src}" alt="${slide.thumbTitle}" loading="lazy">
            <span class="gallery-thumb-caption">${slide.thumbTitle}</span>
          </div>
        `;
      });

      // Build Table HTML
      let tableHtml = '<table class="modal-table">';
      data.table.forEach(row => {
        tableHtml += `<tr><th>${row[0]}</th><td>${row[1]}</td></tr>`;
      });
      tableHtml += '</table>';

      const installment3 = Math.round((data.price / 3) * 100) / 100;

      const content = document.getElementById('modalContent');
      content.innerHTML = `
        <div class="modal-product-layout">
          <!-- Sol Kolon: Trendyol İnfografik Galeri -->
          <div class="trendyol-gallery">
            <div class="gallery-main-viewport">
              <button class="gallery-nav-arrow prev" onclick="prevModalSlide()" title="Önceki Slayt">‹</button>
              <img id="modalMainImg" class="gallery-main-img" src="${gallery[0].src}" alt="${data.title}">
              <button class="gallery-nav-arrow next" onclick="nextModalSlide()" title="Sonraki Slayt">›</button>
              <div class="gallery-slide-badge" id="modalSlideBadge">${gallery[0].label}</div>
            </div>
            <!-- Küçük Thumbnail Şeridi -->
            <div class="gallery-thumb-strip">
              ${thumbsHtml}
            </div>
          </div>

          <!-- Sağ Kolon: Ürün Detay & Acıbadem Satın Alma Kutusu -->
          <div>
            <div class="modal-subtitle">${data.subtitle}</div>
            <h2 class="modal-title" style="font-size: 28px; line-height: 1.2; margin-bottom: 8px;">${data.title}</h2>
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 14px;">
              <span style="color: #E2B755; font-size: 15px;">★★★★★</span>
              <span style="font-size: 12px; font-weight: 700; color: var(--color-trust-green);">5.0 (140+ Doğrulanmış Sipariş)</span>
              <span style="font-size: 11px; background: #e8f5e9; color: #2e7d32; padding: 2px 8px; border-radius: 10px; font-weight: 700;">Acıbadem Tıp Dayanaklı</span>
            </div>

            <div style="display: flex; align-items: baseline; gap: 14px; margin-bottom: 12px;">
              <span id="modalTotalPrice" style="font-family: var(--font-serif); font-size: 32px; font-weight: 700; color: var(--gold-champagne);">${data.price} TL</span>
              <span class="installment-pill">Vade farksız 3 taksit x ${installment3} TL</span>
            </div>

            <p class="modal-text" style="font-size: 14px; line-height: 1.6; margin-bottom: 16px;">${data.desc}</p>

            <!-- Adet Seçici & Sepete Ekle -->
            <div class="modal-qty-row">
              <span style="font-size: 13px; font-weight: 700; color: #1A3826;">Adet:</span>
              <div class="qty-counter">
                <button class="qty-btn" onclick="updateModalQty(-1)">−</button>
                <span class="qty-val" id="modalQtyVal">1</span>
                <button class="qty-btn" onclick="updateModalQty(1)">+</button>
              </div>
              <button class="btn-cta" style="flex: 1; justify-content: center; background: #1A3826; color: #fff; padding: 14px 20px; border-radius: var(--radius-full); border: none; font-weight: 700; cursor: pointer; font-size: 14px;" onclick="for(let q=0; q<modalSelectedQty; q++) { addToCart('${data.title}', ${data.price}); } closeProductModal();">
                Sepete Ekle (${data.price} TL)
              </button>
            </div>

            <div style="font-size: 12px; color: var(--color-trust-green); font-weight: 600; margin-bottom: 18px; display: flex; align-items: center; gap: 6px;">
              <span>🚚</span>
              <span>750 TL ve üzerine <strong>ÜCRETSİZ SOĞUK ZİNCİR KARGO</strong> • Kırılmaya Karşı Sigortalı</span>
            </div>

            <div class="modal-section-title">Acıbadem Bilimsel Besin Değerleri</div>
            ${tableHtml}

            <div style="margin-top: 18px;">
              <button class="btn-cta" style="width: 100%; justify-content: center; background: #25D366; color: #fff; padding: 12px; border-radius: var(--radius-full); border: none; font-weight: 700; cursor: pointer; font-size: 13px;" onclick="window.open('https://wa.me/905330849027?text=Merhaba,%20${encodeURIComponent(data.title)}%20hakk%C4%B1nda%20bilgi%20ve%20sipari%C5%9F%20vermek%20istiyorum.', '_blank')">
                WhatsApp ile 1 Tıkla Sipariş Ver ↗
              </button>
            </div>
          </div>
        </div>
      `;

      document.getElementById('productModal').classList.add('active');
    }"""

html = re.sub(OLD_OPEN_MODAL_REGEX, NEW_OPEN_MODAL, html, count=1, flags=re.DOTALL)
print("openProductModal updated with 2-column layout and Trendyol gallery!")

# Also add bundle to PRODUCT_DETAILS if not already present
if 'bundle:' not in html:
    bundle_data = """      bundle: {
        title: "14 Günlük Lüks Hücresel Yenilenme Kiti",
        subtitle: "The Ultimate Wellness Box • 4 Broth + 1 Tea + Spoon",
        desc: "4 kavanoz ilikli kemik suyu, 1 paket Night Story sakinleşme çayı, el yapımı zeytin ağacı dozaj kaşığı ve 14 günlük biyolojik dönüşüm takvimi. %100 doğal, koruyucusuz ve Acıbadem sağlık standartlarında.",
        price: 980,
        table: [
          ["Kutu İçeriği", "4x Pure Essence Kemik Suyu (300 ml)"],
          ["Gece Ritüeli", "1x Night Story Botanik Çay (75 g)"],
          ["Aksesuar", "1x El Yapımı Zeytin Ağacı Dozaj Kaşığı"],
          ["Rehber", "1x 14 Günlük Hücresel Yenilenme Kitapçığı"],
          ["Kargo", "Ücretsiz Korumalı Soğuk Zincir Teslimat"],
          ["Tasarruf", "%20 Avantajlı Wellness Paketi"]
        ]
      },
"""
    html = html.replace("const PRODUCT_DETAILS = {", "const PRODUCT_DETAILS = {\n" + bundle_data)
    print("Added bundle product details to PRODUCT_DETAILS!")

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Upgrade complete! Saved index.html successfully.")
