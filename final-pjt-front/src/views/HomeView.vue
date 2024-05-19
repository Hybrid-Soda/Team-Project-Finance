<template>
  <div style="height: 100%">
    <div class="main-background">
    <header>
      <nav>
        <ul class="nav">
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{name:'home'}">
              <img src="../assets/img/PICKardº.png" alt="logo" style="margin-right: 60px;">
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name:'cardList' }">카드 모아보기</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name:'searchCard' }">카드 검색</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name:'myCard' }">내 관심 카드</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name:'community' }">커뮤니티</RouterLink>
          </li>
          <li class="nav-item">
            <div class="login-menu">
              <RouterLink :to="{ name:'login' }">
                <button class="login-btn">로그인</button>
              </RouterLink>
              <RouterLink :to="{ name:'signup' }">
                <button class="login-btn" style="font-weight: bold; background-color: rgb(255, 199, 39); color: black;">회원가입</button>
              </RouterLink>
            </div>
          </li>
        </ul>
      </nav>
    </header>
    <main>
      <img src="../assets/img/Analysis-cuate.png" class="main-img">
      <div class="main-content">
        <div class="main-text">
          내게 필요한 신용카드<br>
          <span style="color: rgb(255, 199, 39);">1분만에</span> 추천 받기
        </div>
        <RouterLink :to="{ name:'signup' }">
          <button class="main-text-btn">가입하고 시작하기</button>
        </RouterLink>
      </div>
    </main>
  </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { RouterLink } from 'vue-router';
  

</script>

<style scoped>
.main-background {
  background-color: rgb(33, 95, 255);
  height: 75%;
}
.nav-link {
  color: white;
}
.nav-item {
  padding: auto 30px;
  display: flex;
  align-items: center;
}
nav {
  width: 100%;
  height: 120px;
  display: flex;
  align-items: center;
  justify-content: space-evenly;
}
.nav {
  gap: 60px;
}
.main-img {
  position: absolute;
  top: 22%;
  left: 18%;
  width: 33%;
}
.login-menu {
  display: flex;
  gap: 30px;
  margin-left: 60px;
}
.login-btn {
  background: rgba(250,250,250,1);
  border-radius: 38px;
  padding: 10px 20px;
  border: none;
}
.main-content {
  display: flex;
  align-items: end;
  flex-direction: column;
  position: absolute;
  top: 50%;
  right: 20%;
}
.main-text {
  text-align: end;
  font-size: 38px;
  font-weight: bold;
  color: white;
}
.main-text-btn {
  background: rgb(255, 199, 39);
  border-radius: 38px;
  padding: 10px 20px;
  border: none;
  width: fit-content;
  margin-top: 30px;
  font-weight: bold;
  color: black;
}

</style>