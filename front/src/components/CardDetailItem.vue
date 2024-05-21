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
            <div id="map" @click="openMap">
              <!-- <KakaoMap :lat="35.0961457" :lng="128.8538772" /> -->
              <KakaoMap :lat="35.0961457" :lng="128.8538772" @onLoadKakaoMap="onLoadKakaoMap">
                <KakaoMapMarker
                  v-for="(marker, index) in markerList"
                  :key="marker.key === undefined ? index : marker.key"
                  :lat="marker.lat"
                  :lng="marker.lng"
                  :infoWindow="marker.infoWindow"
                  :clickable="true"
                  @onClickKakaoMapMarker="onClickMapMarker(marker)"
                />
              </KakaoMap>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, defineProps, onMounted } from 'vue'
  import { RouterLink } from 'vue-router'
  import CardDetailContent from './CardDetailContent.vue';
  // import CardReview from '@/components/CardReview.vue'
  import { KakaoMap, KakaoMapMarker } from 'vue3-kakao-maps';
  import CardDetailReview from '@/components/CardDetailReview.vue'

  const props = defineProps({
    card: Object
  })
  const isActive = ref(false)
  const reviewActive = function() {
    isActive.value = !isActive.value
  }

  // kakaomap
  const kakao_api_key = import.meta.env.VITE_KAKAO_API
  // let map = null;

  // onMounted(() => {
  //   if (window.kakao && window.kakao.maps) {
  //     initMap();
  //   } else {
  //     const script = document.createElement('script');
  //     /* global kakao */
  //     script.onload = () => kakao.maps.load(initMap);
  //     script.src = `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${kakao_api_key}`;
  //     document.head.appendChild(script);
  //   }
  // });

  //   const initMap = () => {
  //   const container = document.getElementById('map');
  //   const options = {
  //     center: new kakao.maps.LatLng(35.0961457, 128.8538772),
  //     level: 5,
  //   };

  //   // 지도 객체를 등록합니다.
  //   // 지도 객체는 반응형 관리 대상이 아니므로 initMap에서 선언합니다.
  //   map = new kakao.maps.Map(container, options);
  // };

  let map = null;
  const markerList = ref([]);

  const onLoadKakaoMap = (mapRef) => {
    map = mapRef;

    // 장소 검색 객체를 생성합니다
    const ps = new kakao.maps.services.Places();
    // 키워드로 장소를 검색합니다
    ps.keywordSearch(`${props.card.brand}`, placesSearchCB);
  };

  // 키워드 검색 완료 시 호출되는 콜백함수 입니다
  const placesSearchCB = (data, status) => {
    if (status === kakao.maps.services.Status.OK) {
      // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
      // LatLngBounds 객체에 좌표를 추가합니다
      const bounds = new kakao.maps.LatLngBounds();

      for (let marker of data) {
        const markerItem = {
          lat: marker.y,
          lng: marker.x,
          infoWindow: {
            content: marker.place_name,
            visible: false
          }
        };
        markerList.value.push(markerItem);
        bounds.extend(new kakao.maps.LatLng(Number(marker.y), Number(marker.x)));
      }

      // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
      map.value?.setBounds(bounds);
    }
  };

  //마커 클릭 시 인포윈도우의 visible 값을 반전시킵니다
  const onClickMapMarker = (markerItem) => {
    if (markerItem.infoWindow?.visible !== null && markerItem.infoWindow?.visible !== undefined) {
      markerItem.infoWindow.visible = !markerItem.infoWindow.visible;
    } else {
      markerItem.infoWindow.visible = true;
    }
  };

  const openMap = function () {
    // console.log(map)
    map.relayout();
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
#map {
  width: 100%;
  height: 100%;
  overflow: hidden;
}
</style>