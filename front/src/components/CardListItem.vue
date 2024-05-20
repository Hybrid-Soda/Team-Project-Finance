<template>
  <RouterLink class="wrap" :to="{ name:'cardDetail', params: { 'id': card.id } }">
    <div>
      <img :src="card.image_url" alt="" class="card-img">
    </div>
    <div class="card-content">
      <h2 style="color: black;">{{ card.name }}</h2>
      <ul>
        <li>{{ card.brand }}</li>
        <li v-if="card.record > 0">전월 실적 : {{ card.record }}만원 이상</li>
        <li v-else>전월 실적 : 없음</li>
        <li v-if="card.annual_fee1 > 0">연회비 : {{ card.annual_fee1 }} 원</li>
        <li v-else>연회비 : 없음</li>
      </ul>
    </div>
  </RouterLink>
  <hr style="width: 90%;">
</template>

<script setup>
  import { ref, defineProps } from 'vue'
  import { RouterLink } from 'vue-router'

  defineProps({
    card: Object
  })
</script>

<style scoped>
.wrap {
  display: flex;
  gap: 10%;
  align-items: center;
  margin: 2% auto;
}
.wrap:hover {
  opacity: 0.5;
  -webkit-transition-duration: .3s;
  -webkit-transition-timing-function: ease-out;

}
.card-img {
  width: 300px;
  height: 300px;
  object-fit: contain;
}
ul {
  padding: 10px;
  padding-top: 20px;
}
li {
  margin: 10px 0;
}
</style>