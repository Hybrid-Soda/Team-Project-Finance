<template>
  <main class="container">
    <Header />

    <h1>게시글 작성</h1>
    <form @submit.prevent="createPost">
      <div class="mb-3">
        <label for="title" class="form-label">제목</label>
        <input type="text" class="form-control" v-model.trim="title" id="title">
      </div>
      <div class="mb-3">
        <label for="content" class="form-label">본문</label>
        <textarea class="form-control" v-model.trim="content" id="content" rows="10"></textarea>
      </div>
      <!-- <div class="mb-3">
        <input type="file" class="form-control" id="upload-image" @change="handleFileUpload">
      </div> -->
      <input type="submit" value="발행" class="btn btn-outline-warning login-btn">
    </form>
  </main>
</template>

<script setup>
import { ref } from 'vue'
import { usePostStore } from '@/stores/post'
import Header from '@/components/Header.vue'

const postStore = usePostStore()
const title = ref('')
const content = ref('')
const image = ref(null)

// const handleFileUpload = (event) => {
//   image.value = event.target.files[0]
// }

const createPost = function () {
  const payload = {
    title: title.value,
    content: content.value,
  }
  if (confirm('게시글을 작성하시겠습니까?')) {
    postStore.createPost(payload)
  }
}
</script>

<style scoped>

</style>