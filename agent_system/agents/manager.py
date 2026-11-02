#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Story of Nature - Master Orchestrator (Manager Agent)
The central AI brain coordinating all 6 child subagents.
Generates the daily morning executive brief, dispatches tasks, and logs health.
"""

import json
import os
import subprocess
from datetime import datetime

from lead_finder import LeadFinderAgent
from mail_drafter import MailDrafterAgent
from inventory_tracker import InventoryTrackerAgent
from content_creator import ContentCreatorAgent
from marketing_monitor import MarketingMonitorAgent
from accounting_auditor import AccountingAuditorAgent

class ManagerAgent:
    def __init__(self, config_path=None):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if not config_path:
            config_path = os.path.join(self.base_dir, "config", "brand_config.json")
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)

        self.reports_dir = os.path.join(self.base_dir, "data", "reports")
        os.makedirs(self.reports_dir, exist_ok=True)

    def trigger_full_autonomous_cycle(self, trigger_notification=True):
        """
        Executes the complete multi-agent cycle across all business functions.
        """
        start_time = datetime.now()
        print("\n" + "="*70)
        print("🌿 STORY OF NATURE — OTONOM YAPAY ZEKA EKİBİ ÇALIŞMA DÖNGÜSÜ")
        print(f"⏰ Başlangıç Zamanı: {start_time.strftime('%d.%m.%Y %H:%M:%S')}")
        print("="*70)

        # 1. Lead Finder Agent
        print("\n[1/6] 🔍 LeadFinderAgent çalışıyor: B2B potansiyel müşteriler taranıyor...")
        lead_agent = LeadFinderAgent()
        leads = lead_agent.scan_targeted_leads()
        print(f"      -> {len(leads)} adet yüksek puanlı işletme tespit edildi.")

        # 2. Mail Drafter Agent
        print("\n[2/6] ✉️  MailDrafterAgent çalışıyor: 5 paragraflık özel teklif taslakları yazılıyor...")
        mail_agent = MailDrafterAgent()
        drafts = mail_agent.generate_all_drafts(leads)
        print(f"      -> {len(drafts)} adet kişiselleştirilmiş teklif mektubu 'data/drafts/' dizinine kaydedildi.")

        # 3. Inventory Tracker Agent
        print("\n[3/6] 📦 InventoryTrackerAgent çalışıyor: Stoklar ve tedarik kuralı denetleniyor...")
        inv_agent = InventoryTrackerAgent()
        inv_result = inv_agent.generate_supplier_reorder_po()
        pos = inv_result["generated_pos"]
        print(f"      -> {len(pos)} adet acil tedarik sipariş emri (PO) hazırlandı.")

        # 4. Content Creator Agent
        print("\n[4/6] 📸 ContentCreatorAgent çalışıyor: Sosyal medya ve görsel planı oluşturuluyor...")
        content_agent = ContentCreatorAgent()
        posts = content_agent.generate_weekly_content_schedule()
        print(f"      -> {len(posts)} adet yüksek etkileşimli içerik, kanca (hook) ve görsel promptu hazırlandı.")

        # 5. Marketing Monitor Agent
        print("\n[5/6] 🎯 MarketingMonitorAgent çalışıyor: Meta reklam ve yorum protokolleri taranıyor...")
        mkt_agent = MarketingMonitorAgent()
        cams = mkt_agent.generate_meta_ad_campaigns()
        rev_proto = mkt_agent.generate_review_followup_protocol()
        print(f"      -> {len(cams)} adet Meta kampanya kurgusu ve 4 günlük müşteri memnuniyet takip protokolü güncellendi.")

        # 6. Accounting Auditor Agent
        print("\n[6/6] 📊 AccountingAuditorAgent çalışıyor: Haftalık mali denetim ve P&L tablosu hesaplanıyor...")
        acc_agent = AccountingAuditorAgent()
        pnl = acc_agent.audit_weekly_pnl()
        net_profit = pnl["financial_breakdown"]["net_kar_try"]
        margin = pnl["financial_breakdown"]["net_kar_marji_yuzde"]
        print(f"      -> Finansal özet: Haftalık tahmini Net Kâr: {net_profit} TL (Net Marj: %{margin}).")

        # Compile Master Morning Brief
        brief_md = self.generate_executive_brief_markdown(leads, drafts, inv_result, posts, pnl)
        brief_path = os.path.join(self.reports_dir, f"morning_brief_{start_time.strftime('%Y%m%d')}.md")
        with open(brief_path, "w", encoding="utf-8") as f:
            f.write(brief_md)

        # Trigger native macOS notification if requested
        if trigger_notification:
            try:
                msg = f"Story of Nature: {len(drafts)} teklif taslağı hazır, {len(pos)} tedarik emri oluşturuldu. Net Kâr: {net_profit} TL."
                cmd = f"""osascript -e 'display notification "{msg}" with title "🌿 Story of Nature AI Ekibi" sound name "Glass"'"""
                subprocess.run(cmd, shell=True, check=False)
            except Exception:
                pass

        print("\n" + "="*70)
        print(f"✅ TÜM EKİP DÖNGÜSÜ TAMAMLANDI! (Rapor: {brief_path})")
        print("="*70 + "\n")
        return {
            "status": "SUCCESS",
            "report_path": brief_path,
            "leads_count": len(leads),
            "drafts_count": len(drafts),
            "pos_count": len(pos),
            "net_profit": net_profit,
            "margin": margin
        }

    def generate_executive_brief_markdown(self, leads, drafts, inv_result, posts, pnl):
        now_str = datetime.now().strftime("%d.%m.%Y - %H:%M")
        pos = inv_result["generated_pos"]
        low_items = inv_result["audit"]["low_products"]

        md = f"""# 🌿 Story of Nature — Sabah Yönetici Özeti (AI Morning Executive Brief)
