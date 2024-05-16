<template>
  <div>
    <Header />
  </div>
  <main>
    <div class="card-page-bg">
      <div class="menu-wrap">
        <ul style="border: 2px solid red;">
          <li>개요</li>
          <li>혜택 정보</li>
          <li>카드 신청</li>
          <li>사용자 리뷰</li>
        </ul>
        <div class="info-wrap">
          <CardDetailItem />
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
  import { ref } from 'vue'
  import Header from '@/components/Header.vue';
  import CardDetailItem from '@/components/CardDetailItem.vue'

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
  justify-content: center;
  
}
li {
  display: inline;
  margin: 0 5%;
}
.info-wrap {
  border: 2px solid green;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
</style>