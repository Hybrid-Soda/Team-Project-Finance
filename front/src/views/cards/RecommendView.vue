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
  <div id="carouselExampleIndicators" class="carousel slide">
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="..." class="d-block w-100" alt="...">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
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