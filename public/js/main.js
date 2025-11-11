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
}

// YouTube audio player toggle
const musicToggleEl = document.querySelector(".music-toggle");
let ytPlayer = null;
let ytApiReady = false;
let ytScriptLoading = false;
let pendingPlay = false;

function ensureWaveformMarkup() {
  if (!musicToggleEl) return;
  const box = musicToggleEl.querySelector(".music-icon-box");
  if (!box) return;
  if (box.querySelector(".music-waveform")) return;
  const wf = document.createElement("div");
  wf.className = "music-waveform";
  for (let i = 0; i < 5; i++) {
    const bar = document.createElement("span");
    bar.className = "bar";
    wf.appendChild(bar);
  }
  box.appendChild(wf);
}

function loadYouTubeApi() {
  if (ytScriptLoading) return;
  ytScriptLoading = true;
  const tag = document.createElement("script");
  tag.src = "https://www.youtube.com/iframe_api";
  const firstScriptTag = document.getElementsByTagName("script")[0];
  firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
}

function initYouTubePlayer() {
  if (ytPlayer || !musicToggleEl || typeof YT === "undefined" || !YT.Player) return;
  const videoId = musicToggleEl.getAttribute("data-video-id") || "fdSkbTxkznU";

  const container = document.createElement("div");
  container.id = "yt-audio-player";
  container.style.position = "absolute";
  container.style.left = "-9999px";
  container.style.width = "1px";
  container.style.height = "1px";
  document.body.appendChild(container);

  ytPlayer = new YT.Player(container, {
    width: "1",
    height: "1",
    videoId,
    playerVars: {
      autoplay: 0,
      controls: 0,
      disablekb: 1,
      modestbranding: 1,
      rel: 0,
      playsinline: 1,
    },
    events: {
      onReady: () => {
        if (pendingPlay) {
          try {
            ytPlayer.playVideo();
          } catch (e) {
            // noop
          }
          pendingPlay = false;
        }
      },
      onStateChange: (e) => {
        try {
          if (e.data === YT.PlayerState.PLAYING) {
            musicToggleEl.classList.add("is-playing");
            musicToggleEl.setAttribute("aria-label", "Pause site music");
            musicToggleEl.setAttribute("aria-pressed", "true");
          } else if (e.data === YT.PlayerState.PAUSED || e.data === YT.PlayerState.ENDED) {
            musicToggleEl.classList.remove("is-playing");
            musicToggleEl.setAttribute("aria-label", "Play site music");
            musicToggleEl.setAttribute("aria-pressed", "false");
          }
        } catch (err) {
          // noop
        }
      },
    },
  });
}

// Expose the YouTube API ready callback on window (since this file is a module)
// eslint-disable-next-line no-undef
window.onYouTubeIframeAPIReady = function () {
  ytApiReady = true;
  initYouTubePlayer();
};

if (musicToggleEl) {
  // Inject waveform bars once
  ensureWaveformMarkup();

  musicToggleEl.addEventListener("click", () => {
    try {
      if (!ytApiReady) {
        pendingPlay = true;
        loadYouTubeApi();
        return;
      }

      if (!ytPlayer) {
        initYouTubePlayer();
        pendingPlay = true;
        return;
      }

      const state = typeof ytPlayer.getPlayerState === "function" ? ytPlayer.getPlayerState() : -2;
      // If not currently playing, play; otherwise pause
      if (state !== 1 /* YT.PlayerState.PLAYING */) {
        ytPlayer.playVideo();
      } else {
        ytPlayer.pauseVideo();
      }
    } catch (err) {
      // noop
    }
  });

  // Ensure label is correct on load
  musicToggleEl.setAttribute("aria-label", "Play site music");
  musicToggleEl.setAttribute("aria-pressed", "false");
}
