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
          <button data-bs-toggle="modal" data-bs-target="#exampleModal">오프라인 매장 보기</button>    
          <button @click="commentActive" v-if="isActive">설명보기</button>
          <button @click="commentActive" v-if="!isActive">후기보기</button>
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
      <div class="comment-wrap" v-if="isActive">
        <CardComment />
      </div>
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
import CardDetailContent from './CardDetailContent.vue';
import CardComment from '@/components/CardComment.vue'

defineProps({
  card: Object
})
const isActive = ref(false)
  const commentActive = function() {
    isActive.value = !isActive.value
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
.comment-wrap {
  width: 100%;
  /* overflow-y: scroll; */
}
</style>