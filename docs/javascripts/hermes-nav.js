// Hermes section styling — big bold separator in left nav
document.addEventListener('DOMContentLoaded', function() {
  var links = document.querySelectorAll('.md-nav__link');
  for (var i = 0; i < links.length; i++) {
    var link = links[i];
    if (link.textContent.trim() === 'Hermes Community Hub') {
      var sectionItem = link.closest('.md-nav__item--section');
      if (sectionItem) {
        sectionItem.style.marginTop = '20px';
        sectionItem.style.paddingTop = '16px';
        sectionItem.style.borderTop = '3px solid #c9a961';
      }
      link.style.fontWeight = '800';
      link.style.fontSize = '1.2em';
      link.style.textTransform = 'uppercase';
      link.style.letterSpacing = '0.5px';
      link.style.color = '#0a2540';
      break;
    }
  }
});
