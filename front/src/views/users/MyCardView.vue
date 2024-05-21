<template>
  <div>
    <Header />
  </div>
  <main>
    <div class="main-bg">
      <div class="card-wrap">
        <div class="card-item">
          <MyCardItem />
        </div>
        <div class="line"></div>
        <div class="card-item">
          <MyCardItem />
        </div>
        <div class="line"></div>
        <div class="card-item">
          <MyCardItem />
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
  import Header from '@/components/Header.vue'
  import MyCardItem from '@/components/MyCardItem.vue'

</script>

<style scoped>
main {
  height: 85%;
}
.main-bg {
  background-image: url("@/assets/img/Rectangle 3.png");
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  height: 100%;
}
.card-wrap {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 5%;
}
.card-item {
  width: 30%;
  height: 100%;
}
.line {
  height: 80%;
  border: 1px solid rgb(224, 224, 224);
}
</style>