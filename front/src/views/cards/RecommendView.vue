<template>
  <div>
    <Header />
  </div>
  <main>
    <div class="main-bg">
      <div id="rec_cards" class="page-wrap">
        <h1 style="margin-top: 4%;">추천 카드 모아보기</h1>
        <div class="contain">
          <Carousel :items-to-show="4" :wrap-around="true" class="carousel-wrap">
            <Slide v-for="slide in userStore.userInfo.survey_set" :key="slide">
              <RouterLink :to="{ name:'cardDetail', params:{id:slide} }">
                <div class="carousel__item">
                  <RecommendationItem
                  :card_id="slide"
                  />
                </div>
              </RouterLink>
            </Slide>
            
            <template #addons>
              <Pagination style="position: absolute; bottom: 5%;"/>
              <Navigation />
            </template>
          </Carousel>
          <button @click="goDown()">아래로</button>
        </div>
      </div>
      <div id="sim_cards" class="page-wrap">
        <h1 style="margin-top: 4%;">나와 비슷한 사용자는 이런 카드를 사용했어요</h1>
        <div class="contain">
          <Carousel :items-to-show="4" :wrap-around="true" class="carousel-wrap">
            <Slide v-for="slide in userStore.userInfo.survey_set" :key="slide">
              <RouterLink :to="{ name:'cardDetail', params:{id:slide} }">
                <div class="carousel__item">
                  <RecommendationItem
                  :card_id="slide"
                  />
                </div>
              </RouterLink>
            </Slide>
            
            <template #addons>
              <Pagination style="position: absolute; bottom: 5%;"/>
              <Navigation />
            </template>
          </Carousel>
          <button @click="goUp()">위로</button>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
  import Header from '@/components/Header.vue'
  import RecommendationItem from '@/components/RecommendationItem.vue'
  // import axios from 'axios';
  import { ref, onMounted, defineComponent } from 'vue'
  import { RouterLink } from 'vue-router'
  import { Carousel, Navigation, Slide, Pagination } from 'vue3-carousel'
  import 'vue3-carousel/dist/carousel.css'

  import { useUserStore } from '@/stores/user';
  const userStore = useUserStore()

  function goDown() {
    document.querySelector(".main-bg").scrollTo({top: document.querySelector("#sim_cards").offsetTop, behavior: 'smooth'});
  }
  function goUp() {
    document.querySelector(".main-bg").scrollTo({top: document.querySelector("html").offsetTop, behavior: 'smooth'});
  }
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
  overflow: hidden;
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
.page-wrap {
  width: 100%;
  height: 1000px;
  border: 2px solid red;
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
/* main */
.contain {
  width: 100%;
  height: 90%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 5%;
  border: 1px solid blue;
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