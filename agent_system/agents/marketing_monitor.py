#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Story of Nature - Marketing & Reputation Agent
Manages Meta/Instagram ad target personas, ad copy formulas,
and automated customer post-purchase review collection workflows.
"""

import json
import os
from datetime import datetime

class MarketingMonitorAgent:
    def __init__(self, config_path=None):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if not config_path:
            config_path = os.path.join(base_dir, "config", "brand_config.json")
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)
        self.output_dir = os.path.join(base_dir, "data", "reports")
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_meta_ad_campaigns(self):
        """
        Structures laser-targeted Meta Ads configurations for the Turkish luxury wellness market.
        """
        campaigns = [
            {
                "campaign_id": "META-CAM-001",
                "campaign_name": "TOFU / Bilinçlendirme — Katkısız Gerçek Jel Kolajen",
                "objective": "CONVERSIONS (Satış)",
                "target_audience": {
                    "locations": ["İstanbul", "İzmir", "Ankara", "Bursa", "Muğla", "Antalya"],
                    "age_range": "27 - 54",
                    "gender": "Kadın & Erkek (Öncelik Kadın %65)",
                    "interests": [
                        "Fonksiyonel tıp", "Keto diyeti", "Pilates", "Cilt bakımı ve Kolajen",
                        "Organik gıda", "Slow living", "Erewhon", "Macrocenter"
                    ],
                    "behaviors": ["Üst düzey gelir grubu / iOS son modelleri kullananlar", "Çevrimiçi alışveriş yapanlar"]
                },
                "ad_creatives": [
                    {
                        "headline": "Toz Takviyeleri Unutun. 28 Saatte Demlenen Saf Jelatin.",
                        "primary_text": "Buzdolabından çıkardığınızda kaşıkta sallanan o yoğun kıvam, vücudunuzun biyolojik olarak tanıdığı tek gerçek kolajen kaynağıdır. Sıfır katkı, mera besisi ve cam kavanoz tazeliğiyle.",
                        "call_to_action": "Şimdi Keşfet",
                        "landing_url": "https://storyofnature.com.tr"
                    }
                ],
                "budget_recommendation_daily_try": 350.0,
                "expected_roas": "3.8x - 4.5x"
            },
            {
                "campaign_id": "META-CAM-002",
                "campaign_name": "Niche / Anne & Bebek — No. 04 Pure Baby Ek Gıda",
                "objective": "CONVERSIONS (Satış)",
                "target_audience": {
                    "locations": ["Tüm Türkiye (Öncelikli Büyükşehirler)"],
                    "age_range": "24 - 40",
                    "gender": "Kadın",
                    "interests": [
                        "Ek gıda tarifleri", "Bebek beslenmesi", "BLW Türkiye",
                        "Organik bebek maması", "Montessori eğitimi"
                    ]
                },
                "ad_creatives": [
                    {
                        "headline": "Bebeğinizin İlk Ek Gıdası İçin %100 Tuzsuz ve Baharatsız.",
                        "primary_text": "Annelerin içi rahat etsin diye; sıfır ilave tuz, sıfır baharat. Yalnızca kaval kemiği ve taze sebzelerle 28 saatte ağır ağır demlendi.",
                        "call_to_action": "İncele ve Sipariş Ver",
                        "landing_url": "https://storyofnature.com.tr"
                    }
                ],
                "budget_recommendation_daily_try": 250.0,
                "expected_roas": "4.2x"
            }
        ]
        return campaigns

    def generate_review_followup_protocol(self):
        """
        Builds the post-delivery review & satisfaction email template for customers.
        """
        protocol = {
            "trigger": "Sipariş teslimatından 4 gün sonra (Kavanozun açılıp tadıldığı an)",
            "subject": "Story of Nature deneyiminiz nasıl geçti? — Sizin için buradayız 🌿",
            "body": """Merhaba Değerli Misafirimiz,

Story of Nature ilikli kemik suyu kavanozunuzun mutfağınıza ulaştığını ve ilk şifa fincanınızı demlediğinizi umuyoruz.

Bizim için her bir kavanoz, 28 saatlik sabrın ve doğaya duyulan saygının bir ürünüdür. Deneyiminizin nasıl geçtiğini, lezzet profilini ve kıvamını nasıl bulduğunuzu duymayı çok isteriz.

Eğer deneyiminizden memnun kaldıysanız, Google profilimize ve web sitemize birkaç saniyenizi ayırarak bir yorum bırakmanız; doğallık arayışındaki diğer insanlara rehberlik etmemiz adına bizim için paha biçilemez bir destek olacaktır.

⭐ Deneyiminizi Paylaşın: https://storyofnature.com.tr/yorum-yap

Sevgi ve sağlıkla kalınız,
Story of Nature Ailesi"""
        }
        return protocol

if __name__ == "__main__":
    marketing = MarketingMonitorAgent()
    cams = marketing.generate_meta_ad_campaigns()
    print(f"✅ MarketingMonitorAgent: {len(cams)} adet Meta reklam stratejisi ve müşteri yorum toplama protokolü oluşturuldu.")
