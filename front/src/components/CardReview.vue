<template>
  <div class="container body">
    <div class="content">
      <form class="form-wrap" @submit.prevent="">
        <div class="form-floating mb-3">
          <input type="content" class="form-control" id="reviewContent" placeholder="" v-model="content">
          <label for="reviewContent">내용</label>
        </div>
        <div class="star-rating">
          <input type="radio" class="star" value="1">
          <input type="radio" class="star" value="2">
          <input type="radio" class="star" value="3">
          <input type="radio" class="star" value="4">
          <input type="radio" class="star" value="5">
        </div>
        <input type="submit" value="후기 쓰기" class="submit-btn">
      </form>
      <div class="detail">
        <div class="head">
          <div class="title-wrap">
            <div class="title">안녕하세요</div>
            <div>★&star;</div>
          </div>
          <div class="user">user1</div>
          <!-- <button class="delete-btn" v-if="request.user.username==commentUser">
            <img src="@/assets/img/delete_X.png" alt="" style="width: 24px;">
          </button> -->
        </div>
        <div class="text">이 카드는 ~~~ 암튼 조아요<br>이 카드는 ~~~ 암튼 조아요</div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { useRoute } from 'vue-router'
  import axios from 'axios'
  import { ref, onMounted, computed } from 'vue'
  const route = useRoute()
  const card_pk = route.params.id
  const API_URL = 'http://127.0.0.1:8000'

  onMounted(() => {
    axios({
      method: 'get',
      url: `${API_URL}/cards/${card_pk}/review/`,
    })
    .then(res => {
      cards.value = res.data
      console.value(res.data)
    })
    .catch(err => console.error(err))
  })

  const createReview = function() {
    axios({
      method: 'get',
      url: `${API_URL}/cards/${card_pk}/review/`,
    })
    .then(res => {
      cards.value = res.data
      console.value(res.data)
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