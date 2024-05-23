<template>
  <div class="container">
    <Header />
    <main>
      <div class="card-page-bg">
        <button @click="this.$router.go(-1)" class="backBtn">
          <img src="../../assets/img/backArrow.png" alt="goBack" class="backImg">
        </button>
        <body>
          <form @submit.prevent="createPost" enctype="multipart/form-data" class="post-form">
            <h3>게시글 작성하기</h3>
            <div class="mb-3 title">
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
            <input type="submit" value="등록" class="btn btn-outline-warning submit-btn">
          </form>
        </body>
      </div>
    </main>
  </div>
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
  // if (window.confirm('게시글을 작성하시겠습니까?')) {
  //   postStore.createPost(formData)
  // }
  Swal.fire({
        title: '제출',
        text: '게시글 작성을 완료하시겠습니까?',
        icon: 'question',
        confirmButtonText: '확인',
        showCancelButton: true,
        denyButtonText: `취소`
      }).then ((res) => {
        if (res.isConfirmed) {
          postStore.createPost(formData)
          router.push({ name:'postList' })
        }
      })
}
</script>

<style scoped>
main {
  display: flex;
  justify-content: center;
  margin-top: 2%;
  width: 100%;
}
body {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 5%;
}
h3 {
  width: 100%;
  text-align: center;
  margin-top: 8%;
}
.title {
  margin-top: 3%;
}
.post-form {
  width: 80%;
  background-color: rgba(0, 0, 0, 0);
}
.backBtn {
  position: absolute;
  margin: 10px 15px;
  background-color: rgba(0, 0, 0, 0);
}
.backImg {
  width: 50px;
  opacity: .5;
}
.card-page-bg {
  border-radius: 50px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
  width: 100%;
  height: 100%;
  padding: 2%;
}
.menu-wrap {
  /* border: 2px solid blue; */
  margin-top: 1%;
}
.submit-btn {
  width: 100%;
  border-radius: 38px;
  font-weight: bold;
}
</style>