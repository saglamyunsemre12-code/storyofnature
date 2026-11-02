#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Story of Nature - Inventory Tracker & Supply Chain Agent
Monitors finished products, packaging, and raw ingredient stock.
Executes supplier price comparisons, minimum order checks, and automated PO drafting.
"""

import json
import os
import math
from datetime import datetime

class InventoryTrackerAgent:
    def __init__(self, data_path=None, config_path=None):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if not data_path:
            data_path = os.path.join(base_dir, "data", "inventory_state.json")
        if not config_path:
            config_path = os.path.join(base_dir, "config", "brand_config.json")

        self.data_path = data_path
        with open(data_path, "r", encoding="utf-8") as f:
            self.inventory = json.load(f)
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)

        self.orders_dir = os.path.join(base_dir, "data", "orders")
        os.makedirs(self.orders_dir, exist_ok=True)

    def audit_stock_levels(self):
        """
        Inspects all items and categorizes into HEALTHY, LOW, CRITICAL.
        """
        low_products = []
        low_packaging = []
        low_ingredients = []

        for p in self.inventory.get("products", []):
            if p["current_stock"] <= p["safety_stock"]:
                urgency = "CRITICAL" if p["current_stock"] <= 12 else "WARNING"
                low_products.append({**p, "urgency": urgency})

        for pkg in self.inventory.get("packaging_materials", []):
            if pkg["current_stock"] <= pkg["safety_stock"]:
                urgency = "CRITICAL" if pkg["current_stock"] <= 50 else "WARNING"
                low_packaging.append({**pkg, "urgency": urgency})

        for raw in self.inventory.get("raw_ingredients", []):
            stock = raw.get("current_stock_kg", raw.get("current_stock_liter", 0))
            safety = raw.get("safety_stock_kg", raw.get("safety_stock_liter", 0))
            if stock <= safety:
                low_ingredients.append({**raw, "urgency": "WARNING"})

        return {
            "timestamp": datetime.now().isoformat(),
            "low_products": low_products,
            "low_packaging": low_packaging,
            "low_ingredients": low_ingredients,
            "has_reorder_needed": len(low_products) > 0 or len(low_packaging) > 0 or len(low_ingredients) > 0
        }

    def generate_supplier_reorder_po(self):
        """
        Builds automated purchase orders with supplier minimum order rule logic.
        """
        audit = self.audit_stock_levels()
        pos = []

        # 1. Glass Packaging Reorder PO (Şişecam vs Ege Cam)
        jar_item = next((x for x in self.inventory.get("packaging_materials", []) if x["sku"] == "PKG-JAR-300"), None)
        if jar_item and jar_item["current_stock"] <= jar_item["safety_stock"]:
            # Need to reorder jars. Check supplier options
            supplier_conf = self.config["inventory_settings"]["suppliers"]["glass_packaging"]
            primary = supplier_conf["primary"]
            
            # Calculate required boxes (box of 24)
            deficit = 250 - jar_item["current_stock"]
            boxes_needed = max(primary["min_order_box"], math.ceil(deficit / primary["box_capacity"]))
            total_jars = boxes_needed * primary["box_capacity"]
            total_price = total_jars * primary["price_per_jar"]

            po_glass = {
                "po_id": f"PO-GLASS-{datetime.now().strftime('%Y%m%d-%H%M')}",
                "supplier": primary["name"],
                "supplier_contact": primary["contact"],
                "item_name": "300ml Standart Silindirik Cam Kavanoz (Vakumlu)",
                "boxes_ordered": boxes_needed,
                "units_ordered": total_jars,
                "unit_price_try": primary["price_per_jar"],
                "total_cost_try": total_price,
                "lead_time": f"{primary['lead_time_days']} iş günü",
                "status": "DRAFT_READY_FOR_APPROVAL",
                "notes": f"Stok kritik seviyeye indi ({jar_item['current_stock']} adet kaldı). Minimum sipariş kuralı ({primary['min_order_box']} koli) uygulandı."
            }
            pos.append(po_glass)

        # 2. Mera Besisi Kemik Tedarik PO (Trakya Organik Çiftliği)
        bone_item = next((x for x in self.inventory.get("raw_ingredients", []) if x["sku"] == "RAW-BONE-MERA"), None)
        if bone_item and bone_item["current_stock_kg"] <= bone_item["safety_stock_kg"]:
            bone_supp = self.config["inventory_settings"]["suppliers"]["organic_bones"]["primary"]
            kg_to_order = max(bone_supp["min_order_kg"], 50)
            total_bone_cost = kg_to_order * bone_supp["price_per_kg"]

            po_bone = {
                "po_id": f"PO-BONE-{datetime.now().strftime('%Y%m%d-%H%M')}",
                "supplier": bone_supp["name"],
                "supplier_contact": "tedarik@trakyaorganikciftlik.com",
                "item_name": bone_supp["item"],
                "units_ordered": f"{kg_to_order} KG",
                "unit_price_try": bone_supp["price_per_kg"],
                "total_cost_try": total_bone_cost,
                "lead_time": "2 iş günü (Soğuk zincir taze kesim)",
                "status": "DRAFT_READY_FOR_APPROVAL",
                "notes": f"Mera kaval kemiği stoku {bone_item['current_stock_kg']} kg seviyesine indi. Yeni 28 saatlik demleme kazanı için acil sipariş taslağı."
            }
            pos.append(po_bone)

        # Save POs to orders directory
        for po in pos:
            file_path = os.path.join(self.orders_dir, f"{po['po_id']}.json")
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(po, f, ensure_ascii=False, indent=2)

        return {
            "audit": audit,
            "generated_pos": pos
        }

if __name__ == "__main__":
    tracker = InventoryTrackerAgent()
    result = tracker.generate_supplier_reorder_po()
    print(f"✅ InventoryTrackerAgent: {len(result['generated_pos'])} adet tedarik sipariş taslağı (PO) oluşturuldu.")
