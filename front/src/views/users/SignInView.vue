<template>
  <body>
    <main>
      <RouterLink :to="{ name:'home' }">
        <img src="@/assets/img/PICKardº_blue.png" alt="">
      </RouterLink>
  
      <form @submit.prevent="logIn">
        <div class="form-floating mb-3">
          <input type="text" class="form-control" id="id" placeholder="" v-model.trim="username">
          <label for="id">아이디</label>
        </div>
        <div class="form-floating">
          <input type="password" class="form-control" id="password" placeholder="" v-model.trim="password">
          <label for="password">비밀번호</label>
        </div>
        <div v-show="!isRight">
          <p class="text-danger mt-3">아이디 또는 비밀번호를 잘못 입력했습니다.<br>입력하신 내용을 다시 확인해주세요.</p>
        </div>
        <input type="submit" value="로그인" class="btn btn-outline-warning login-btn">
      </form>
    </main>
  </body>
</template>

<script setup>
  import { ref } from 'vue'
  import { RouterLink } from 'vue-router'
  import { useUserStore } from '@/stores/user'
  
  const store = useUserStore()
  const username = ref('')
  const password = ref('')
  const isRight = ref(true)

  const logIn = function() {
    const payload = {
      username: username.value,
      password: password.value
    }
    const temp = store.logIn(payload)

    setTimeout(() => {
      isRight.value = temp
      if (!isRight.value) {
        username.value = ''
        password.value = ''
      }
    }, 250)
  }
</script>

<style scoped>
body {
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