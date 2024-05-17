import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCardStore = defineStore('card', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const signUp = function (payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
     .then((response) => {
       console.log('회원가입 성공!')
       const password = password1
       logIn({ username, password })
     })
     .catch((error) => {
       console.log(error)
     })
  }

  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((response) => {
        token.value = response.data.key
        router.push({ name : 'cardList' })
      })
      .catch((error) => {
        console.log(error)
      })
  }
  
  
  const brands = ['BC카드', '부산은행', '대구은행', '기업은행', '국민카드', '농협카드']



  return { brands, signUp, logIn }
})
