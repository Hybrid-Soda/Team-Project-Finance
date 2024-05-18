<template>
  <div>
    <Header />
    <div style="position: absolute; top: 100px;">
      <div class="my-page-bg">
        <div class="my-info-item">
          <MyPageItem />
        </div>
      </div>
    </div>
    <div class="my-page-wrap">
      <div class="my-page-menu">
        <ul class="my-page-menu-list">
          <li class="isNow">
            <a href="#">
              회원 정보 수정
            </a>
          </li>
          <li>
            <a href="">
              비밀번호 변경
            </a>
          </li>
          <li>
            <a href="">
              회원 탈퇴
            </a>
          </li>
          <li>
            <a href="">
              카드 추천 받기
            </a>
          </li>
          <li>
            <a href="">
              홈으로 가기
            </a>
          </li>
        </ul>
      </div>

    </div>
  </div>
</template>

<script setup>
  import MyPageItem from '@/components/MyPageItem.vue'
  import Header from '@/components/Header.vue'
  import { ref } from 'vue'

</script>

<style scoped>
.my-page-bg {
  /* width: 1760px; */
  width: 90vw;
  height: 700px;
  border-radius: 47px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
  position: absolute;
  left: -100px;
  top: 45px;
}
.my-page-wrap {
  display: flex;
  justify-content: end;
  margin-top: 100px;
  margin-right: 90px
}
.my-page-menu {
  padding: 10px auto;
}
.my-page-menu-list {
  font-size: large;
  /* font-weight: bold; */
  display: flex;
  justify-content: left;
  flex-direction: column;
  gap: 30px
}
.isNow {
  color: rgb(33, 95, 255);
  font-weight: bold;
}
.my-info-item {
  /* border: 2px solid brown; */
  width: 38%;
  margin-left: 35%;
  margin-top: 10%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>