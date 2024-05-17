<template>
  <div class="body">
    <main>
      <RouterLink :to="{ name:'home' }">
        <img src="../assets/img/PICKardº_blue.png" alt="">
      </RouterLink>

      <h1>회원가입</h1>
      <form @submit.prevent="signUp">
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
        <div class="form-floating">
          <input type="email" class="form-control" placeholder="" v-model.trim="email" id="email">
          <label for="email">이메일 [선택]</label>
        </div>
        <input type="submit" value="회원가입" class="btn btn-outline-warning login-btn">
      </form>
    </main>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { RouterLink } from 'vue-router'
  import { useAuthStore } from '@/stores/auth'

  const store = useAuthStore()
  const username = ref(null) 
  const password1 = ref(null)
  const password2 = ref(null)
  const email = ref(null)

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
  height: 100vh;
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
.login-btn {
  margin-top: 20px;
  width: 100%;
  font-weight: bold;
}
</style>
