<template>
  <div class="body">
    <div class="main-background">
      <header>
        <nav>
          <ul class="nav">
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'home' }">
                <img src="@/assets/img/PICKardº.png" alt="logo" class="logo"/>
              </RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name:'cardList' }">카드 모아보기</RouterLink>
            </li>
            <li class="nav-item" v-if="userStore.isLogIn">
              <RouterLink class="nav-link" :to="{ name:'survey', params: { username: userStore.userInfo.username } }">카드 검색</RouterLink>
            </li>
            <li class="nav-item" v-if="!userStore.isLogIn">
              <RouterLink class="nav-link" :to="{ name:'signIn' }" onclick="alert('로그인이 필요합니다!')">카드 검색</RouterLink>
            </li>
            <li class="nav-item" v-if="userStore.isLogIn">
              <RouterLink class="nav-link" :to="{ name:'myCard', params: { username: userStore.userInfo.username } }">내 관심 카드</RouterLink>
            </li>
            <li class="nav-item" v-if="!userStore.isLogIn">
            <RouterLink class="nav-link" :to="{ name:'signIn' }" onclick="alert('로그인이 필요합니다!')">내 관심 카드</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name:'postList' }">커뮤니티</RouterLink>
            </li>
            <li class="nav-item">
              <div v-if="!userStore.isLogIn" class="user-menu">
                <RouterLink :to="{ name: 'signIn' }">
                  <button class="login-btn">로그인</button>
                </RouterLink>
                <RouterLink :to="{ name: 'signUp' }">
                  <button class="login-btn" style="font-weight: bold; background-color: rgb(255, 199, 39); color: black;">
                    회원가입
                  </button>
                </RouterLink>
              </div>
              <div v-else class="user-menu">
                <RouterLink :to="{ name: 'myPage', params: { 'username': userStore.userInfo.username } }">
                  <button class="login-btn" style=" font-weight: bold; background-color: rgb(255, 199, 39); color: black;">
                    마이페이지
                  </button>
                </RouterLink>
                <button class="login-btn" @click.prevent="userStore.logOut">
                  로그아웃
                </button>
              </div>
            </li>
          </ul>
        </nav>
      </header>
      <main>
        <img src="@/assets/img/Analysis-cuate.png" class="main-img" />
        <div class="main-content">
          <div class="main-text">
            내게 필요한 신용카드<br/>
            <span style="color: rgb(255, 199, 39)">1분만에</span> 추천 받기
          </div>
          <button v-if="!userStore.isLogIn" class="main-text-btn">
            <RouterLink :to="{ name: 'signUp' }">가입하고 시작하기</RouterLink>
          </button>
          <button v-else class="main-text-btn">
            <RouterLink :to="{ name: 'survey', params: { 'username': userStore.userInfo.username } }">카드 추천받기</RouterLink>
          </button>
        </div>
      </main>
    </div>
  </div>
  <button class="chatbot main-text-btn">
    <RouterLink :to="{ name: 'chatBot' }">chatbot</RouterLink>
  </button>
  <Footer />
</template>

<script setup>
  import { ref } from "vue"
  import { RouterLink } from "vue-router"
  import { useUserStore } from "@/stores/user"
  import Footer from '@/components/Footer.vue'

  const userStore = useUserStore()
</script>

<style scoped>
.body {
  min-width: 900px;
}
.main-background {
  background-color: rgb(33, 95, 255);
  height: 700px;
}
.nav-link {
  color: white;
}
.nav-item {
  padding: auto 30px;
  display: flex;
  align-items: center;
}
.logo {
  margin-right: 60px;
}
nav {
  width: 100%;
  height: 120px;
  display: flex;
  align-items: center;
  justify-content: space-evenly;
}
.nav {
  gap: 50px;
}
.main-img {
  position: absolute;
  top: 210px;
  left: 17%;
  width: 630px;
}
.user-menu {
  display: flex;
  gap: 30px;
  margin-left: 60px;
}
.login-btn {
  background: rgba(250, 250, 250, 1);
  border-radius: 38px;
  padding: 10px 20px;
  border: none;
}
.main-content {
  display: flex;
  align-items: end;
  flex-direction: column;
  position: absolute;
  top: 450px;
  right: 23%;
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
.chatbot {
  position: fixed;
  bottom: 20px;
  right: 20px;
}

@media (max-width: 1300px) {
  .nav {
    gap: 0;
  }
  .nav-item {
    margin: 10px 0;
  }
  .logo {
    margin: 0;
  }
  .main-img {
    position: absolute;
    top: 210px;
    left: 17%;
    width: 500px;
  }
  .main-text {
    font-size: 28px;
  }
  .user-menu {
    display: flex;
    gap: 15px;
    margin-left: 20px;
  }
}
</style>
