import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import { useUserStore } from '@/stores/user'

export const usePostStore = defineStore('post', () => {
  const userStore = useUserStore()
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()
  const posts = ref(null)
  const tempPosts = ref([])

  // 게시글 생성
  const createPost = function (payload) {
    const { title, content } = payload
  
    axios({
      method: 'post',
      url: `${API_URL}/posts/`,
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
      data: {
        title, content
      }
    })
    .then(res => {
      router.push({ name: 'postList' })
    })
    .catch(err => {
      alert('게시글 업로드에 실패했습니다.')
      console.error(err)
    })
  }
  
  // 게시글 조회
  const readPost = function () {
    axios({
      method: 'get',
      url: `${API_URL}/posts/`,
    })
    .then(res => {
      posts.value = res.data
      tempPosts.value = posts.value
    })
    .catch(err => console.error(err))
  }

  // 게시글 삭제
  const deletePost = function (postId) {
    if (window.confirm('정말 삭제하시겠습니까?')) {
      axios({
        method: 'delete',
        url: `${API_URL}/posts/${postId}/`,
        headers: {
          Authorization: `Token ${userStore.token}`
        }
      })
      .then((res) => {
        posts.value = posts.value.filter(post => post.id !== postId)
        alert('게시글이 삭제 되었습니다')
      })
      .catch(err => console.error(err))
    }
  }

  // 게시글 수정
  const updatePost = function (payload) {
    const { postId, title, content } = payload
  
    axios({
      method: 'put',
      url: `${API_URL}/posts/${postId}/`,
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
      data: {
        title, content
      }
    })
    .then(res => {
      router.push({ name: 'postList' })
      alert('게시글 수정을 완료했습니다')
    })
    .catch(err => {
      alert('게시글 수정에 실패했습니다')
      console.error(err)
    })
  }

  const searchPost = function (payload) {
    const { searchValue, searchOption } = payload
    
    tempPosts.value = posts.value.filter((post) => {
      if (searchOption === 'writer') {
        return post.user.includes(searchValue)
      } else {
        return post.content.includes(searchValue)
      }
    })
  }
  return {
    posts, tempPosts, API_URL,
    createPost, readPost, updatePost, deletePost, searchPost,
  }
}, { persist: true })
