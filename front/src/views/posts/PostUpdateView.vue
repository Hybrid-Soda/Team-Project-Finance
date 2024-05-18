<template>
  <main class="container">
    <Header />

    <h1>게시글 수정</h1>
    <form @submit.prevent="updatePost">
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
      <input type="submit" value="수정" class="btn btn-outline-warning login-btn">
    </form>
  </main>
</template>


<script setup>
  import { usePostStore } from '@/stores/post'
  import { useRoute } from 'vue-router'
  import { ref } from 'vue'
  import Header from '@/components/Header.vue'

  const postStore = usePostStore()
  const route = useRoute()
  
  const postId = route.params.id
  const title = ref('')
  const content = ref('')

  const updatePost = function () {
    const payload = {
      postId,
      title: title.value,
      content: content.value,
    }
    if (window.confirm('게시글을 수정하시겠습니까?')) {
      postStore.updatePost(payload)
    }
  }
</script>

<style scoped>
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
  color: rgb(33, 95, 255);
  background-color: rgba(0, 0, 0, 0);
  border: none;
  /* border: 1px solid rgb(106, 106, 106); */
  font-size: large;
  font-weight: 900;
  position: absolute;
  bottom: 50px;
  right: 60px;
}
</style>