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

// Hide/Show fixed header on scroll direction with small threshold
let lastScrollY = window.pageYOffset || document.documentElement.scrollTop || 0;
const headerEl = document.querySelector(".header");
const scrollThreshold = 10;
const menuCheckboxEl = document.getElementById("openSidebarMenu");

function shouldKeepHeaderVisible() {
  return menuCheckboxEl && menuCheckboxEl.checked;
}

function updateHeaderForScroll(currentScrollY) {
  if (!headerEl) return;
  if (shouldKeepHeaderVisible()) {
    headerEl.classList.remove("hidden");
    lastScrollY = currentScrollY;
    return;
  }

  if (Math.abs(currentScrollY - lastScrollY) < scrollThreshold) {
    return; // ignore small movements to prevent flicker
  }

  if (currentScrollY > lastScrollY) {
    headerEl.classList.add("hidden");
  } else {
    headerEl.classList.remove("hidden");
  }

  if (currentScrollY <= 0) {
    headerEl.classList.remove("hidden");
  }

  lastScrollY = currentScrollY;
}

if (headerEl) {
  // Move nav (#sidebarMenu) into header on desktop so logo, links, icons share container
  const sidebarMenuEl = document.getElementById("sidebarMenu");
  const menuCheckboxEl = document.getElementById("openSidebarMenu");
  const originalParent = sidebarMenuEl ? sidebarMenuEl.parentNode : null;
  const originalNextSibling = sidebarMenuEl ? sidebarMenuEl.nextSibling : null;

  function mountDesktopNav() {
    if (!headerEl || !sidebarMenuEl) return;
    if (window.innerWidth >= 1024 && sidebarMenuEl.parentNode !== headerEl) {
      headerEl.appendChild(sidebarMenuEl);
      if (menuCheckboxEl) menuCheckboxEl.checked = false;
    }
  }

  function unmountDesktopNav() {
    if (!sidebarMenuEl || !originalParent) return;
    if (window.innerWidth < 1024 && sidebarMenuEl.parentNode !== originalParent) {
      if (originalNextSibling && originalNextSibling.parentNode === originalParent) {
        originalParent.insertBefore(sidebarMenuEl, originalNextSibling);
      } else {
        originalParent.appendChild(sidebarMenuEl);
      }
    }
  }

  const handleResizeRelocate = () => {
    if (window.innerWidth >= 1024) {
      mountDesktopNav();
    } else {
      unmountDesktopNav();
    }
  };

  // Initial placement and resize handling
  handleResizeRelocate();
  window.addEventListener("resize", handleResizeRelocate, { passive: true });

  // Native scroll listener (desktop/mobile)
  window.addEventListener(
    "scroll",
    () => {
      const currentScrollY = window.pageYOffset || document.documentElement.scrollTop || 0;
      updateHeaderForScroll(currentScrollY);
    },
    { passive: true }
  );

  // Hook into Lenis scroll (smooth/touch)
  try {
    if (typeof lenis !== "undefined" && lenis && typeof lenis.on === "function") {
      lenis.on("scroll", (e) => {
        const current = e && typeof e.scroll === "number" ? e.scroll : window.pageYOffset || document.documentElement.scrollTop || 0;
        updateHeaderForScroll(current);
      });
    }
  } catch (err) {
    // noop
  }

  // Ensure hamburger menu is closed on desktop to avoid showing an 'X'
  const closeMenuOnDesktop = () => {
    if (window.innerWidth >= 1024 && menuCheckboxEl) {
      menuCheckboxEl.checked = false;
    }
  };
  closeMenuOnDesktop();
  window.addEventListener("resize", closeMenuOnDesktop, { passive: true });
}
