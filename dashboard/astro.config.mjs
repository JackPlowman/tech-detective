import sitemap from "@astrojs/sitemap";
import robotsTxt from "astro-robots-txt";
import { defineConfig } from "astro/config";

// https://astro.build/config
export default defineConfig({
  site: "https://jackplowman.github.io",
  base: "tech-detective",
  integrations: [robotsTxt(), sitemap()],
});
