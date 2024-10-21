import sitemap from "@astrojs/sitemap";
import robotsTxt from "astro-robots-txt";
import webmanifest from "astro-webmanifest";
import { defineConfig } from "astro/config";

// https://astro.build/config
export default defineConfig({
  site: "https://jackplowman.github.io",
  base: "tech-detective",
  integrations: [
    robotsTxt(),
    sitemap(),
    webmanifest({
      name: "Tech Detective",
      icon: "public/favicon.svg",
      short_name: "Tech Detective",
      description: "What Technologies are used in my projects?",
      start_url: "/tech-detective",
      theme_color: "#3367D6",
      background_color: "#3367D6",
      display: "standalone",
    }),
  ],
});
