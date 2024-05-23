<template>
  <div class="wrap">
    <div style="width: 90%; height: 100%;">
      <header class="header">
        <div v-if="userStore.isLogIn && post.user.username === userStore.userInfo.username">
          <button class="btn btn-outline-warning me-3">
            <RouterLink :to="{ name: 'postUpdate', params: { 'id': post.id } }">
              수정
            </RouterLink>
          </button>
          <button class="btn btn-outline-danger" @click="deletePost">글 삭제</button>
        </div>
        <div class="title">{{ post.title }}</div>
        <div class="user">
          닉네임 : {{ post.user.nickname }} | 
          작성일 : {{ post.created_at.slice(0, 10) }} | 
          수정일 : {{ post.updated_at.slice(0, 10) }}
        </div>
      </header>

      <main class="main">
        <img
        v-if="post.image"
        class="postImage mt-3"
        :src="`${postStore.API_URL}${post.image}`"
        alt="image">
        <div class="content">{{ post.content }}</div>
        <div>
          <button v-if="likeUsers.includes(userId)" @click="toggleLike" class="my-2">&#9829; {{ likeLength }}</button>
          <button v-else @click="toggleLike" class="my-2">&#9825; {{ likeLength }}</button>
        </div>
      </main>

      <section class="comment">
        <h6>댓글 | {{ comments.length }}</h6>
        <PostComment
        v-for="comment in comments"
        :key="comment.id"
        :post="post"
        :comment="comment"
        @delete-comment="deleteComment"
        @update-comment="updateComment"
        />
        <form @submit.prevent="createComment">
          <textarea class="form-control mb-3" placeholder="댓글을 남겨보세요" v-model.trim="content" rows="3"></textarea>
          <input type="submit" value="등록" class="btn btn-outline-success login-btn"/>
        </form>
      </section>
    </div>
  </div>
</template>

<script setup>
import PostComment from '@/components/PostComment.vue'
import { ref, defineEmits, computed, defineProps } from 'vue'
import { usePostStore } from '@/stores/post'
import { useUserStore } from '@/stores/user'
import axios from 'axios'

const postStore = usePostStore()
const userStore = useUserStore()
const props = defineProps({
  post: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['closeDetail'])

const deletePost = function () {
  postStore.deletePost(props.post.id)
  emit('closeDetail')
}

const comments = computed(() => {
  return props.post.comment_set
})
const content = ref('')
const postId = props.post.id
const userId = userStore.userInfo ? userStore.userInfo.id : 0

const likeUsers = computed(() => {
  return postStore.tempPosts.find(post => post.id === postId).like_users
})
const likeLength = ref(likeUsers.value.length)

// 좋아요 & 취소
const toggleLike = function () {
  axios({
    method: 'post',
    url: `${postStore.API_URL}/posts/${props.post.id}/likes/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
  .then(res => {
    if (res.data.is_liked) {
      postStore.tempPosts.find(post => post.id === postId).like_users.push(userId)
      likeLength.value += 1
    } else {
      postStore.tempPosts.find(post => post.id === postId).like_users = postStore.tempPosts.find(post => post.id === postId).like_users.filter(user => user !== userId)
      likeLength.value -= 1
    }
  })
  .catch(err => console.error(err))
}

// 댓글 생성
const createComment = function () {
  if (userStore.isLogIn) {
    axios({
      method: 'post',
      url: `${postStore.API_URL}/posts/${props.post.id}/comments/`,
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
      data: {
        content: content.value
      }
    })
    .then(res => {
      comments.value.push(res.data)
      content.value = ''
    })
    .catch(err => console.error(err))
  } else {
    window.alert('로그인 후 작성해주세요')
  }
}

// 댓글 삭제
const deleteComment = function (commentId) {
  comments.value = comments.value.filter(comment => comment.id !== commentId)
}
// 댓글 수정
const updateComment = function (commentId, resData) {
  const index = comments.value.findIndex(comment => comment.id === commentId)
    if (index !== -1) { comments.value[index] = resData }
}
</script>

<style scoped>
.wrap {
  overflow-y: scroll;
  width: 100%;
  height: 100%
}
.header {
  padding-bottom: 2%;
  border-bottom: 3px solid rgb(224, 224, 224);
}
.title {
  font-size: x-large;
  color: black;
  font-weight: bold;
  margin-bottom: 10px;
}
.main {
  width: 100%;
  display: flex;
  flex-direction: column;
  padding-bottom: 2%;
  border-bottom: 3px solid rgb(224, 224, 224);
}
.content {
  width: 100%;
  display: block;
  margin-top: 3%;
}
.comment {
  margin-top: 3%;
}
.postImage {
  width: 100%;
}
</style>