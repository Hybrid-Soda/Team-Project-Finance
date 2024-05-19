<template>
  <div v-if="post" class="container">
    <Header/>

    <section class="d-flex justify-space-between mb-4">
      <div class="me-auto">
        <RouterLink :to="{ name: 'postList' }">뒤로가기</RouterLink>
      </div>
      <div v-if="userStore.isLogIn && post.user.username === userStore.userInfo.username">
        <button class="btn btn-outline-warning me-3">
          <RouterLink :to="{ name: 'postUpdate', params: { 'id': postId } }">
            수정
          </RouterLink>
        </button>
        <button class="btn btn-outline-danger" @click="postStore.deletePost(postId)">글 삭제</button>
      </div>
    </section>

    <!-- 게시글 본문 -->
    <main>
      <h2>
        {{ post.title }}
      </h2>
      <p>
        닉네임 : {{ post.user.nickname }} | 
        작성일 : {{ post.created_at.slice(0, 10) }} | 
        수정일 : {{ post.updated_at.slice(0, 10) }}
      </p>
      <hr>
      <p>
        {{ post.content }}
      </p>
    </main><hr>
    
    <section>
      <h6>댓글 | {{ comments.length }}</h6>
      <article v-for="comment in comments" :key="comment.id" class="row">

        <!-- 댓글 본문 -->
        <div class="col-10">
          <p class="m-0">{{ comment.user.nickname }}</p>
          <p v-if="editingCommentId !== comment.id" class="fw-light m-0">{{ comment.content }}</p>
          <textarea v-else v-model.trim="editingCommentContent" rows="2" class="form-control"></textarea>
          <p class="fw-lighter">{{ comment.created_at.slice(0, 10) }}. {{ comment.created_at.slice(11, 16) }}</p>
        </div>

        <!-- 댓글 수정 및 삭제 -->
        <div v-if="userStore.isLogIn && comment.user.username === userStore.userInfo.username" class="d-flex justify-content-end align-self-center col-2">
          <div v-if="editingCommentId !== comment.id">
            <button @click="startEditComment(comment)" class="btn btn-outline-primary btn-sm me-2">
              수정
            </button>
            <button @click="deleteComment(comment.id)" class="btn btn-outline-danger btn-sm">
              삭제
            </button>
          </div>
          <div v-else>
            <button @click="updateComment(comment.id)" class="btn btn-outline-primary btn-sm me-2">
              저장
            </button>
            <button @click="cancelEditComment" class="btn btn-outline-secondary btn-sm">
              취소
            </button>
          </div>
        </div><hr>

      </article>

      <!-- 댓글 작성 -->
      <form @submit.prevent="createComment">
        <div class="mb-3">
          <textarea class="form-control" placeholder="댓글을 남겨보세요" v-model.trim="commentContent" rows="3"></textarea>
        </div>
        <input type="submit" value="등록" class="btn btn-outline-success login-btn">
      </form>
    </section>
  </div>
</template>

<script setup>
import Header from '@/components/Header.vue'
import { ref, onMounted } from 'vue'
import { usePostStore } from '@/stores/post'
import { useUserStore } from '@/stores/user'
import { useRoute } from 'vue-router'
import axios from 'axios'

const postStore = usePostStore()
const userStore = useUserStore()
const route = useRoute()

const post = ref(null)
const postId = route.params.id
const comments = ref([])
const commentContent = ref('')
const editingCommentId = ref(null)
const editingCommentContent = ref('')


// 게시글 상세 조회
const readPostDetail = function () {
  axios({
    method: 'get',
    url: `${postStore.API_URL}/posts/${postId}/`,
  })
  .then(res => {
    post.value = res.data
    comments.value = res.data.comment_set
    postStore.currentPost = { title: res.data.title, content: res.data.content }
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
      url: `${postStore.API_URL}/posts/${postId}/comments/${commentId}/`,
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
    .then(res => {
      comments.value = comments.value.filter(comment => comment.id !== commentId)
    })
    .catch(err => console.error(err))
  }
}

// 댓글 수정
const updateComment = function (commentId) {
  axios({
    method: 'put',
    url: `${postStore.API_URL}/posts/${postId}/comments/${commentId}/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
    data: { content: editingCommentContent.value }
  })
  .then(res => {
    const index = comments.value.findIndex(comment => comment.id === commentId)
    if (index !== -1) {
      comments.value[index] = res.data
    }
    editingCommentId.value = null
    editingCommentContent.value = ''
  })
  .catch(err => console.error(err))
}

// 댓글 수정 모드 시작
const startEditComment = function(comment) {
  editingCommentId.value = comment.id
  editingCommentContent.value = comment.content
}

// 댓글 수정 모드 취소
const cancelEditComment = function() {
  editingCommentId.value = null
  editingCommentContent.value = ''
}
</script>

<style scoped>

</style>