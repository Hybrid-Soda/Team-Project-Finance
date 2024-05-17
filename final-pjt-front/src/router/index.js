import { createRouter, createWebHistory } from 'vue-router'
// card 
import HomeView from '../views/HomeView.vue'
import MyPageView from '@/views/MyPageView.vue'
import CardListView from '@/views/CardListView.vue'
import CardDetailView from '@/views/CardDetailView.vue'
// auth
import LoginView from '@/views/LoginView.vue'
import SignupView from '@/views/SignupView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/:username',
      name: 'myPage',
      component: MyPageView
    },
    {
      path: '/2',
      name: 'cardList',
      component: CardListView
    },
    {
      path: '/3',
      name: 'cardDetail',
      component: CardDetailView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },
  ]
})

export default router
