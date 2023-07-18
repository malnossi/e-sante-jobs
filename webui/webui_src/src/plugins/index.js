/**
 * plugins/index.js
 *
 * Automatically included in `./src/main.js`
 */

// Plugins
import { loadFonts } from "./webfontloader";
import vuetify from "./vuetify";
import pinia from "../store";
import router from "../router";

// Set http client to store
import http from "@/http";
pinia.use(({ store }) => {
  store.$http = http;
});

export function registerPlugins(app) {
  loadFonts();
  app.use(vuetify).use(router).use(pinia);
}
