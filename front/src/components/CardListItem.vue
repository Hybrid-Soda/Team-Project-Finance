<template>
  <RouterLink class="wrap" :to="{ name:'cardDetail' }">
    <div>
      <img src="@/assets/img/example_card.png" alt="" class="card-img">
    </div>
    <div class="card-content">
      <h2 style="color: black;">신한카드 Point Plan</h2>
      <ul>
        <li>큰 소비일수록 계획이 필요한 법</li>
        <li>실적: 30만원 이상</li>
        <li>연회비: 50,000 원</li>
      </ul>
    </div>
  </RouterLink>
  <hr style="width: 90%;">
</template>

<script setup>
  import { ref } from 'vue'
  import { RouterLink } from 'vue-router';

</script>

<style scoped>
.wrap {
  display: flex;
  gap: 10%;
  align-items: center;
  margin: 5% auto;
}
.wrap:hover {
  opacity: 0.5;
  -webkit-transition-duration: .3s;
  -webkit-transition-timing-function: ease-out;

}
.card-img {
  width: 300px;
}
ul {
  padding: 10px;
  padding-top: 20px;
}
li {
  margin: 10px 0;
}
</style>