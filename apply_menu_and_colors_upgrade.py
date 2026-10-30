#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Story of Nature - Mini Menu Window Popover & Diversified Color Palette Engine
Implements:
1. Sleek slide-out / floating mini menu popover window in the header.
2. Direct links on every product card leading to dedicated PDPs.
3. Diversified luxury botanical color palette (Terracotta, Honey Amber, Sage, Twilight Lavender).
"""

import re

FILE_PATH = "/Users/emre/.gemini/antigravity/scratch/story-of-nature/site/index.html"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. ADD CSS FOR MINI MENU WINDOW & DIVERSIFIED PALETTE
PALETTE_AND_MENU_CSS = """
    /* ========================================================
       DIVERSIFIED BOTANICAL PALETTE & MINI MENU WINDOW
       ======================================================== */
    :root {
      --color-terracotta: #C86D51;
      --color-terracotta-bg: #FCF2EE;
      --color-amber: #D49B36;
      --color-amber-bg: #FCF4E6;
      --color-sage: #3D6E49;
      --color-sage-bg: #EBF3EC;
      --color-lavender: #5C527F;
      --color-lavender-bg: #F2EFF9;
      --color-gold-deep: #A8833E;
    }

    /* Menu Window Trigger Button */
    .btn-menu-window-trigger {
      background: var(--bg-card);
      color: var(--color-dark);
      border: 1px solid var(--border-subtle);
      padding: 9px 16px;
      border-radius: var(--radius-full);
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      transition: all 0.2s ease;
    }
    .btn-menu-window-trigger:hover {
      background: #fff;
      border-color: var(--color-dark);
      transform: translateY(-1px);
    }

    /* Menu Window Popover */
    .menu-window-backdrop {
      position: fixed;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(18, 30, 22, 0.45);
      backdrop-filter: blur(4px);
      z-index: 240;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.25s ease;
    }
    .menu-window-backdrop.active {
      opacity: 1;
      pointer-events: auto;
    }

    .menu-window-popover {
      position: fixed;
      top: 75px;
      right: 24px;
      width: 440px;
      max-width: calc(100vw - 32px);
      max-height: calc(100vh - 100px);
      overflow-y: auto;
      background: rgba(255, 255, 255, 0.98);
      backdrop-filter: blur(20px);
      border-radius: 24px;
      border: 1px solid var(--border-subtle);
      box-shadow: 0 25px 60px rgba(0,0,0,0.22);
      z-index: 250;
      opacity: 0;
      transform: translateY(-12px) scale(0.97);
      pointer-events: none;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .menu-window-popover.active {
      opacity: 1;
      transform: translateY(0) scale(1);
      pointer-events: auto;
    }
    @media (max-width: 600px) {
      .menu-window-popover {
        top: 65px;
        right: 16px;
        left: 16px;
        width: auto;
      }
    }

    .menu-window-header {
      padding: 18px 22px;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: var(--bg-card);
      border-radius: 24px 24px 0 0;
    }
    .btn-close-menu-window {
      background: none;
      border: none;
      font-size: 20px;
      color: var(--text-muted);
      cursor: pointer;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background 0.15s;
    }
    .btn-close-menu-window:hover { background: rgba(0,0,0,0.06); color: var(--color-dark); }

    .menu-window-body {
      padding: 20px 22px;
      display: flex;
      flex-direction: column;
      gap: 22px;
    }
    .menu-window-section-title {
      font-size: 10.5px;
      font-weight: 800;
      letter-spacing: 1.5px;
      color: var(--gold-champagne);
      text-transform: uppercase;
      margin-bottom: 12px;
    }
    .menu-pdp-links-grid {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .menu-pdp-link-card {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 10px 14px;
      border-radius: 14px;
      border: 1px solid transparent;
      text-decoration: none;
      transition: all 0.2s ease;
      background: #fff;
    }
    .menu-pdp-link-card:hover {
      background: var(--bg-card);
      border-color: var(--border-subtle);
      transform: translateX(3px);
    }
    .menu-pdp-link-card.highlight {
      background: var(--color-amber-bg);
      border-color: rgba(212, 155, 54, 0.3);
    }
    .pdp-link-bullet {
      width: 30px;
      height: 30px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 11px;
      flex-shrink: 0;
    }
    .pdp-link-name {
      font-size: 13px;
      font-weight: 700;
      color: var(--color-dark);
      line-height: 1.25;
    }
    .pdp-link-sub {
      font-size: 11px;
      color: var(--text-muted);
      margin-top: 2px;
    }
    .pdp-link-arrow {
      margin-left: auto;
      color: var(--text-muted);
      font-weight: bold;
      font-size: 14px;
      transition: transform 0.2s;
    }
    .menu-pdp-link-card:hover .pdp-link-arrow {
      transform: translateX(3px);
      color: var(--color-dark);
    }

    .menu-quick-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }
    .menu-quick-tag {
      background: var(--bg-card);
      color: var(--color-dark);
      padding: 8px 14px;
      border-radius: 12px;
      font-size: 12px;
      font-weight: 700;
      text-decoration: none;
      border: 1px solid var(--border-subtle);
      transition: all 0.15s;
    }
    .menu-quick-tag:hover {
      background: var(--color-dark);
      color: #fff;
    }
    .menu-quick-tag.whatsapp {
      background: #25D366;
      color: #fff;
      border-color: #25D366;
    }

    /* Card Direct PDP Link */
    .card-actions-row {
      display: flex;
      gap: 8px;
      margin: 12px 0 16px;
    }
    .btn-card-pdp {
      flex: 1;
      text-align: center;
      text-decoration: none;
      background: var(--bg-card);
      color: var(--color-dark);
      font-size: 12px;
      font-weight: 700;
      padding: 9px 12px;
      border-radius: 10px;
      border: 1px solid var(--border-subtle);
      transition: all 0.2s;
    }
    .btn-card-pdp:hover {
      background: var(--color-dark);
      color: #fff;
      border-color: var(--color-dark);
    }
"""

# Append CSS
html = html.replace("</head>", f"<style>{PALETTE_AND_MENU_CSS}</style>\n</head>")

# 2. UPDATE HEADER WITH MINI MENU WINDOW BUTTON
HEADER_OLD = '<div class="header-right">'
HEADER_NEW = """<div class="header-right">
        <!-- Açılır Kapanır Mini Menü Butonu -->
        <button class="btn-menu-window-trigger" onclick="toggleMenuWindow()" aria-label="Açılır Menü Penceresi">
          <span style="font-size: 14px;">☰</span>
          <span>Menü</span>
          <span style="font-size: 10px; color: var(--gold-champagne);">▾</span>
        </button>"""

html = html.replace(HEADER_OLD, HEADER_NEW, 1)

# 3. ADD MINI MENU WINDOW POPOVER HTML RIGHT AFTER </header>
POPOVER_HTML = """
  <!-- AÇILIR KAPANIR UFAK MENÜ PENCERESİ (MINI WINDOW POPOVER) -->
  <div class="menu-window-backdrop" id="menuWindowBackdrop" onclick="closeMenuWindow()"></div>
  <div class="menu-window-popover" id="menuWindowPopover">
    <div class="menu-window-header">
      <div style="display: flex; align-items: center; gap: 8px;">
        <span style="font-size: 20px;">🌿</span>
        <div>
          <div style="font-size: 10px; font-weight: 800; letter-spacing: 1.5px; color: var(--gold-champagne); text-transform: uppercase;">STORY OF NATURE</div>
          <div style="font-family: var(--font-serif); font-size: 18px; font-weight: 700; color: var(--color-dark);">Zanaatkar Menü &amp; Sayfalar</div>
        </div>
      </div>
      <button class="btn-close-menu-window" onclick="closeMenuWindow()" aria-label="Menüyü Kapat">✕</button>
    </div>

    <div class="menu-window-body">
      <!-- Bölüm 1: Ürünlerin Kendi Sayfaları -->
      <div class="menu-window-section">
        <div class="menu-window-section-title">✦ ÜRÜNLERİN ÖZEL SAYFALARI</div>
        <div class="menu-pdp-links-grid">
          <a href="pure-essence.html" class="menu-pdp-link-card">
            <span class="pdp-link-bullet" style="background: #EBF3EC; color: #237443;">01</span>
            <div>
              <div class="pdp-link-name">No. 01 Pure Essence İlikli Kemik Suyu</div>
              <div class="pdp-link-sub">28 Saat Demleme • 300 ml Cam • 220 TL</div>
            </div>
            <span class="pdp-link-arrow">→</span>
          </a>

          <a href="golden-immunity.html" class="menu-pdp-link-card">
            <span class="pdp-link-bullet" style="background: #FCF4E6; color: #9C6B18;">02</span>
            <div>
              <div class="pdp-link-name">No. 02 Golden Immunity Zerdeçal &amp; Zencefil</div>
              <div class="pdp-link-sub">Bağışıklık Kürü • 300 ml Cam • 240 TL</div>
            </div>
            <span class="pdp-link-arrow">→</span>
          </a>

          <a href="saf-bebek-kolajeni.html" class="menu-pdp-link-card">
            <span class="pdp-link-bullet" style="background: #EBF3EC; color: #237443;">04</span>
            <div>
              <div class="pdp-link-name">No. 04 Saf Bebek Kolajeni</div>
              <div class="pdp-link-sub">6. Aydan İtibaren • Sıfır Tuz • 210 TL</div>
            </div>
            <span class="pdp-link-arrow">→</span>
          </a>

          <a href="rosemary-elixir.html" class="menu-pdp-link-card">
            <span class="pdp-link-bullet" style="background: #FCF2EE; color: #C86D51;">05</span>
            <div>
              <div class="pdp-link-name">No. 05 Rosemary Collagen Elixir</div>
              <div class="pdp-link-sub">Yabani Biberiye &amp; Kekik • 230 TL</div>
            </div>
            <span class="pdp-link-arrow">→</span>
          </a>

          <a href="gece-masali.html" class="menu-pdp-link-card">
            <span class="pdp-link-bullet" style="background: #F2EFF9; color: #5C527F;">03</span>
            <div>
              <div class="pdp-link-name">No. 03 Night Story Botanik Çayı</div>
              <div class="pdp-link-sub">Lavanta &amp; Papatya • 75 gr • 240 TL</div>
            </div>
            <span class="pdp-link-arrow">→</span>
          </a>

          <a href="14-gunluk-paket.html" class="menu-pdp-link-card highlight">
            <span class="pdp-link-bullet" style="background: #FCF4E6; color: #9C6B18;">★</span>
            <div>
              <div class="pdp-link-name">14 Günlük Lüks Hücresel Yenilenme Paketi</div>
              <div class="pdp-link-sub">4 Kavanoz + Çay + Kaşık + Rehber • 980 TL</div>
            </div>
            <span class="pdp-link-arrow">→</span>
          </a>
        </div>
      </div>

      <!-- Bölüm 2: Hızlı Keşif & Rehberler -->
      <div class="menu-window-section">
        <div class="menu-window-section-title">✦ MUTFAK &amp; REHBERLER</div>
        <div class="menu-quick-tags">
          <a href="#tarifler" class="menu-quick-tag" onclick="closeMenuWindow()">🍲 Mutfak Yemek Tarifleri</a>
          <a href="#jole-testi" class="menu-quick-tag" onclick="closeMenuWindow()">🧊 Buzdolabı Jöle Testi</a>
          <a href="#faydalar" class="menu-quick-tag" onclick="closeMenuWindow()">🔬 Acıbadem Tıp Raporu</a>
          <a href="#neden-kokusuz" class="menu-quick-tag" onclick="closeMenuWindow()">🚚 Kargo &amp; Kırılma Sigortası</a>
          <a href="https://wa.me/905330849027?text=Merhaba,%20Story%20of%20Nature%20hakk%C4%B1nda%20bilgi%20almak%20istiyorum." target="_blank" class="menu-quick-tag whatsapp">💬 WhatsApp Danışma</a>
        </div>
      </div>
    </div>
  </div>
"""

html = html.replace("</header>", "</header>\n" + POPOVER_HTML)

# 4. ADD JAVASCRIPT FOR MINI MENU WINDOW
WINDOW_JS = """
    function toggleMenuWindow() {
      const popover = document.getElementById('menuWindowPopover');
      const backdrop = document.getElementById('menuWindowBackdrop');
      if (popover && backdrop) {
        const isActive = popover.classList.contains('active');
        if (isActive) {
          closeMenuWindow();
        } else {
          popover.classList.add('active');
          backdrop.classList.add('active');
          document.body.style.overflow = 'hidden';
        }
      }
    }

    function closeMenuWindow() {
      const popover = document.getElementById('menuWindowPopover');
      const backdrop = document.getElementById('menuWindowBackdrop');
      if (popover && backdrop) {
        popover.classList.remove('active');
        backdrop.classList.remove('active');
        document.body.style.overflow = '';
      }
    }

    // Close on ESC
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        closeMenuWindow();
        closeProductModal();
      }
    });
