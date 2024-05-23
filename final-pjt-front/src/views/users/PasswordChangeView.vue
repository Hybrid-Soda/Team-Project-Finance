<template>
  <div class="body">
    <main>
      <RouterLink :to="{ name:'home' }">
        <img src="@/assets/img/PICKardº_blue.png" alt="">
      </RouterLink>

      <div class="title">비밀번호 변경</div>
      <form @submit.prevent="changePassword" class="sign-up-form">
        <div class="form-floating mb-3">
          <input type="password" class="form-control" placeholder="" v-model.trim="password1" id="password1">
          <label for="password1">새로운 비밀번호</label>
        </div>
        <div class="form-floating mb-3">
          <input type="password" class="form-control" placeholder="" v-model.trim="password2" id="password2">
          <label for="password2">비밀번호 확인</label>
        </div>
        <input type="submit" value="비밀번호 변경" class="btn btn-outline-warning login-btn">
      </form>
    </main>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { RouterLink } from 'vue-router'
  import { useUserStore } from '@/stores/user'

  const userStore = useUserStore()
  const password1 = ref(null)
  const password2 = ref(null)

  const changePassword = function () {
    const payload = {
      new_password1: password1.value,
      new_password2: password2.value,
    }
    userStore.changePassword(payload)
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
  width: 800px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 50px;
  padding: 50px 0;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 30px;
  background-color: white;
}
form {
  width: 600px;
}
.login-btn {
  margin-top: 20px;
  width: 100%;
  font-weight: bold;
}
.sign-up-form {
  height: 80%;
}
</style>
