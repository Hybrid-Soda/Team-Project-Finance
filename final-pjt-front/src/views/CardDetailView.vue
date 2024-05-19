<template>
  <div>
    <Header />
  </div>
  <main>
    <div class="card-page-bg">
      <div class="menu-wrap">
        <button @click="this.$router.go(-1)" class="backBtn"><img src="../assets/img/backArrow.png" alt="" class="backImg"></button>
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
  height: 80%;
}
.card-page-bg {
  width: 70%;
  border-radius: 50px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
  margin-top: 40px;
}
.menu-wrap {
  /* border: 2px solid blue; */
  display: flex;
  height: 100%;
  width: 100%;
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
  width: 100%;
  height: 100%;
  padding-top: 7%;
}
.backBtn {
  position: absolute;
  margin: 20px;
  background-color: rgba(0, 0, 0, 0);
}
.backImg {
  width: 50px;
  opacity: .5;
}
</style>