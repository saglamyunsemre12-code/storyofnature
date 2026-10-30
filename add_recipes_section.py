#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Story of Nature - Recipes & Culinary Chapter Generator
Inserts an interactive, gourmet recipe module into index.html
offering actionable culinary recipes using Story of Nature broths.
"""

import re

FILE_PATH = "/Users/emre/.gemini/antigravity/scratch/story-of-nature/site/index.html"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. RECIPES CSS STYLES
RECIPES_CSS = """
    /* ========================================================
       RECIPES & CULINARY CHAPTER (Mutfaktan Şifa Reçeteleri)
       ======================================================== */
    .recipes-section {
      padding: 90px 24px;
      max-width: 1240px;
      margin: 0 auto;
    }
    .recipes-header {
      text-align: center;
      max-width: 760px;
      margin: 0 auto 40px;
    }
    .recipes-eyebrow {
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
    .recipes-title {
      font-family: var(--font-serif);
      font-size: 42px;
      font-weight: 600;
      color: var(--color-dark);
      line-height: 1.2;
      margin-bottom: 12px;
    }
    .recipes-desc {
      font-size: 16px;
      color: var(--text-muted);
      line-height: 1.6;
    }
    .recipe-tabs-bar {
      display: flex;
      justify-content: center;
      gap: 10px;
      flex-wrap: wrap;
      margin-bottom: 40px;
    }
    .recipe-tab-btn {
      background: #fff;
      border: 1px solid var(--border-subtle);
      color: var(--color-dark);
      padding: 10px 22px;
      border-radius: var(--radius-full);
      font-size: 13.5px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .recipe-tab-btn:hover {
      background: var(--bg-card);
      border-color: var(--color-dark);
    }
    .recipe-tab-btn.active {
      background: var(--color-dark);
      color: #fff;
      border-color: var(--color-dark);
      box-shadow: 0 4px 14px rgba(18, 30, 22, 0.15);
    }
    .recipes-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
      gap: 28px;
    }
    @media (max-width: 768px) {
      .recipes-grid { grid-template-columns: 1fr; }
    }
    .recipe-card {
      background: #fff;
      border-radius: 22px;
      border: 1px solid var(--border-subtle);
      padding: 30px 26px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.03);
      display: flex;
      flex-direction: column;
      gap: 16px;
      transition: all 0.25s ease;
      position: relative;
    }
    .recipe-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 14px 35px rgba(0,0,0,0.07);
      border-color: var(--gold-champagne);
    }
    .recipe-meta-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11px;
      font-weight: 700;
    }
    .recipe-cat-badge {
      background: #e8f5e9;
      color: var(--color-trust-green);
      padding: 4px 10px;
      border-radius: 10px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .recipe-time-badge {
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .recipe-card-title {
      font-family: var(--font-serif);
      font-size: 22px;
      font-weight: 600;
      color: var(--color-dark);
      line-height: 1.3;
    }
    .recipe-prod-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 11.5px;
      font-weight: 700;
      color: var(--gold-champagne);
      background: var(--gold-tint);
      padding: 5px 12px;
      border-radius: 12px;
      width: fit-content;
    }
    .recipe-benefit-tag {
      font-size: 12px;
      font-weight: 600;
      color: var(--color-trust-green);
    }
    .recipe-box-ingredients {
      background: var(--bg-card);
      padding: 16px 18px;
      border-radius: 14px;
      border: 1px solid var(--border-subtle);
      font-size: 13px;
    }
    .recipe-box-ingredients strong {
      display: block;
      color: var(--color-dark);
      margin-bottom: 6px;
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .recipe-box-ingredients ul {
      margin: 0;
      padding-left: 18px;
      color: var(--text-main);
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .recipe-box-steps {
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.6;
      flex: 1;
    }
    .recipe-box-steps strong {
      display: block;
      color: var(--color-dark);
      margin-bottom: 6px;
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .recipe-box-steps ol {
      margin: 0;
      padding-left: 18px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .recipe-card-footer {
      padding-top: 16px;
      border-top: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
    }
    .recipe-atc-btn {
      flex: 1;
      background: var(--color-dark);
      color: #fff;
      padding: 11px 16px;
      border-radius: var(--radius-full);
      font-size: 13px;
      font-weight: 700;
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: background 0.2s;
    }
    .recipe-atc-btn:hover {
      background: #1e3a27;
    }
"""

# Insert CSS
html = html.replace("</head>", f"<style>{RECIPES_CSS}</style>\n</head>")

# 2. RECIPES HTML SECTION
RECIPES_HTML = """  <!-- 9.8 MUTFAKTAN ŞİFA: ZANAATKAR REÇETELER & YEMEK TARİFLERİ -->
  <section class="recipes-section" id="tarifler">
    <div class="recipes-header">
      <span class="recipes-eyebrow">MUTFAKTAN ŞİFA • PRATİK REÇETELER</span>
      <h2 class="recipes-title">İlikli Kemik Suyuyla Hazırlanan<br>Zanaatkar Yemek Tarifleri</h2>
      <p class="recipes-desc">
        Bebek ek gıdasından sabah kahvesi yerine geçen şifa shot'larına, lokanta usulü çorbalardan gurme pilavlara kadar en sevilen 5 fonksiyonel mutfak reçetesi.
      </p>
    </div>

    <!-- Filtre Sekmeleri -->
    <div class="recipe-tabs-bar">
      <button class="recipe-tab-btn active" onclick="filterRecipes('all', this)">Tüm Tarifler (5)</button>
      <button class="recipe-tab-btn" onclick="filterRecipes('bebek', this)">👶 Bebek Ek Gıda</button>
      <button class="recipe-tab-btn" onclick="filterRecipes('sabah', this)">☕ Sabah İksiri</button>
      <button class="recipe-tab-btn" onclick="filterRecipes('corba', this)">🍲 Şifalı Çorbalar</button>
      <button class="recipe-tab-btn" onclick="filterRecipes('yemek', this)">🍚 Gurme Yemekler</button>
    </div>

    <!-- Tarifler Kart Izgarası -->
    <div class="recipes-grid">
      <!-- Tarif 1: Bebek Püresi -->
      <div class="recipe-card" data-recipe-cat="bebek">
        <div class="recipe-meta-row">
          <span class="recipe-cat-badge">👶 BEBEK EK GIDA</span>
          <span class="recipe-time-badge">⏱ 12 Dakika • Kolay</span>
        </div>
        <h3 class="recipe-card-title">Balkabaklı &amp; İlikli Bebek Ek Gıda Püresi</h3>
        <div class="recipe-prod-pill">✦ No. 04 Saf Bebek Kolajeni ile</div>
        <div class="recipe-benefit-tag">✓ Sıfır Tuz • Kemik &amp; Diş Gelişimi • Kolay Sindirim</div>

        <div class="recipe-box-ingredients">
          <strong>Malzemeler (1 Porsiyon):</strong>
          <ul>
            <li>1 küçük dilim tatlı balkabağı (yaklaşık 100 gr)</li>
            <li>1/2 adet küçük boy havuç</li>
            <li>2-3 yemek kaşığı No. 04 Saf Bebek Kolajeni (ılık)</li>
            <li>1 tatlı kaşığı soğuk sıkım sızma zeytinyağı</li>
          </ul>
        </div>

        <div class="recipe-box-steps">
          <strong>Hazırlanışı:</strong>
          <ol>
            <li>Balkabağı ve havucu buharda veya az suda yumuşayana kadar haşlayın.</li>
            <li>Lif yapısını korumak için çatalla ezerek pürüzsüz kıvama getirin.</li>
            <li>Hafifçe ılıtılmış 2-3 kaşık No. 04 Saf Bebek Kolajeni ve zeytinyağını ilave edip karıştırın. Bebeğinizin ilk kaşık şifası hazır!</li>
          </ol>
        </div>

        <div class="recipe-card-footer">
          <button class="recipe-atc-btn" onclick="addToCart('No.04 Saf Bebek Kolajeni', 210)">
            <span>No. 04 Kolajen Ekle (210 TL)</span>
            <span>+</span>
          </button>
        </div>
      </div>

      <!-- Tarif 2: Sabah Şifa İksiri -->
      <div class="recipe-card" data-recipe-cat="sabah">
        <div class="recipe-meta-row">
          <span class="recipe-cat-badge">☕ GÜNLÜK İKSİR</span>
          <span class="recipe-time-badge">⏱ 3 Dakika • Zahmetsiz</span>
        </div>
        <h3 class="recipe-card-title">Altın Sabah İksiri (Limon &amp; Tane Karabiberli)</h3>
        <div class="recipe-prod-pill">✦ No. 02 Golden Immunity ile</div>
        <div class="recipe-benefit-tag">✓ %2000 Kurkumin Emilimi • Kafeinsiz Zindelik • Mukoza Onarımı</div>

        <div class="recipe-box-ingredients">
          <strong>Malzemeler (1 Fincan):</strong>
          <ul>
            <li>150 ml No. 02 Golden Immunity İlikli Kemik Suyu</li>
            <li>1/4 adet taze sıkılmış Akdeniz limonu</li>
            <li>1 tutam taze çekilmiş tane karabiber (piperin katalizörü)</li>
            <li>Arzuya göre 1 yaprak taze nane veya biberiye</li>
          </ul>
        </div>

        <div class="recipe-box-steps">
          <strong>Hazırlanışı:</strong>
          <ol>
            <li>Kemik suyunu cezvede kaynatmadan, sadece 60°C içim sıcaklığına kadar hafifçe ısıtın.</li>
            <li>Fincana aktarıp taze limon suyunu ve tane karabiberi ekleyin.</li>
            <li>Sabah aç karnına kahvaltıdan 20 dakika önce yavaş yudumlarla için. Güne zinde ve hafif başlayın.</li>
          </ol>
        </div>

        <div class="recipe-card-footer">
          <button class="recipe-atc-btn" onclick="addToCart('No.02 Golden Immunity Zencefil', 240)">
            <span>No. 02 Immunity Ekle (240 TL)</span>
            <span>+</span>
          </button>
        </div>
      </div>

      <!-- Tarif 3: Sarı Mercimek Çorbası -->
      <div class="recipe-card" data-recipe-cat="corba">
        <div class="recipe-meta-row">
          <span class="recipe-cat-badge">🍲 ŞİFALI ÇORBA</span>
          <span class="recipe-time-badge">⏱ 25 Dakika • Kolay</span>
        </div>
        <h3 class="recipe-card-title">Lokanta Usulü İlikli Sarı Mercimek Çorbası</h3>
        <div class="recipe-prod-pill">✦ No. 01 Pure Essence ile</div>
        <div class="recipe-benefit-tag">✓ 1 Kasede 14g Protein • Kadifemsi Kıvam • Bulyonsuz Saf Lezzet</div>

        <div class="recipe-box-ingredients">
          <strong>Malzemeler (4 Kişilik):</strong>
          <ul>
            <li>1 su bardağı yıkanmış kırmızı mercimek</li>
            <li>1 kavanoz (300 ml) No. 01 Pure Essence İlikli Kemik Suyu</li>
            <li>1 küçük patates, 1 havuç ve 1 soğan</li>
            <li>3 su bardağı sıcak su</li>
            <li>1 yemek kaşığı yayık tereyağı, kimyon ve tuz</li>
          </ul>
        </div>

        <div class="recipe-box-steps">
          <strong>Hazırlanışı:</strong>
          <ol>
            <li>Soğanı hafif tereyağında soteleyin; mercimek, patates ve havuçları ekleyin.</li>
            <li>1 kavanoz No. 01 Kemik Suyu ve 3 bardak sıcak suyu tencereye boşaltın.</li>
            <li>Sebzeler yumuşayana kadar 20 dk kısık ateşte kaynatıp blenderdan geçirin. Lokanta kıvamında şifa hazır!</li>
          </ol>
        </div>

        <div class="recipe-card-footer">
          <button class="recipe-atc-btn" onclick="addToCart('No.01 Pure Essence Kemik Suyu', 220)">
            <span>No. 01 Pure Essence Ekle (220 TL)</span>
            <span>+</span>
          </button>
        </div>
      </div>

      <!-- Tarif 4: Biberiyeli Siyez Pilavı -->
      <div class="recipe-card" data-recipe-cat="yemek">
        <div class="recipe-meta-row">
          <span class="recipe-cat-badge">🍚 GURME AKŞAM YEMEĞİ</span>
          <span class="recipe-time-badge">⏱ 30 Dakika • Kolay</span>
        </div>
        <h3 class="recipe-card-title">Biberiyeli &amp; İlikli Tereyağlı Siyez Pilavı</h3>
        <div class="recipe-prod-pill">✦ No. 05 Rosemary Elixir ile</div>
        <div class="recipe-benefit-tag">✓ Yavaş Salınımlı Lif • Akdeniz Aroması • Doğal Mineral Deposu</div>

        <div class="recipe-box-ingredients">
          <strong>Malzemeler (4 Kişilik):</strong>
          <ul>
            <li>1 su bardağı taş değirmen siyez bulguru (veya baldo pirinç)</li>
            <li>1 kavanoz (300 ml) No. 05 Rosemary Collagen Elixir</li>
            <li>1 su bardağı sıcak su</li>
            <li>1.5 yemek kaşığı yayık tereyağı ve 1 defne yaprağı</li>
          </ul>
        </div>

        <div class="recipe-box-steps">
          <strong>Hazırlanışı:</strong>
          <ol>
            <li>Tereyağını tencerede eritin; siyez bulgurunu kokusu çıkana kadar 2-3 dakika kavurun.</li>
            <li>No. 05 Rosemary kemik suyunu, suyu ve defne yaprağını ilave edin.</li>
            <li>Kısık ateşte suyunu çekene kadar demlendirip 15 dakika kapağı kapalı dinlendirin.</li>
          </ol>
        </div>

        <div class="recipe-card-footer">
          <button class="recipe-atc-btn" onclick="addToCart('No.05 Rosemary Collagen Elixir', 230)">
            <span>No. 05 Rosemary Ekle (230 TL)</span>
            <span>+</span>
          </button>
        </div>
      </div>

      <!-- Tarif 5: Gece Masalı Sakinleşme Kürü -->
      <div class="recipe-card" data-recipe-cat="sabah">
        <div class="recipe-meta-row">
          <span class="recipe-cat-badge">🌙 GECE RİTÜELİ</span>
          <span class="recipe-time-badge">⏱ 6 Dakika • Zahmetsiz</span>
        </div>
        <h3 class="recipe-card-title">Gece Masalı &amp; Kolajenli Mukoza Onarım Kürü</h3>
        <div class="recipe-prod-pill">✦ No. 03 Night Story + No. 01 ile</div>
        <div class="recipe-benefit-tag">✓ Glisin ile Derin REM Uykusu • Sinir Sistemi Dinlenmesi • Mide Sakinliği</div>

        <div class="recipe-box-ingredients">
          <strong>Malzemeler (1 Kişilik):</strong>
          <ul>
            <li>1 tatlı kaşığı No. 03 Night Story Botanik Çayı</li>
            <li>150 ml taze kaynamış su (90°C)</li>
            <li>1 yemek kaşığı No. 01 Pure Essence İlikli Kemik Suyu</li>
            <li>1 tatlı kaşığı saf çiçek balı (arzuya göre)</li>
          </ul>
        </div>

        <div class="recipe-box-steps">
          <strong>Hazırlanışı:</strong>
          <ol>
            <li>No. 03 botanik çayı kapalı fincanda 6-8 dakika demleyin ve süzün.</li>
            <li>İçerisine 1 yemek kaşığı saf kemik suyu (doğal glisin kaynağı) ve bal ilave edip karıştırın.</li>
            <li>Uykudan 40 dakika önce ılık olarak yudumlayın; gece boyu derin hücresel dinlenmeyi hissedin.</li>
          </ol>
        </div>

        <div class="recipe-card-footer">
          <button class="recipe-atc-btn" onclick="addToCart('No.03 Night Story Sakinleşme Çayı', 240)">
            <span>No. 03 Çay Ekle (240 TL)</span>
            <span>+</span>
          </button>
        </div>
      </div>
    </div>
  </section>
"""

# Insert Recipes HTML right before Reviews Section
html = html.replace("<!-- 10. Reviews Section -->", RECIPES_HTML + "\n  <!-- 10. Reviews Section -->")

# 3. ADD JAVASCRIPT FOR RECIPE FILTERING
RECIPES_JS = """
    function filterRecipes(category, btn) {
      const cards = document.querySelectorAll('.recipe-card');
      const tabs = document.querySelectorAll('.recipe-tab-btn');
      tabs.forEach(t => t.classList.remove('active'));
      btn.classList.add('active');

      cards.forEach(card => {
        if (category === 'all' || card.getAttribute('data-recipe-cat') === category) {
          card.style.display = 'flex';
          setTimeout(() => { card.style.opacity = '1'; }, 10);
        } else {
          card.style.display = 'none';
          card.style.opacity = '0';
        }
      });
    }
"""

html = html.replace("let cart = {};", "let cart = {};\n" + RECIPES_JS)

# 4. UPDATE HEADER NAV LINKS
html = html.replace('<a href="#magaza">Mağaza</a>', '<a href="#katalog">Koleksiyon</a>\n        <a href="#tarifler" style="color: var(--gold-champagne); font-weight: 700;">Yemek Tarifleri</a>')
html = html.replace('<a href="#faydalar">Klinik Faydaları</a>', '<a href="#neden-kokusuz">Neden Kokusuz?</a>\n        <a href="#jole-testi">Jöle Testi</a>')

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Recipes module added to index.html successfully!")
