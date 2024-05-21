<template>
  <div class="container body">
    <div class="content">
      <form class="form-wrap" @submit.prevent="createReview">
        <div class="form-floating mb-3">
          <input type="content" class="form-control" id="reviewContent" placeholder="" v-model.trim="content">
          <label for="reviewContent">내용</label>
        </div>
        <div class="star-rating">
          <input type="radio" class="star" value="1" v-model="rating">
          <input type="radio" class="star" value="2" v-model="rating">
          <input type="radio" class="star" value="3" v-model="rating">
          <input type="radio" class="star" value="4" v-model="rating">
          <input type="radio" class="star" value="5" v-model="rating">
        </div>
        <input type="submit" value="후기 쓰기" class="submit-btn">
      </form>
      <div class="detail">
        <div v-for="review in reviews" class="head">
          <div class="title-wrap">
            <div class="title">{{  }}</div>
            <div class="text"><strong>{{ review.user.nickname }}</strong> | {{ review.content }}</div>
          </div>
          <div>★{{ review.rating }}</div>
          <button 
          class="delete-btn" 
          v-if="userStore.userInfo.username === review.user.username"
          @click="deleteReview(review.id)"
          >
            <img src="@/assets/img/delete_X.png" alt="" style="width: 20px;">
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useCardStore } from '@/stores/card'

const cardStore = useCardStore()
import { ref, onMounted, computed } from 'vue'
import { useRoute } from 'vue-router'
import { useUserStore } from '@/stores/user'
import axios from 'axios'

const props = defineProps({
  card: {
    type: Object,
    required: true
  }
})

const route = useRoute()
const cardId = route.params.id
const API_URL = 'http://127.0.0.1:8000'
const rating = ref(0)
const content = ref('')
const userStore = useUserStore()
const reviews = ref(props.card.review_set)

const createReview = function() {
  if (Number(rating.value) > 0 && content.value) {
    axios({
      method: 'post',
      url: `${API_URL}/cards/${cardId}/review/`,
      headers: {
        Authorization: `Token ${userStore.token}`
      },
      data: {
        content: content.value,
        rating: Number(rating.value)
      }
    })
    .then(res => {
      reviews.value.push(res.data)
    })
    .catch(err => console.error(err))
  }
}

const deleteReview = function(reviewId) {
  axios({
    method: 'delete',
    url: `${API_URL}/cards/${cardId}/review/${reviewId}/`,
    headers: {
      Authorization: `Token ${userStore.token}`
    },
  })
  .then(res => {
    reviews.value = reviews.value.filter(review => review.id !== reviewId)
  })
  .catch(err => console.error(err))
}
</script>

<style scoped>
.body {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  gap: 2%;
  flex-wrap: wrap;
  align-items: center;
  padding: 0% 2%;
}
form {
  display: flex;
  gap: 2%;
}
.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 80%;
  height: 80%;
  margin: 2% 0;
  gap: 5%;
  overflow-y: scroll;
}
.d-img {
  width: 15%;
  opacity: .7;
}
.detail {
  width: 100%;
  margin: 1% 0;
}
.title {
  color: black;
  font-size: 24px;
  font-weight: 800;
}
.title-wrap {
  display: flex;
  align-items: center;
  gap: 2%;
  width: 100%;
}
.head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 2%;
}
.user {
  font-size: 18px;
}
.form-wrap {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}
.form-floating {
  width: 100%;
  margin-bottom: 0;
}
.submit-btn {
  border-radius: 38px;
  padding: 10px 20px;
  border: none;
}
/* star */
.star-rating {
  display: flex;
}
.star {
  appearance: none;
  padding: 1px;
}
.star::after {
  content: '☆';
  color: rgb(255, 199, 39);
  font-size: 20px;
}
.star:hover::after,
.star:has(~ .star:hover)::after,
.star:checked::after,
.star:has(~ .star:checked)::after {
  content: '★';
}
.star:hover ~ .star::after {
  content: '☆';
}
.delete-btn {
  background-color: rgba(0, 0, 0, 0);
  opacity: .5;
  margin: 0;
}
</style>