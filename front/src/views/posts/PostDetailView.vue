<template>
  <div class="container">
    <Header/>
    <div class="d-flex justify-space-between">
      <div class="me-auto">
        <RouterLink :to="{ name: 'postList' }">뒤로가기</RouterLink>
      </div>
      <div v-if="post && post.user.username === userStore.userInfo.username">
        <button class="btn btn-outline-warning me-3">
          <RouterLink :to="{ name: 'postUpdate', params: { 'id': postId } }">
            수정
          </RouterLink>
        </button>
        <button class="btn btn-outline-danger" @click="postStore.deletePost(postId)">글 삭제</button>
      </div>
    </div><br>

    <main v-if="post">
      <h2>{{ post.title }}</h2>
      <p>
        <span>닉네임 : {{ post.user.nickname }}</span> | 
        <span>작성일 : {{ post.created_at.slice(0, 10) }}</span> | 
        <span>수정일 : {{ post.updated_at.slice(0, 10) }}</span>
      </p><hr>
      <p>{{ post.content }}</p>
    </main>

    <div v-else>
      <p>Loading...</p>
    </div>

    <hr>
    <footer>
      <h5 class="mb-3">댓글</h5>
      <p>댓글 개수 : {{ comments.length }}</p>
      <div v-if="post">
        <div v-for="comment in comments">
          <!-- <p>{{ comment }}</p> -->
          <h6 class="mb-1">{{ comment.user.nickname }}</h6>
          <p class="m-0">{{ comment.content }}</p>
          <p class="m-0">{{ comment.created_at.slice(0, 10) }}. {{ comment.created_at.slice(11, 16) }}</p>
          <hr>
        </div>
      </div><br>

      <form @submit.prevent="createComment">
        <div class="mb-3">
          <textarea class="form-control" placeholder="댓글을 남겨보세요" v-model.trim="commentContent" rows="3"></textarea>
        </div>
        <input type="submit" value="등록" class="btn btn-outline-success login-btn">
      </form>
    </footer>
  </div>
</template>

<script setup>
import Header from '@/components/Header.vue'
import { ref, onMounted, computed, watch } from 'vue'
import { usePostStore } from '@/stores/post'
import { useUserStore } from '@/stores/user'
import { useRoute } from 'vue-router'
import axios from 'axios'

const postStore = usePostStore()
const userStore = useUserStore()
const route = useRoute()

const commentContent = ref('')
const comments = ref([])
const postId = route.params.id
const post = ref(null)

// 게시글 상세 조회
const readPostDetail = function () {
  axios({
    method: 'get',
    url: `${postStore.API_URL}/posts/${postId}/`,
  })
  .then(res => {
    post.value = res.data
    comments.value = res.data.comment_set
  })
  .catch(err => console.error(err))
}

onMounted(() => {
  readPostDetail()
})

// 댓글 생성
const createComment = function () {
  if (userStore.isLogIn) {
    axios({
      method: 'post',
      url: `${postStore.API_URL}/posts/${postId}/comments/`,
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
      data: {
        content: commentContent.value
      }
    })
    .then(res => {
      comments.value.push(res.data)
      commentContent.value = ''
    })
    .catch(err => console.error(err))
  } else {
    window.alert('로그인 후 작성해주세요')
  }
}

// 댓글 삭제
const deleteComment = function (commentId) {
  if (window.confirm('정말 삭제하시겠습니까?')) {
    axios({
      method: 'delete',
      url: `${API_URL}/posts/${postId}/comments/${commentId}/`,
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
    .then(res => {})
    .catch(err => console.error(err))
  }
}
</script>

<style scoped>

</style>