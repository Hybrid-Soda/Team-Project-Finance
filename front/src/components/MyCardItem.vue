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
  import axios from 'axios';
  import { useCardStore } from '@/stores/card';
  const cardStore = useCardStore()

  const props = defineProps({
    card_id: Number
  })

  const card = ref(null)
  const itemRefs = ref(null)
  const isRotate = ref(false)
  onMounted(() => {
    axios({
      method: 'get',
      url: `${cardStore.API_URL}/cards/${props.card_id}/`,
    })
    .then(res => {
      card.value = res.data
      // console.log(card.value)
    })
    .then(() => {
      // console.log('w',itemRefs.value.width)
      // console.log('h',itemRefs.value.height)
      if (itemRefs.value.width > itemRefs.value.height) {
        isRotate.value = true
      }
    })
    .catch(err => console.error(err))
  })

  const isHovered = ref(false)
  const hover = function() {
    isHovered.value = !isHovered.value
  }

</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 25rem;
}
img {
  width: 70%;
  height: 100%;
}
img:hover {
  filter: blur(4px);
  -webkit-filter: blur(4px);
  transition-duration: .3s;
  filter: brightness(10%);
}
.vertical {
  transform: rotate(90deg);
  scale: 1.6;
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