<template>
  <div class="container">
    <Header/>
    <div class="d-flex justify-space-between">
      <h1>글 상세</h1>
    </div><br>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { usePostStore } from '@/stores/post'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import Header from '@/components/Header.vue'

const postStore = usePostStore()
const authStore = useAuthStore()
const router = useRouter()

</script>

<style scoped>

</style>