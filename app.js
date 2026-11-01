const money = n => n.toLocaleString('tr-TR') + ' TL';
const $ = s => document.querySelector(s);

let cart = {};
try {
  const saved = JSON.parse(localStorage.getItem('nature-quote-v2') || '{}');
  for (const p of products) {
    if (Number.isInteger(saved[p.id]) && saved[p.id] > 0) {
      cart[p.id] = Math.min(99, saved[p.id]);
    }
  }
} catch {}

let toastTimer;
function notify(message) {
  const t = $('#toast');
  if (!t) return;
  t.textContent = message;
  t.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => t.classList.remove('show'), 2800);
}

function spawnSproutParticle(btn, label = '🌱 +1 Fidan Filizlendi!') {
  if (!btn) return;
  btn.classList.add('added-pulse');
  const origHTML = btn.dataset.origHtml || btn.innerHTML;
  if (!btn.dataset.origHtml) btn.dataset.origHtml = origHTML;
  btn.innerHTML = '✓ Listeye Eklendi 🌱';
  setTimeout(() => {
    btn.classList.remove('added-pulse');
    if (btn.dataset.origHtml) btn.innerHTML = btn.dataset.origHtml;
  }, 1200);

  try {
    const r = btn.getBoundingClientRect();
    const el = document.createElement('div');
    el.className = 'sprout-float-particle';
    el.textContent = label;
    el.style.left = (r.left + r.width / 2) + 'px';
    el.style.top = r.top + 'px';
    document.body.appendChild(el);
    setTimeout(() => el.remove(), 1300);
  } catch {}
}