**Tarih:** {now_str}  
**Yönetici Ajan:** Manager AI Orchestrator  
**Web Sitesi:** https://storyofnature.com.tr  

---

### 1. 🔍 B2B Pazar & Müşteri Fırsatları ({len(leads)} Yeni Hedef)
Aşağıdaki prestijli işletmeler markamıza %95+ uyumla eşleşti ve incelemenize hazır:
"""
        for lead in leads:
            md += f"- **{lead['name']} ({lead['district']} / {lead['city']})** — Uyum Puanı: %{lead['alignment_score']}\n"
            md += f"  - *Hedef Ürün:* {lead['target_product']}\n"
            md += f"  - *Neden Seçildi:* {lead['fit_reason']}\n"

        md += f"""
---

### 2. ✉️ Hazırlanan Teklif Taslakları ({len(drafts)} E-posta)
Tüm e-postalar 5 paragraflık Forbes lüks standartlarında hazırlanmış ve `data/drafts/` klasörüne konulmuştur. Siz sadece okuyup 'Gönder' diyeceksiniz:
"""
        for d in drafts[:3]:
            md += f"- **Kime:** {d['to_name']} ({d['to_email']})\n"
            md += f"  - *Konu:* {d['subject']}\n"

        md += f"""
---

### 3. 📦 Stok Takibi & Tedarik Sipariş Emirleri ({len(pos)} PO Hazır)
"""
        if pos:
            for po in pos:
                md += f"- **{po['supplier']}** ({po['item_name']}):\n"
                md += f"  - *Sipariş Miktarı:* {po.get('units_ordered', po.get('boxes_ordered'))}\n"
                md += f"  - *Toplam Tutar:* {po['total_cost_try']} TL (Teslim Süresi: {po['lead_time']})\n"
                md += f"  - *Kural Gerekçesi:* {po['notes']}\n"
        else:
            md += "Tüm stok seviyeleri ve ambalaj malzemeleri emniyet eşiğinin üzerindedir.\n"

        md += f"""
---

### 4. 📸 Haftalık Sosyal Medya & Görsel Takvimi
Bugün yayınlanmaya hazır öne çıkan içerik:
- **Günün Başlığı:** {posts[0]['topic']} ({posts[0]['format']})
- **Örnek Kanca (Hook):** *"{posts[0]['hook_alternatives'][0]}"*
- **Görsel Promptu:** `{posts[0]['visual_prompt']}`

---

### 5. 📊 Finansal Durum & Kârlılık Özeti
- **Brüt Gelir:** {pnl['financial_breakdown']['brut_gelir_try']} TL
- **Hammadde (COGS) & Ambalaj Gideri:** {pnl['financial_breakdown']['hammadde_maliyeti_cogs_try'] + pnl['financial_breakdown']['ambalaj_ve_kutu_maliyeti_try']} TL
- **Kargo & İyzico Komisyon Gideri:** {pnl['financial_breakdown']['kargo_ve_lojistik_gideri_try'] + pnl['financial_breakdown']['sanal_pos_komisyonu_iyzico_try']} TL
- **Net Kâr:** **{pnl['financial_breakdown']['net_kar_try']} TL**
- **Net Kâr Marjı:** **%{pnl['financial_breakdown']['net_kar_marji_yuzde']}**
"""
        return md

if __name__ == "__main__":
    manager = ManagerAgent()
    manager.trigger_full_autonomous_cycle(trigger_notification=True)
