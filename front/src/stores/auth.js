import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', () => {
  const router = useRouter()

  const isAuthenticated = ref(false)
  const userInfo = ref(null)
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)

  // 유저정보
  const getUserInfo = function (username) {
    axios({
      method: 'get',
      url: `${API_URL}/users/${username}/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => {
      userInfo.value = res.data
    })
    .catch(err => console.error(err))
  }

  // 회원가입
  const signUp = function (payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
    .then(res => {
      alert('회원가입이 완료되었습니다!')
      router.push({ name: 'login' })
    })
    .catch(err => console.error(err))
  }

  // 로그인
  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
    .then(res => {
      token.value = res.data.key
      getUserInfo(username)
      isAuthenticated.value = true
      router.push({ name: 'home' })
    })
    .catch(err => console.error(err))
  }

  // 로그아웃
  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
    .then(res => {
      token.value = null
      userInfo.value = null
      isAuthenticated.value = false
      router.push({ name: 'home' })
    })
    .catch(err => console.error(err))
  }

  // 프로필변경
  const changeProfile = function (payload) {
    const { username, nickname, gender, email, age } = payload

    axios({
      method: 'put',
      url: `${API_URL}/users/${username}/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
      data: {
        username, nickname, gender: '남자', email, age
      }
    })
    .then(res => {
      userInfo.value = res.data
    })
    .catch(err => console.error(err))
  }

  return {
    token, isAuthenticated, userInfo, 
    signUp, logIn, logOut, changeProfile
  }
}, { persist: true })
