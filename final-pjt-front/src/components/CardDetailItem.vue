<template>
  <div class="detail-main">
    <img src="../assets/img/example_card.png" class="card-img">
    <div class="card-content">
      <p class="card-name">신한카드 Point Plan</p>
      <p>&nbsp; 큰 소비일수록 계획이 필요한 법</p>
      <div class="btn-wrap">
        <button class="go-button">신청하러 가기</button>
        <button data-bs-toggle="modal" data-bs-target="#exampleModal">오프라인 매장 보기</button>    
        <button @click="commentActive" v-if="isActive">설명보기</button>
        <button @click="commentActive" v-if="!isActive">후기보기</button>
      </div>
    </div>
  </div>
  <div class="detail-content">
    <CardDetailContent v-if="!isActive"/>
    <CardComment v-if="isActive"/>
  </div>
  <div>

  </div>

  <!-- Modal -->
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          ...
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary">Save changes</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import CardDetailContent from './CardDetailContent.vue';
  import CardComment from '@/components/CardComment.vue'

  const isActive = ref(false)
  const commentActive = function() {
    isActive.value = !isActive.value
  }
</script>

<style scoped>
.card-img {
  width: 300px;
  height: fit-content;
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
  width: 100%;
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
  margin-top: 5%;
}
</style>