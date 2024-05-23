<template>
  <div class="container">
    <div class="box">
      <div class="imgBox" @mouseover="hover()" @mouseout="hover()">
        <img :src="card?.image_url" ref="itemRefs" :class="{'vertical':isRotate}">
      </div>
      <div class="card-name" v-if="isHovered">
        <div class="card-content">
          {{ card?.name }}
        </div>
      </div>
      <main> 
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, defineProps, onMounted } from 'vue'

const props = defineProps({
  card: {
    type: Object,
    required: true
  }
})

const itemRefs = ref(null)
const isRotate = ref(false)
const isHovered = ref(false)
const hover = function() {
  isHovered.value = !isHovered.value
}

onMounted(() => {
  if (itemRefs.value.width > itemRefs.value.height) {
    isRotate.value = true
  }
})

</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 20px;
  width: 25rem;
}
img {
  width: 50%;
  object-fit: contain;
}
img:hover {
  filter: blur(4px);
  -webkit-filter: blur(4px);
  transition-duration: .3s;
  filter: brightness(10%);
}
.vertical {
  transform: rotate(90deg);
  scale: 1.7;
}
.card-name {
  position: absolute;
  width: 50%;
  display: flex;
  display: flex;
  align-items: center;
  justify-content: center;
}
.box {
  display: flex;
  justify-content: center;
  align-items: center;
}
.card-content {
  color: white;
  word-break: keep-all; 
  font-size: 24px; 
  font-weight: bold;
}
</style>