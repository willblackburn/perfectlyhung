import { defineConfig } from "vite";

export default defineConfig({
  root: "public",
  build: {
    outDir: "../dist",
    emptyOutDir: true,
  },
  server: {
    watch: {
      usePolling: true,
    },
    hmr: true,
  },
});
