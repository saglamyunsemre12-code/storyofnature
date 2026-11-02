#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Story of Nature - Content Creator & Social Media Agent
Plans rolling 7-day Instagram & TikTok/Reels editorial calendar, viral hooks,
carousel educational slides, recipe pairings, and luxury photography briefs.
"""

import json
import os
from datetime import datetime, timedelta

class ContentCreatorAgent:
    def __init__(self, config_path=None):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if not config_path:
            config_path = os.path.join(base_dir, "config", "brand_config.json")
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)
        self.output_dir = os.path.join(base_dir, "data", "content")
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_weekly_content_schedule(self):
        """
        Creates a 7-day high-converting content plan aligned with the brand aesthetic.
        """
        today = datetime.now()
        schedule = [
            {
                "day": "Pazartesi (10:30)",
                "date": (today + timedelta(days=0)).strftime("%d.%m.%Y"),
                "format": "Eğitici Çoklu Kaydırmalı Gönderi (Carousel)",
                "topic": "Neden Toz Kolajen Değil de Jelatinize İlikli Kemik Suyu?",
                "hook_alternatives": [
                    "Bedeninizin toz kolajen yerine gerçek ilikli kemik suyunu neden 4 kat daha hızlı emdiğini biliyor musunuz?",
                    "Laboratuvarda işlenmiş beyaz tozlar mı, 28 saatte sabırla demlenen saf jelatin mi?",
                    "Bağırsak duvarınızı onarmanın en kadim ve biyoyararlı yolu."
                ],
                "caption": """Toz kolajen takviyeleri son yıllarda her yerde. Ancak kadim biyoloji bize şunu hatırlatıyor: Beden, doğanın sunduğu bütünsel matrisi sentetik izole tozlara kıyasla çok daha yüksek biyoyararlanımla tanır ve kullanır.

Story of Nature ilikli kemik suyu buzdolabından çıktığında neden katı bir jöle kıvamındadır?
1. Yüksek Glisin & Prolin Matrisi: Jelatin kıvamı, sindirim mukozasını kaplayan ve 'sızdıran bağırsak' mikro-deliklerini onaran glisin aminoasidinin en zengin kanıtıdır.
2. Doğal Minerallerle Bütünleşik: Kalsiyum, magnezyum, fosfor ve potasyum; kemik iliğinden suya organik elma sirkesi yardımıyla doğal formunda geçer.
3. Sıfır Katkı, Sıfır Şeker, Sıfır Kıvam Artırıcı.

Sabahları aç karnına fincanınızı ısıtın, derin bir nefes alın ve bedeninize hak ettiği sabırlı şifayı verin.