function update() {
  let count = 0;
  for (const p of products) count += cart[p.id] || 0;
  if ($('#count')) $('#count').textContent = count;

  const total = products.reduce((sum, p) => sum + (cart[p.id] || 0) * p.estimatedPrice, 0);
  if ($('#cart-total')) $('#cart-total').textContent = money(total);

  // 1 Order / Items = Tree Counter
  const treesCount = Math.max(1, count > 0 ? Math.ceil(count / 2) : 1);
  if ($('#header-tree-count')) $('#header-tree-count').textContent = treesCount;
  if ($('#tree-tracker-fill')) $('#tree-tracker-fill').style.width = '100%';
  if ($('#tree-tracker-pct')) $('#tree-tracker-pct').textContent = `🌱 ${treesCount} Fidan`;
  if ($('#tree-tracker-text')) {
    $('#tree-tracker-text').textContent = count > 0
      ? `Seçkinle doğaya ${treesCount} fidan izi bırakıyorsun`
      : 'Her alışveriş doğaya 1 fidan izi bırakır';
  }
  if ($('#tree-live-status')) {
    $('#tree-live-status').innerHTML = count > 0
      ? `🪐 Harika! Şu an listendeki <strong>${count} ürün</strong> ile Gezegen B-612’de <strong>${treesCount} fidan ve gül</strong> çiçek açmaya hazır.`
      : '🪐 Şu an listendeki seçkinle <strong>1 fidan ve 1 gül</strong> Gezegen B-612’de çiçek açmaya hazır (Planlanan doğa programı).';
  }

  // Cart items
  if ($('#cart-items')) {
    $('#cart-items').innerHTML = count
      ? products.filter(p => cart[p.id]).map(p => `<div class="cart-row">
          <a href="${p.pageUrl}"><img src="assets/${p.image}" alt="${p.series}, temsili sunum" width="65" height="75"></a>
          <div>
            <h3><a href="${p.pageUrl}">${p.series}</a></h3>
            <p>${p.variant}</p>
            <p class="cart-item-price">${p.priceBasis} · Yaklaşık ${money(p.estimatedPrice)} / adet</p>
            <div class="quantity">
              <button type="button" data-change="${p.id}" data-delta="-1" aria-label="${p.name} azalt">−</button>
              <span>${cart[p.id]}</span>
              <button type="button" data-change="${p.id}" data-delta="1" aria-label="${p.name} artır">+</button>
            </div>
          </div>
          <button type="button" class="remove" data-remove="${p.id}" aria-label="${p.name} listeden çıkar">Çıkar</button>
        </div>`).join('')
      : '<p style="padding:36px 0">Listen henüz boş.<br>Koleksiyondan veya özel kraft kutulardan seçim yaparak başlayabilirsin.</p>';
  }

  // Complementary Ritual Upsell
  const upsellBox = $('#cart-upsell');
  if (upsellBox) {
    let candidate = null;
    if (count > 0) {
      const hasBroth = products.some(p => p.family === 'kemik' && cart[p.id]);
      const hasTea = products.some(p => p.family === 'cay' && cart[p.id]);
      const hasGranola = products.some(p => p.family === 'granola' && cart[p.id]);
      if (hasBroth && !hasTea) candidate = products.find(p => p.id === 'cay--papatya-melisa');
      else if (!hasGranola) candidate = products.find(p => p.id === 'granola--findik-kakao');
      else if (!cart['icecek--orman-meyveleri']) candidate = products.find(p => p.id === 'icecek--orman-meyveleri');
    }
    if (candidate) {
      upsellBox.hidden = false;
      upsellBox.innerHTML = `<p class="cart-upsell-head">SOFRANI TAMAMLA</p>
        <div class="cart-upsell-row">
          <div><strong><a href="${candidate.pageUrl}">${candidate.variant}</a></strong><span>${candidate.series} · Yaklaşık ${money(candidate.estimatedPrice)}</span></div>
          <button type="button" data-add="${candidate.id}">Listeye ekle +</button>
        </div>`;
    } else {
      upsellBox.hidden = true;
      upsellBox.innerHTML = '';
    }
  }

  const message = 'Merhaba, Story of Nature ürünleri için fiyat teklifi almak istiyorum:\n' +
    products.filter(p => cart[p.id]).map(p => `${cart[p.id]} × ${p.name}`).join('\n') +
    '\nTahmini ürün toplamı: ' + money(total) + ' (kargo hariç; nihai fiyat teyidi rica ederim).\n🌱 Doğa izi: ' + treesCount + ' fidan.\nGüncel fiyat, üretim uygunluğu, tam içerik, alerjen, ambalaj ve teslimat bilgilerini paylaşabilir misiniz?';

  if ($('#checkout')) {
    $('#checkout').href = 'https://wa.me/905330849027?text=' + encodeURIComponent(message);
    $('#checkout').hidden = !count;
    $('#checkout').style.display = count ? 'flex' : 'none';
  }
  if ($('#cart-clear')) {
    $('#cart-clear').hidden = !count;
    $('#cart-clear').style.display = count ? 'block' : 'none';
  }

  try {
    localStorage.setItem('nature-quote-v2', JSON.stringify(cart));
  } catch {}
}

function add(id, qty = 1, silent = false) {
  const p = products.find(p => p.id === id);
  if (!p) return;
  cart[id] = Math.min(99, (cart[id] || 0) + qty);
  update();
  if (!silent) notify(`🌱 ${p.variant} teklif listene eklendi (+1 Fidan İzi)`);
}

function addSet(id) {
  const set = catalog.sets.find(s => s.id === id);
  if (!set) return;
  for (const [item, qty] of set.items) add(item, qty, true);
  notify(`🌳 ${set.name} teklif listene eklendi!`);
}

