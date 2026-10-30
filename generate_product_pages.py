#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Story of Nature - Dedicated High-Converting Product Detail Pages Generator
Generates standalone, responsive, modern PDP pages:
- pure-essence.html
- golden-immunity.html
- gece-masali.html
- saf-bebek-kolajeni.html
- rosemary-elixir.html
- 14-gunluk-paket.html
And product.html router.
"""

import os
import json

SITE_DIR = "/Users/emre/.gemini/antigravity/scratch/story-of-nature/site"
PRODUCTS = {
    "no01": {
        "filename": "pure-essence.html",
        "category_eyebrow": "ZANAATKAR İLİKLİ KEMİK SUYU SERİSİ • 300 ML",
        "title": "No. 01 Pure Essence İlikli Kemik Suyu",
        "subtitle": "28 Saat Kısık Ateşte Ağır Pişirilmiş • %100 Doğal Taş Jöle Kıvamı",
        "price": 220,
        "old_price": 260,
        "vol": "300 ml Cam Kavanoz",
        "badge": "✦ EN ÇOK SATAN #1",
        "badge_color": "#163824",
        "badge_bg": "#EBF3EC",
        "category_name": "İlikli Kemik Suları",
        "rating": "5.0",
        "review_count": 218,
        "lead": "Acıbadem Sağlık rehberi standartlarında; serbest gezen dana kaval kemikleri, organik elma sirkesi ve aromatik kök sebzelerle 28 saat boyunca kısık ateşte demlendi. Çift ön haşlama sayesinde ağır kokusuz, buzdolabında kaşık dik duran doğal taş jöle kıvamı.",
        "slides": [
            {
                "src": "assets/product_no01_bone_broth.jpg",
                "pill": "✦ Zanaatkar Üretim • 300 ml Cam",
                "label": "1 / 6 • Zanaatkar Cam Kavanoz & 121°C Emniyet Vakumu",
                "thumb": "Ürün"
            },
            {
                "src": "assets/photo_01_morning_pour.jpg",
                "pill": "✦ Sabah İksiri • Sıfır Ağır Koku",
                "label": "2 / 6 • Buharlı Sabah Rutini: 60°C Berrak Altın İçim",
                "thumb": "Sabah İksiri"
            },
            {
                "src": "assets/hero_collagen_jelly.jpg",
                "pill": "✦ +4°C Taş Jöle Testi • %100 Jelatin",
                "label": "3 / 6 • Reddit #1 Kalite Kanıtı: Kaşıkla Kalkan Doğal Jöle",
                "thumb": "Jöle Kanıtı"
            },
            {
                "src": "assets/photo_02_ingredients_flatlay.jpg",
                "pill": "✦ Organik Çiftlik İçerikleri",
                "label": "4 / 6 • Taze Zencefil, Zerdeçal, Kereviz Sapı & Elma Sirkesi",
                "thumb": "İçindekiler"
            },
            {
                "src": "assets/photo_03_gourmet_soup.jpg",
                "pill": "✦ Gurme Tarif • 14g Saf Protein",
                "label": "5 / 6 • Lokanta Usulü İlikli Sarı Mercimek Çorbası",
                "thumb": "Tarif"
            },
            {
                "src": "assets/bundle_14day_box.jpg",
                "pill": "✦ Özel Darbe Korumalı Kargo",
                "label": "6 / 6 • Air-Column Kırılmaz Ambalaj & Lüks Kutu",
                "thumb": "Kargo Paketi"
            }
        ],
        "highlights": [
            "Çift Ön Haşlama Teknolojisi: Sıfır hayvansal ağır koku, kadifemsi berrak içim.",
            "Taş Jöle Garantisi: Buzdolabında (+4°C) jöleleşmezse %100 para iadesi.",
            "3 Kademeli Soğuk Filtrasyon: <%0.2 yağ oranı, sindirimi yormaz.",
            "Acıbadem Standardında 7.800 mg Tip 1 & 3 Biyoaktif Kolajen.",
            "121°C Otoklav Basınçlı Cam Kapama: Katkısız 6 ay oda sıcaklığında raf ömrü."
        ],
        "table": [
            [
                "Protein (100 ml)",
                "12.4 g Saf Biyoaktif Protein"
            ],
            [
                "Doğal Kolajen (Tip 1 & 3)",
                "7.800 mg Konsantrasyon"
            ],
            [
                "Glisin & Prolin Aminoasitleri",
                "Zengin Bağırsak Bariyeri & Mukoza Desteği"
            ],
            [
                "İlave Tuz / Bulyon / MSG",
                "%0.0 (Kesinlikle Katkısız)"
            ],
            [
                "Yağ Oranı",
                "<%0.2 (Doymuş Yağdan Arındırılmış)"
            ],
            [
                "Sterilizasyon",
                "121°C Otoklav Basınçlı Cam Kapama"
            ],
            [
                "Saklama",
                "Açılmadan 6 Ay Oda Sıcaklığı / Açıldıktan Sonra +4°C 48 Saat veya Buzlukta 6 Ay"
            ]
        ],
        "recipe_title": "Lokanta Usulü İlikli Sarı Mercimek Çorbası",
        "recipe_desc": "Mercimek ve sebzeler tencereye konur; 1 kavanoz No. 01 kemik suyu ve 3 bardak suyla 20 dakika kısık ateşte pişirilip blenderdan geçirilir. 1 kasede 14g doğal kolajen proteini!",
        "recipe_time": "⏱ 25 Dakika • Kolay",
        "faq_objections": [
            [
                "Kokusu ağır mı? İçebilir miyim?",
                "Kesinlikle kokmaz. Kemikler pişirilmeden önce 2 kez şok ön haşlamadan geçirilir ve ilk suları atılır. Ardından taze kereviz, havuç, defne yaprağı ve elma sirkesiyle demlenir. Çocukların ve hassas burunların rahatlıkla içebileceği berrak, hafif ve iştah açıcı bir aromaya sahiptir."
            ],
            [
                "Dolapta gerçekten jöleleşiyor mu yoksa su gibi mi?",
                "Story of Nature No. 01, buzdolabına (+4°C) girdiğinde taş gibi katı bir jöle halini alır; kaşığı daldırdığınızda kaşık dik durur. Şikayetvar'daki 'su gibi geldi' şikayetlerine inat, jöleleşmeme durumunda koşulsuz %100 iade garantisi veriyoruz."
            ],
            [
                "Açtıktan sonra 2 günde biter mi? Bozulur mu?",
                "Koruyucu ve kimyasal içermediği için kapağı açıldıktan sonra buzdolabında 48 saat içinde tüketilmelidir. Ancak tamamını bitiremeyecekseniz, kavanozu açtığınız gibi buz kalıplarına döküp dondurun! 6 ay boyunca her pilav ve çorbaya 2'şer küp atarak taptaze kullanabilirsiniz."
            ],
            [
                "Kargoda kavanoz kırılır mı?",
                "Özel petekli hava kanallı (air-column) şişme zırhlı kutularda sevk edilir. 2 metreden düşse dahi kırılmaz. Nadir bir aksilikte tek bir fotoğrafınızla aynı gün ücretsiz yenisi kargolanır."
            ]
        ]
    },
    "no02": {
        "filename": "golden-immunity.html",
        "category_eyebrow": "ZANAATKAR İLİKLİ KEMİK SUYU SERİSİ • 300 ML",
        "title": "No. 02 Golden Immunity Zencefil & Zerdeçal",
        "subtitle": "28 Saat Kısık Ateşte Ağır Pişirilmiş • %2000 Piperin Emilimli Bağışıklık Kürü",
        "price": 240,
        "old_price": 280,
        "vol": "300 ml Cam Kavanoz",
        "badge": "✦ BAĞIŞIKLIK & ANTİOKSİDAN",
        "badge_color": "#8B4513",
        "badge_bg": "#FEF3C7",
        "category_name": "İlikli Kemik Suları",
        "rating": "4.9",
        "review_count": 184,
        "lead": "28 saat kaynatılmış ilikli kemik suyuna; taze tırnak zencefil, taze kök zerdeçal, tane karabiber ve organik elma sirkesi eklendi. Karabiberdeki doğal piperin, zerdeçalın kurkumin emilimini %2000 artırarak hücresel savunma kalkanı oluşturur.",
        "slides": [
            {
                "src": "assets/product_no02_golden_immunity.jpg",
                "pill": "✦ Taze Kök Zencefil & Zerdeçal",
                "label": "1 / 6 • Golden Immunity Zanaatkar Cam Kavanoz",
                "thumb": "Ürün"
            },
            {
                "src": "assets/photo_01_morning_pour.jpg",
                "pill": "✦ Sabah Bağışıklık İksiri",
                "label": "2 / 6 • Altın Renkli Buharlı Kupa: Güne Zinde Başlangıç",
                "thumb": "Altın İksir"
            },
            {
                "src": "assets/photo_02_ingredients_flatlay.jpg",
                "pill": "✦ %2000 Biyoyararlanım Formülü",
                "label": "3 / 6 • Taze Zerdeçal + Taze Zencefil + Tane Karabiber",
                "thumb": "Kök İçerik"
            },
            {
                "src": "assets/hero_collagen_jelly.jpg",
                "pill": "✦ +4°C Doğal Jelatin Dokusu",
                "label": "4 / 6 • Taş Jöle Garantisi: Bağırsak Bariyeri Onarımı",
                "thumb": "Jöle Testi"
            },
            {
                "src": "assets/photo_03_gourmet_soup.jpg",
                "pill": "✦ Şifa Çorbası Tarifi",
                "label": "5 / 6 • Zencefilli Tavuk & Kemik Suyu Çorbası",
                "thumb": "Tarif"
            },
            {
                "src": "assets/bundle_14day_box.jpg",
                "pill": "✦ Zırhlı Kargo Ambalajı",
                "label": "6 / 6 • Kırılmaya Karşı Güvenli Teslimat",
                "thumb": "Paketleme"
            }
        ],
        "highlights": [
            "Bilimsel Sinerji: Piperin (karabiber) destekli %2000 kurkumin biyoyararlanımı.",
            "Mevsim Geçişleri & Boğaz Rahatlatıcı: Taze zencefilin ısıtıcı, yatıştırıcı etkisi.",
            "Taş Jöle Garantisi: +4°C'de kaşık tutan yoğun kolajen matrisi.",
            "Sıfır İlave Şeker, Nişasta veya Kıvam Artırıcı.",
            "Acıbadem Kriterlerinde 8.200 mg Zengin Kolajen Peptit."
        ],
        "table": [
            [
                "Protein (100 ml)",
                "12.6 g Biyoaktif Protein"
            ],
            [
                "Doğal Kolajen",
                "8.200 mg Tip 1 & 3 Kolajen"
            ],
            [
                "Aktif Kurkumin & Gingerol",
                "Standart Ekstrakt Seviyesi"
            ],
            [
                "Piperin (Tane Karabiber)",
                "Emilim Hızlandırıcı Katalizör"
            ],
            [
                "İlave Tuz & Şeker",
                "%0.0"
            ],
            [
                "Sterilizasyon",
                "121°C Otoklav Basınçlı Cam Kapama"
            ],
            [
                "Saklama",
                "Açılmadan 6 Ay Oda Sıcaklığı / Açıldıktan Sonra +4°C 48 Saat"
            ]
        ],
        "recipe_title": "Zencefilli Altın Şifa Tavuk Çorbası",
        "recipe_desc": "Didilmiş köy tavuğu, havuç ve 1 kavanoz No. 02 Golden Immunity tencerede 15 dakika kaynatılır. Taze limon suyu ile servis edilir. Grip ve halsizlik dönemlerinde anında toparlar.",
        "recipe_time": "⏱ 20 Dakika • Kolay",
        "faq_objections": [
            [
                "Tadı acı veya yakıcı mı?",
                "Hayır. Taze zencefil ve karabiber dozajı içimi ısıtacak tatlı bir ferahlıkta dengelenmiştir. Asla boğazı yakmaz; içtikten sonra göğsünüzü ve midenizi sıcacık sarar."
            ],
            [
                "İçindeki zerdeçal tortu yapar mı?",
                "Ürünlerimiz 3 aşamalı mikron filtreden geçirilir. Şişenin dibinde göreceğiniz hafif altın tonundaki partiküller taze kök zerdeçalın doğal lifleridir, çalkalayarak afiyetle içiniz."
            ],
            [
                "Çocuklar içebilir mi?",
                "1 yaş üzeri çocuklarda özellikle kış aylarında çorbalara katılarak güvenle kullanılabilir. 1 yaş altı bebekler için No. 04 Saf Bebek Kolajeni önerilir."
            ]
        ]
    },
    "no03": {
        "filename": "gece-masali.html",
        "category_eyebrow": "FONKSİYONEL BOTANİK ÇAY SERİSİ • 75 GR",
        "title": "No. 03 Night Story Sakinleşme Çayı",
        "subtitle": "Organik Fransız Lavantası, Tıbbi Papatya & Melisa • %100 Kafeinsiz Akşam Ritüeli",
        "price": 195,
        "old_price": 230,
        "vol": "75 gr Kraft Doypack Pouch",
        "badge": "✦ DERİN UYKU & STRES KARŞITI",
        "badge_color": "#4A3B69",
        "badge_bg": "#F3E8FF",
        "category_name": "Fonksiyonel Çaylar",
        "rating": "4.9",
        "review_count": 97,
        "lead": "Akşam saatlerinde kortizol seviyesini düşürmek ve derin REM uykusuna geçişi desteklemek için formüle edildi. Bütün çiçekli Fransız lavantası, tıbbi papatya başçıkları ve melisa yaprakları ile günün tüm zihinsel yorgunluğunu geride bırakın.",
        "slides": [
            {
                "src": "assets/product_no03_night_tea.jpg",
                "pill": "✦ Bütün Çiçekli Botanik Harman",
                "label": "1 / 6 • Kraft Fermuarlı Korumalı Doypack Pouch",
                "thumb": "Ürün"
            },
            {
                "src": "assets/photo_01_morning_pour.jpg",
                "pill": "✦ Akşam Ritüeli",
                "label": "2 / 6 • Buharlı Seramik Fincanda Huzur Dolu Demleme",
                "thumb": "Ritüel"
            },
            {
                "src": "assets/photo_02_ingredients_flatlay.jpg",
                "pill": "✦ Saf Fransız Lavantası & Papatya",
                "label": "3 / 6 • Taze Kurutulmuş Aromatik Bitkiler",
                "thumb": "Bitkiler"
            },
            {
                "src": "assets/bundle_14day_box.jpg",
                "pill": "✦ 14 Günlük Kür Tamamlayıcısı",
                "label": "4 / 6 • Hücresel Yenilenme Seti Parçası",
                "thumb": "Set Uyumu"
            }
        ],
        "highlights": [
            "%100 Kafeinsiz: Gece kalp çarpıntısı yapmaz, uykuyu bölmez.",
            "Bütün Çiçek Garantisi: Toz veya sap içermez, sadece seçkin çiçek başçıkları.",
            "GABA Nörotransmitter Desteği: Melisa ve papatyanın doğal sinir yatıştırıcı etkisi.",
            "Aroma Korumalı Kilitli Kraft Ambalaj.",
            "Kemik Suyu Kürünün Akşam Fazı Tamamlayıcısı."
        ],
        "table": [
            [
                "İçindekiler",
                "Tıbbi Papatya (%40), Melisa (%35), Fransız Lavantası (%25)"
            ],
            [
                "Kafein Oranı",
                "%0.0 (Kafeinsiz)"
            ],
            [
                "Aroma Verici / Esans",
                "Sıfır Katkı (Saf Bitki Çiçeği)"
            ],
            [
                "Porsiyon Sayısı",
                "75 gr (~35-40 Fincan)"
            ],
            [
                "Demleme Süresi",
                "95°C Suda 6-8 Dakika"
            ],
            [
                "Ambalaj",
                "Aroma Kilitli Çok Katmanlı Kraft Doypack"
            ]
        ],
        "recipe_title": "Lavanta & Ballı Gece İksiri",
        "recipe_desc": "1 tatlı kaşığı Night Story harmanı 200 ml kaynamış suda 7 dakika demlenir. Süzüldükten sonra 1 çay kaşığı ham çiçek balı eklenerek yudumlanır. Uykudan 45 dakika önce önerilir.",
        "recipe_time": "⏱ 7 Dakika • Çok Kolay",
        "faq_objections": [
            [
                "Tadı acı mı?",
                "Hayır. Bütün papatya ve melisa çiçekleri kullanıldığı için yumuşak, tatlımsı ve son derece ferah bir içime sahiptir."
            ],
            [
                "Sabah sersemlik yapar mı?",
                "İlaç veya melatonin takviyesi değildir; vücudun kendi doğal GABA dengesini destekler. Sabah dinç ve berrak bir zihinle uyanırsınız."
            ]
        ]
    },
    "no04": {
        "filename": "saf-bebek-kolajeni.html",
        "category_eyebrow": "ZANAATKAR İLİKLİ KEMİK SUYU SERİSİ • 300 ML",
        "title": "No. 04 Saf Bebek Kolajeni",
        "subtitle": "28 Saat Kısık Ateşte Ağır Pişirilmiş • Sıfır Tuz & Baharat Pediatrik Ek Gıda",
        "price": 230,
        "old_price": 270,
        "vol": "300 ml Cam Kavanoz",
        "badge": "✦ EK GIDA & PEDİATRİK GÜVEN",
        "badge_color": "#2D6A4F",
        "badge_bg": "#D8F3DC",
        "category_name": "İlikli Kemik Suları",
        "rating": "5.0",
        "review_count": 165,
        "lead": "Annelerin ve çocuk doktorlarının en hassas beklentilerine göre üretildi: %0.0 ilave tuz, %0.0 baharat, %0.0 soğan ve sarımsak. Sadece serbest gezen dana ilikli kemikleri ve birkaç damla organik elma sirkesi ile 28 saatte demlenen saf kolajen ve kalsiyum kaynağı.",
        "slides": [
            {
                "src": "assets/product_no04_baby_broth.jpg",
                "pill": "✦ Pediatrik Kriter • Sıfır Tuz",
                "label": "1 / 6 • Saf Bebek Kolajeni Cam Kavanoz & Ahşap Kaşık",
                "thumb": "Ürün"
            },
            {
                "src": "assets/hero_collagen_jelly.jpg",
                "pill": "✦ +4°C Doğal Taş Jöle",
                "label": "2 / 6 • Bebek Çorbalarına 2 Yemek Kaşığı Doğal Kolajen",
                "thumb": "Jöle Kanıtı"
            },
            {
                "src": "assets/photo_01_morning_pour.jpg",
                "pill": "✦ Kokusuz & Berrak",
                "label": "3 / 6 • Bebeklerin Kolayca Kabul Ettiği Doğal Lezzet",
                "thumb": "İçim"
            },
            {
                "src": "assets/photo_03_gourmet_soup.jpg",
                "pill": "✦ Ek Gıda Çorba Tarifi",
                "label": "4 / 6 • Bebekler İçin Balkabaklı & İlikli Sebze Püresi",
                "thumb": "Bebek Püresi"
            },
            {
                "src": "assets/bundle_14day_box.jpg",
                "pill": "✦ Kırılmaz Güvenli Kargo",
                "label": "5 / 6 • Anneler İçin Endişesiz Hızlı Teslimat",
                "thumb": "Kargo"
            }
        ],
        "highlights": [
            "Pediatrik Formül: Sıfır tuz, sıfır soğan, sarımsak veya gaz yapıcı baharat.",
            "Kemik & Diş Gelişimi: Doğal kalsiyum, magnezyum, fosfor ve kolajen.",
            "Bağırsak Florası Desteği: Ek gıdaya geçişte sindirimi kolaylaştırır.",
            "Alerjen İçermez: Gluten, laktoz, koruyucu, renklendirici kesinlikle yoktur.",
            "Pratik Kullanım: Buzlukta dondurularak her sebze püresine 1 küp eklenebilir."
        ],
        "table": [
            [
                "İlave Tuz (Sodyum)",
                "%0.0 (Sıfır İlave Tuz)"
            ],
            [
                "Baharat / Soğan / Sarımsak",
                "%0.0 (Bebek Sindirimine Uygun)"
            ],
            [
                "Doğal Kolajen (Tip 1 & 3)",
                "7.600 mg / 100 ml"
            ],
            [
                "Alerjenler (Gluten, Süt)",
                "%0.0 (Tamamen Alerjensiz)"
            ],
            [
                "Sterilizasyon",
                "121°C Basınçlı Otoklav"
            ],
            [
                "Önerilen Başlangıç Yaşı",
                "6. Aydan İtibaren (Doktor Onayı ile)"
            ]
        ],
        "recipe_title": "Bebekler İçin Balkabaklı İlikli Güç Püresi",
        "recipe_desc": "1 dilim balkabağı ve yarım havuç buharda haşlanır. Çatalla ezilirken içine 2 yemek kaşığı (veya 2 donmuş küp) No. 04 Bebek Kemik Suyu eklenir. Ilık olarak bebeğe yedirilir.",
        "recipe_time": "⏱ 15 Dakika • Çok Kolay",
        "faq_objections": [
            [
                "Bebeğimin böbreklerini yorar mı? Tuz var mı?",
                "Kesinlikle tuz eklenmemiştir (%0.0). Analiz raporlarımızda çıkan sodyum miktarı tamamen kemiklerin doğal yapısından kaynaklanan eser miktardır. Bebeğinizin böbreklerini yormaz."
            ],
            [
                "Gaz veya alerji yapar mı?",
                "Soğan, sarımsak, kereviz gibi gaz veya alerji potansiyeli olan hiçbir sebze konulmamıştır. Sadece ilikli kaval kemiği ve arıtılmış su kullanılmıştır."
            ],
            [
                "Kavanozu nasıl saklamalıyım?",
                "Kavanozu açar açmaz bebek buz kalıplarına döküp dondurmanızı tavsiye ederiz. Her gün çorbasına 1-2 küp ekleyerek 6 ay boyunca taze kullanabilirsiniz."
            ]
        ]
    },
    "no05": {
        "filename": "rosemary-elixir.html",
        "category_eyebrow": "ZANAATKAR İLİKLİ KEMİK SUYU SERİSİ • 300 ML",
        "title": "No. 05 Rosemary Collagen Elixir",
        "subtitle": "28 Saat Kısık Ateşte Ağır Pişirilmiş • Yabani Biberiye & Dağ Kekiği Gurme Aroma",
        "price": 235,
        "old_price": 275,
        "vol": "300 ml Cam Kavanoz",
        "badge": "✦ GURME ŞEF SERİSİ",
        "badge_color": "#1B4332",
        "badge_bg": "#D8F3DC",
        "category_name": "İlikli Kemik Suları",
        "rating": "4.9",
        "review_count": 112,
        "lead": "Akdeniz'in vahşi dağlarından toplanan taze biberiye, dağ kekiği ve defne yapraklarıyla zenginleştirilmiş gurme kolajen iksiri. Soslara, et yemeklerine, risottoya ve doğrudan içime eşsiz bir zenginlik katar.",
        "slides": [
            {
                "src": "assets/product_no05_rosemary_broth.jpg",
                "pill": "✦ Taze Yabani Biberiye & Kekik",
                "label": "1 / 6 • Rosemary Collagen Elixir Cam Kavanoz",
                "thumb": "Ürün"
            },
            {
                "src": "assets/photo_01_morning_pour.jpg",
                "pill": "✦ Aromatik Gurme İçim",
                "label": "2 / 6 • Akdeniz Baharatlarıyla Dingin ve Zengin Sabah Kupası",
                "thumb": "Gurme Kupa"
            },
            {
                "src": "assets/photo_02_ingredients_flatlay.jpg",
                "pill": "✦ Dağ Kekiği & Defne Yaprağı",
                "label": "3 / 6 • Doğal Antioksidan Kaynağı Taze Otlar",
                "thumb": "İçerikler"
            },
            {
                "src": "assets/hero_collagen_jelly.jpg",
                "pill": "✦ +4°C Doğal Taş Jöle",
                "label": "4 / 6 • Yüksek Jelatin Yoğunluğu Garantisi",
                "thumb": "Jöle Kanıtı"
            },
            {
                "src": "assets/photo_03_gourmet_soup.jpg",
                "pill": "✦ Şef Usulü Risotto & Soslar",
                "label": "5 / 6 • Şef Mutfağı: Biberiyeli İlikli Et Redüksiyonu",
                "thumb": "Yemek Tarifi"
            },
            {
                "src": "assets/bundle_14day_box.jpg",
                "pill": "✦ Zırhlı Kargo Ambalajı",
                "label": "6 / 6 • Kırılmaya Karşı Güvenli Teslimat",
                "thumb": "Kargo"
            }
        ],
        "highlights": [
            "Akdeniz Gurme Buketi: Taze yabani biberiye, kekik ve defne yaprağı.",
            "Yemeklerin Gizli İmzası: Risotto, makarna sosu ve et yemeklerine restoran lezzeti.",
            "Taş Jöle Garantisi: Buzdolabında yoğun, kaşıkla kalkan jelatin formu.",
            "Sindirim ve Karaciğer Desteği: Biberiyedeki rosmarinik asit ile güçlü antioksidan etki.",
            "121°C Basınçlı Otoklav Cam Kapama ile 6 Ay Koruyucusuz Raf Ömrü."
        ],
        "table": [
            [
                "Protein (100 ml)",
                "12.5 g Saf Biyoaktif Protein"
            ],
            [
                "Doğal Kolajen",
                "7.900 mg Tip 1 & 3 Kolajen"
            ],
            [
                "Bitkisel Ekstraktlar",
                "Yabani Biberiye, Dağ Kekiği, Defne Yaprağı"
            ],
            [
                "İlave Tuz & Şeker",
                "%0.0 (Doğal Aromatik)"
            ],
            [
                "Yağ Oranı",
                "<%0.2 (Arındırılmış Hafif İçim)"
            ],
            [
                "Sterilizasyon",
                "121°C Otoklav"
            ],
            [
                "Saklama",
                "Açılmadan 6 Ay / Açıldıktan Sonra +4°C 48 Saat"
            ]
        ],
        "recipe_title": "Şef Usulü Biberiyeli Mantarlı Risotto",
        "recipe_desc": "Arborio pirinci zeytinyağında sotelenir; her aşamada sıcak No. 05 Rosemary kemik suyu azar azar eklenerek çektirilir. Son dokunuşta parmesan ve trüf yağı ile bağlanır.",
        "recipe_time": "⏱ 30 Dakika • Orta",
        "faq_objections": [
            [
                "Biberiye kokusu çok mu baskın?",
                "Dozajı şefler tarafından hassasiyetle ayarlanmıştır; ne eti bastırır ne de boğazı sıkar. Çok zarif, Akdeniz esintili bir ferahlık verir."
            ],
            [
                "Sadece yemekte mi kullanılır, içilir mi?",
                "Doğrudan kupaya döküp ısıtarak keyifle içebilirsiniz. Özellikle akşam yemeklerinden önce harika bir iştah açıcı ve sindirim başlatıcıdır."
            ]
        ]
    },
    "bundle": {
        "filename": "14-gunluk-paket.html",
        "category_eyebrow": "HÜCRESEL YENİLENME KÜR SERİSİ • FULL SET",
        "title": "14 Günlük Lüks Yenilenme Kiti",
        "subtitle": "4 Kavanoz Kemik Suyu + 1 Botanik Çay + Dozaj Kaşığı + 14 Günlük Rehber",
        "price": 890,
        "old_price": 1150,
        "vol": "Özel Hediye & Kür Kutusu",
        "badge": "✦ %23 AVANTAJLI KÜR SETİ",
        "badge_color": "#163824",
        "badge_bg": "#FEF3C7",
        "category_name": "Yenilenme Kürleri",
        "rating": "5.0",
        "review_count": 89,
        "lead": "Bağırsak mukozasını sıfırlamak, eklem ağrılarını hafifletmek ve cilt elastikiyetini gözle görülür şekilde artırmak için tasarlanmış 14 günlük tam protokol. 2x Pure Essence + 1x Golden Immunity + 1x Rosemary Elixir + 1x Night Story Çay + El Yapımı Zeytin Ağacı Kaşık.",
        "slides": [
            {
                "src": "assets/bundle_14day_box.jpg",
                "pill": "✦ Lüks Açılır Hediye Kutusu",
                "label": "1 / 6 • 14 Günlük Hücresel Yenilenme Protokol Seti",
                "thumb": "Kutu Seti"
            },
            {
                "src": "assets/photo_01_morning_pour.jpg",
                "pill": "✦ Sabah Ritüeli",
                "label": "2 / 6 • Sabahları Aç Karnına 100 ml Ilık Kemik Suyu",
                "thumb": "Sabah Rutini"
            },
            {
                "src": "assets/hero_collagen_jelly.jpg",
                "pill": "✦ Doğal Taş Jöle Garantisi",
                "label": "3 / 6 • Katkısız Tip 1 & 3 Biyoaktif Kolajen",
                "thumb": "Jöle Kanıtı"
            },
            {
                "src": "assets/product_no03_night_tea.jpg",
                "pill": "✦ Akşam Uyku Fazı",
                "label": "4 / 6 • Gece Yatmadan Önce Night Story Çayı",
                "thumb": "Akşam Çayı"
            },
            {
                "src": "assets/photo_03_gourmet_soup.jpg",
                "pill": "✦ 14 Günlük Beslenme Rehberi",
                "label": "5 / 6 • Kutuda Gelen Şef Tarifleri & Kullanım Takvimi",
                "thumb": "Beslenme Kılavuzu"
            },
            {
                "src": "assets/photo_02_ingredients_flatlay.jpg",
                "pill": "✦ Çiftlikten Sofraya",
                "label": "6 / 6 • %100 Doğal Organik Hammaddeler",
                "thumb": "İçerikler"
            }
        ],
        "highlights": [
            "Tam Bütüncül Kür: 14 gün boyunca sabah kemik suyu iksiri, akşam dinlendirici bitki çayı.",
            "Hediye Özel Aksesuar: Masif zeytin ağacından elde oyulmuş zanaatkar dozaj kaşığı.",
            "14 Günlük Takvim Kitapçığı: Gün gün ne zaman nasıl içileceğini anlatan adım adım kılavuz.",
            "%23 Fiyat Avantajı: Tek tek alıma göre 260 TL doğrudan tasarruf ve ücretsiz kargo.",
            "Zırhlı Çift Katmanlı Koruma: Sıfır sızıntı ve kırılma garantisi."
        ],
        "table": [
            [
                "Kutu İçeriği",
                "4x 300ml Kemik Suyu + 1x 75g Botanik Çay"
            ],
            [
                "Aksesuar",
                "1x El Yapımı Masif Zeytin Ağacı Kaşık"
            ],
            [
                "Rehber",
                "1x Kuşe Baskı 14 Günlük Kullanım Kılavuzu"
            ],
            [
                "Toplam Kolajen",
                "31.500 mg Tip 1 & 3 Kolajen Peptit"
            ],
            [
                "Kargo",
                "Aynı Gün Ücretsiz Sigortalı Kargo"
            ],
            [
                "Tasarruf",
                "260 TL İndirimli Paket"
            ]
        ],
        "recipe_title": "14 Günlük Yenilenme Rutini",
        "recipe_desc": "Güne başlarken 100 ml ılık No. 01 veya No. 02 kemik suyu limonla içilir. Akşam yemeğinden sonra 1 fincan No. 03 Night Story çayı demlenir. 14 günün sonunda sindirim hafifliği ve cilt ışıltısı hissedilir.",
        "recipe_time": "⏱ 14 Günlük Protokol",
        "faq_objections": [
            [
                "Kür sırasında nasıl beslenmeliyim?",
                "Kutunun içinden çıkan 14 günlük kılavuzda inflamasyonu azaltan, gluten ve rafine şekeri kısıtlayan kolay bir beslenme rehberi yer almaktadır."
            ],
            [
                "Kutudaki kavanozlar bozulmadan dayanır mı?",
                "Evet, tüm kavanozlarımız 121°C otoklav kapaklı olduğu için açılmadığı sürece oda sıcaklığında 6 ay taze kalır. Açılan kavanoz ise 48 saatte tüketilir veya buz kalıplarına aktarılır."
            ]
        ]
    }
}


PDP_TEMPLATE = """<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Story of Nature</title>
  <meta name="description" content="{lead}">
  <link rel="canonical" href="https://storyofnature.com.tr/{filename}">
  
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🌿</text></svg>">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <style>
    :root {
      --bg-canvas: #FAF7F2;
      --bg-surface: #ffffff;
      --bg-card: #F3EFE6;
      --color-dark: #14281D;
      --color-dark-hover: #1E3D2C;
      --text-main: #141D17;
      --text-muted: #556258;
      --gold-champagne: #C5A059;
      --gold-hover: #A8833E;
      --gold-tint: #FDFBF7;
      --border-subtle: rgba(20, 40, 29, 0.10);
      --border-gold: rgba(197, 160, 89, 0.35);
      --font-serif: 'Cormorant Garamond', Georgia, serif;
      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --radius-sm: 8px;
      --radius-md: 16px;
      --radius-lg: 24px;
      --shadow-soft: 0 4px 20px rgba(20, 40, 29, 0.05);
      --shadow-float: 0 12px 36px rgba(20, 40, 29, 0.10);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; font-size: 16px; }
    body {
      background-color: var(--bg-canvas);
      color: var(--text-main);
      font-family: var(--font-sans);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }
    a { color: inherit; text-decoration: none; }
    img { display: block; max-width: 100%; height: auto; }

    /* TOP BANNER */
    .top-banner {
      background: var(--color-dark);
      color: #FAF7F2;
      font-size: 0.8rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 0.55rem 1rem;
      text-align: center;
      display: flex;
      justify-content: center;
      gap: 1.5rem;
      font-weight: 500;
      border-bottom: 1px solid var(--border-gold);
    }

    /* HEADER */
    .pdp-header {
      background: rgba(250, 247, 242, 0.95);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-subtle);
      position: sticky;
      top: 0;
      z-index: 100;
      transition: all 0.3s ease;
    }
    .header-inner {
      max-width: 1280px;
      margin: 0 auto;
      padding: 0.9rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .brand-logo {
      font-family: var(--font-serif);
      font-size: 1.65rem;
      font-weight: 700;
      letter-spacing: 0.04em;
      color: var(--color-dark);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .brand-logo span.leaf { color: var(--gold-champagne); }
    .header-nav { display: flex; gap: 1.5rem; align-items: center; font-size: 0.9rem; font-weight: 500; }
    .header-nav a:hover { color: var(--gold-champagne); }
    .btn-menu-trigger {
      background: none;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 0.4rem 0.75rem;
      font-family: var(--font-sans);
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--color-dark);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s ease;
    }
    .btn-menu-trigger:hover { border-color: var(--gold-champagne); background: var(--bg-surface); }

    /* MINI MENU WINDOW POPOVER */
    .mini-menu-window {
      position: absolute;
      top: calc(100% + 8px);
      right: 1.5rem;
      width: 320px;
      background: var(--bg-surface);
      border: 1px solid var(--border-gold);
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-float);
      padding: 1.25rem;
      display: none;
      z-index: 200;
      transition: opacity 0.25s ease, transform 0.25s ease;
    }
    .mini-menu-window.open {
      display: block;
      animation: menuPopIn 0.2s ease forwards;
    }
    @keyframes menuPopIn {
      from { opacity: 0; transform: translateY(-8px) scale(0.98); }
      to { opacity: 1; transform: translateY(0) scale(1); }
    }
    .menu-title {
      font-family: var(--font-serif);
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--color-dark);
      margin-bottom: 0.75rem;
      padding-bottom: 0.5rem;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .menu-links { list-style: none; display: flex; flex-direction: column; gap: 0.4rem; }
    .menu-link-item a {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.45rem 0.6rem;
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      font-weight: 500;
      color: var(--text-main);
      transition: background 0.15s ease;
    }
    .menu-link-item a:hover { background: var(--bg-card); color: var(--gold-hover); }
    .menu-link-item a span.tag {
      font-size: 0.7rem;
      padding: 0.15rem 0.45rem;
      border-radius: 999px;
      background: var(--bg-card);
      color: var(--text-muted);
      font-weight: 600;
    }

    /* BREADCRUMB */
    .breadcrumbs {
      max-width: 1280px;
      margin: 1rem auto 0;
      padding: 0 1.5rem;
      font-size: 0.8rem;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .breadcrumbs a:hover { color: var(--color-dark); text-decoration: underline; }

    /* PDP MAIN CONTAINER */
    .pdp-container {
      max-width: 1280px;
      margin: 1.5rem auto 3rem;
      padding: 0 1.5rem;
      display: grid;
      grid-template-columns: 1.15fr 1fr;
      gap: 3rem;
      align-items: start;
    }
    @media (max-width: 960px) {
      .pdp-container { grid-template-columns: 1fr; gap: 2rem; }
    }

    /* LEFT: HIGH-IMPACT CULINARY GALLERY */
    .gallery-col { position: sticky; top: 5rem; }
    @media (max-width: 960px) { .gallery-col { position: static; } }

    .main-view-box {
      position: relative;
      background: var(--bg-surface);
      border: 1px solid var(--border-gold);
      border-radius: var(--radius-lg);
      overflow: hidden;
      aspect-ratio: 4 / 3.4;
      box-shadow: var(--shadow-soft);
    }
    .main-view-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.4s ease, opacity 0.25s ease;
    }
    .gallery-overlay-badge {
      position: absolute;
      top: 1rem;
      left: 1rem;
      background: rgba(20, 40, 29, 0.88);
      color: #FAF7F2;
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      padding: 0.4rem 0.85rem;
      border-radius: 999px;
      font-size: 0.75rem;
      font-weight: 600;
      letter-spacing: 0.04em;
      border: 1px solid var(--border-gold);
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
      z-index: 2;
    }
    .gallery-slide-caption {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      background: linear-gradient(to top, rgba(20,40,29,0.92) 0%, rgba(20,40,29,0) 100%);
      color: #FAF7F2;
      padding: 2rem 1.25rem 0.85rem;
      font-size: 0.82rem;
      font-weight: 500;
      z-index: 2;
    }

    /* THUMBNAILS */
    .thumbnails-row {
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 0.6rem;
      margin-top: 0.85rem;
    }
    .thumb-btn {
      background: var(--bg-surface);
      border: 2px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      overflow: hidden;
      padding: 0;
      cursor: pointer;
      aspect-ratio: 1;
      position: relative;
      transition: all 0.2s ease;
    }
    .thumb-btn:hover { border-color: var(--gold-champagne); }
    .thumb-btn.active {
      border-color: var(--color-dark);
      box-shadow: 0 0 0 2px var(--gold-champagne);
    }
    .thumb-btn img { width: 100%; height: 100%; object-fit: cover; }
    .thumb-label {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      background: rgba(20, 40, 29, 0.85);
      color: #fff;
      font-size: 0.58rem;
      text-align: center;
      padding: 2px 0;
      font-weight: 600;
    }

    /* RIGHT: BUY BOX & CONVERSION ACCELERATORS */
    .buy-col { display: flex; flex-direction: column; gap: 1.25rem; }

    .category-eyebrow {
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 0.12em;
      color: var(--gold-hover);
      text-transform: uppercase;
    }
    .product-title {
      font-family: var(--font-serif);
      font-size: 2.35rem;
      line-height: 1.15;
      font-weight: 700;
      color: var(--color-dark);
    }
    .product-subtitle {
      font-size: 0.95rem;
      color: var(--text-muted);
      font-weight: 500;
      margin-top: -0.25rem;
    }
    .rating-row {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.85rem;
    }
    .stars { color: #D97706; font-size: 1rem; }
    .review-text { color: var(--text-muted); font-weight: 500; }

    /* PRICE BOX */
    .price-box {
      background: var(--bg-surface);
      border: 1px solid var(--border-gold);
      border-radius: var(--radius-md);
      padding: 1.15rem 1.35rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      box-shadow: var(--shadow-soft);
    }
    .price-current {
      font-family: var(--font-serif);
      font-size: 2.2rem;
      font-weight: 700;
      color: var(--color-dark);
    }
    .price-old {
      font-size: 1.1rem;
      text-decoration: line-through;
      color: var(--text-muted);
      margin-left: 0.5rem;
    }
    .serving-calc {
      font-size: 0.78rem;
      color: var(--text-muted);
      text-align: right;
    }
    .serving-calc strong { color: var(--color-dark); }

    /* GUARANTEE PILLS */
    .guarantees-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 0.65rem;
    }
    .guarantee-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 0.75rem 0.9rem;
      display: flex;
      align-items: center;
      gap: 0.65rem;
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--color-dark);
    }
    .guarantee-card .icon { font-size: 1.25rem; flex-shrink: 0; }

    /* CTA BUTTONS */
    .cta-stack { display: flex; flex-direction: column; gap: 0.65rem; }
    .btn-add-main {
      background: var(--color-dark);
      color: #FAF7F2;
      border: none;
      border-radius: var(--radius-sm);
      padding: 1.1rem 1.5rem;
      font-family: var(--font-sans);
      font-size: 1.05rem;
      font-weight: 700;
      letter-spacing: 0.04em;
      cursor: pointer;
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 0.65rem;
      box-shadow: 0 4px 16px rgba(20, 40, 29, 0.25);
      transition: all 0.2s ease;
    }
    .btn-add-main:hover {
      background: var(--color-dark-hover);
      transform: translateY(-1px);
      box-shadow: 0 6px 20px rgba(20, 40, 29, 0.35);
    }
    .btn-whatsapp-order {
      background: #25D366;
      color: #ffffff;
      border: none;
      border-radius: var(--radius-sm);
      padding: 0.85rem 1.5rem;
      font-size: 0.9rem;
      font-weight: 600;
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 0.5rem;
      cursor: pointer;
      transition: opacity 0.2s ease;
    }
    .btn-whatsapp-order:hover { opacity: 0.92; }

    /* HIGHLIGHTS BULLETS */
    .highlights-box {
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1.25rem;
    }
    .highlights-title {
      font-family: var(--font-serif);
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--color-dark);
      margin-bottom: 0.75rem;
    }
    .highlights-list { list-style: none; display: flex; flex-direction: column; gap: 0.5rem; }
    .highlights-list li {
      font-size: 0.86rem;
      color: var(--text-main);
      display: flex;
      align-items: flex-start;
      gap: 0.5rem;
    }
    .highlights-list li::before {
      content: "✦";
      color: var(--gold-champagne);
      font-weight: bold;
    }

    /* DEEP DIVE TABS */
    .deep-dive-section {
      max-width: 1280px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }
    .pdp-tabs-nav {
      display: flex;
      gap: 1rem;
      border-bottom: 2px solid var(--border-subtle);
      margin-bottom: 1.5rem;
    }
    .pdp-tab-trigger {
      background: none;
      border: none;
      padding: 0.75rem 1.25rem;
      font-family: var(--font-sans);
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      position: relative;
      transition: all 0.2s ease;
    }
    .pdp-tab-trigger:hover { color: var(--color-dark); }
    .pdp-tab-trigger.active {
      color: var(--color-dark);
      font-weight: 700;
    }
    .pdp-tab-trigger.active::after {
      content: "";
      position: absolute;
      bottom: -2px;
      left: 0;
      right: 0;
      height: 3px;
      background: var(--color-dark);
      border-radius: 3px 3px 0 0;
    }
    .pdp-tab-panel { display: none; background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 2rem; }
    .pdp-tab-panel.active { display: block; animation: fadeIn 0.25s ease; }
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

    /* TABLE */
    .specs-table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
    .specs-table tr { border-bottom: 1px solid var(--border-subtle); }
    .specs-table td { padding: 0.85rem 1rem; }
    .specs-table td:first-child { font-weight: 600; color: var(--color-dark); width: 35%; background: var(--bg-card); }

    /* FAQ OBJECTIONS */
    .objections-grid { display: flex; flex-direction: column; gap: 1rem; }
    .objection-item {
      background: var(--bg-card);
      border-left: 4px solid var(--gold-champagne);
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      padding: 1rem 1.25rem;
    }
    .objection-q { font-weight: 700; font-size: 0.95rem; color: var(--color-dark); margin-bottom: 0.35rem; }
    .objection-a { font-size: 0.88rem; color: var(--text-main); line-height: 1.55; }

    /* RECIPE CARD */
    .recipe-showcase {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2rem;
      align-items: center;
    }
    @media (max-width: 768px) { .recipe-showcase { grid-template-columns: 1fr; } }
    .recipe-img { border-radius: var(--radius-md); overflow: hidden; aspect-ratio: 4/3; }
    .recipe-img img { width: 100%; height: 100%; object-fit: cover; }
    .recipe-content h4 { font-family: var(--font-serif); font-size: 1.5rem; color: var(--color-dark); margin-bottom: 0.5rem; }
    .recipe-time-badge {
      display: inline-block;
      background: var(--gold-tint);
      border: 1px solid var(--border-gold);
      color: var(--gold-hover);
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.2rem 0.6rem;
      border-radius: 999px;
      margin-bottom: 0.75rem;
    }

    /* FOOTER */
    .pdp-footer {
      background: var(--color-dark);
      color: #FAF7F2;
      padding: 3rem 1.5rem 2rem;
      margin-top: 4rem;
      border-top: 1px solid var(--border-gold);
    }
    .footer-inner {
      max-width: 1280px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1.5rem;
      font-size: 0.85rem;
      color: rgba(250, 247, 242, 0.7);
    }
  </style>
