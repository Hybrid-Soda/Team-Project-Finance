<template>
  <div class="d-flex" style="min-width: 600px;">
    <div class="profile-img me-5">
      <div class="img-div"></div>
      <button style="background-color: rgb(255, 199, 39); font-weight: 600;">사진 변경하기</button>
    </div>
    <form>
      <!-- 아이디 -->
      <div class="row">
        <label for="id" class="col-sm-3 col-form-label">아이디</label>
        <div class="col-sm-9">
          <input type="text" class="form-control" v-model.trim="username" id="id" disabled><br>
        </div>
      </div>
      <!-- 닉네임 -->
      <div class="row">
        <label for="nickname" class="col-sm-3 col-form-label">닉네임</label>
        <div class="col-sm-9">
          <input type="text" class="form-control" v-model.trim="nickname" id="nickname"><br>
        </div>
      </div>
      <!-- 이메일 -->
      <div class="row">
        <label for="email" class="col-sm-3 col-form-label">이메일</label>
        <div class="col-sm-9">
          <input type="text" class="form-control" v-model.trim="email" id="email"><br>
        </div>
      </div>
      <!-- 나이 -->
      <div class="row">
        <label for="age" class="col-sm-3 col-form-label">나이</label>
        <div class="col-sm-9">
          <input type="number" class="form-control" v-model="age" min="0" max="200" id="age"><br>
        </div>
      </div>
      <!-- 성별 -->
      <div class="row">
        <legend class="col-form-label col-sm-3 pt-0">성별</legend>
        <div class="col-sm-9">
          <div class="form-check form-check-inline">
            <input class="form-check-input" type="radio" name="gridRadios" id="gender1" value="option1" checked>
            <label class="form-check-label" for="gender1">남자</label>
          </div>
          <div class="form-check form-check-inline">
            <input class="form-check-input" type="radio" name="gridRadios" id="gender2" value="option2">
            <label class="form-check-label" for="gender2">여자</label>
          </div>
        </div>
      </div>

      <input type="submit" class="submit-button" value="저장하기" @click.prevent="editProfile">
      <input type="reset" class="submit-button" value="취소" style="color: rgb(106, 106, 106); right: 150px; font-weight: 500;">
    </form>
  </div>
</template>

<script setup>
  import { useUserStore } from '@/stores/user'
  import { ref, onMounted } from 'vue'
  import axios from 'axios'

  const userStore = useUserStore()
  const userInfo = userStore.userInfo
  const username = ref(userInfo.username)
  const nickname = ref(userInfo.nickname)
  const gender = ref(userInfo.gender)
  const email = ref(userInfo.email)
  const age = ref(userInfo.age)

  const editProfile = function () {
    const payload = {
      username: username.value,
      nickname: nickname.value,
      gender: gender.value,
      email: email.value,
      age: age.value,
    }
    userStore.updateProfile(payload)
  }
</script>

<style scoped>
.img-div {
  background: #6b6b6b;
  width: 213px;
  height: 213px;
  opacity: 1;
  border-radius: 50%;
  background-image: url("@/assets/img/profile-man.png");
  background-position: center;
  background-size: contain;
}
.profile-img {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 30px;
}
.info-input {
  display: flex;
  flex-direction: column;
}
.input-wrap {
  display: flex;
  justify-content: space-between;
  gap: 20px;
}
.submit-button {
  color: rgb(33, 95, 255);
  background-color: rgba(0, 0, 0, 0);
  border: none;
  /* border: 1px solid rgb(106, 106, 106); */
  font-size: large;
  font-weight: 900;
  position: absolute;
  bottom: 50px;
  right: 60px;
}
</style>