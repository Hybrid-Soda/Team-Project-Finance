<template>
  <div class="row">
    <!-- 댓글 본문 -->
    <div class="col-8">
      <p class="m-0">{{ comment.user.nickname }}</p>
      <p v-if="editValueId !== comment.id" class="fw-light mb-1">{{ comment.content }}</p>
      <textarea v-else class="form-control" v-model.trim="editValue" rows="2"></textarea>
      <p class="fw-lighter">{{ comment.created_at.slice(0, 10) }}</p>
    </div>

    <div v-if="comment.user.username === userStore.userInfo?.username" class="d-flex align-self-start col-4 justify-content-end">
      <div v-if="editValueId !== comment.id" class="d-flex">
        <button @click="startEdit(comment)" class="btn btn-outline-primary btn-sm me-2">
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
        <button @click="cancelEdit" class="btn btn-outline-secondary btn-sm">
          취소
        </button>
      </div>
    </div><hr>
  </div>
</template>

<script setup>
import axios from 'axios'

import { ref, defineProps, defineEmits } from 'vue'
import { usePostStore } from '@/stores/post'
import { useUserStore } from '@/stores/user'

const emit = defineEmits(['deleteComment', 'updateComment'])
const postStore = usePostStore()
const userStore = useUserStore()

const editValueId = ref(null)
const editValue = ref('')

const props = defineProps({
  comment: {
    type: Object,
    required: true
  },
  post: {
    type: Object,
    required: true
  },
})

// 댓글 삭제
const deleteComment = function () {
  if (window.confirm('정말 삭제하시겠습니까?')) {
    axios({
      method: 'delete',
      url: `${postStore.API_URL}/posts/${props.post.id}/comments/${props.comment.id}/`,
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
    .then(res => emit('deleteComment', props.comment.id))
    .catch(err => console.error(err))
  }
}

// 댓글 수정
const updateComment = function () {
  axios({
    method: 'put',
    url: `${postStore.API_URL}/posts/${props.post.id}/comments/${props.comment.id}/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
    data: { content: editValue.value }
  })
  .then(res => emit('updateComment', props.comment.id, res.data))
  .catch(err => console.error(err))

  editValueId.value = null
    editValue.value = ''
}

// 댓글 수정 모드 시작
const startEdit = function(comment) {
  editValueId.value = comment.id
  editValue.value = comment.content
}

// 댓글 수정 모드 취소
const cancelEdit = function() {
  editValueId.value = null
  editValue.value = ''
}
</script>

<style scoped>
</style>
