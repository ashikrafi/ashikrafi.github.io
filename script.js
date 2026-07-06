(function () {
  'use strict';

  // Sync page copy from canonical sidebar profile (single source of truth)
  var profileCard = document.getElementById('profile-card');
  if (profileCard) {
    var profileFields = {
      name: profileCard.querySelector('[data-profile="name"]'),
      title: profileCard.querySelector('[data-profile="title"]'),
      location: profileCard.getAttribute('data-profile-location')
    };

    document.querySelectorAll('[data-profile-sync]').forEach(function (el) {
      var key = el.getAttribute('data-profile-sync');
      if (key === 'location' && profileFields.location) {
        el.textContent = profileFields.location;
      } else if (profileFields[key]) {
        el.textContent = profileFields[key].textContent.trim();
      }
    });
  }

  // Mobile nav toggle
  var toggle = document.getElementById('navToggle');
  var menu = document.querySelector('.site-nav__menu');

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
  var navLinks = document.querySelectorAll('.site-nav__menu a');

  function setActiveNav() {
    var scrollY = window.scrollY + 120;
    var current = '';

    sections.forEach(function (section) {
      if (section.offsetTop <= scrollY) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(function (link) {
      link.classList.remove('active');
      link.removeAttribute('aria-current');
      if (link.getAttribute('href') === '#' + current) {
        link.classList.add('active');
        link.setAttribute('aria-current', 'true');
      }
    });
  }

  window.addEventListener('scroll', setActiveNav, { passive: true });
  setActiveNav();

  // View CV: open formatted resume with toolbar at top
  var printCv = document.getElementById('printCv');
  if (printCv) {
    printCv.addEventListener('click', function () {
      window.open('cv.html', '_blank', 'noopener');
    });
  }

  // Keep profile photo sharp after tab switches (browser may downscale in background)
  var profileImg = document.querySelector('.profile_card__img');
  if (profileImg) {
    function refreshProfileImage() {
      if (document.visibilityState !== 'visible') return;
      var src = profileImg.currentSrc || profileImg.getAttribute('src');
      if (!src) return;
      profileImg.src = src;
    }

    document.addEventListener('visibilitychange', refreshProfileImage);
    window.addEventListener('pageshow', refreshProfileImage);
  }
})();
