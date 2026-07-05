(function () {
  'use strict';

  // Sync page copy from canonical sidebar profile (single source of truth)
  var profileCard = document.getElementById('profile-card');
  if (profileCard) {
    var profileFields = {
      name: profileCard.querySelector('[data-profile="name"]'),
      title: profileCard.querySelector('[data-profile="title"]'),
      org: profileCard.querySelector('[data-profile="org"] a'),
      location: profileCard.getAttribute('data-profile-location')
    };

    document.querySelectorAll('[data-profile-sync]').forEach(function (el) {
      var key = el.getAttribute('data-profile-sync');
      if (key === 'location' && profileFields.location) {
        el.textContent = profileFields.location;
      } else if (key === 'org-link' && profileFields.org) {
        el.textContent = profileFields.org.textContent.trim();
        el.setAttribute('href', profileFields.org.getAttribute('href'));
      } else if (profileFields[key]) {
        el.textContent = profileFields[key].textContent.trim();
      }
    });
  }

  // Mobile nav toggle (sidebar navigation)
  var toggle = document.getElementById('navToggle');
  var menu = document.querySelector('.sidebar-nav');

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
  var navLinks = document.querySelectorAll('.sidebar-nav a');

  function setActiveNav() {
    var scrollY = window.scrollY + 100;
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

  // Download CV: open formatted resume and trigger print (Save as PDF)
  var printCv = document.getElementById('printCv');
  if (printCv) {
    printCv.addEventListener('click', function () {
      window.open('resume.html?print=1', '_blank', 'noopener');
    });
  }
})();
