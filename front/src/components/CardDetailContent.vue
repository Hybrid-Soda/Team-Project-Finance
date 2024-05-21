<template>
  <div class="content">
    <img :src="src" alt="" class="d-img" v-if="benefit.title in cardStore.benefit_dict">
    <img src="@/assets/img/icons/default.png" alt="" class="d-img" v-else>
    <div class="detail">
      <p class="title">{{ benefit.title }}</p>
      <p>{{ benefit.content }}</p>
    </div>
  </div>
</template>

<script setup>
import { useCardStore } from '@/stores/card'
import { ref, defineProps } from 'vue'
const props = defineProps({
  benefit: Object
})
const cardStore = useCardStore()
const src = new URL(`../assets/img/icons/${ cardStore.benefit_dict[`${props.benefit.title}`]}.png`, import.meta.url)
</script>

<style scoped>
.content {
  display: flex;
  align-items: center;
  margin: 2% 0;
  gap: 5%;
  width: 50%;
}
.d-img {
  width: 12%;
  opacity: .7;
}
.detail {
  width: 100%;
}
.title {
  color: black;
  font-size: 24px;
  font-weight: 800;
}
p {
  margin: 0;
}
</style>