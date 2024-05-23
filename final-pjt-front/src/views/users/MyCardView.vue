<template>
  <div>
    <Header />
  </div>
  <main>
    <div class="main-bg">
      <div class="title">내 관심카드 모아보기</div>
      <div class="contain" v-if="(userStore.userInfo.favorite_cards.length < 4) && (userStore.userInfo.favorite_cards.length > 0)" style="width: 50%;">
        <Carousel :items-to-show="userStore.userInfo.favorite_cards.length" class="carousel-wrap">
          <Slide v-for="slide in userStore.userInfo.favorite_cards" :key="slide">
            <div class="carousel__item">
              <RouterLink :to="{ name:'cardDetail', params:{ id:slide }}">
                <MyCardItem
                :card_id="slide"
                />
              </RouterLink>
            </div>
          </Slide>
        </Carousel>
      </div>
      <div class="contain" v-if="userStore.userInfo.favorite_cards.length >= 4">
        <Carousel :items-to-show="3.95" :wrap-around="true" class="carousel-wrap" :autoplay="2000" :loop="true" :pauseAutoplayOnHover="true">
          <Slide v-for="slide in userStore.userInfo.favorite_cards" :key="slide">
            <div class="carousel__item">
              <RouterLink :to="{ name:'cardDetail', params:{ id:slide }}">
                <MyCardItem
                :card_id="slide"
                />
              </RouterLink>
            </div>
          </Slide>
          
          <template #addons>
            <Pagination style="position: absolute; bottom: 5%;"/>
            <Navigation />
          </template>
        </Carousel>
      </div>
      <div class="contain" v-if="userStore.userInfo.favorite_cards.length == 0">
        <img src="@/assets/img/Empty.png" alt="" style="width: 30%; margin-top: -2%;">
        <RouterLink :to="{ name:'cardList' }">
          <div style="margin-top: -15%; margin-bottom: 15%;">관심 카드가 없어요.</div>
          <button style="font-weight: bold;">카드 보러 가기</button>
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
.title {
  width: 100%;
  margin-top: 3%;
  margin-left: 8%;
  font-size: 20px;
  font-weight: bold;
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
.carousel__viewport {
  height: 100% !important;
}

.contain {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
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