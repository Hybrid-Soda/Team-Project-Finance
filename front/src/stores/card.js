import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'

export const useCardStore = defineStore('card', () => {
  const cards = ref(null)
  const API_URL = 'http://127.0.0.1:8000'
  const brands = ['BC카드', '부산은행', '대구은행', '기업은행', '국민카드', '농협카드']

  const readCard = function () {
    axios({
      method: 'get',
      url: `${API_URL}/cards/`,
    })
    .then(res => {
      cards.value = res.data
    })
    .catch(err => console.error(err))
  }

  return {
    cards, brands, API_URL,
    readCard,
  }
})
