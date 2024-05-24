<template>
  <div>
    <Header />
  </div>
  <main>
    <div class="main-bg" @mousewheel="goWheel">
      <div id="rec_cards" class="page-wrap">
        <div class="title">추천 카드 모아보기</div>
        <div class="contain">
          <Carousel :items-to-show="3.95" :wrap-around="true" class="carousel-wrap"  :autoplay="2000" :loop="true" :pauseAutoplayOnHover="true">
            <Slide v-for="slide in rec_cardList" :key="slide">
              <div class="carousel__item">
                <RouterLink :to="{ name:'cardDetail', params:{ id:slide.id } }">
                  <RecommendationItem
                  :card="slide"
                  />
                </RouterLink>
              </div>
            </Slide>

            <template #addons>
              <Pagination style="position: absolute; bottom: 5%;"/>
              <Navigation />
            </template>
          </Carousel>
          <button class="move-button" @click="goDown()">↓</button>
        </div>
      </div>

      <div id="sim_cards" class="page-wrap">
        <div style="height: 13.5%;"> </div>
        <div class="title">나와 비슷한 사용자는 이런 카드를 사용했어요</div>
        <div class="contain">
          <Carousel :items-to-show="4" :wrap-around="true" class="carousel-wrap" :autoplay="2000" :loop="true" :pauseAutoplayOnHover="true">
            <Slide v-for="slide in sim_cardList" :key="slide">
              <div class="carousel__item">
                <RouterLink :to="{ name:'cardDetail', params:{ id:slide.id } }">
                  <RecommendationItem
                  :card="slide"
                  />
                </RouterLink>
              </div>
            </Slide>

            <template #addons>
              <Pagination style="position: absolute; bottom: 5%;"/>
              <Navigation />
            </template>
          </Carousel>
          <button class="move-button" @click="goUp()">↑</button>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
  import Header from '@/components/Header.vue'
  import RecommendationItem from '@/components/RecommendationItem.vue'
  import { ref, onMounted, defineComponent } from 'vue'
  import { RouterLink } from 'vue-router'
  import { Carousel, Navigation, Slide, Pagination } from 'vue3-carousel'
  import 'vue3-carousel/dist/carousel.css'
  
  import { useCardStore } from '@/stores/card'
  import { useUserStore } from '@/stores/user'
  import axios from 'axios'

  const userStore = useUserStore()
  const cardStore = useCardStore()

  function goDown() {
    document.querySelector(".main-bg").scrollTo({top: document.querySelector("#sim_cards").offsetTop, behavior: 'smooth'});
  }
  function goUp() {
    document.querySelector(".main-bg").scrollTo({top: document.querySelector("html").offsetTop, behavior: 'smooth'});
  }
  function goWheel(e) {
    if (e.wheelDelta >= 0) {
      goUp()
    } else {
      goDown()
    }
  }

  const sim_cardList = ref([])
  const rec_cardList = ref([])

  onMounted(() => {
    axios({
      method: 'get',
      url: `${cardStore.API_URL}/cards/${userStore.userInfo.username}/recommend/`,
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
    .then(res => {
  
    for (const [key, value] of Object.entries(res.data)) {
      if (key.startsWith('content')) {
        rec_cardList.value.push(value)
      } else if (key.startsWith('coop')) {
        sim_cardList.value.push(value)
      }
    }
    console.log(rec_cardList.value)
    })
    .catch(err => console.error(err))
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
  overflow: hidden;
}
.title {
  width: 100%;
  margin-top: 3.5%;
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
.page-wrap {
  width: 100%;
  padding: 0 4%
}
/* ca */
.carousel__item {
  /* min-height: 200px; */
  height: 100%;
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

/* main */
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
  height: 600px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.move-button {
  background-color: rgba(0, 0, 0, 0);
}
</style>