(() => {
  'use strict';

  document.querySelectorAll('[data-research-carousel]').forEach((carousel) => {
    const slides = Array.from(carousel.querySelectorAll('.research-carousel-slide'));
    if (slides.length < 2) return;

    const controls = carousel.querySelector('.research-carousel-controls');
    const imageLink = carousel.querySelector('.research-card-image');
    const counter = carousel.querySelector('[data-carousel-count]');
    const caption = carousel.querySelector('[data-carousel-caption]');
    const captions = Array.from(carousel.querySelectorAll('[data-carousel-caption-slide]'));
    const toggle = carousel.querySelector('[data-carousel-toggle]');
    const title = carousel.getAttribute('aria-label').replace(/ images$/, '');
    const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
    const interval = Number(carousel.dataset.interval) || 2000;
    let index = 0;
    let timer = null;
    let hovered = false;
    let focused = false;
    let inView = !('IntersectionObserver' in window);
    let paused = true;

    function show(nextIndex) {
      index = (nextIndex + slides.length) % slides.length;
      slides.forEach((slide, slideIndex) => {
        slide.hidden = slideIndex !== index;
      });
      captions.forEach((slide, slideIndex) => {
        slide.hidden = slideIndex !== index;
      });
      counter.textContent = `${index + 1}/${slides.length}`;
      carousel.dataset.carouselIndex = String(index);
    }

    function syncTimer() {
      window.clearInterval(timer);
      timer = null;
      const playing = inView && !paused && !hovered && !focused && !document.hidden;
      carousel.dataset.carouselPlaying = String(playing);
      if (playing) timer = window.setInterval(() => show(index + 1), interval);
    }

    function syncToggle() {
      carousel.dataset.carouselPaused = String(paused);
      counter.setAttribute('aria-live', paused ? 'polite' : 'off');
      if (caption) caption.setAttribute('aria-live', paused ? 'polite' : 'off');
      toggle.setAttribute('aria-label', `${paused ? 'Play' : 'Pause'} image rotation in ${title}`);
      toggle.title = paused ? 'Play' : 'Pause';
      toggle.querySelector('span').textContent = paused ? '▶' : 'Ⅱ';
      syncTimer();
    }

    function step(direction) {
      show(index + direction);
      syncTimer();
    }

    carousel.querySelector('[data-carousel-previous]').addEventListener('click', () => step(-1));
    carousel.querySelector('[data-carousel-next]').addEventListener('click', () => step(1));
    toggle.addEventListener('click', () => {
      paused = !paused;
      syncToggle();
    });
    carousel.addEventListener('keydown', (event) => {
      if (event.key !== 'ArrowLeft' && event.key !== 'ArrowRight') return;
      event.preventDefault();
      step(event.key === 'ArrowLeft' ? -1 : 1);
    });
    imageLink.addEventListener('pointerenter', (event) => {
      if (event.pointerType === 'touch') return;
      hovered = true;
      syncTimer();
    });
    imageLink.addEventListener('pointerleave', () => {
      hovered = false;
      syncTimer();
    });
    carousel.addEventListener('focusin', (event) => {
      focused = event.target !== toggle;
      syncTimer();
    });
    carousel.addEventListener('focusout', (event) => {
      focused = event.relatedTarget !== toggle && carousel.contains(event.relatedTarget);
      syncTimer();
    });
    document.addEventListener('visibilitychange', syncTimer);
    motion.addEventListener('change', (event) => {
      if (event.matches) paused = true;
      syncToggle();
    });

    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver(([entry]) => {
        inView = entry.isIntersecting;
        if (inView) slides.forEach((slide) => { slide.loading = 'eager'; });
        syncTimer();
      }, { threshold: 0.1 });
      observer.observe(carousel);
    } else {
      slides.forEach((slide) => { slide.loading = 'eager'; });
    }

    controls.hidden = false;
    show(0);
    syncToggle();
  });
})();
