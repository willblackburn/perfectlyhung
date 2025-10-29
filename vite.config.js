import { defineConfig } from "vite";
import { resolve } from "path";

export default defineConfig({
  root: "public",
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