function quick(id, selected) {
  const f = catalog.families.find(f => f.id === id);
  if (!f) return;
  const v = f.variants.find(v => v.id === selected) || f.variants[0];
  $('#detail-content').innerHTML = `<img id="quick-image" src="assets/${v.image || f.image}" alt="${f.name} · ${v.name}, temsili sunum" width="1448" height="1086">
    <div>
      <p class="eyebrow">${f.name} · 🌱 1 Fidan İzi</p>
      <h2 id="quick-title">${v.name}</h2>
      <p id="quick-note">${v.note}</p>
      <p id="quick-aroma" class="quick-aroma">${v.aroma} · ${v.pair}</p>
      <p id="quick-price" class="quick-price">Yaklaşık <strong>${money(v.estimatedPrice)}</strong> / ${v.priceBasis}</p>
      <label class="quick-label">Aynı seriden başka bir lezzet
        <select id="quick-variant">${f.variants.map(x => `<option value="${f.id}--${x.id}" ${x.id === v.id ? 'selected' : ''}>${x.name} (${money(x.estimatedPrice)})</option>`).join('')}</select>
      </label>
      <a id="quick-link" class="text-link quick-link" href="${v.pageUrl}">Bu ürünün kendi özel sayfasına git ↗</a>
      <button type="button" class="button" id="quick-add">Bu çeşidi listeme ekle +</button>
      <p class="image-disclosure quick-note">Görsel temsili sunumdur. Tam içerik, gramaj ve fiyat teklif sırasında paylaşılır.</p>
    </div>`;

  $('#quick-variant').onchange = () => {
    const chosen = f.variants.find(x => f.id + '--' + x.id === $('#quick-variant').value);
    $('#quick-title').textContent = chosen.name;
    $('#quick-note').textContent = chosen.note;
    $('#quick-aroma').textContent = chosen.aroma + ' · ' + chosen.pair;
    $('#quick-price').innerHTML = 'Yaklaşık <strong>' + money(chosen.estimatedPrice) + '</strong> / ' + chosen.priceBasis;
    $('#quick-link').href = chosen.pageUrl;
    replaceImage($('#quick-image'), 'assets/' + (chosen.image || f.image), f.name + ' · ' + chosen.name + ', temsili sunum');
  };
  $('#detail').showModal();
}

let selectedFilter = 'all';
const searchTerm = s => s.toLocaleLowerCase('tr').normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/ı/g, 'i');

function filterCatalog() {
  const container = $('#products');
  if (!container) return;
  const term = searchTerm($('#catalog-search')?.value.trim() || '');
  const sort = $('#catalog-sort')?.value || 'curated';
  const cards = [...container.querySelectorAll('[data-product-card]')];
  let total = 0;

  for (const card of cards) {
    card.hidden = (selectedFilter !== 'all' && card.dataset.productCard !== selectedFilter) || !searchTerm(card.dataset.search).includes(term);
    if (!card.hidden) total++;
  }

  cards.sort((a, b) => {
    if (sort === 'name') return a.dataset.name.localeCompare(b.dataset.name, 'tr');
    if (sort === 'price-asc') return Number(a.dataset.price) - Number(b.dataset.price);
    if (sort === 'price-desc') return Number(b.dataset.price) - Number(a.dataset.price);
    if (sort === 'family') return a.dataset.productCard.localeCompare(b.dataset.productCard, 'tr') || Number(a.dataset.order) - Number(b.dataset.order);
    return Number(a.dataset.order) - Number(b.dataset.order);
  }).forEach(card => container.appendChild(card));

  document.querySelectorAll('[data-family-card]').forEach(x => {
    x.hidden = selectedFilter !== 'all' && x.dataset.familyCard !== selectedFilter;
  });
  if ($('#catalog-count')) $('#catalog-count').textContent = total + ' ana başlık gösteriliyor';
  if ($('#catalog-empty')) $('#catalog-empty').hidden = total > 0;
  if ($('#koleksiyon')) $('#koleksiyon').setAttribute('data-active-theme', selectedFilter);
}

function setFilter(value) {
  selectedFilter = value;
  document.querySelectorAll('[data-filter]').forEach(x => {
    const active = x.dataset.filter === value;
    x.classList.toggle('active', active);
    x.setAttribute('aria-pressed', String(active));
  });
  filterCatalog();
}

