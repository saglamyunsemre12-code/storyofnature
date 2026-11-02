#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Story of Nature - Mail Drafter Agent
Crafts bespoke, 5-paragraph luxury B2B partnership proposals and customer VIP drafts.
Outputs ready-to-send email drafts for 1-click approval.
"""

import json
import os
from datetime import datetime

class MailDrafterAgent:
    def __init__(self, config_path=None):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if not config_path:
            config_path = os.path.join(base_dir, "config", "brand_config.json")
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)
        self.drafts_dir = os.path.join(base_dir, "data", "drafts")
        os.makedirs(self.drafts_dir, exist_ok=True)

    def generate_b2b_proposal(self, lead):
        """
        Builds a tailored 5-paragraph luxury proposal email for a specific lead.
        """
        lead_name = lead["name"]
        contact = lead.get("contact_person", "Yetkili")
        district = lead.get("district", "bölgeniz")
        target_prod = lead.get("target_product", "Artizan İlikli Kemik Suyu Serisi")

        subject = f"Story of Nature & {lead_name} — Artizan Kolajen & Doğal İksir İş Birliği Önerisi"

        body = f"""Sayın {contact}, Merhabalar,

{district} bölgesinde yarattığınız seçkin konsepti, misafirlerinize sunduğunuz nitelikli deneyimi ve tavizsiz kalite anlayışınızı uzun süredir takdirle takip ediyoruz. Story of Nature olarak; modern hayatın hızında kaybolan kadim beslenme ritüellerini, en saf ve sabırlı reçetelerle yeniden canlandırmak amacıyla yola çıktık. {lead_name} misafir profilinin bedenine ve ruhuna gösterdiği özenin, felsefemizle kusursuz bir uyum içinde olduğuna inanıyoruz.

Story of Nature ilikli kemik sularımız; yalnızca sertifikalı mera besisi serbest gezen hayvanların kaval kemiklerinden, filtrelenmiş kaynak suyu ve doğal organik fermente elma sirkesi eşliğinde tam 28 saat boyunca kısık ateşte demlenerek hazırlanır. Hiçbir koruyucu, katkı maddesi, renklendirici veya endüstriyel kıvam artırıcı içermez. Buzdolabına girdiğinde aldığı katı jelatin kıvamı; zengin tip-1 ve tip-3 kolajen, glisin, prolin ve biyoyararlanımı yüksek minerallerin doğal bir kanıtıdır.

İşletmeniz için özel olarak önerdiğimiz {target_prod}; hem menünüzde sıcak fincanda şifalı bir iksir olarak servis edilmeye, hem de gurme reyonunuzda estetik fildişi etiketli cam ambalajıyla satışa sunulmaya hazır durumdadır. Özellikle sabah saatlerinde veya öğün aralarında sunulacak taze zencefil-zerdeçal dokunuşlu kemik suyu fincanları, misafirlerinizin güne yenileyici ve fonksiyonel bir başlangıç yapmasını sağlayacaktır.

Story of Nature olarak iş ortaklarımıza; düzenli haftalık soğuk zincir teslimatı, toptan alımlara özel avantajlı fiyat marjları (kavanoz başına %40+ brüt kâr oranı) ve personelinize ürün hikâyesini aktaracak özel eğitim/sunum materyalleri sağlıyoruz. İlk sevkiyat öncesinde ürünlerimizi bizzat tatmanız ve mutfak ekibinizle değerlendirmeniz adına size özel bir 'Tadım ve Tanışma Kiti' göndermekten onur duyarız.

Bu kıymetli iş birliğini başlatmak ve tadım kitinizi hangi adrese iletmemizi arzu ettiğinizi paylaşmak üzere bu e-postayı yanıtlamanız yeterlidir. Dilerseniz uygun bir gününüzde kahve eşliğinde detayları konuşmaktan büyük mutluluk duyarız.

Saygılarımla,

Yunus Emre Sağlam
Kurucu, Story of Nature
Telefon: +90 533 084 90 27
E-posta: saglam.yunsemre12@gmail.com
Web: https://storyofnature.com.tr
"""
        draft_item = {
            "lead_id": lead.get("id"),
            "to_name": lead_name,
            "to_email": lead.get("email"),
            "subject": subject,
            "body": body,
            "created_at": datetime.now().isoformat(),
            "status": "READY_FOR_APPROVAL"
        }
        return draft_item

    def generate_all_drafts(self, leads):
        """
        Generates and saves drafts for all scanned leads.
        """
        all_drafts = []
        for lead in leads:
            draft = self.generate_b2b_proposal(lead)
            all_drafts.append(draft)
            
            # Save single draft file
            safe_name = lead["name"].replace(" ", "_").replace("/", "_").lower()
            draft_path = os.path.join(self.drafts_dir, f"draft_{safe_name}.json")
            with open(draft_path, "w", encoding="utf-8") as f:
                json.dump(draft, f, ensure_ascii=False, indent=2)

        index_path = os.path.join(self.drafts_dir, "drafts_queue_latest.json")
        with open(index_path, "w", encoding="utf-8") as f:
            json.dump({
                "brand": self.config["brand"]["name"],
                "total_drafts": len(all_drafts),
                "generated_at": datetime.now().isoformat(),
                "drafts": all_drafts
            }, f, ensure_ascii=False, indent=2)

        return all_drafts

if __name__ == "__main__":
    from lead_finder import LeadFinderAgent
    lf = LeadFinderAgent()
    leads = lf.scan_targeted_leads()
    drafter = MailDrafterAgent()
    drafts = drafter.generate_all_drafts(leads)
    print(f"✅ MailDrafterAgent: {len(drafts)} adet 5 paragraflık kişiselleştirilmiş teklif taslağı hazırlandı.")
