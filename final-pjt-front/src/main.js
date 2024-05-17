import './assets/style.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import PiniaPluginPersistedState from 'pinia-plugin-persistedstate'

import App from './App.vue'
import router from './router'

const app = createApp(App)
const pinia = createPinia()

pinia.use(PiniaPluginPersistedState)
app.use(pinia)
app.use(router)

app.mount('#app')
