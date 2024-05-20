<template>
  <div style="height: 100%;">
    <Header />
    <main>
      <div class="bg">
        <div class="head">
          <img src="@/assets/img/CreditCard.png" alt="">
          내 카드를 찾아보자 !
          <progress :value="questionIdx" min="0" max="10"></progress>
        </div>
        <form @submit.prevent="">
          <!-- <div v-for="surveyQ in surveyQuestions" class="content"> -->
          <div class="content">
            <div class="title">
              {{ surveyQ.question }}
            </div>
            <div class="question">
              <button class="question-item" v-for="answer in surveyQ.answers" @click="count">
                {{ answer }}
              </button>
            </div>
            </div>
        </form>
      </div>
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

// const surveyQuestions = [
//   { question: '자차를 갖고 계십니까?', var: 'car_owner' },
//   { question: '자취를 하십니까?', var: 'live_alone' },
//   { question: '학생이십니까?', var: 'student' },
//   { question: '육아를 하고 계십니까?', var: 'baby' },
//   { question: '반려동물이 있습니까?', var: 'pets' },
//   { question: '간편결제를 사용하십니까?', var: 'easy_pay' },
//   { question: '병원이나 약국을 자주 이용하십니까?', var: 'healthcare' },
//   { question: '통신 관련 서비스를 이용하십니까?', var: 'telecom' },
//   { question: '스포츠를 좋아하십니까?', var: 'sports' },
//   { question: '쇼핑을 즐기십니까?', var: 'shopping' },
//   { question: '친구들과 자주 어울리십니까?', var: 'friends' },
//   { question: '운동을 즐기십니까?', var: 'fitness' },
//   { question: '영화를 자주 보십니까?', var: 'movie' },
//   { question: '해외여행을 좋아하십니까?', var: 'travel_inter' },
//   { question: '국내여행을 좋아하십니까?', var: 'trevel_dome' },
// ]

const questionIdx = ref(0)

const surveyQuestions = ref([
  { 
    question:'오늘은 놀러가는 날! 여행지까지 나는...',
    answers: {
      true: '차가 있으니 내 차로 가야지!',
      false: '차가 없으니 버스 타고 가야지!'
    },
    var: 'car_owner'
  },
  { 
    question:'하루가 끝나고 집에 가는 길! 나는...',
    answers: {
      true: '내 자취방으로 돌아가자!',
      false: '부모님과 함께사는 집으로 돌아가자!'
    },
    var: 'live_alone'
  },
  { 
    question:'아침에 눈을 뜨면 나는...',
    answers: {
      true: '학교 가자',
      false: '다시 눕자',
    },
    var: 'student'
  },
  { 
    question:'날씨 좋다! 나는...',
    answers: {
      true: '자식들과 놀러 가야지!',
      false: '자식 없어!'
    },
    var: 'baby' 
  },
  { 
    question:'아침에 눈을 뜨면 나는...',
    answers: {
      true: '학교 가자',
      false: '다시 눕자'
    },
    var: 'student'
  },
])
const surveyQ = ref(surveyQuestions.value[questionIdx.value])
const count = function() {
  questionIdx.value += 1
  surveyQ.value = surveyQuestions.value[questionIdx.value]
}

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
main {
  display: flex;
  justify-content: center;
  height: 80%;
}
img {
  width: 20%;
}
.bg {
  width: 70%;
  border-radius: 50px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
  /* background-color: rgb(33, 95, 255); */
  margin-top: 40px;
  display: flex;
  align-items: center;
  flex-direction: column;
  gap: 10%;
  padding-top: 2%;
}
.content {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  gap: 50px;
  /* height: 70%; */
}
.head {
  font-size: large;
  font-weight: bold;
  width: 70%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
progress {
  margin-top: 3%;
  width: 60%;
}
.title {
  font-size: large;
  font-weight: bold;
}
.question {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 30px;
  width: 150%;
}
.question-item {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
}
.question-item:hover {
  background-color: rgb(255, 199, 39);
  color: black;
  font-weight: bold;
}
</style>