🌿 Sipariş ve detaylı laboratuvar analizleri için: storyofnature.com.tr
#StoryOfNature #İlikliKemikSuyu #Kolajen #BağırsakSağlığı #SlowLiving #FonksiyonelTıp""",
                "visual_prompt": "Editorial food photography, a handcrafted wooden spoon lifting a dense, translucent amber gelatinous scoop of set bone broth jelly from an open luxury glass jar, morning sun rays, rustic oak counter, Aesop aesthetic, 8k.",
                "status": "SCHEDULED"
            },
            {
                "day": "Çarşamba (11:15)",
                "date": (today + timedelta(days=2)).strftime("%d.%m.%Y"),
                "format": "Dikey Video / Reels",
                "topic": "No. 04 Pure Baby — Ek Gıdaya Geçişte Annelerin En Güvenli Sırrı",
                "hook_alternatives": [
                    "Bebeğinizin ilk ek gıda çorbasına tuzsuz, katkısız gerçek kemik suyu eklediniz mi?",
                    "Bebekler için üretilen kemik suyunda neden ASLA ilave tuz veya baharat olmamalı?",
                    "Minik bedenlerin kemik ve kıkırdak gelişimi için en saf destek: No. 04 Pure Baby."
                ],
                "caption": """Ek gıdaya geçiş dönemi, bir annenin hayatındaki en hassas süreçlerden biridir. Bebeğinizin sindirim sistemi henüz gelişme aşamasındayken, ona sunulan her besinin katkısız ve en saf halinde olması gerekir.

Story of Nature No. 04 Pure Baby:
• %100 Sıfır İlave Tuz (Sodyum yükü oluşturmaz)
• Sıfır Karabiber ve Baharat (Alerjen riski minimum)
• Yalnızca Mera Dana Kemiği, Kereviz Sapı, Havuç ve Arıtılmış Su ile 28 Saat Kısık Ateşte Demleme

Bebeğinizin sebze pürelerine, tarhana çorbasına veya yulaf lapasına 1-2 yemek kaşığı ekleyerek doğal kolajen ve kalsiyum desteğini güvenle sağlayabilirsiniz.

🍼 Cam kavanoz güvencesiyle kapınıza teslim.
#StoryOfNature #PureBaby #EkGıda #BebekBeslenmesi #BebekKemikSuyu #DoğalBeslenme""",
                "visual_prompt": "Bright, soft morning light in a clean Scandinavian kitchen, small artisanal ceramic baby bowl with warm yellow bone broth soup and small wooden baby spoon, glass jar of Pure Baby beside it, tender motherly aura, 85mm f/2.8.",
                "status": "SCHEDULED"
            },
            {
                "day": "Cuma (18:00)",
                "date": (today + timedelta(days=4)).strftime("%d.%m.%Y"),
                "format": "Hafta Sonu Gurme Mutfak & Yaşam",
                "topic": "Şefin Reçetesi: Golden Immunity ile Ağır Demlenmiş Mantarlı Risotto",
                "hook_alternatives": [
                    "Sıradan bir akşam yemeğini Michelin standartlarında bir şölene dönüştürmenin tek bir sırrı var.",
                    "Restorandaki o derin, gövdeli lezzetin arkasında saklanan 28 saatlik kemik suyu sırrı.",
                    "Bu hafta sonu mutfağınızda zencefilli zerdeçallı gurme bir risotto pişirin."
                ],
                "caption": """Gerçek bir risotto veya gurme çorbanın lezzet derinliği; kullandığınız pirinçten çok, ona hayat veren et suyunun kalitesinde gizlidir.

Story of Nature No. 02 Golden Immunity (Zerdeçal & Zencefilli İlikli Kemik Suyu); kestane mantarları ve taze kekikle birleştiğinde ortaya sadece bir yemek değil, bütünsel bir şifa deneyimi çıkıyor.

İpucu: Risotto pirincinizi kavurduktan sonra kemik suyunuzu ayrı bir sos tenceresinde hafifçe kaynama noktasına getirin ve kepçe kepçe ekleyin. Zerdeçalın verdiği ipeksi altın rengi tabağınızı aydınlatacak.

Afiyet ve şifa olsun.
#StoryOfNature #GoldenImmunity #GurmeTarifler #MutfakSanatı #Risotto #DoğalLezzet""",
                "visual_prompt": "Steaming gourmet risotto in a dark ceramic wide bowl topped with sautéed wild mushrooms and fresh thyme, warm restaurant ambiance, subtle glass jar in background, Bon Appétit magazine style, cinematic lighting.",
                "status": "SCHEDULED"
            }
        ]

        output_path = os.path.join(self.output_dir, f"weekly_plan_{today.strftime('%Y%m%d')}.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump({
                "brand": self.config["brand"]["name"],
                "generated_at": today.isoformat(),
                "total_posts": len(schedule),
                "schedule": schedule
            }, f, ensure_ascii=False, indent=2)

        return schedule

if __name__ == "__main__":
    creator = ContentCreatorAgent()
    posts = creator.generate_weekly_content_schedule()
    print(f"✅ ContentCreatorAgent: {len(posts)} adet haftalık sosyal medya içerik ve görsel planı hazırlandı.")