if ($('#catalog-search')) $('#catalog-search').addEventListener('input', filterCatalog);
if ($('#catalog-sort')) $('#catalog-sort').addEventListener('change', filterCatalog);
if ($('#catalog-reset')) {
  $('#catalog-reset').onclick = () => {
    if ($('#catalog-search')) $('#catalog-search').value = '';
    if ($('#catalog-sort')) $('#catalog-sort').value = 'curated';
    setFilter('all');
  };
}

// Interactive Tree Growth Stages (Küçük Prens — Asteroid B-612)
const treeStageNames = {
  1: '🪐 1. Aşama · Gezegen B-612’de Cam Fanus Altında Tohum',
  2: '🌱 2. Aşama · Cam Fanus Kalkıyor & İlk Filiz Uyanıyor',
  3: '🌧️ 3. Aşama · Yıldız Yağmuruyla Kök Salan Fidan & Gül Goncası',
  4: '🌹 4. Aşama · Gezegen B-612’de Ağaç ve Gül Çiçek Açtı'
};

function setTreeStage(stage, withWater = false) {
  const card = $('#tree-interactive-card');
  if (!card) return;
  const s = Math.max(1, Math.min(4, Number(stage) || 4));
  card.setAttribute('data-tree-stage', String(s));
  if ($('#tree-stage-label')) $('#tree-stage-label').textContent = treeStageNames[s];
  document.querySelectorAll('.tree-step-btn').forEach(btn => {
    btn.classList.toggle('active', Number(btn.dataset.treeStep) === s);
  });
  if (withWater && $('#water-drops')) {
    const drops = $('#water-drops');
    drops.classList.remove('watering');
    void drops.offsetWidth;
    drops.classList.add('watering');
  }
}

// Interactive 4-Step Chronology Tabs
const chronoSteps = [
  {
    badge: 'ADIM 01 / HAMMADDE SEÇİMİ',
    title: 'Mevsiminde toplanan botanikler, özenle seçilen kemik, meyve ve kuruyemişler.',
    desc: 'Kemik sularında ve bebek ek gıda serisinde ilikli kemikler, tatlı kök sebzeler ve yumuşak meyveler; çay ve içeceklerde bütün yapraklar; ezme ve granolalarda ise kavurma profili dengelenmiş kuruyemişler kullanılır.',
    m1: ['7 Ana Başlık', 'Bebek & Ek Gıda dahil bütünlüklü aile'],
    m2: ['34 Özel Sayfa', 'Her ürün için şeffaf içerik kartı']
  },
  {
    badge: 'ADIM 02 / AĞIR ATEŞ & HARMAN',
    title: 'Uzun süreli kaynatma, düşük ısıda fırınlama ve dengeli harmanlama.',
    desc: 'İlikli kemik suları kısık ateşte uzun süre kaynatılarak aromatik sebze ve baharatlarla buluşturulur. Bebek püreleri pürüzsüz dokuda hazırlanır; granolalar kıtır dokusunu koruyacak şekilde fırınlanır.',
    m1: ['Ağır Ateş', 'Geleneksel mutfak temposu'],
    m2: ['34 Lezzet', 'Her damak tadına uygun çeşitlilik']
  },
  {
    badge: 'ADIM 03 / DOĞAL KIVAM & DOKU',
    title: 'Soğukta doğal jel, fincanda berrak içim, kaşıkta yoğun kıvam.',
    desc: 'Ürünlerin dokusu katkı maddeleriyle değil, kullanılan malzemenin kendi doğasıyla şekillenir. Kemik suyu soğukta jelimsi bir yapı alırken, sıcak suda çözünen meyveli içecekler ferah veya ısıtan bir fincana dönüşür.',
    m1: ['+4°C / +75°C', 'İki farklı doğal kullanım hali'],
    m2: ['Doğal Doku', 'Temsili değil, malzemenin kendi özü']
  },
  {
    badge: 'ADIM 04 / CAM KAVANOZ & KRAFT KORUMA',
    title: 'Cam kavanozlarda tazelik, pencereli kraft poşetlerde doğal sunum.',
    desc: 'Sıvı, püre ve sürülebilir ürünler cam kavanozlarda; bitki çayları, meyveli içecekler, kaşık karışımı ve granolalar ise içeriği gösteren pencereli doğal kraft ambalajlarda ve özel kraft hediye kutularında sofrana ulaşır.',
    m1: ['Cam & Kraft', 'Ürünün yapısına uygun ambalaj'],
    m2: ['Özel Kutular', '6 hazır kraft kutu veya kişisel seçki']
  }
];

