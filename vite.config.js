import { defineConfig } from "vite";
import { resolve } from "path";
import { viteStaticCopy } from "vite-plugin-static-copy";

export default defineConfig({
  root: "public",
  plugins: [
    viteStaticCopy({
      targets: [
        {
          src: "robots.txt",
          dest: ".",
        },
        {
          src: "sitemap.xml",
          dest: ".",
        },
        {
          src: "img/*-modal.webp",
          dest: "img",
        },
      ],
    }),
  ],
  build: {
    outDir: "../dist",
    emptyOutDir: true,
    rollupOptions: {
      // ⚠️ IMPORTANT: Every standalone HTML page must be listed here or it will not exist in
      // `dist/` after build. Missing files 404 in production (or hit Firebase's SPA rewrite to
      // index.html). Includes root pages and subfolders e.g. public/locations/*.html.
      // Format: "rollup-key": resolve(__dirname, "public/relative/path.html"),
      input: {
        main: resolve(__dirname, "public/index.html"),
        areas: resolve(__dirname, "public/areas-covered.html"),
        "picture-hanging": resolve(__dirname, "public/picture-hanging.html"),
        "curtain-fitting": resolve(__dirname, "public/curtain-fitting.html"),
        "tv-audiovisual-installation": resolve(__dirname, "public/tv-audiovisual-installation.html"),
        "residential-installation": resolve(__dirname, "public/residential-installation.html"),
        "commercial-installation": resolve(__dirname, "public/commercial-installation.html"),
        "terms-conditions": resolve(__dirname, "public/terms-conditions.html"),
        "locations-mayfair": resolve(__dirname, "public/locations/mayfair.html"),
        "locations-marylebone": resolve(__dirname, "public/locations/marylebone.html"),
        "locations-fitzrovia": resolve(__dirname, "public/locations/fitzrovia.html"),
        "locations-bloomsbury": resolve(__dirname, "public/locations/bloomsbury.html"),
        "locations-covent-garden": resolve(__dirname, "public/locations/covent-garden.html"),
        "locations-soho": resolve(__dirname, "public/locations/soho.html"),
        "locations-westminster": resolve(__dirname, "public/locations/westminster.html"),
        gallery: resolve(__dirname, "public/gallery.html"),
        blog: resolve(__dirname, "public/blog.html"),
      },
    },
  },
  server: {
    watch: {
      usePolling: true,
      interval: 100,
    },
  },
});
