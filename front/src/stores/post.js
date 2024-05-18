import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import { useAuthStore } from '@/stores/auth'

export const usePostStore = defineStore('post', () => {
  const authStore = useAuthStore()
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()
  const posts = ref(null)

  // 게시글 조회
  const readPosts = function () {
    axios({
      method: 'get',
      url: `${API_URL}/posts/`,
    })
    .then(res => {
      posts.value = res.data
    })
    .catch(err => console.error(err))
  }

  // 게시글 생성
  const createPost = function (payload) {
    const { title, content } = payload
  
    axios({
      method: 'post',
      url: `${API_URL}/posts/`,
      headers: {
        Authorization: `Token ${authStore.token}`,
      },
      data: {
        title, content
      }
    })
    .then(res => {
      console.log(res.data)
      router.push({ name: 'postDetail', params: { 'id': res.data.id } })
    })
    .catch(err => {
      alert('게시글 업로드에 실패했습니다.')
      console.error(err)
    })
  }

  return {
    posts, 
    readPosts, createPost }
})
