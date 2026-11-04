(() => {
  const section = document.getElementById('nature-grove');
  if (!section || !Element.prototype.animate) return;

  const play = section.querySelector('.grove-play');
  const frames = [...section.querySelectorAll('[data-grove-chapter]')];
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  let timeline = [];

  function pause() {
    if (timeline.at(-2)?.playState !== 'running') return;
    timeline.filter(animation => animation.playState === 'running').forEach(animation => animation.pause());
    play.textContent = 'Devam et';
  }

  function start() {
    timeline.forEach(animation => animation.cancel());
    const chapterLength = 3000;
    const startTime = document.timeline.currentTime;
    timeline = frames.map((frame, index) => {
      frame.hidden = false;
      const reveal = frame.animate([{ opacity: 0 }, { opacity: 1 }], {
        delay: index * chapterLength,
        duration: index ? 650 : 0,
        fill: 'both'
      });
      const camera = frame.querySelector('img').animate(
        [{ transform: 'scale(1)' }, { transform: 'scale(1.045)' }],
        { delay: index * chapterLength, duration: chapterLength, fill: 'both' }
      );
      reveal.startTime = camera.startTime = startTime;
      return [camera, reveal];
    }).flat();
    const end = timeline.at(-2);
    end.onfinish = () => { play.textContent = 'Yeniden izle'; };
  }

  play.hidden = false;
  play.addEventListener('click', () => {
    if (motion.matches) {
      const current = frames.findIndex(frame => !frame.hidden);
      const next = (current + 1) % frames.length;
      frames.forEach((frame, index) => { frame.hidden = index !== next; });
      play.textContent = next === frames.length - 1 ? 'Başa dön' : 'Sonraki sahne';
      return;
    }
    const status = timeline.at(-2)?.playState;
    if (status === 'running') {
      pause();
      return;
    }
    if (status === 'paused') timeline.filter(animation => animation.playState === 'paused').forEach(animation => animation.play());
    else start();
    play.textContent = 'Duraklat';
  });

  function reset() {
    timeline.forEach(animation => animation.cancel());
    timeline = [];
    frames.forEach((frame, index) => { frame.hidden = index !== 0; });
    play.textContent = motion.matches ? 'Sonraki sahne' : 'Hikâyeyi izle';
  }
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(([entry]) => {
      if (!entry.isIntersecting) pause();
    }).observe(section);
  }
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) pause();
  });
  motion.addEventListener('change', reset);
  reset();
})();
