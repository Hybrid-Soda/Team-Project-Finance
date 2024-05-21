<template>
  <div>
    <div class="detail-main">
      <div class="card-img-wrap">
        <img :src="card.image_url" class="card-img">
      </div>
      <div class="card-content">
        <p class="card-name">{{ card.name }}</p>
        <p>{{ card.brand }}</p>
        <p>{{ card.type }}</p>
        <!-- <div>★{{ card.review_set }}</div> -->
        <div class="btn-wrap">
          <button class="go-button">
            <a :href="`https://www.card-gorilla.com/card/detail/${card.id}`">신청하러 가기</a>
          </button>
          <button data-bs-toggle="modal" data-bs-target="#exampleModal" @click="openMap()">오프라인 매장 보기</button>    
          <button @click="reviewActive" v-if="isActive">설명보기</button>
          <button @click="reviewActive" v-if="!isActive">후기보기</button>
        </div>
      </div>
    </div>
    <div class="detail-content">
      <div class="row benefit-wrap" v-if="!isActive">
          <CardDetailContent
          v-for="benefit in card.benefit_set" 
          :key="benefit.id"
          :benefit="benefit"
          />
      </div>
      <div class="review-wrap" v-if="isActive">
        <CardDetailReview 
        :card="card"
        />
      </div>
    </div>

    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">근처 은행 보기</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <button @click="openMap">지도</button>
            <div class="map">
              <KakaoMap :lat="33.450701" :lng="126.570667"/>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, defineProps } from 'vue'
  import { RouterLink } from 'vue-router'
  import CardDetailContent from './CardDetailContent.vue';
  // import CardReview from '@/components/CardReview.vue'
  import { KakaoMap, KakaoMapMarker } from 'vue3-kakao-maps';
  import CardDetailReview from '@/components/CardDetailReview.vue'

  defineProps({
    card: Object
  })
  const isActive = ref(false)
  const reviewActive = function() {
    isActive.value = !isActive.value
  }
  const coordinate = {
  lat: 33.450701,
  lng: 126.570667
  };

  const map = ref(kakao.maps.Map);
  // const map = new Map(coordinate, options);
  const openMap = function() {
    KakaoMap.relayout()
    // console.log('hi')
  }

</script>

<style scoped>
.card-img {
  max-width: 300px;
  max-height: 300px;
  object-fit: contain;
}
.card-img-wrap {
  width: 300px;
  height: 300px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.card-content {
  /* border: 2px solid pink; */
  display: flex;
  flex-direction: column;
  justify-content: baseline;
}
.go-button {
  background-color: rgb(255, 199, 39);
  font-weight: bold;
  color: black;
}
.detail-main {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 5%;
  margin-top: 2%;
  /* border: 2px solid blueviolet; */
}
.btn-wrap {
  display: flex;
  gap: 4%;
  width: 120%;
}
.card-name {
  color: black;
  font-size: 36px;
  font-weight: 800;
}
.detail-content {
  /* margin-top: 2%; */
  height: 400px;
  background-color: rgba(0, 0, 0, 0);
  overflow-y: scroll;
  overflow-x: hidden;
}
.benefit-wrap {
  display: flex;
  align-items: center;
  /* justify-content: center; */
  padding: 2% 5%;
}
.review-wrap {
  width: 100%;
  /* overflow-y: scroll; */
}
.map {
  width: 100%;
  height: 100%;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>