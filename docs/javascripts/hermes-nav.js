document.addEventListener('DOMContentLoaded', function() {
  var links = document.querySelectorAll('.md-nav__link');
  for (var i = 0; i < links.length; i++) {
    if (links[i].textContent.indexOf('Hermes Community Hub') > -1) {
      var section = links[i].closest('.md-nav__item--section');
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
      break;
    }
  }
});