"""

html = html.replace("let cart = {};", "let cart = {};\n" + WINDOW_JS)

# 5. UPDATE PRODUCT CARDS WITH DIRECT PDP BUTTONS
html = html.replace(
    """          <button class="btn-quick-look" onclick="openProductModal('no01')">
            6 Slayt İnfografik Galeri & Besin Analizi ↗
          </button>""",
    """          <div class="card-actions-row">
            <button class="btn-quick-look" style="margin:0; flex:1;" onclick="openProductModal('no01')">Hızlı İncele ↗</button>
            <a href="pure-essence.html" class="btn-card-pdp">Ürün Sayfası →</a>
          </div>"""
)

html = html.replace(
    """          <button class="btn-quick-look" onclick="openProductModal('no02')">
            5 Slayt İnfografik Galeri & Besin Analizi ↗
          </button>""",
    """          <div class="card-actions-row">
            <button class="btn-quick-look" style="margin:0; flex:1;" onclick="openProductModal('no02')">Hızlı İncele ↗</button>
            <a href="golden-immunity.html" class="btn-card-pdp">Ürün Sayfası →</a>
          </div>"""
)

html = html.replace(
    """          <button class="btn-quick-look" onclick="openProductModal('no03')">
            İnfografik Galeri & Bitki Analizi ↗
          </button>""",
    """          <div class="card-actions-row">
            <button class="btn-quick-look" style="margin:0; flex:1;" onclick="openProductModal('no03')">Hızlı İncele ↗</button>
            <a href="gece-masali.html" class="btn-card-pdp">Ürün Sayfası →</a>
          </div>"""
)

html = html.replace(
    """          <button class="btn-quick-look" onclick="openProductModal('no04')">
            Pediatrik Güvenlik Galerisi ↗
          </button>""",
    """          <div class="card-actions-row">
            <button class="btn-quick-look" style="margin:0; flex:1;" onclick="openProductModal('no04')">Hızlı İncele ↗</button>
            <a href="saf-bebek-kolajeni.html" class="btn-card-pdp">Ürün Sayfası →</a>
          </div>"""
)

html = html.replace(
    """          <button class="btn-quick-look" onclick="openProductModal('no05')">
            İnfografik Galeri & Analiz ↗
          </button>""",
    """          <div class="card-actions-row">
            <button class="btn-quick-look" style="margin:0; flex:1;" onclick="openProductModal('no05')">Hızlı İncele ↗</button>
            <a href="rosemary-elixir.html" class="btn-card-pdp">Ürün Sayfası →</a>
          </div>"""
)

html = html.replace(
    """          <button class="btn-quick-look" onclick="openProductModal('bundle')">
            Kutu Detayları & İnfografik Galeri ↗
          </button>""",
    """          <div class="card-actions-row">
            <button class="btn-quick-look" style="margin:0; flex:1;" onclick="openProductModal('bundle')">Hızlı İncele ↗</button>
            <a href="14-gunluk-paket.html" class="btn-card-pdp">Ürün Sayfası →</a>
          </div>"""
)

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("index.html upgraded with Mini Menu Window, Direct PDP Links, and Diversified Palette!")
