<template>
  <main class="container">
    <Header />
    <button @click="this.$router.go(-1)" class="backBtn">
      <img src="@/assets/img/backArrow.png" alt="goBack" class="backImg">
    </button>
    <h1 class="post-title">게시글 작성</h1>
    <form @submit.prevent="createPost" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="title" class="form-label">제목</label>
        <input type="text" class="form-control" v-model.trim="title" id="title">
      </div>
      <div class="mb-3">
        <label for="content" class="form-label">본문</label>
        <textarea class="form-control" v-model.trim="content" id="content" rows="10"></textarea>
      </div>
      <div class="mb-3">
        <input type="file" class="form-control" id="upload-image" @change="handleFileUpload">
      </div>
      <input type="submit" value="등록" class="btn btn-outline-warning login-btn">
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

const handleFileUpload = (event) => {
  image.value = event.target.files[0]
}

const createPost = function () {
  const formData = new FormData()
  formData.append('title', title.value)
  formData.append('content', content.value)
  if (image.value) {
    formData.append('image', image.value)
  }
  if (window.confirm('게시글을 작성하시겠습니까?')) {
    postStore.createPost(formData)
  }
}
</script>

<style scoped>
.post-title {
  text-align: center;
  margin: 20px 0;
}
.backBtn {
  position: absolute;
  background-color: rgba(0, 0, 0, 0);
}
.backImg {
  width: 50px;
  opacity: .5;
}
</style>