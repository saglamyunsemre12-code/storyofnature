#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Story of Nature — Autonomous Agent Executive Console
Run, inspect, and supervise your 7-agent AI team from your Mac terminal or the cloud.

Usage:
  python3 run_agents.py --all           # Runs full 6-agent cycle and generates Morning Brief
  python3 run_agents.py --leads         # Scans fresh B2B leads
  python3 run_agents.py --drafts        # Inspects ready-to-send email drafts
  python3 run_agents.py --stock         # Audits stock & prints supplier POs
  python3 run_agents.py --content       # Prints weekly Instagram/Reels content plan
  python3 run_agents.py --pnl           # Displays financial cashflow audit
  python3 run_agents.py --brief         # Displays the latest morning brief
"""

import sys
import os
import argparse

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "agents"))

from manager import ManagerAgent
from lead_finder import LeadFinderAgent
from mail_drafter import MailDrafterAgent
from inventory_tracker import InventoryTrackerAgent
from content_creator import ContentCreatorAgent
from marketing_monitor import MarketingMonitorAgent
from accounting_auditor import AccountingAuditorAgent

def main():
    parser = argparse.ArgumentParser(description="Story of Nature AI Agent Team Console")
    parser.add_argument("--all", action="store_true", help="Run full 6-agent cycle")
    parser.add_argument("--leads", action="store_true", help="Scan B2B prospects")
    parser.add_argument("--drafts", action="store_true", help="Inspect email drafts queue")
    parser.add_argument("--stock", action="store_true", help="Audit inventory & POs")
    parser.add_argument("--content", action="store_true", help="View weekly content schedule")
    parser.add_argument("--pnl", action="store_true", help="Display financial P&L audit")
    parser.add_argument("--brief", action="store_true", help="Print latest executive morning brief")

    args = parser.parse_args()

    # If no flags passed, default to --all
    if not any([args.all, args.leads, args.drafts, args.stock, args.content, args.pnl, args.brief]):
        args.all = True

    manager = ManagerAgent()

    if args.all:
        manager.trigger_full_autonomous_cycle(trigger_notification=True)
    elif args.leads:
        lf = LeadFinderAgent()
        results = lf.scan_targeted_leads()
        print(f"\n🔍 {len(results)} B2B Hedef Tespit Edildi:")
        for r in results:
            print(f"  • {r['name']} ({r['district']}) - Uyum Puanı: %{r['alignment_score']} | Hedef: {r['target_product']}")
    elif args.stock:
        inv = InventoryTrackerAgent()
        res = inv.generate_supplier_reorder_po()
        print(f"\n📦 Stok Denetimi ve Tedarik Emirleri:")
        for po in res["generated_pos"]:
            print(f"  • {po['supplier']} -> {po['units_ordered']} {po['item_name']} (Tutar: {po['total_cost_try']} TL)")
    elif args.content:
        cc = ContentCreatorAgent()
        posts = cc.generate_weekly_content_schedule()
        print(f"\n📸 Haftalık Sosyal Medya İçerik Planı ({len(posts)} Gönderi):")
        for p in posts:
            print(f"  • {p['day']} [{p['format']}]: {p['topic']}")
            print(f"    Hook: {p['hook_alternatives'][0]}\n")
    elif args.pnl:
        acc = AccountingAuditorAgent()
        pnl = acc.audit_weekly_pnl()
        fb = pnl["financial_breakdown"]
        print(f"\n📊 Finansal P&L Denetimi:")
        print(f"  • Brüt Gelir: {fb['brut_gelir_try']} TL")
        print(f"  • Toplam Gider: {fb['toplam_isletme_gideri_try']} TL")
        print(f"  • Net Kâr: {fb['net_kar_try']} TL (Marj: %{fb['net_kar_marji_yuzde']})\n")
    elif args.brief:
        brief_files = sorted(os.listdir(manager.reports_dir))
        if brief_files:
            latest = os.path.join(manager.reports_dir, brief_files[-1])
            with open(latest, "r", encoding="utf-8") as f:
                print(f.read())
        else:
            print("Henüz bir sabah özeti bulunamadı. Lütfen '--all' ile çalıştırın.")

if __name__ == "__main__":
    main()
