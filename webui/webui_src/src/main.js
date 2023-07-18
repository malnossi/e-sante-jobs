/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'

// Plugins
import { registerPlugins } from '@/plugins'

// http
import http from './http'
const app = createApp(App)
app.config.globalProperties.$http = http

registerPlugins(app)

app.mount('#app')
