
new fullpage('#fullpage', {
  //options
  scrollBar: false,
  autoScrolling: true,
  scrollingSpeed: 1000,
  // responsiveWidth: 800,
  scrollOverflow: true,
  normalScrollElements: '.section gallery',
  fitToSection: true,
  fitToSectionDelay: 1000,
  loopBottom: true,
  anchors: [
    'home',
    'aboutus',
    'services',
    'residential',
    'commercial',
    'process',
    'gallery',
    'contact',
  ],
  //Design
  css3: true,
  controlArrows: true,
  verticalCentered: true,
  dropEffect: true,
  dropEffectOptions: { speed: 2300, color: '#F82F4D', zIndex: 9999 },
  waterEffect: false,
  waterEffectOptions: { animateContent: true, animateOnMouseMove: true },
  cards: false,
  cardsOptions: {
    perspective: 100,
    fadeContent: true,
    fadeBackground: true,
  },
  //Accessibility
  keyboardScrolling: true,
  animateAnchor: true,
  recordHistory: true,
})