// Standalone PDP Quantity State
let pdpQty = 1;
const standaloneSection = $('[data-standalone-product]');
function updateStandaloneQty(delta) {
  if (!standaloneSection) return;
  pdpQty = Math.max(1, Math.min(99, pdpQty + delta));
  if ($('#pdp-qty-val')) $('#pdp-qty-val').textContent = pdpQty;
  const unitPrice = Number(standaloneSection.dataset.unitPrice) || 0;
  const basis = standaloneSection.dataset.unitBasis || '';
  const fullName = standaloneSection.dataset.fullName || '';
  const total = unitPrice * pdpQty;
  if ($('#pdp-live-price')) $('#pdp-live-price').textContent = money(total);
  if ($('#pdp-wa-direct')) {
    const text = `Merhaba, Story of Nature "${fullName}" (${pdpQty} adet, yaklaşık ${money(total)} / ${basis}) ürünü için güncel fiyat, içerik ve teslimat bilgisi almak istiyorum.`;
    $('#pdp-wa-direct').href = 'https://wa.me/905330849027?text=' + encodeURIComponent(text);
  }
}

document.addEventListener('click', e => {
  const b = e.target.closest('button');
  if (!b) return;

  if (b.dataset.add) {
    spawnSproutParticle(b);
    add(b.dataset.add);
  }
  if (b.dataset.addCustom) {
    spawnSproutParticle(b, `🌱 +${pdpQty} Ürün Listene Eklendi!`);
    add(b.dataset.addCustom, pdpQty);
  }
  if (b.dataset.set) {
    spawnSproutParticle(b, '🌳 Kutu Listene Eklendi!');
    addSet(b.dataset.set);
  }
  if (b.dataset.openCart) {
    $('#cart').showModal();
  }
  if (b.dataset.familyDetail) quick(b.dataset.familyDetail);
  if (b.dataset.productDetail) {
    const [family, variant] = b.dataset.productDetail.split('--');
    quick(family, variant);
  }
  if (b.id === 'quick-add') {
    spawnSproutParticle(b);
    add($('#quick-variant').value);
  }
  if (b.id === 'cart-clear') {
    cart = {};
    update();
    notify('Teklif listen temizlendi');
  }
  if (b.id === 'pdp-qty-minus') updateStandaloneQty(-1);
  if (b.id === 'pdp-qty-plus') updateStandaloneQty(1);

  if (b.classList.contains('pdp-thumb')) {
    document.querySelectorAll('.pdp-thumb').forEach(t => t.classList.toggle('active', t === b));
    if ($('#standalone-main-img')) {
      replaceImage($('#standalone-main-img'), b.dataset.thumbSrc, b.dataset.thumbAlt || '');
    }
  }

  if (b.classList.contains('pdp-tab-btn')) {
    const tabIdx = b.dataset.pdpTab;
    document.querySelectorAll('.pdp-tab-btn').forEach(t => {
      const active = t === b;
      t.classList.toggle('active', active);
      t.setAttribute('aria-selected', String(active));
    });
    for (let i = 0; i < 4; i++) {
      const panel = $('#pdp-tab-' + i);
      if (panel) panel.hidden = String(i) !== String(tabIdx);
    }
  }

  if (b.classList.contains('tree-step-btn')) {
    setTreeStage(Number(b.dataset.treeStep), true);
  }
  if (b.id === 'water-tree-btn') {
    const card = $('#tree-interactive-card');
    const cur = Number(card?.getAttribute('data-tree-stage') || 3);
    const next = cur >= 4 ? 1 : cur + 1;
    setTreeStage(next === 1 ? 2 : next, true);
    spawnSproutParticle(b, '💧 Can Suyu Verildi · Fidan Büyüyor! 🌱');
  }

  if (b.dataset.close) $('#' + b.dataset.close).close();
  if (b.dataset.change) {
    const id = b.dataset.change;
    cart[id] = Math.min(99, (cart[id] || 0) + Number(b.dataset.delta));
    if (cart[id] <= 0) delete cart[id];
    update();
  }
  if (b.dataset.remove) {
    delete cart[b.dataset.remove];
    update();
  }
  if (b.dataset.filter) setFilter(b.dataset.filter);

  if (b.classList.contains('chrono-tab')) {
    const idx = Number(b.dataset.step);
    const step = chronoSteps[idx];
    if (!step) return;
    document.querySelectorAll('.chrono-tab').forEach(t => {
      const active = t === b;
      t.classList.toggle('active', active);
      t.setAttribute('aria-selected', String(active));
    });
    $('#chrono-badge').textContent = step.badge;
    $('#chrono-title').textContent = step.title;
    $('#chrono-desc').textContent = step.desc;
    $('#chrono-metrics').innerHTML = `<div><strong>${step.m1[0]}</strong><span>${step.m1[1]}</span></div><div><strong>${step.m2[0]}</strong><span>${step.m2[1]}</span></div>`;
  }
});

