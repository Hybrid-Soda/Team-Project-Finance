import './assets/style.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { useKakao } from 'vue3-kakao-maps/@utils'
import PiniaPluginPersistedState from 'pinia-plugin-persistedstate'

import App from './App.vue'
import router from './router'

const app = createApp(App)
const pinia = createPinia()
const kakao_api_key = import.meta.env.VITE_KAKAO_API

pinia.use(PiniaPluginPersistedState)
app.use(pinia)
app.use(router)
useKakao(kakao_api_key)

app.mount('#app')
