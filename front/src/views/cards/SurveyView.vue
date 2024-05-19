<template>
  <Header />
  <div class="body">
    <main>
      <h2>설문</h2>
      <form @submit.prevent="submitSurvey">
        <div v-for="surveyQ in surveyQuestions">
          <legend class="col-form-label pt-0">{{ surveyQ.question }}</legend>
          <div class="form-check form-check-inline">
            <input class="form-check-input" type="radio" :name="surveyQ.var" id="yes" v-model.trim="surveyResponses[surveyQ.var]" value=true>
            <label class="form-check-label" for="yes">맞다</label>
          </div>
          <div class="form-check form-check-inline">
            <input class="form-check-input" type="radio" :name="surveyQ.var" id="no" v-model.trim="surveyResponses[surveyQ.var]" value=false>
            <label class="form-check-label" for="no">아니다</label>
          </div><hr>
        </div>
        <input type="submit" value="제출" class="btn btn-outline-warning survey-btn">
      </form>
    </main>
  </div>
  <p class="text-center mt-3">&copy; 2024 PICKard. All rights reserved.</p>
</template>

<script setup>
import Header from '@/components/Header.vue'
import { useCardStore } from '@/stores/card'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import axios from 'axios'

const router = useRouter()
const cardStore = useCardStore()
const userStore = useUserStore()

const surveyResponses = ref({
  car_owner: null,
  live_alone: null,
  student: null,
  baby: null,
  pets: null,
  easy_pay: null,
  healthcare: null,
  telecom: null,
  sports: null,
  shopping: null,
  friends: null,
  fitness: null,
  movie: null,
  travel_inter: null,
  trevel_dome: null,
})

const surveyQuestions = [
  { question: '자차를 갖고 계십니까?', var: 'car_owner' },
  { question: '자취를 하십니까?', var: 'live_alone' },
  { question: '학생이십니까?', var: 'student' },
  { question: '육아를 하고 계십니까?', var: 'baby' },
  { question: '반려동물이 있습니까?', var: 'pets' },
  { question: '간편결제를 사용하십니까?', var: 'easy_pay' },
  { question: '병원이나 약국을 자주 이용하십니까?', var: 'healthcare' },
  { question: '통신 관련 서비스를 이용하십니까?', var: 'telecom' },
  { question: '스포츠를 좋아하십니까?', var: 'sports' },
  { question: '쇼핑을 즐기십니까?', var: 'shopping' },
  { question: '친구들과 자주 어울리십니까?', var: 'friends' },
  { question: '운동을 즐기십니까?', var: 'fitness' },
  { question: '영화를 자주 보십니까?', var: 'movie' },
  { question: '해외여행을 좋아하십니까?', var: 'travel_inter' },
  { question: '국내여행을 좋아하십니까?', var: 'trevel_dome' },
]

const submitSurvey = function () {
  axios({
    method: 'post',
    url: `${cardStore.API_URL}/users/${userStore.userInfo.username}/survey/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
    data: surveyResponses.value
  })
  .then(res => {
    window.alert('설문이 완료되었습니다!')
    axios({
      method: 'post',
      url: `${cardStore.API_URL}/cards/${userStore.userInfo.username}/card_recommend/`,
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
    })
    .then(res => {
      router.push({ name: 'recommend', params: { 'username': userStore.userInfo.username } })
    })
    .catch(err => console.error(err))
  })
  .catch(err => console.error(err))
}
</script>

<style scoped>
.body {
  display: flex;
  align-items: center;
  justify-content: center;
}
main {
  /* border: 1px solid black; */
  width: 500px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 50px;
  padding: 5% 0;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 30px;
  background-color: white;
}
form {
  width: 70%;
}
.survey-btn {
  margin-top: 20px;
  width: 100%;
  font-weight: bold;
}
</style>