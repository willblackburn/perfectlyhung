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
        "locations-chelsea": resolve(__dirname, "public/locations/chelsea.html"),
        "locations-kensington": resolve(__dirname, "public/locations/kensington.html"),
        "locations-south-kensington": resolve(__dirname, "public/locations/south-kensington.html"),
        "locations-knightsbridge": resolve(__dirname, "public/locations/knightsbridge.html"),
        "locations-belgravia": resolve(__dirname, "public/locations/belgravia.html"),
        "locations-notting-hill": resolve(__dirname, "public/locations/notting-hill.html"),
        "locations-holland-park": resolve(__dirname, "public/locations/holland-park.html"),
        "locations-earls-court": resolve(__dirname, "public/locations/earls-court.html"),
        "locations-fulham": resolve(__dirname, "public/locations/fulham.html"),
        "locations-hammersmith": resolve(__dirname, "public/locations/hammersmith.html"),
        "locations-chiswick": resolve(__dirname, "public/locations/chiswick.html"),
        "locations-barnes": resolve(__dirname, "public/locations/barnes.html"),
        "locations-richmond": resolve(__dirname, "public/locations/richmond.html"),
        "locations-putney": resolve(__dirname, "public/locations/putney.html"),
        "locations-wandsworth": resolve(__dirname, "public/locations/wandsworth.html"),
        "locations-battersea": resolve(__dirname, "public/locations/battersea.html"),
        "locations-clapham": resolve(__dirname, "public/locations/clapham.html"),
        "locations-shepherds-bush": resolve(__dirname, "public/locations/shepherds-bush.html"),
        "locations-hampstead": resolve(__dirname, "public/locations/hampstead.html"),
        "locations-hampstead-heath": resolve(__dirname, "public/locations/hampstead-heath.html"),
        "locations-highgate": resolve(__dirname, "public/locations/highgate.html"),
        "locations-primrose-hill": resolve(__dirname, "public/locations/primrose-hill.html"),
        "locations-camden": resolve(__dirname, "public/locations/camden.html"),
        "locations-st-johns-wood": resolve(__dirname, "public/locations/st-johns-wood.html"),
        "locations-swiss-cottage": resolve(__dirname, "public/locations/swiss-cottage.html"),
        "locations-kentish-town": resolve(__dirname, "public/locations/kentish-town.html"),
        "locations-islington": resolve(__dirname, "public/locations/islington.html"),
        "locations-angel": resolve(__dirname, "public/locations/angel.html"),
        "locations-stoke-newington": resolve(__dirname, "public/locations/stoke-newington.html"),
        "locations-crouch-end": resolve(__dirname, "public/locations/crouch-end.html"),
        "locations-muswell-hill": resolve(__dirname, "public/locations/muswell-hill.html"),
        "locations-finchley": resolve(__dirname, "public/locations/finchley.html"),
        "locations-golders-green": resolve(__dirname, "public/locations/golders-green.html"),
        "locations-barnet": resolve(__dirname, "public/locations/barnet.html"),
        "locations-maida-vale": resolve(__dirname, "public/locations/maida-vale.html"),
        "locations-little-venice": resolve(__dirname, "public/locations/little-venice.html"),
        "locations-kilburn": resolve(__dirname, "public/locations/kilburn.html"),
        "locations-queens-park": resolve(__dirname, "public/locations/queens-park.html"),
        "locations-willesden": resolve(__dirname, "public/locations/willesden.html"),
        "locations-harrow": resolve(__dirname, "public/locations/harrow.html"),
        "locations-wembley": resolve(__dirname, "public/locations/wembley.html"),
        "locations-brent": resolve(__dirname, "public/locations/brent.html"),
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
