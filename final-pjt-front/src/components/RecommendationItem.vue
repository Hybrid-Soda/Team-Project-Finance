<template>
  <!-- <div class="wrap">
    <header>
      <img :src="card?.image_url" class="card-img">
      <div class="title">{{ card?.title }}</div>
    </header>
    <main> 
      <p>혜택</p>
      <p>실적</p>
    </main>
  </div> -->
</template>

<script setup>
  import { ref, defineProps, onMounted } from 'vue'
  import axios from 'axios';
  import { useCardStore } from '@/stores/card';
  const cardStore = useCardStore()

</script>

<style scoped>
.wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  width: 100%;
  height: 100%;
}
header, main {
  display: flex;
  flex-direction: column;
  align-items: center;
}
header {
  gap: 20px;
}
img {
  width: 50%;
}
.title {
  font-size: 24px;
  color: black;
  font-weight: bold;
}
.card-img {
  width: 90%;
  height: 90%;
  object-fit: contain;
}
</style>