<template>
  <div>
    <Header />
  </div>
  <main>
    <div class="main-bg">
      <h1 style="margin-top: 4%;">내 관심카드 모아보기</h1>
      <div class="contain" v-if="userStore.userInfo.favorite_cards">
        <Carousel :items-to-show="4" :wrap-around="true" class="carousel-wrap" :autoplay="2000">
          <Slide v-for="slide in userStore.userInfo.favorite_cards" :key="slide">
            <div class="carousel__item">
              <MyCardItem
              :card_id="slide"
              />
            </div>
          </Slide>
          
          <template #addons>
            <Pagination style="position: absolute; bottom: 5%;"/>
            <Navigation />
          </template>
        </Carousel>
      </div>
      <div class="contain" v-else>
        <img src="@/assets/img/404Error.png" alt="" style="width: 300px;">
        <p>관심 카드가 없어요</p>
        <RouterLink :to="{ name:'cardList' }">
          <button>카드 보러 가기</button>
        </RouterLink>
      </div>
    </div>
  </main>
</template>

<script setup>
  import Header from '@/components/Header.vue'
  import MyCardItem from '@/components/MyCardItem.vue'
  // import axios from 'axios';
  import { ref, onMounted, defineComponent } from 'vue'
  import { Carousel, Navigation, Slide, Pagination } from 'vue3-carousel'
  import 'vue3-carousel/dist/carousel.css'

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
  height: 100%;
  width: 100%;
  background-color: var(--vc-clr-primary);
  color: var(--vc-clr-white);
  font-size: 20px;
  border-radius: 8px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: white;
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
  /* border: 4px solid pink; */
  width: 90%;
  height: 90%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>