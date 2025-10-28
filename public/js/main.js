// Import CSS for Vite HMR
import "../css/main.css";

// Import Lenis for smooth scrolling
import Lenis from "lenis";

// Initialize Lenis smooth scrolling
const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  direction: "vertical",
  gestureDirection: "vertical",
  smooth: true,
  mouseMultiplier: 1,
  smoothTouch: false,
  touchMultiplier: 2,
  infinite: false,
});

// Lenis RAF loop
function raf(time) {
  lenis.raf(time);
  requestAnimationFrame(raf);
}

requestAnimationFrame(raf);

// Enable HMR for CSS
if (import.meta.hot) {
  import.meta.hot.accept("../css/main.css", () => {
    console.log("CSS updated");
  });
}
