<template>
  <div class="header-wrap">
    <div>
      <RouterLink :to="{ name:'home' }">
        <img src="@/assets/img/PICKardº_blue.png" alt="">
      </RouterLink>
    </div>
    <div class="header-menu">
      <nav>
        <ul class="nav">
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name:'cardList' }">카드 모아보기</RouterLink>
          </li>
          <li class="nav-item">
            <!-- <RouterLink class="nav-link" :to="{ name:'searchCard' }">카드 검색</RouterLink> -->
          </li>
          <li class="nav-item" v-if="store.isLogIn">
            <RouterLink class="nav-link" :to="{ name:'myCard', params: { username: store.userInfo?.username } }">내 관심 카드</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name:'postList' }">커뮤니티</RouterLink>
          </li>
        </ul>
      </nav>
    </div>
    <div v-if="!store.isLogIn" class="login-menu-wrap">
      <RouterLink class="header-menu nav-link" :to="{ name:'signIn' }">
        <div>
          로그인
        </div>
      </RouterLink>
      <RouterLink :to="{ name:'signUp' }" class="header-menu nav-link" style="background-color: rgb(33, 95, 255);">
        <div style="color: white; font-weight: bold;">
          회원가입
        </div>
      </RouterLink>
    </div>
    <div v-else class="login-menu-wrap">
      <button class="header-menu nav-link" @click.prevent="store.logOut">로그아웃</button>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useUserStore } from '@/stores/user'

  const store = useUserStore()

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
  background: white;
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
  padding: 30px 0;
}
.login-menu-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
}
</style>