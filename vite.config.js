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
      // ⚠️ IMPORTANT: When creating a new HTML page in the public directory,
      // you MUST add it here for it to be included in the Vite build and deployed to Vercel.
      // Format: "page-name": resolve(__dirname, "public/page-name.html"),
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
        gallery: resolve(__dirname, "public/gallery.html"),
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