</head>
<body>

  <!-- TOP BANNER -->
  <div class="top-banner">
    <span>✦ TÜRKİYE GENELİ AYNI GÜN SOĞUK ZIRHLI KARGO</span>
    <span>•</span>
    <span>✦ ACIBADEM SAĞLIK STANDARTLARINDA 28 SAAT DEMLEME</span>
    <span>•</span>
    <span>✦ %100 DOĞAL TAŞ JÖLE GARANTİSİ</span>
  </div>

  <!-- HEADER -->
  <header class="pdp-header">
    <div class="header-inner">
      <a href="index.html" class="brand-logo">
        <span class="leaf">🌿</span> STORY OF NATURE
      </a>
      <div class="header-nav">
        <a href="index.html#urunler">Koleksiyon</a>
        <a href="index.html#felsefe">Felsefemiz</a>
        <a href="index.html#tarifler">Gurme Tarifler</a>
        <button class="btn-menu-trigger" onclick="toggleMiniMenu()">
          <span>Menü & Ürünler</span>
          <span>▾</span>
        </button>
      </div>

      <!-- MINI MENU WINDOW POPOVER -->
      <div class="mini-menu-window" id="miniMenuWindow">
        <div class="menu-title">
          <span>Koleksiyon & Sayfalar</span>
          <span style="cursor:pointer; font-size: 0.9rem;" onclick="toggleMiniMenu()">✕</span>
        </div>
        <ul class="menu-links">
          <li class="menu-link-item"><a href="pure-essence.html"><span>No. 01 Pure Essence Kemik Suyu</span> <span class="tag">Çok Satan</span></a></li>
          <li class="menu-link-item"><a href="golden-immunity.html"><span>No. 02 Golden Immunity Zencefil</span> <span class="tag">Bağışıklık</span></a></li>
          <li class="menu-link-item"><a href="gece-masali.html"><span>No. 03 Night Story Sakinleşme Çayı</span> <span class="tag">Kafeinsiz</span></a></li>
          <li class="menu-link-item"><a href="saf-bebek-kolajeni.html"><span>No. 04 Saf Bebek Kolajeni</span> <span class="tag">0 Tuz</span></a></li>
          <li class="menu-link-item"><a href="rosemary-elixir.html"><span>No. 05 Rosemary Collagen Elixir</span> <span class="tag">Gurme</span></a></li>
          <li class="menu-link-item"><a href="14-gunluk-paket.html"><span>14 Günlük Lüks Yenilenme Kiti</span> <span class="tag">%23 Avantaj</span></a></li>
          <li style="border-top: 1px solid var(--border-subtle); margin-top: 0.4rem; padding-top: 0.4rem;" class="menu-link-item">
            <a href="index.html#tarifler"><span>✦ Gurme Tarif Rehberi</span></a>
          </li>
          <li class="menu-link-item">
            <a href="index.html#acibadem"><span>✦ Acıbadem Klinik Raporu</span></a>
          </li>
        </ul>
      </div>
    </div>
  </header>

  <!-- BREADCRUMBS -->
  <div class="breadcrumbs">
    <a href="index.html">Ana Sayfa</a>
    <span>›</span>
    <a href="index.html#urunler">{category_name}</a>
    <span>›</span>
    <span style="color: var(--color-dark); font-weight: 600;">{title}</span>
  </div>

  <!-- PDP MAIN CONTAINER -->
  <main class="pdp-container">

    <!-- LEFT GALLERY -->
    <div class="gallery-col">
      <div class="main-view-box">
        <span class="gallery-overlay-badge" id="galleryPill">{first_pill}</span>
        <img id="mainImage" src="{first_image}" alt="{title}" fetchpriority="high">
        <div class="gallery-slide-caption" id="galleryCaption">{first_label}</div>
      </div>

      <div class="thumbnails-row">
        {thumbnails_html}
      </div>
    </div>

    <!-- RIGHT BUY BOX -->
    <div class="buy-col">
      <div class="category-eyebrow">{category_eyebrow}</div>
      <h1 class="product-title">{title}</h1>
      <p class="product-subtitle">{subtitle}</p>

      <div class="rating-row">
        <span class="stars">★★★★★</span>
        <span class="review-text"><strong>{rating} / 5.0</strong> ({review_count} Doğrulanmış Müşteri Değerlendirmesi • Acıbadem Standartlarında)</span>
      </div>

      <div class="price-box">
        <div>
          <span class="price-current">{price} TL</span>
          <span class="price-old">{old_price} TL</span>
          <div style="font-size: 0.8rem; color: #166534; font-weight: 600; margin-top: 0.2rem;">✦ 100 TL Üzeri Ücretsiz Soğuk Zincir Kargo</div>
        </div>
        <div class="serving-calc">
          <div><strong>1 Porsiyon = ~35 TL</strong></div>
          <div>1 Kupa Kahveden Daha Ekonomik</div>
        </div>
      </div>

      <p style="font-size: 0.95rem; color: var(--text-main); line-height: 1.6;">
        {lead}
      </p>

      <!-- GUARANTEES GRID -->
      <div class="guarantees-grid">
        <div class="guarantee-card">
          <span class="icon">❄️</span>
          <div>
            <div>Taş Jöle Garantisi</div>
            <div style="font-size: 0.72rem; color: var(--text-muted); font-weight: 400;">Dolapta jöleleşmezse %100 iade</div>
          </div>
        </div>
        <div class="guarantee-card">
          <span class="icon">🌿</span>
          <div>
            <div>Sıfır Ağır Koku</div>
            <div style="font-size: 0.72rem; color: var(--text-muted); font-weight: 400;">Çift ön haşlama ile saf içim</div>
          </div>
        </div>
        <div class="guarantee-card">
          <span class="icon">🛡️</span>
          <div>
            <div>Kırılmaz Zırhlı Kargo</div>
            <div style="font-size: 0.72rem; color: var(--text-muted); font-weight: 400;">Air-column hava yastıklı koli</div>
          </div>
        </div>
        <div class="guarantee-card">
          <span class="icon">🧊</span>
          <div>
            <div>Pratik Buzluk Kullanımı</div>
            <div style="font-size: 0.72rem; color: var(--text-muted); font-weight: 400;">Kalıplarda 6 ay taze saklama</div>
          </div>
        </div>
      </div>

      <!-- CTA ACTIONS -->
      <div class="cta-stack">
        <button class="btn-add-main" onclick="handlePdpAddCart('{title}', {price})">
          <span>🛍️ Sepete Ekle</span>
          <span>•</span>
          <span>{price} TL</span>
        </button>
        <button class="btn-whatsapp-order" onclick="window.open('https://wa.me/905330849027?text=Merhaba,%20Story%20of%20Nature%20{title}%20siparişi%20vermek%20istiyorum.', '_blank')">
          <span>💬 WhatsApp ile Hızlı Sipariş Ver</span>
        </button>
      </div>

      <!-- HIGHLIGHTS -->
      <div class="highlights-box">
        <div class="highlights-title">Neden Story of Nature Zanaatkar Kalitesi?</div>
        <ul class="highlights-list">
          {highlights_html}
        </ul>
      </div>

    </div>

  </main>

  <!-- DEEP DIVE TABS -->
  <section class="deep-dive-section">
    <div class="pdp-tabs-nav">
      <button class="pdp-tab-trigger active" onclick="switchPdpTab(0)">Laboratuvar & Besin Değerleri</button>
      <button class="pdp-tab-trigger" onclick="switchPdpTab(1)">Sık Sorulan Sorular (Şikayetvar & Reddit Yanıtları)</button>
      <button class="pdp-tab-trigger" onclick="switchPdpTab(2)">Gurme Şef Tarifi & Pratik Saklama</button>
    </div>

    <!-- TAB 1: SPECS -->
    <div class="pdp-tab-panel active" id="tabPanel0">
      <h3 style="font-family: var(--font-serif); font-size: 1.5rem; color: var(--color-dark); margin-bottom: 1rem;">
        Doğrulanmış Laboratuvar Analiz Değerleri
      </h3>
      <table class="specs-table">
        <tbody>
          {table_rows_html}
        </tbody>
      </table>
    </div>

    <!-- TAB 2: OBJECTIONS / FAQ -->
    <div class="pdp-tab-panel" id="tabPanel1">
      <h3 style="font-family: var(--font-serif); font-size: 1.5rem; color: var(--color-dark); margin-bottom: 1rem;">
        Tüketicilerin En Çok Merak Ettiği 4 Kritik Soru
      </h3>
      <div class="objections-grid">
        {objections_html}
      </div>
    </div>

    <!-- TAB 3: RECIPES -->
    <div class="pdp-tab-panel" id="tabPanel2">
      <div class="recipe-showcase">
        <div class="recipe-img">
          <img src="assets/photo_03_gourmet_soup.jpg" alt="{recipe_title}" loading="lazy">
        </div>
        <div class="recipe-content">
          <div class="recipe-time-badge">{recipe_time}</div>
          <h4>{recipe_title}</h4>
          <p style="font-size: 0.95rem; color: var(--text-main); margin-bottom: 1rem;">
            {recipe_desc}
          </p>
          <div style="background: var(--bg-card); padding: 0.85rem; border-radius: var(--radius-sm); font-size: 0.82rem; border-left: 3px solid var(--gold-champagne);">
            <strong>💡 Şefin Pratik Saklama İpucu:</strong> Kavanozu açtığınızda kullanmadığınız kısmı buz kalıplarına aktararak dondurunuz. Her yemek, pilav veya bebek püresi için 2 buz küpü ilave ederek 6 ay boyunca taze kullanabilirsiniz.
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="pdp-footer">
    <div class="footer-inner">
      <div>
        <div style="font-family: var(--font-serif); font-size: 1.25rem; font-weight: 700; color: #FAF7F2; margin-bottom: 0.35rem;">
          STORY OF NATURE
        </div>
        <div>Zanaatkar İlikli Kemik Suyu & Fonksiyonel Botanikler • Acıbadem Standartları</div>
      </div>
      <div>
        © 2026 Story of Nature. Tüm hakları saklıdır. Sağlam E-Ticaret ve Doğa Ürünleri.
      </div>
    </div>
  </footer>

  <script>
    const SLIDES = {slides_json};

    function selectThumbnail(index) {
      const slide = SLIDES[index];
      if (!slide) return;
      
      const img = document.getElementById("mainImage");
      const pill = document.getElementById("galleryPill");
      const caption = document.getElementById("galleryCaption");

      img.style.opacity = "0.4";
      setTimeout(() => {
        img.src = slide.src;
        pill.textContent = slide.pill;
        caption.textContent = slide.label;
        img.style.opacity = "1";
      }, 150);

      document.querySelectorAll(".thumb-btn").forEach((btn, idx) => {
        btn.classList.toggle("active", idx === index);
      });
    }

    function switchPdpTab(index) {
      document.querySelectorAll(".pdp-tab-trigger").forEach((btn, idx) => {
        btn.classList.toggle("active", idx === index);
      });
      document.querySelectorAll(".pdp-tab-panel").forEach((panel, idx) => {
        panel.classList.toggle("active", idx === index);
      });
    }

    function toggleMiniMenu() {
      const menu = document.getElementById("miniMenuWindow");
      menu.classList.toggle("open");
    }

    document.addEventListener("click", function(e) {
      const menu = document.getElementById("miniMenuWindow");
      const trigger = document.querySelector(".btn-menu-trigger");
      if (menu && menu.classList.contains("open")) {
        if (!menu.contains(e.target) && !trigger.contains(e.target)) {
          menu.classList.remove("open");
        }
      }
    });

    function handlePdpAddCart(productName, price) {
      alert("✦ " + productName + " (" + price + " TL) sepetinize eklendi!\n\nSiparişinizi tamamlamak için Ana Sayfadaki Sepetim sekmesine geçebilirsiniz.");
    }
  </script>
