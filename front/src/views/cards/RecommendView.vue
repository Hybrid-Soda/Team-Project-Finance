<template>
  <div class="container">
    <Header />
      <h1>Recommend</h1>
    <p>{{ recommendCardPk }}</p>
  </div>
</template>

<script setup>
import Header from '@/components/Header.vue'
import { useCardStore } from '@/stores/card'
import { useUserStore } from '@/stores/user'
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'

const cardStore = useCardStore()
const userStore = useUserStore()
const recommendCardPk = ref(null)
const recommendCards = computed(() => {
  
  return
})

onMounted(() => {
  axios({
    method: 'get',
    url: `${cardStore.API_URL}/cards/${userStore.userInfo.username}/recommend/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
  .then(res => {
    recommendCardPk.value = res.data
  })
  .catch(err => console.error(err))
})
</script>

<style scoped>

</style>