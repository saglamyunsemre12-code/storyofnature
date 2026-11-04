(() => {
  const section = document.getElementById('nature-grove');
  if (!section || !Element.prototype.animate) return;

  const play = section.querySelector('.grove-play');
  const photo = section.querySelector('.grove-photo');
  const light = section.querySelector('.grove-light');
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
  let scene = [];

  function pause() {
    if (scene[0]?.playState !== 'running') return;
    scene.forEach(animation => animation.pause());
    play.textContent = 'Devam et';
  }

  function reset() {
    scene.forEach(animation => animation.cancel());
    scene = [];
    play.hidden = reducedMotion.matches;
    play.textContent = 'Sahneyi oynat';
  }

  play.addEventListener('click', () => {
    if (reducedMotion.matches) return;
    if (scene[0]?.playState === 'running') {
      pause();
      return;
    }
    if (scene[0]?.playState === 'paused') {
      scene.forEach(animation => animation.play());
    } else {
      scene.forEach(animation => animation.cancel());
      const timing = { duration: 6800, easing: 'ease-in-out', fill: 'forwards' };
      const camera = photo.animate([
        { transform: 'scale(1)' },
        { transform: 'scale(1.07) translateX(-1%)' }
      ], timing);
      const daylight = light.animate([{ opacity: 0 }, { opacity: .9 }, { opacity: .35 }], timing);
      camera.onfinish = () => { play.textContent = 'Yeniden izle'; };
      scene = [camera, daylight];
    }
    play.textContent = 'Duraklat';
  });

  if ('IntersectionObserver' in window) {
    new IntersectionObserver(([entry]) => {
      if (!entry.isIntersecting) pause();
    }).observe(section);
  }
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) pause();
  });
  reducedMotion.addEventListener('change', reset);
  reset();
})();
