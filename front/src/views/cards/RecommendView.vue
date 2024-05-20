<template>
  <div class="container">
    <Header />
      <h1>Recommend</h1>
    <div v-for="card in recommendCards" :key="card.id">
      <p>{{ card.name }}</p>
      <img :src="card.image_url" width="300px">
      <p>브랜드 : {{ card.brand }}</p>
      <p>연회비1 : {{ card.annual_fee1 }}</p>
      <p>연회비2 : {{ card.annual_fee2 }}</p>
      <p>전월실적 : {{ card.record }}</p>
      <p>타입 : {{ card.type }}</p>
    </div>
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
const recommendCards = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${cardStore.API_URL}/cards/${userStore.userInfo.username}/recommend/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
  .then(res => {
    recommendCards.value = res.data
  })
  .catch(err => console.error(err))
})
</script>

<style scoped>

</style>