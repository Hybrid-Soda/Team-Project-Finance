<template>
  <div class="body">
    <main>
      <RouterLink :to="{ name:'home' }">
        <img src="../assets/img/PICKardº_blue.png" alt="">
      </RouterLink>

      <form @submit.prevent="signUp" class="sign-up-form">
      <div class="form-floating mb-3">
        <input type="text" class="form-control" id="id" placeholder="ID" v-model.trim="username">
        <label for="id">아이디</label>
      </div>
      <div class="form-floating mb-3">
        <input type="e-mail" class="form-control" id="id" placeholder="ID" v-model.trim="username">
        <label for="id">이메일</label>
      </div>
      <div class="form-floating mb-3">
        <input type="text" class="form-control" id="id" placeholder="ID" v-model.trim="username">
        <label for="id">비밀번호</label>
      </div>
      <div class="form-floating mb-3">
        <input type="text" class="form-control" id="id" placeholder="ID" v-model.trim="username">
        <label for="id">비밀번호 확인</label>
      </div>
      <div class="form-floating mb-3">
        <input type="text" class="form-control" id="id" placeholder="ID" v-model.trim="username">
        <label for="id">이름</label>
      </div>
      <div class="form-floating mb-3">
        <input type="number" class="form-control" id="id" placeholder="ID" v-model.trim="username">
        <label for="id">나이</label>
      </div>
      
      <input type="submit" value="회원가입" class="btn btn-outline-warning login-btn">
      </form>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCardStore } from '@/stores/card'

const username = ref(null) 
const password1 = ref(null)
const password2 = ref(null)
const store = useCardStore()

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  store.signUp(payload)
}

</script>

<style scoped>
.body {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}
main {
  /* border: 1px solid black; */
  width: 40%;
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
.login-btn {
  margin-top: 20px;
  width: 100%;
  font-weight: bold;
}
.sign-up-form {
  height: 80%;
  overflow: scroll;
}
.sign-up-form::-webkit-scrollbar {
  display: none;
}
</style>
