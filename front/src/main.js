import './assets/style.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { useKakao } from 'vue3-kakao-maps/@utils'
import PiniaPluginPersistedState from 'pinia-plugin-persistedstate'

import App from './App.vue'
import router from './router'

const app = createApp(App)
const pinia = createPinia()

pinia.use(PiniaPluginPersistedState)
app.use(pinia)
app.use(router)
useKakao('c2a6a895a4df6feef5eb2995c15ff5da')

app.mount('#app')
