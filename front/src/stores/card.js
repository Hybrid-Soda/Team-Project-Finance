import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'

export const useCardStore = defineStore('card', () => {
  
  const brands = ['BC카드', '부산은행', '대구은행', '기업은행', '국민카드', '농협카드']

  return { brands }
})
