import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCardStore = defineStore('card', () => {
  const count = ref(0)

  return { count }
})
