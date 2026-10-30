/* Decode before swapping; only the most recent request may update the frame. */
const visualRequests = new WeakMap();
async function setProductVisual(img, src, alt) {
  if (!img) return;
  const request = {};
  visualRequests.set(img, request);
  const next = new Image();
  next.src = src;
  try { await next.decode(); } catch {
    if (visualRequests.get(img) === request) img.style.opacity = '1';
    return;
  }
  if (visualRequests.get(img) !== request) return;
  img.style.opacity = '0.35';
  const delay = matchMedia('(prefers-reduced-motion: reduce)').matches ? 0 : 120;
  setTimeout(() => {
    if (visualRequests.get(img) !== request) return;
    img.src = src;
    img.alt = alt;
    img.style.opacity = '1';
  }, delay);
}
function switchStageVisual(mode) {
  const liquid = mode === 'liquid';
  setProductVisual(document.getElementById('stageImage'), liquid ? 'assets/photo_01_morning_pour.jpg' : 'assets/hero_collagen_jelly.jpg', liquid ? 'Isıtılmış berrak kemik suyunun fincana dökülüşü' : 'Soğuk kemik suyunun kaşıkla alınan jöle dokusu');
  for (const [id, active] of [['tabLiquid', liquid], ['tabJelly', !liquid]]) {
    const button = document.getElementById(id);
    button.classList.toggle('active', active);
    button.setAttribute('aria-pressed', String(active));
  }
  document.getElementById('stagePhotoText').textContent = liquid ? '60°C · Sıvı Altın' : '+4°C · Taş Jöle';
  document.getElementById('stageInfoDesc').textContent = liquid ? 'Nazikçe ısıtıldığında jöle dokusu çözülür. Fincanda yudumlamak veya yemeklere eklemek için akışkan bir kıvam alır.' : 'Buzdolabında dinlenen kemik suyu, kaşıkla alınabilen jöle dokusuna dönüşür.';
}
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.card-tab-btn, .thumb-btn').forEach(button => button.setAttribute('aria-pressed', String(button.classList.contains('active'))));
});