if ($('#cart-open')) $('#cart-open').onclick = () => $('#cart').showModal();

for (const d of document.querySelectorAll('dialog')) {
  d.addEventListener('click', e => {
    if (e.target === d) {
      const r = d.getBoundingClientRect();
      if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) d.close();
    }
  });
}

const imageRequests = new WeakMap();
async function replaceImage(img, src, alt) {
  const request = { src };
  imageRequests.set(img, request);
  const next = new Image();
  next.src = src;
  try {
    await next.decode();
    if (imageRequests.get(img)!== request) return;
    img.src = src;
    img.alt = alt;
    img.animate([{ opacity: 0.35, transform: 'scale(1.015)' }, { opacity: 1, transform: 'scale(1)' }], { duration: 300, easing: 'ease-out' });
  } catch {
    if (imageRequests.get(img) === request) notify('Görsel yüklenemedi. Lütfen yeniden dene.');
  }
}

function texture(warm) {
  $('#cold').classList.toggle('active', !warm);
  $('#warm').classList.toggle('active', warm);
  $('#cold').setAttribute('aria-pressed', String(!warm));
  $('#warm').setAttribute('aria-pressed', String(warm));
  replaceImage(
    $('#texture-image'),
    'assets/' + (warm ? 'hero-real.jpg' : 'gel-real.jpg'),
    warm ? 'Sıcak kemik suyunun normal sıvı akışı, temsili sunum' : 'Soğuk kemik suyunun yumuşak jel dokusu, temsili sunum'
  );
  $('#texture-note').textContent = warm
    ? '+75°C sıcak sunumda jel çözülür; kemik suyu fincanda veya tariflerde akışkan sıvı haline dönüşür.'
    : '+4°C buzdolabı sıcaklığında doğal jel kıvamı; yoğunluk tarife ve süzmeye göre değişebilir.';
}

if ($('#cold')) {
  $('#cold').onclick = () => texture(false);
  $('#warm').onclick = () => texture(true);
}

if ($('#year')) $('#year').textContent = new Date().getFullYear();
update();

document.querySelectorAll('.nav-menu').forEach(m => {
  document.addEventListener('click', e => {
    if (!m.contains(e.target)) m.open = false;
  });
  m.addEventListener('keydown', e => {
    if (e.key === 'Escape') m.open = false;
  });
});

