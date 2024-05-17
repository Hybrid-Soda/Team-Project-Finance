<template>
  <div style="width: 100%;">
    <form>
      <div class="profile-img">
        <div class="img-div"></div>
        <button style="background-color: rgb(255, 199, 39); font-weight: 600;">사진 변경하기</button>
      </div>
      <div class="info-input">
        <div class="input-wrap">
          <label for="id">아이디</label>
          <input type="text" id="id"><br>
        </div>
        <div class="input-wrap">
          <label for="email">이메일</label>
          <input type="text" id="email"><br>
        </div>
        <div class="input-wrap">
          <label for="username">닉네임</label>
          <input type="text" id="username"><br>
        </div>
        <div class="input-wrap">
          <label for="gender">성별</label>
          <div class="gender-input">
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="gender">
              <label class="form-check-label" for="gender">
                남자
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="gender" checked>
              <label class="form-check-label" for="gender">
                여자
              </label>
            </div>
          </div>
        </div>
        <div class="input-wrap">
          <label for="age">나이</label>
          <input type="number" id="age" min="0" max="200"><br>
        </div>
      </div>
      <input type="submit" class="submit-button" value="저장하기">
      <input type="reset" class="submit-button" value="취소" style="color: rgb(106, 106, 106); right: 150px; font-weight: 500;">
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  

</script>

<style scoped>
.img-div {
  background: #6b6b6b;
  width: 213px;
  height: 213px;
  opacity: 1;
  border-radius: 50%;
  background-image: url("../assets/img/profile-man.png");
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
form {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.info-input {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.input-wrap {
  display: flex;
  justify-content: space-between;
  gap: 20px;
}
select {
  width: 130%;
}
.form-check-label {
  width: max-content;
}
.gender-input {
  display: flex;
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