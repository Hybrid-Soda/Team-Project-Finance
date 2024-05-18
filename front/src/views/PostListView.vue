<template>
  <div class="container">
    <Header/>

    <div class="d-flex justify-space-between">
      <h1>금융상품 자유 게시판</h1>
      <RouterLink v-if="authStore.isAuthenticated" :to="{ name: 'postCreate' }">
        <button>글 쓰기</button>
      </RouterLink>
    </div><br>

    <table class="table">
      <thead>
        <tr>
          <th scope="col">글 번호</th>
          <th scope="col">제목</th>
          <th scope="col">작성자</th>
          <th scope="col">작성일자</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="post in postStore.posts" :key="post.id" @click="goDetail(post.id)" class="post">
          <th scope="row">{{ post.id }}</th>
          <td>{{ post.title }}</td>
          <td>{{ post.user.nickname }}</td>
          <td>{{ truncate(post.created_at, 10) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { useRouter, RouterLink } from 'vue-router'
import { usePostStore } from '@/stores/post'
import { useAuthStore } from '@/stores/auth'
import { onMounted } from 'vue'
import Header from '@/components/Header.vue'

const router = useRouter()
const postStore = usePostStore()
const authStore = useAuthStore()

onMounted(() => {
  postStore.readPosts()
})

const goDetail = (id) => {
  router.push({ name: 'postDetail', params: { id } })
}

const truncate = (text, length) => {
  return text.substring(0, length)
}
</script>

<style scoped>
.post:hover {
  cursor: pointer;
}
</style>