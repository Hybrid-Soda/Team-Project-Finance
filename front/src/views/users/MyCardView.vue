<template>
  <div>
    <Header />
  </div>
  <main>
    <div class="main-bg">
      <div class="contain">
        <Carousel v-bind="settings" :breakpoints="breakpoints" class="carousel-wrap">
          <Slide v-for="slide in 10" :key="slide">
            <div class="carousel__item">{{ slide }}</div>
          </Slide>
            
          <template #addons>
            <Navigation />
          </template>
        </Carousel>
      </div>
    </div>
  </main>
</template>

<script setup>
  import Header from '@/components/Header.vue'
  // import MyCardItem from '@/components/MyCardItem.vue'
  // import axios from 'axios';
  import { ref, onMounted, defineComponent } from 'vue'
  import { Carousel, Navigation, Slide, Pagination } from 'vue3-carousel'
  import 'vue3-carousel/dist/carousel.css'
  
  const settings = ref({
    itemsToShow: 1,
    snapAlign: 'center',
  });
  const breakpoints = ref({
    // 700px and up
    700: {  
        itemsToShow: 3.5,
        snapAlign: 'center',
      },
      // 1024 and up
      1024: {
        itemsToShow: 5,
        snapAlign: 'start'
      }
  })

  import { useUserStore } from '@/stores/user';
  const userStore = useUserStore()
  
  const cards = ref(null)
  onMounted(() => {
    cards.value = userStore.userInfo.favorite_cards
  })

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
/* ca */
.carousel__item {
  min-height: 200px;
  width: 100%;
  background-color: var(--vc-clr-primary);
  color: var(--vc-clr-white);
  font-size: 20px;
  border-radius: 8px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.carousel__slide {
  padding: 10px;
}

.carousel__prev,
.carousel__next {
  box-sizing: content-box;
  border: 5px solid white;
}

.contain {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.carousel-wrap {
  border: 4px solid pink;
  width: 90%;
  height: 90%;
}
</style>