// Hermes section big bold separator — watches for MkDocs Material nav render
(function() {
  function styleHermes() {
    var links = document.querySelectorAll('.md-nav__link');
    for (var i = 0; i < links.length; i++) {
      if (links[i].textContent.indexOf('Hermes Community Hub') > -1) {
        var section = links[i].closest('.md-nav__item');
        if (section) {
          section.style.marginTop = '20px';
          section.style.paddingTop = '16px';
          section.style.borderTop = '3px solid #c9a961';
        }
        links[i].style.fontWeight = '800';
        links[i].style.fontSize = '1.2em';
        links[i].style.textTransform = 'uppercase';
        links[i].style.letterSpacing = '0.5px';
        links[i].style.color = '#0a2540';
        return true;
      }
    }
    return false;
  }

  // Try immediately
  if (!styleHermes()) {
    // Watch for DOM changes (MkDocs Material renders nav dynamically)
    var observer = new MutationObserver(function() {
      if (styleHermes()) observer.disconnect();
    });
    observer.observe(document.body, { childList: true, subtree: true });
  }
})();