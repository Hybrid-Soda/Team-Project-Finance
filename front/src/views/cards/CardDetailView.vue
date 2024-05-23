<template>
  <div class="container">
    <Header />
    <main v-if="card">
      <div class="card-page-bg">
        <div class="menu-wrap">
          <button @click="this.$router.go(-1)" class="backBtn">
          <!-- <RouterLink :to="{ name:'cardList' }"> -->
            <button class="backBtn">
              <img src="@/assets/img/backArrow.png" alt="goBack" class="backImg">
            </button>
          <!-- </RouterLink> -->
          </button>
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
  margin-top: 2%;
  width: 100%;
}
.card-page-bg {
  border-radius: 50px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
  width: 100%;
  height: 100%;
}
.menu-wrap {
  /* border: 2px solid blue; */
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
  /* border: 2px solid green; */
  display: flex;
  flex-direction: column;
  justify-content: center;
  background-color: rgba(0, 0, 0, 0);

}
.backBtn {
  position: absolute;
  margin: 0 15px;
  background-color: rgba(0, 0, 0, 0);
}
.backImg {
  width: 50px;
  opacity: .5;
}
</style>