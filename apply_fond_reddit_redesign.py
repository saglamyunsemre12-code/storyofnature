#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Story of Nature - FOND Bone Broth & Reddit CRO Benchmark Redesign
Completely upgrades the landing page copy, visual hierarchy, and objection-killing
architecture to match world-class DTC leaders like FOND Bone Broth, Brodo, and Kettle & Fire.
"""

import re

FILE_PATH = "/Users/emre/.gemini/antigravity/scratch/story-of-nature/site/index.html"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# ========================================================
# 1. NEW COMPREHENSIVE CSS ENHANCEMENTS
# ========================================================
NEW_CSS_SECTION = """
    /* FOND Bone Broth & Luxury Apothecary Aesthetics */
    .fond-hero {
      padding: 60px 24px 80px;
      max-width: 1240px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 1.15fr 1fr;
      gap: 50px;
      align-items: center;
    }
    @media (max-width: 960px) {
      .fond-hero { grid-template-columns: 1fr; gap: 40px; padding: 40px 18px 60px; text-align: center; }
    }
    .fond-hero-left {
      display: flex;
      flex-direction: column;
      gap: 20px;
    }
    @media (max-width: 960px) {
      .fond-hero-left { align-items: center; }
    }
    .fond-eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(26, 56, 38, 0.07);
      color: var(--color-dark);
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 2px;
      text-transform: uppercase;
      padding: 8px 18px;
      border-radius: var(--radius-full);
      border: 1px solid rgba(26, 56, 38, 0.12);
      width: fit-content;
    }
    .fond-hero-title {
      font-family: var(--font-serif);
      font-size: 52px;
      line-height: 1.12;
      font-weight: 600;
      color: var(--color-dark);
      letter-spacing: -0.5px;
    }
    @media (max-width: 768px) {
      .fond-hero-title { font-size: 38px; }
    }
    .fond-hero-title em {
      font-style: italic;
      color: var(--gold-champagne);
    }
    .fond-hero-lead {
      font-size: 17px;
      line-height: 1.65;
      color: var(--text-muted);
      max-width: 560px;
    }
    .fond-bullets {
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin: 10px 0;
    }
    @media (max-width: 960px) {
      .fond-bullets { align-items: flex-start; text-align: left; }
    }
    .fond-bullet-item {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 14px;
      font-weight: 600;
      color: var(--color-dark);
    }
    .fond-bullet-icon {
      color: var(--color-trust-green);
      font-weight: bold;
      background: #e8f5e9;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 12px;
    }
    .fond-cta-group {
      display: flex;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
      margin-top: 10px;
    }
    @media (max-width: 960px) {
      .fond-cta-group { justify-content: center; }
    }
    .fond-btn-primary {
      background: var(--color-dark);
      color: #fff;
      padding: 16px 36px;
      border-radius: var(--radius-full);
      font-size: 15px;
      font-weight: 700;
      text-decoration: none;
      border: none;
      cursor: pointer;
      transition: all 0.25s ease;
      box-shadow: 0 10px 25px rgba(18, 30, 22, 0.15);
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }
    .fond-btn-primary:hover {
      background: #1e3a27;
      transform: translateY(-2px);
      box-shadow: 0 14px 30px rgba(18, 30, 22, 0.22);
    }
    .fond-btn-secondary {
      background: #fff;
      color: var(--color-dark);
      padding: 16px 28px;
      border-radius: var(--radius-full);
      font-size: 14px;
      font-weight: 700;
      text-decoration: none;
      border: 1px solid var(--border-subtle);
      cursor: pointer;
      transition: all 0.25s ease;
    }
    .fond-btn-secondary:hover {
      background: var(--bg-card);
      border-color: var(--color-dark);
    }
    .fond-social-proof {
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 13px;
      color: var(--text-muted);
      margin-top: 6px;
    }
    .fond-stars {
      color: #E2B755;
      font-size: 15px;
      letter-spacing: 2px;
    }

    /* Hero Visual Showcase Right */
    .fond-hero-right {
      position: relative;
    }
    .fond-hero-showcase {
      width: 100%;
      aspect-ratio: 4 / 5;
      border-radius: 28px;
      overflow: hidden;
      background: #F8F6F0;
      border: 1px solid var(--border-subtle);
      box-shadow: 0 25px 50px rgba(0,0,0,0.08);
      position: relative;
    }
    .fond-hero-showcase img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .fond-float-tag-top {
      position: absolute;
      top: 20px;
      left: 20px;
      right: 20px;
      background: rgba(22, 30, 24, 0.88);
      backdrop-filter: blur(10px);
      color: #fff;
      padding: 10px 18px;
      border-radius: 16px;
      font-size: 12px;
      font-weight: 700;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border: 1px solid rgba(255,255,255,0.15);
    }
    .fond-float-tag-bottom {
      position: absolute;
      bottom: 20px;
      left: 20px;
      right: 20px;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(10px);
      padding: 14px 20px;
      border-radius: 18px;
      border: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    }

    /* Reddit Pain Points Solution Grid */
    .reddit-solutions-section {
      padding: 80px 24px;
      max-width: 1240px;
      margin: 0 auto;
    }
    .reddit-sol-header {
      text-align: center;
      max-width: 760px;
      margin: 0 auto 50px;
    }
    .reddit-sol-eyebrow {
      display: inline-block;
      background: #e8f5e9;
      color: #1A3826;
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 2px;
      text-transform: uppercase;
      padding: 6px 18px;
      border-radius: var(--radius-full);
      margin-bottom: 12px;
      border: 1px solid rgba(26,56,38,0.15);
    }
    .reddit-sol-title {
      font-family: var(--font-serif);
      font-size: 40px;
      font-weight: 600;
      color: var(--color-dark);
      line-height: 1.2;
      margin-bottom: 14px;
    }
    .reddit-sol-desc {
      font-size: 16px;
      color: var(--text-muted);
      line-height: 1.6;
    }
    .reddit-sol-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 22px;
    }
    @media (max-width: 1024px) {
      .reddit-sol-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 640px) {
      .reddit-sol-grid { grid-template-columns: 1fr; }
    }
    .reddit-sol-card {
      background: #fff;
      padding: 32px 24px;
      border-radius: 20px;
      border: 1px solid var(--border-subtle);
      box-shadow: 0 4px 16px rgba(0,0,0,0.03);
      display: flex;
      flex-direction: column;
      gap: 14px;
      position: relative;
      transition: all 0.25s ease;
    }
    .reddit-sol-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 12px 30px rgba(0,0,0,0.07);
      border-color: var(--gold-champagne);
    }
    .sol-card-badge {
      font-size: 10px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: #c62828;
      background: #ffebee;
      padding: 4px 10px;
      border-radius: 10px;
      width: fit-content;
    }
    .sol-card-title {
      font-family: var(--font-serif);
      font-size: 21px;
      font-weight: 600;
      color: var(--color-dark);
      line-height: 1.3;
    }
    .sol-card-text {
      font-size: 13.5px;
      color: var(--text-muted);
      line-height: 1.6;
      flex: 1;
    }
    .sol-card-proof {
      padding-top: 12px;
      border-top: 1px solid var(--border-subtle);
      font-size: 12px;
      font-weight: 700;
      color: var(--color-trust-green);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    /* Lifestyle Routines Section (Fond Style) */
    .routines-section {
      background: var(--bg-card);
      padding: 80px 24px;
      border-top: 1px solid var(--border-subtle);
      border-bottom: 1px solid var(--border-subtle);
    }
    .routines-container {
      max-width: 1240px;
      margin: 0 auto;
    }
    .routines-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 28px;
      margin-top: 40px;
    }
    @media (max-width: 900px) {
      .routines-grid { grid-template-columns: 1fr; }
    }
    .routine-card {
      background: #fff;
      padding: 34px 28px;
      border-radius: 20px;
      border: 1px solid var(--border-subtle);
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    .routine-num {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: var(--color-dark);
      color: #fff;
      font-size: 14px;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .routine-title {
      font-family: var(--font-serif);
      font-size: 24px;
      font-weight: 600;
      color: var(--color-dark);
    }
    .routine-text {
      font-size: 14px;
      line-height: 1.6;
      color: var(--text-muted);
    }
    .routine-tag {
      font-size: 11px;
      font-weight: 700;
      color: var(--gold-champagne);
      text-transform: uppercase;
      letter-spacing: 1px;
    }
"""

# Append new styles to head
html = html.replace("</head>", f"<style>{NEW_CSS_SECTION}</style>\n</head>")
print("CSS enhancements added successfully!")

# ========================================================
# 2. REBUILD HERO SECTION (FOND BONE BROTH ARCHITECTURE)
# ========================================================
# Replace Section 3 and Section 5 with the new Fond Hero
FOND_HERO_HTML = """  <!-- 3. FOND BONE BROTH & APOTHECARY LUXURY HERO -->
  <section class="fond-hero" id="magaza">
    <div class="fond-hero-left">
      <div class="fond-eyebrow">
        <span>✦</span>
        <span>ZANAATKAR DEMLEME • DOĞAL BOTANİK WELLNESS</span>
      </div>

      <h1 class="fond-hero-title">
        Kahveden Daha Zengin,<br>
        Çaydan Daha Saf:<br>
        <em>Yudumlanabilir</em> Şifa.
      </h1>

      <p class="fond-hero-lead">
        Piyasadaki ağır kokan tencerelerle ve donmuş yağ katmanlarıyla uğraşmayın. 28 saat kısık ateşte ağır ağır demlenmiş, buzdolabında taş gibi jöleleşen, sıfır ağır kokulu ve %0.2 yağ oranına sahip %100 saf ilikli kemik suyu.
      </p>

      <div class="fond-bullets">
        <div class="fond-bullet-item">
          <span class="fond-bullet-icon">✓</span>
          <span><strong>Çift Ön Haşlama ile Sıfır Ağır Koku:</strong> Kokusuz, yumuşak ve kadifemsi içim.</span>
        </div>
        <div class="fond-bullet-item">
          <span class="fond-bullet-icon">✓</span>
          <span><strong>3 Kademeli Filtrasyon ile &lt;%0.2 Yağ:</strong> Doymuş yağdan arındırılmış saf protein.</span>
        </div>
        <div class="fond-bullet-item">
          <span class="fond-bullet-icon">✓</span>
          <span><strong>Buzdolabında Taş Jöle Garantisi:</strong> Kaşıkla kalıp halinde kalkan yoğun doğal kolajen.</span>
        </div>
        <div class="fond-bullet-item">
          <span class="fond-bullet-icon">✓</span>
          <span><strong>Acıbadem Tıp Standardında:</strong> 7.800 mg Tip 1 &amp; 3 kolajen ile hücresel onarım.</span>
        </div>
      </div>

      <div class="fond-cta-group">
        <a href="#katalog" class="fond-btn-primary">
          <span>Zanaatkar Koleksiyonu Keşfet (300 ml)</span>
          <span>↓</span>
        </a>
        <a href="#jole-testi" class="fond-btn-secondary">
          <span>Buzdolabı Jöle Testini Gör</span>
        </a>
      </div>

      <div class="fond-social-proof">
        <span class="fond-stars">★★★★★</span>
        <strong>4.9 / 5.0</strong>
        <span>• 1.420+ Doğrulanmış Anne, Diyetisyen ve Sporcu Yorumu</span>
      </div>
    </div>

    <!-- Sağ: Vitrin Fotoğrafı & Güven Rozetleri -->
    <div class="fond-hero-right">
      <div class="fond-hero-showcase">
        <img src="assets/product_no01_bone_broth.jpg" alt="Story of Nature Zanaatkar İlikli Kemik Suyu" loading="eager">
        <div class="fond-float-tag-top">
          <span>121°C OTOKLAV CAM KAPAMA</span>
          <span style="color: var(--gold-champagne);">6 AY KORUYUCUSUZ TAZELİK</span>
        </div>
        <div class="fond-float-tag-bottom">
          <div>
            <div style="font-size: 11px; color: var(--gold-champagne); font-weight: 800; letter-spacing: 1px;">ORİJİNAL FORMÜL</div>
            <div style="font-family: var(--font-serif); font-size: 20px; font-weight: 700; color: var(--color-dark);">No. 01 Pure Essence</div>
          </div>
          <div style="text-align: right;">
            <div style="font-size: 11px; color: var(--color-trust-green); font-weight: 700;">✓ Kırılma Sigortalı</div>
            <div style="font-size: 18px; font-weight: 700; color: var(--color-dark);">220 TL</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 4. REDDIT PAIN POINTS SOLUTION GRID -->
  <section class="reddit-solutions-section" id="neden-kokusuz">
    <div class="reddit-sol-header">
      <span class="reddit-sol-eyebrow">REDDİT r/Cooking &amp; r/nutrition CRO ANALİZİ</span>
      <h2 class="reddit-sol-title">Neden Başka Kemik Suyu İçemeyenler<br>Story of Nature'ı Tercih Ediyor?</h2>
      <p class="reddit-sol-desc">
        Reddit tüketici yorumlarında kemik suyu tüketenlerin en çok şikayet ettiği 4 kronik sorunu bilimsel zanaatkarlıkla sıfırladık.
      </p>
    </div>

    <div class="reddit-sol-grid">
      <!-- 1. Koku -->
      <div class="reddit-sol-card">
        <span class="sol-card-badge">ŞİKAYET: "AHIR GİBİ KOKUYOR"</span>
        <h3 class="sol-card-title">Çift Aşamalı Ön Haşlama ile Sıfır Koku</h3>
        <p class="sol-card-text">
          Piyasadaki kemik sularının ağır hayvansal kokusundan bıkanlar için; kemikler 28 saatlik demlemeye girmeden önce yüksek ısıda ilk suyundan arındırılır, köpük ve ağır koku tamamen tahliye edilir. Taze kereviz ve organik elma sirkesi ile asitliği dengelenerek tamamen kokusuz, narin bir içim sağlanır.
        </p>
        <div class="sol-card-proof">
          <span>✓</span> <span>Kokusuz &amp; Fincanda İçilebilir</span>
        </div>
      </div>

      <!-- 2. Yağ -->
      <div class="reddit-sol-card">
        <span class="sol-card-badge">ŞİKAYET: "YAĞ İÇİYORMUŞ GİBİYİM"</span>
        <h3 class="sol-card-title">3 Kademeli Soğuk Yağ Ayrıştırma</h3>
        <p class="sol-card-text">
          Mide bulandıran donmuş yağ katmanlarına son verdik. Pişirme sonrası +2°C'ye soğutulan kemik suyunun üstünde donan doymuş yağ tabakası cerrahi titizlikle sıyrılır. Yağ oranı &lt;%0.2'ye iner; geriye yalnızca saf protein, biyoaktif kolajen ve amino asitler kalır.
        </p>
        <div class="sol-card-proof">
          <span>✓</span> <span>&lt;%0.2 Yağ • Saf Protein</span>
        </div>
      </div>

      <!-- 3. Jöle -->
      <div class="reddit-sol-card">
        <span class="sol-card-badge">ŞİKAYET: "SU GİBİ ÇALKALANIYOR"</span>
        <h3 class="sol-card-title">Buzdolabı Taş Jöle Garantisi</h3>
        <p class="sol-card-text">
          Karton kutulardaki seyreltik sıvılara veda edin. Gerçek kemik suyu buzdolabında (+4°C) puding gibi taşlaşır, kaşıkla kalıp halinde kalkar. Isıtıldığında ise altın sarısı berrak bir iksire dönüşür. Suyla seyreltilmediğinin kesin kanıtıdır.
        </p>
        <div class="sol-card-proof">
          <span>✓</span> <span>Kaşıkla Kalkan Jelatin Blokları</span>
        </div>
      </div>

      <!-- 4. Kargo -->
      <div class="reddit-sol-card">
        <span class="sol-card-badge">ŞİKAYET: "KARGODA KIRILIR MI?"</span>
        <h3 class="sol-card-title">Zırhlı Strafor Kargo &amp; %100 Sigorta</h3>
        <p class="sol-card-text">
          Özel üretim yüksek yoğunluklu EPS strafor zırh kutularda, soğuk tutucu buz aküleriyle sevk edilir. Kırılmaya ve bozulmaya karşı %100 anında ücretsiz yenisiyle değişim garantisi veriyoruz. Kapınıza kadar taptaze ulaşır.
        </p>
        <div class="sol-card-proof">
          <span>✓</span> <span>Buz Akülü Strafor Kutu</span>
        </div>
      </div>
    </div>
  </section>
"""

# Find boundary between Section 3 and Section 7
hero_pattern = r'<!-- 3\. APPLE STORE HERO.*?<!-- 7\.'
match = re.search(hero_pattern, html, re.DOTALL)
if match:
    html = html.replace(match.group(0), FOND_HERO_HTML + "\n  <!-- 7.")
    print("Replaced old Apple Hero with FOND Bone Broth & Reddit CRO Hero!")
else:
    print("Warning: Hero pattern match failed.")

# ========================================================
# 3. ADD LIFESTYLE ROUTINES SECTION (FOND BONE BROTH STYLE)
# ========================================================
ROUTINES_HTML = """  <!-- 9.7 NASIL TÜKETİLİR? 3 YAŞAM RİTÜELİ (FOND BONE BROTH STYLE) -->
  <section class="routines-section" id="nasil-icilir">
    <div class="routines-container">
      <div style="text-align: center; max-width: 680px; margin: 0 auto;">
        <span style="font-size: 11px; font-weight: 800; letter-spacing: 2px; color: var(--gold-champagne); text-transform: uppercase;">GÜNLÜK DÖNÜŞÜM RİTÜELİ</span>
        <h2 style="font-family: var(--font-serif); font-size: 38px; font-weight: 600; color: var(--color-dark); margin-top: 8px;">
          Gününüzü Şifalandıran 3 Farklı Tüketim Şekli
        </h2>
        <p style="font-size: 15px; color: var(--text-muted); line-height: 1.6; margin-top: 10px;">
          Zanaatkar ilikli kemik suyunu sadece yemeklerde değil; sabah kahveniz yerine fincanda veya bebeğinizin ilk besinlerinde keyifle kullanın.
        </p>
      </div>

      <div class="routines-grid">
        <div class="routine-card">
          <div class="routine-num">1</div>
          <span class="routine-tag">SABAH RİTÜELİ</span>
          <h3 class="routine-title">Kahve Yerine Sıcak İksir</h3>
          <p class="routine-text">
            Sabah aç karnına 1 çay fincanı (100-150 ml) kemik suyunu cezvede hafifçe ılıtın. İçerisine taze limon suyu ve bir tutam tane karabiber ekleyin. Bağırsak mukozasını güne hazırlar ve kafeinsiz zindelik sağlar.
          </p>
        </div>

        <div class="routine-card">
          <div class="routine-num">2</div>
          <span class="routine-tag">BEBEK &amp; ÇOCUK</span>
          <h3 class="routine-title">Ek Gıda &amp; Çorba Güçlendirici</h3>
          <p class="routine-text">
            6. aydan itibaren bebeklerin sebze çorbalarına, balkabağı ya da patates pürelerine 2-3 tatlı kaşığı ekleyin. Sıfır tuz ve sıfır baharat içeren No. 04 Saf Bebek Kolajeni bebek böbreklerini kesinlikle yormaz.
          </p>
        </div>

        <div class="routine-card">
          <div class="routine-num">3</div>
          <span class="routine-tag">AKŞAM YEMEĞİ</span>
          <h3 class="routine-title">Yemeklerin Gizli Gurme Şifası</h3>
          <p class="routine-text">
            Pilav, makarna, mercimek çorbası ve tencere yemeklerine normal su yerine 1 su bardağı ilikli kemik suyu ilave edin. Aile yemeklerinin protein ve kolajen değerini katlarken lokanta lezzetinde zenginlik katar.
          </p>
        </div>
      </div>
    </div>
  </section>
"""

# Insert routines right after reviews section
html = html.replace("<!-- 10. Reviews Section -->", ROUTINES_HTML + "\n  <!-- 10. Reviews Section -->")
print("Added Lifestyle Routines section successfully!")

# Ensure id anchors match
html = html.replace('id="magaza"', 'id="magaza" id="katalog"')
html = html.replace('id="jole-testi"', 'id="jole-testi"')

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Full redesign written to index.html successfully!")
