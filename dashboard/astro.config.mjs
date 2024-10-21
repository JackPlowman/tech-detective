// @ts-check
import { defineConfig } from "astro/config";
import robotsTxt from "astro-robots-txt";

// https://astro.build/config
export default defineConfig({
  site: "https://jackplowman.github.io",
  base: "tech-detective",
  integrations: [robotsTxt()],
});
