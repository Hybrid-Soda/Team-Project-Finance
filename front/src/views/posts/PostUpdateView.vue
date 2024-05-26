<template>
  <main class="container">
    <Header />
    <button @click="this.$router.go(-1)" class="backBtn">
      <img src="@/assets/img/backArrow.png" alt="goBack" class="backImg">
    </button>
    <h1 class="post-title">게시글 수정</h1>
    <form @submit.prevent="updatePost">
      <div class="mb-3">
        <label for="title" class="form-label">제목</label>
        <input type="text" class="form-control" v-model.trim="title" id="title">
      </div>
      <div class="mb-3">
        <label for="content" class="form-label">본문</label>
        <textarea class="form-control" v-model.trim="content" id="content" rows="15"></textarea>
      </div>
      <div class="mb-3">
        <input type="file" class="form-control" id="upload-image" @change="handleFileUpload">
      </div>
      <input type="submit" value="수정" class="submit-button">
    </form>
  </main>
</template>


<script setup>
  import { usePostStore } from '@/stores/post'
  import { useRoute } from 'vue-router'
  import { ref, onMounted, computed } from 'vue'
  import Header from '@/components/Header.vue'

  const postStore = usePostStore()
  const route = useRoute()
  
  const postId = Number(route.params.id)
  const post = ref(null)
  const title = ref('')
  const content = ref('')
  const image = ref(null)
  
  onMounted(() => {
    post.value = postStore.posts.find(post => post.id === postId)
    title.value = post.value.title
    content.value = post.value.content
    image.value = post.value.image
  })

  const updatePost = function () {
    const formData = new FormData()
    formData.append('title', title.value)
    formData.append('content', content.value)
    if (image.value) {
      formData.append('image', image.value)
    }
    if (window.confirm('게시글을 수정하시겠습니까?')) {
      postStore.updatePost(payload)
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
.img-div {
  background: #6b6b6b;
  width: 213px;
  height: 213px;
  opacity: 1;
  border-radius: 50%;
  background-image: url("@/assets/img/profile-man.png");
  background-position: center;
  background-size: contain;
}
.profile-img {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 30px;
}
.info-input {
  display: flex;
  flex-direction: column;
}
.input-wrap {
  display: flex;
  justify-content: space-between;
  gap: 20px;
}
.submit-button {
  width: 10%;
  padding: 5px;
  font-weight: 600;
  text-align: center;
  border-radius: 37px;
  color: rgb(255, 199, 39);
  border: 2px solid rgb(255, 199, 39);
  background-color: rgba(0, 0, 0, 0);
}
.submit-button:hover {
  color: rgb(255, 255, 255);
  background-color: rgb(255, 199, 39);
}
</style>