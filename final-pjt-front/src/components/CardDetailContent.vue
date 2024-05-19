<template>
  <div class="container body">
    <div class="content">
      <img src="@\assets\img\icons\shopping.png" alt="" class="d-img">
      <div class="detail">
        <p class="title">쇼핑</p>
        <p>백화점/할인점/홈쇼핑·온라인몰 1.0~5.0% 적립</p>
      </div>
    </div>
    <div class="content">
      <img src="@\assets\img\icons\shopping.png" alt="" class="d-img">
      <div class="detail">
        <p class="title">주유</p>
        <p>S-OIL, 에이치디현대오일뱅크 주유 시 리터 당 60원 적립</p>
      </div>
    </div>
    <div class="content">
      <img src="@\assets\img\icons\shopping.png" alt="" class="d-img">
      <div class="detail">
        <p class="title">쇼핑</p>
        <p>백화점/할인점/홈쇼핑·온라인몰 1.0~5.0% 적립</p>
      </div>
    </div>
    <div class="content">
      <img src="@\assets\img\icons\shopping.png" alt="" class="d-img">
      <div class="detail">
        <p class="title">쇼핑</p>
        <p>백화점/할인점/홈쇼핑·온라인몰 1.0~5.0% 적립</p>
      </div>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
.body {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  gap: 2%;
  flex-wrap: wrap;
  align-items: center;
  padding: 0% 2%;
}
.content {
  display: flex;
  align-items: center;
  width: 40%;
  margin: 2% 0;
  gap: 5%;
}
.d-img {
  width: 15%;
  opacity: .7;
}
.detail {
  width: 100%;
}
.title {
  color: black;
  font-size: 24px;
  font-weight: 800;
}
p {
  margin: 0;
}
</style>