const page = $('[data-family-page]');
if (page) {
  const family = catalog.families.find(f => f.id === page.dataset.familyPage);
  function selectVariant(id) {
    const v = family.variants.find(v => v.id === id) || family.variants[0];
    const radio = page.querySelector(`input[value="${v.id}"]`);
    if (radio) radio.checked = true;
    $('#selected-name').textContent = v.name;
    $('#selected-note').textContent = v.note;
    if ($('#selected-price')) $('#selected-price').textContent = money(v.estimatedPrice) + ' / ' + v.priceBasis;
    if ($('#selected-page-link')) $('#selected-page-link').href = v.pageUrl;
    $('#add-selected').dataset.add = family.id + '--' + v.id;
    replaceImage($('#pdp-image'), 'assets/' + (v.image || family.image), family.name + ' · ' + v.name + ', temsili ürün sunumu');
  }
  page.addEventListener('change', e => {
    if (e.target.name === 'lezzet') {
      selectVariant(e.target.value);
      history.replaceState(null, '', '#' + e.target.value);
    }
  });
  window.addEventListener('hashchange', () => selectVariant(location.hash.slice(1)));
  selectVariant(location.hash.slice(1));
}

if ($('#set-builder')) {
  const familySelect = $('#builder-family');
  const populateBuilderVariants = (selectedVarId) => {
    const f = catalog.families.find(f => f.id === familySelect.value);
    $('#builder-variant').innerHTML = f.variants.map(v => `<option value="${v.id}" ${v.id === selectedVarId ? 'selected' : ''}>${v.name} (${money(v.estimatedPrice)})</option>`).join('');
  };
  familySelect.onchange = () => populateBuilderVariants();

  // Check URL ?preselect=family--variant
  try {
    const params = new URLSearchParams(location.search);
    const pre = params.get('preselect');
    if (pre && pre.includes('--')) {
      const [pf, pv] = pre.split('--');
      if (catalog.families.some(f => f.id === pf)) {
        familySelect.value = pf;
        populateBuilderVariants(pv);
      }
    }
  } catch {}

  $('#set-builder').onsubmit = e => {
    e.preventDefault();
    const qty = Number($('#builder-quantity').value);
    if (!Number.isInteger(qty) || qty < 1 || qty > 99) return;
    const btn = $('#set-builder button[type="submit"]');
    spawnSproutParticle(btn, `🌱 +${qty} Ürün Kutuna Eklendi!`);
    add(familySelect.value + '--' + $('#builder-variant').value, qty);
  };
  $('#builder-review').onclick = () => $('#cart').showModal();
}

if ($('#bulk-form')) {
  $('#bulk-form').onsubmit = e => {
    e.preventDefault();
    const form = e.currentTarget;
    const data = new FormData(form);
    const groups = data.getAll('groups');
    if (!groups.length) {
      $('#bulk-error').textContent = 'Lütfen en az bir ürün grubu seç.';
      return;
    }
    $('#bulk-error').textContent = '';
    const msg = 'Merhaba, Story of Nature için toplu teklif almak istiyorum.\nKullanım alanı: ' + data.get('business') +
      '\nÜrün grupları: ' + groups.join(', ') +
      '\nYaklaşık adet: ' + data.get('quantity') +
      '\nTeslimat şehri: ' + data.get('city') +
      '\nNotlar: ' + (data.get('notes') || '—') +
      '\nGüncel fiyat, tam içerik, üretim uygunluğu ve teslimat seçeneklerini paylaşabilir misiniz?';
    $('#bulk-summary').textContent = msg;
    $('#bulk-send').href = 'https://wa.me/905330849027?text=' + encodeURIComponent(msg);
    $('#bulk-preview').hidden = false;
  };
}

if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        observer.unobserve(entry.target);
      }
    }
  }, { threshold: 0.08 });
  document.querySelectorAll('.section-title,.store-card,.moment-card,.selection-copy,.texture>div,.bulk-band>div,.flavor-card,.set-card,.chronology-panel,.tree-stage-card').forEach(el => {
    el.classList.add('scroll-reveal');
    observer.observe(el);
  });
}
