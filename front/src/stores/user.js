import axios from 'axios'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useUserStore = defineStore('user', () => {
  const isLogIn = computed(() => {
    return token.value === null ? false : true
  })
  const router = useRouter()
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
    const { username, password1, password2, nickname, gender, email, age } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, nickname, gender, email, age
      }
    })
    .then((res) => {
      Swal.fire({
        title: '성공',
        text: '회원가입이 완료되었습니다.',
        icon: 'success',
        confirmButtonText: '로그인 하러 가기'
      }).then ((res) => {
        if (res.isConfirmed) {
          router.push({ name:'signIn' })
        }
      })
    })
    .catch(err => {console.error(err)})
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
      router.push({ name: 'home' })
    })
    .catch(err => console.error(err))
  }

  // 프로필 변경
  const updateProfile = function (payload) {
    const { username, nickname, gender, email, age } = payload

    axios({
      method: 'put',
      url: `${API_URL}/users/${username}/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
      data: {
        username, nickname, gender, email, age
      }
    })
    .then(res => {
      userInfo.value = res.data
      window.alert('저장 되었습니다!')
    })
    .catch(err => console.error(err))
  }

  // 비밀번호 변경
  const changePassword = function (payload) {
    const { new_password1, new_password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/password/change/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
      data: {
        new_password1, new_password2
      }
    })
    .then(res => {
      window.alert('비밀번호가 변경되었습니다!')
      router.push({ name: 'myPage', params: { 'username': userInfo.username } })
    })
    .catch(err => console.error(err))
  }

  // 로그인 창 경고
  const login_alert = function() {
    Swal.fire({
      title: '잠시만요.',
      text: '로그인이 필요한 페이지입니다!',
      icon: 'info',
      confirmButtonText: '로그인 하러 가기'
    }).then ((res) => {
      if (res.isConfirmed) {
        router.push({ name:'signIn' })
      }
    })
  }
  return {
    token, isLogIn, userInfo, 
    signUp, logIn, logOut, updateProfile, changePassword, login_alert
  }
}, { persist: true })
