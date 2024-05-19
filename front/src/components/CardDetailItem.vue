<template>
  <div>
    <div class="detail-main">
      <img :src="card.image_url" class="card-img">
      <div class="card-content">
        <p class="card-name">{{ card.name }}</p>
        <p>{{ card.brand }}</p>
        <p>{{ card.type }}</p>
        <div>
          <button class="go-button">
            <a :href="`https://www.card-gorilla.com/card/detail/${card.id}`">신청하러 가기</a>
          </button>
          <button data-bs-toggle="modal" data-bs-target="#exampleModal">오프라인 매장 보기</button>    
        </div>
      </div>
    </div>
    <div v-for="benefit in card.benefit_set" :key="benefit.id">
      <h4>{{ benefit.title }}</h4>
      <p>{{ benefit.content }}</p>
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
  </div>
</template>

<script setup>
import { ref, defineProps } from 'vue'
import { RouterLink } from 'vue-router'

defineProps({
  card: Object
})
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
}
.detail-main {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 5%;
  border: 2px solid blueviolet;
}
.card-name {
  color: black;
  font-size: 36px;
  font-weight: 800;
}
</style>