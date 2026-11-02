#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Story of Nature - Accounting & Cashflow Auditor Agent
Monitors unit sales, cost of goods sold (COGS), shipping fees,
payment gateway commissions (İyzico), and generates weekly P&L summaries.
"""

import json
import os
from datetime import datetime

class AccountingAuditorAgent:
    def __init__(self, config_path=None):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if not config_path:
            config_path = os.path.join(base_dir, "config", "brand_config.json")
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)
        self.output_dir = os.path.join(base_dir, "data", "financials")
        os.makedirs(self.output_dir, exist_ok=True)

    def audit_weekly_pnl(self, simulated_orders=None):
        """
        Audits revenues, COGS, packaging, shipping, payment commission, and net margin.
        """
        if not simulated_orders:
            # Baseline weekly operating volume (Retail + Small B2B sample)
            simulated_orders = [
                {"sku": "SON-BB-01", "name": "Pure Essence", "units": 45, "price": 220.0, "cogs": 45.0},
                {"sku": "SON-BB-02", "name": "Golden Immunity", "units": 30, "price": 240.0, "cogs": 48.0},
                {"sku": "SON-TEA-03", "name": "Night Story Tea", "units": 20, "price": 195.0, "cogs": 38.0},
                {"sku": "SON-BB-04", "name": "Pure Baby", "units": 25, "price": 230.0, "cogs": 46.0},
                {"sku": "SON-BB-05", "name": "Rosemary Elixir", "units": 15, "price": 235.0, "cogs": 47.0}
            ]

        total_gross_revenue = 0.0
        total_cogs = 0.0
        total_units = 0

        for item in simulated_orders:
            revenue = item["units"] * item["price"]
            cogs = item["units"] * item["cogs"]
            total_gross_revenue += revenue
            total_cogs += cogs
            total_units += item["units"]

        # Packaging & Logistics costs
        packaging_per_unit = 15.70  # Glass jar, metal lid, gold foil label, cushioning
        total_packaging_cost = total_units * packaging_per_unit
        
        # Payment Gateway fee (İyzico ~2.8% + 0.25 TL / transaction)
        est_transactions = max(1, total_units // 3)  # Avg basket is 3 jars
        payment_gateway_fees = (total_gross_revenue * 0.028) + (est_transactions * 0.25)

        # Shipping cost estimate (Yurtiçi Kargo soğuk izolasyonlu ~65 TL per parcel)
        shipping_costs = est_transactions * 65.0

        # Net Profit Calculation
        total_operating_costs = total_cogs + total_packaging_cost + payment_gateway_fees + shipping_costs
        net_profit = total_gross_revenue - total_operating_costs
        net_margin_percent = (net_profit / total_gross_revenue) * 100 if total_gross_revenue > 0 else 0.0

        pnl_report = {
            "period": f"Haftalık Mali Denetim ({datetime.now().strftime('%d.%m.%Y')})",
            "audited_at": datetime.now().isoformat(),
            "currency": "TRY",
            "sales_summary": {
                "total_units_sold": total_units,
                "total_orders_count": est_transactions,
                "average_order_value_try": round(total_gross_revenue / est_transactions, 2)
            },
            "financial_breakdown": {
                "brut_gelir_try": round(total_gross_revenue, 2),
                "hammadde_maliyeti_cogs_try": round(total_cogs, 2),
                "ambalaj_ve_kutu_maliyeti_try": round(total_packaging_cost, 2),
                "kargo_ve_lojistik_gideri_try": round(shipping_costs, 2),
                "sanal_pos_komisyonu_iyzico_try": round(payment_gateway_fees, 2),
                "toplam_isletme_gideri_try": round(total_operating_costs, 2),
                "net_kar_try": round(net_profit, 2),
                "net_kar_marji_yuzde": round(net_margin_percent, 2)
            },
            "profitability_status": "EXCELLENT_HEALTHY" if net_margin_percent > 45 else "ACCEPTABLE"
        }

        output_path = os.path.join(self.output_dir, f"pnl_audit_{datetime.now().strftime('%Y%m%d')}.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(pnl_report, f, ensure_ascii=False, indent=2)

        return pnl_report

if __name__ == "__main__":
    auditor = AccountingAuditorAgent()
    pnl = auditor.audit_weekly_pnl()
    print(f"✅ AccountingAuditorAgent: Net Kâr: {pnl['financial_breakdown']['net_kar_try']} TL (%{pnl['financial_breakdown']['net_kar_marji_yuzde']} Net Marj).")
