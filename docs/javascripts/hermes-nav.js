// Hermes section styling — big bold separator in left nav
document.addEventListener('DOMContentLoaded', function() {
  const links = document.querySelectorAll('.md-nav__link');
  links.forEach(function(link) {
    if (link.textContent.includes('🫡') && link.textContent.includes('Hermes')) {
      // Style the section item
      const sectionItem = link.closest('.md-nav__item--section');
      if (sectionItem) {
        sectionItem.style.marginTop = '16px';
        sectionItem.style.paddingTop = '16px';
        sectionItem.style.borderTop = '3px solid #c9a961';
      }
      // Style the link itself
      link.style.fontWeight = '800';
      link.style.fontSize = '1.15em';
      link.style.textTransform = 'uppercase';
      link.style.letterSpacing = '0.5px';
      link.style.color = '#0a2540';
    }
  });
});
