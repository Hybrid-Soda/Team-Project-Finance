<template>
  <div class="body">
    <main>
      <RouterLink :to="{ name:'home' }">
        <img src="@/assets/img/PICKardº_blue.png" alt="">
      </RouterLink>

      <div class="title">회원가입</div>
      <form @submit.prevent="signUp" class="sign-up-form">
        <div class="form-floating mb-3">
          <input type="text" class="form-control" placeholder="" v-model.trim="username" id="username">
          <label for="username">아이디</label>
        </div>
        <div class="form-floating mb-3">
          <input type="password" class="form-control" placeholder="" v-model.trim="password1" id="password1">
          <label for="password1">비밀번호</label>
        </div>
        <div class="form-floating mb-3">
          <input type="password" class="form-control" placeholder="" v-model.trim="password2" id="password2">
          <label for="password2">비밀번호 확인</label>
        </div>
        <hr>
        <div class="form-floating mb-3">
          <input type="email" class="form-control" placeholder="" v-model.trim="email" id="email">
          <label for="email">이메일 [선택]</label>
        </div>
        <div class="form-floating mb-3">
          <input type="text" class="form-control" placeholder="" v-model.trim="nickname" id="nickname">
          <label for="nickname">닉네임</label>
        </div>
        <div class="form-floating mb-3">
          <input type="number" class="form-control" placeholder="" v-model.trim="age" id="age">
          <label for="age">나이</label>
        </div>
        <div class="row">
          <legend class="col-form-label col-sm-3 pt-0">성별</legend>
          <div class="col-sm-9">
            <div class="form-check form-check-inline">
              <input class="form-check-input" type="radio" name="gender" id="male" v-model.trim="gender" value="남자">
              <label class="form-check-label" for="male">남자</label>
            </div>
            <div class="form-check form-check-inline">
              <input class="form-check-input" type="radio" name="gender" id="female" v-model.trim="gender" value="여자">
              <label class="form-check-label" for="female">여자</label>
            </div>
          </div>
        </div>
        <input type="submit" value="회원가입" class="btn btn-outline-warning login-btn"><hr>
      </form>
      <button class="kakao" @click="kakaoLogin">
        <img src="@/assets/img/kakao_login_medium.png" alt="kakao_login">
      </button>
      <p>Already have an account? <RouterLink :to="{ name: 'signIn' }">Login</RouterLink></p>
    </main>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useRouter, RouterLink } from 'vue-router'
  import { useUserStore } from '@/stores/user'
  import axios from 'axios'

  const store = useUserStore()
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()

  const password1 = ref(null)
  const password2 = ref(null)
  const username = ref(null) 
  const nickname = ref(null)
  const gender = ref('남자')
  const email = ref(null)
  const age = ref(null)

  const signUp = function () {
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value,
      nickname: nickname.value,
      gender: gender.value,
      email: email.value,
      age: age.value,
    }

    if (!email.value) {
      delete payload.email
    }
    store.signUp(payload)
  }

const kakaoLogin = function () {
  axios({
    method: 'get',
    url: `${API_URL}/users/kakao/callback/`,
  })
  .then(res => {
    console.log(res)
  })
  .catch(err => console.log(err))
}
</script>

<style scoped>
.body {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
main {
  /* border: 1px solid black; */
  width: 70%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 30px;
  padding: 40px 0;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 30px;
  background-color: white;
}
form {
  width: 70%;
}
.login-btn {
  margin-top: 20px;
  width: 100%;
  font-weight: bold;
}
.kakao {
  width: 70%;
  height: 60px;
  text-align: center;
  background-color: #FEE500;
  border-radius: 6px;
}
</style>
