<template>
  <div style="height: 100%;">
    <Header />
    <main>
      <div class="bg">
        <div class="head">
          <img src="../assets/img/CreditCard.png" alt="">
          내 카드를 찾아보자 !
          <progress value="25" min="0" max="100"></progress>
        </div>
        <div class="content">
          <div class="title">
            오늘은 놀러가는 날! 여행지까지 나는...
          </div>
          <div class="question">
            <button class="question-item">차가 있으니 내 차로 가야지!</button>
            <button class="question-item">차가 없으니 버스 타고 가야지!</button>
            <!-- <button class="question-item">차가 없으니 버스 타고 가야지!</button>
            <button class="question-item">차가 없으니 버스 타고 가야지!</button> -->
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import Header from '@/components/Header.vue';
</script>

<style scoped>
main {
  display: flex;
  justify-content: center;
  height: 80%;
}
img {
  width: 20%;
}
.bg {
  width: 70%;
  border-radius: 50px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
  /* background-color: rgb(33, 95, 255); */
  margin-top: 40px;
  display: flex;
  align-items: center;
  flex-direction: column;
  gap: 10%;
  padding-top: 2%;
}
.content {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  gap: 50px;
  /* height: 70%; */
}
.head {
  font-size: large;
  font-weight: bold;
  width: 70%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
progress {
  margin-top: 3%;
  width: 60%;
}
.title {
  font-size: large;
  font-weight: bold;
}
.question {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 30px;
  width: 150%;
}
.question-item {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
}
.question-item:hover {
  background-color: rgb(255, 199, 39);
  color: black;
  font-weight: bold;
}
</style>