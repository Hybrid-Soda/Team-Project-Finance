import { createRouter, createWebHistory } from 'vue-router'
// cards
import HomeView from '@/views/cards/HomeView.vue'
import CardListView from '@/views/cards/CardListView.vue'
import CardDetailView from '@/views/cards/CardDetailView.vue'
// users
import MyPageView from '@/views/users/MyPageView.vue'
import SignInView from '@/views/users/SignInView.vue'
import SignUpView from '@/views/users/SignUpView.vue'
// posts
import PostListView from '@/views/posts/PostListView.vue'
import PostCreateView from '@/views/posts/PostCreateView.vue'
import PostDetailView from '@/views/posts/PostDetailView.vue'
import PostUpdateView from '@/views/posts/PostUpdateView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // cards
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
    // users
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
    // posts
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
    {
      path: '/posts/:id/update',
      name: 'postUpdate',
      component: PostUpdateView
    },
  ]
})

export default router
