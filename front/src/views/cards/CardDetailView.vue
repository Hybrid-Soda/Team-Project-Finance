<template>
  <div class="container">
    <Header />
    <main v-if="card">
      <RouterLink :to="{ name: 'cardList' }">뒤로가기</RouterLink>
      <!-- <ul>
        <li><a href="">개요</a></li>
        <li><a href="">혜택 정보</a></li>
        <li><a href="">사용자 리뷰</a></li>
      </ul> -->
      <div class="card-page-bg">
        <div class="menu-wrap">
          <div class="info-wrap">
            <CardDetailItem :card="card"/>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import CardDetailItem from '@/components/CardDetailItem.vue'
import Header from '@/components/Header.vue'
import axios from 'axios'

import { ref, onMounted } from 'vue'
import { useCardStore } from '@/stores/card'
import { useRoute, RouterLink } from 'vue-router'

const cardStore = useCardStore()
const route = useRoute()

const cardId = route.params.id
const card = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${cardStore.API_URL}/cards/${cardId}/`,
  })
  .then(res => {
    card.value = res.data
  })
  .catch(err => console.error(err))
})
</script>

<style scoped>
main {
  display: flex;
  justify-content: center;
  height: 843px;
  overflow: hidden;
}
.card-page-bg {
  width: 70%;
  height: 1000px;
  border-radius: 50px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
  margin-top: 40px;
}
.menu-wrap {
  border: 2px solid blue;
  margin-top: 2%;
}
ul {
  display: flex;
  flex-direction: column;
  align-items: end;
  width: 150px;  
  padding-top: 200px;
  gap: 20px;
  padding-right: 20px;
}
li {
  /* display: inline; */
  margin: 0 5%;
  font-size: large;
  font-weight: 500;
}
.info-wrap {
  border: 2px solid green;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
</style>