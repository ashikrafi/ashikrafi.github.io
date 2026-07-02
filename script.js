(function () {
  'use strict';

  // Mobile nav toggle
  var toggle = document.getElementById('navToggle');
  var menu = document.querySelector('.masthead__menu');

  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var isOpen = menu.classList.toggle('open');
      toggle.classList.toggle('open', isOpen);
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    menu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        menu.classList.remove('open');
        toggle.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // Highlight active nav link on scroll
  var sections = document.querySelectorAll('.page__content[id], #contact');
  var navLinks = document.querySelectorAll('.masthead__menu a');

  function setActiveNav() {
    var scrollY = window.scrollY + 80;
    var current = '';

    sections.forEach(function (section) {
      if (section.offsetTop <= scrollY) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(function (link) {
      link.classList.remove('active');
      if (link.getAttribute('href') === '#' + current) {
        link.classList.add('active');
      }
    });
  }

  window.addEventListener('scroll', setActiveNav, { passive: true });
  setActiveNav();

  // Download CV: open the browser print dialog (Save as PDF)
  var printCv = document.getElementById('printCv');
  if (printCv) {
    printCv.addEventListener('click', function () {
      window.print();
    });
  }

  // Count-up animation for metrics strip
  var metricNums = document.querySelectorAll('.metric__num[data-count]');
  var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function animateCount(el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var suffix = el.getAttribute('data-suffix') || '';
    var duration = 1200;
    var start = null;

    function step(timestamp) {
      if (!start) start = timestamp;
      var progress = Math.min((timestamp - start) / duration, 1);
      var eased = 1 - Math.pow(1 - progress, 3);
      var current = Math.round(target * eased);
      el.textContent = current + suffix;
      if (progress < 1) {
        requestAnimationFrame(step);
      }
    }

    requestAnimationFrame(step);
  }

  if (metricNums.length && !prefersReducedMotion) {
    var metricsStrip = document.querySelector('.metrics-strip');
    if (metricsStrip && 'IntersectionObserver' in window) {
      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            metricNums.forEach(function (el) {
              if (!el.dataset.animated) {
                el.dataset.animated = 'true';
                el.textContent = '0' + (el.getAttribute('data-suffix') || '');
                animateCount(el);
              }
            });
            observer.disconnect();
          }
        });
      }, { threshold: 0.3 });
      observer.observe(metricsStrip);
    }
  }

  // Scroll-reveal animations
  var revealTargets = [];
  document.querySelectorAll('#main > .page__content').forEach(function (section) {
    var heading = section.querySelector(':scope > h2');
    if (heading) revealTargets.push(heading);

    var groups = section.querySelectorAll(
      ':scope > .exp-block, :scope > .metrics-section, :scope > .intro, ' +
      ':scope > .edu-card, :scope > .profile_box, :scope > .pub-title, ' +
      ':scope > .pub-authors, :scope > .pub-group, :scope > .pub-more, ' +
      ':scope > .skills-list, :scope > .awards-list, :scope > p'
    );
    groups.forEach(function (el) {
      revealTargets.push(el);
    });
  });

  if (prefersReducedMotion || !('IntersectionObserver' in window)) {
    revealTargets.forEach(function (el) {
      el.classList.add('is-visible');
    });
  } else {
    revealTargets.forEach(function (el) {
      el.classList.add('reveal');
    });

    var revealObserver = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });

    revealTargets.forEach(function (el) {
      revealObserver.observe(el);
    });
  }
})();
