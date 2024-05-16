<template>
  <div class="header-wrap">
    <div>
      <RouterLink :to="{ name:'home' }">
        <img src="../assets/img/PICKardº_blue.png" alt="">
      </RouterLink>   
    </div>
    <div class="header-menu">
      <nav>
        <ul class="nav">
          <li class="nav-item">
            <a class="nav-link" href="#">카드 모아보기</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">카드 검색</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">내 관심 카드</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">커뮤니티</a>
          </li>
        </ul>
      </nav>
    </div>
    <div class="login-menu-wrap">
      <a class="header-menu nav-link" href="#">
        <div>
          로그인
        </div>
      </a>
      <a class="header-menu nav-link" style="background-color: rgb(33, 95, 255);" href="#">
        <div style="color: white; font-weight: bold;">
          회원가입
        </div>
      </a>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  

</script>

<style scoped>
.nav-link {
  color: rgb(106, 106, 106);
}
nav {
  display: flex;
  justify-content: space-around;
  margin: 0 40px;
}
.nav {
  gap: 30px;
}
.header-menu {
  background: rgba(250,250,250,1);
  border-radius: 38px;
  padding: 5px 20px;
  border: none;
  width: max-content;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  height: 50px;
}
.header-wrap {
  display: flex;
  align-items: center;
  justify-content: space-around;
  margin: 30px 0;
}
.login-menu-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
}
</style>