</body>
</html>
"""

def generate_all():
    print("Generating dedicated PDP pages with unified taxonomy & real culinary photos...")
    for key, p in PRODUCTS.items():
        first_slide = p["slides"][0]
        
        # Build thumbnails
        thumbs_parts = []
        for i, s in enumerate(p["slides"]):
            active_cls = "active" if i == 0 else ""
            thumbs_parts.append(f'''<button class="thumb-btn {active_cls}" onclick="selectThumbnail({i})" title="{s["label"]}">
  <img src="{s["src"]}" alt="{s["thumb"]}" loading="lazy" fetchpriority="low">
  <span class="thumb-label">{s["thumb"]}</span>
</button>''')
        thumbnails_html = "\n".join(thumbs_parts)
        
        # Build highlights
        highlights_html = "\n".join([f"<li>{h}</li>" for h in p["highlights"]])
        
        # Build table rows
        table_rows_html = "\n".join([f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in p["table"]])
        
        # Build objections / FAQs
        objections_parts = []
        for q, a in p.get("faq_objections", []):
            objections_parts.append(f'''<div class="objection-item">
  <div class="objection-q">❓ {q}</div>
  <div class="objection-a">{a}</div>
</div>''')
        objections_html = "\n".join(objections_parts)
        
        html_out = PDP_TEMPLATE
        replacements = {
            "{title}": str(p["title"]),
            "{category_eyebrow}": str(p["category_eyebrow"]),
            "{subtitle}": str(p["subtitle"]),
            "{price}": str(p["price"]),
            "{old_price}": str(p["old_price"]),
            "{vol}": str(p["vol"]),
            "{rating}": str(p["rating"]),
            "{review_count}": str(p["review_count"]),
            "{category_name}": str(p["category_name"]),
            "{lead}": str(p["lead"]),
            "{filename}": str(p["filename"]),
            "{first_image}": str(first_slide["src"]),
            "{first_pill}": str(first_slide["pill"]),
            "{first_label}": str(first_slide["label"]),
            "{thumbnails_html}": str(thumbnails_html),
            "{highlights_html}": str(highlights_html),
            "{table_rows_html}": str(table_rows_html),
            "{objections_html}": str(objections_html),
            "{recipe_title}": str(p["recipe_title"]),
            "{recipe_desc}": str(p["recipe_desc"]),
            "{recipe_time}": str(p["recipe_time"]),
            "{slides_json}": json.dumps(p["slides"], ensure_ascii=False)
        }
        for k, v in replacements.items():
            html_out = html_out.replace(k, v)
        
        out_path = os.path.join(SITE_DIR, p["filename"])
        with open(out_path, "w", encoding="utf-8") as out_f:
            out_f.write(html_out)
        print(f"Generated: {p['filename']} ({len(html_out)} bytes)")

if __name__ == "__main__":
    generate_all()
