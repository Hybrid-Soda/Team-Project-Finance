import { createRouter, createWebHistory } from 'vue-router'
// card 
import HomeView from '../views/HomeView.vue'
import CardListView from '@/views/CardListView.vue'
import CardDetailView from '@/views/CardDetailView.vue'
// auth
import MyPageView from '@/views/MyPageView.vue'
import SignInView from '@/views/SignInView.vue'
import SignUpView from '@/views/SignUpView.vue'
// post
import PostListView from '@/views/PostListView.vue'
import PostCreateView from '@/views/PostCreateView.vue'
import PostDetailView from '@/views/PostDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // card
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/cards',
      name: 'cardList',
      component: CardListView
    },
    {
      path: '/cards/:id',
      name: 'cardDetail',
      component: CardDetailView
    },
    // auth
    {
      path: '/:username',
      name: 'myPage',
      component: MyPageView
    },
    {
      path: '/signin',
      name: 'signIn',
      component: SignInView
    },
    {
      path: '/signup',
      name: 'signUp',
      component: SignUpView
    },
    // post
    {
      path: '/posts',
      name: 'postList',
      component: PostListView
    },
    {
      path: '/posts/:id',
      name: 'postDetail',
      component: PostDetailView
    },
    {
      path: '/posts/create',
      name: 'postCreate',
      component: PostCreateView
    },
  ]
})

export default router
