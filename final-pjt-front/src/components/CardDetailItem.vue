<template>
  <div class="detail-main">
    <img src="../assets/img/example_card.png" class="card-img">
    <div class="card-content">
      <p class="card-name">신한카드 Point Plan</p>
      <p>큰 소비일수록 계획이 필요한 법</p>
      <div>
        <button class="go-button">신청하러 가기</button>
        <button data-bs-toggle="modal" data-bs-target="#exampleModal">오프라인 매장 보기</button>    
      </div>
    </div>
  </div>
  <div>
    <h1>일상 생활비 적립</h1>
    <p>국내 건당 결제 금액별 0.5~3% 포인트 적립</p>
    <p>신한 SOL페이 국내 결제시 0.1% 추가 적립</p>
    <h1>주말 외식비 적립</h1>
    <h1>정기결제 자동납부 적립</h1>
    <h1>공통 유의사항</h1>
  </div>

  <!-- Modal -->
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          ...
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary">Save changes</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  

</script>

<style scoped>
.card-img {
  width: 300px;
  height: fit-content;
}
.card-content {
  /* border: 2px solid pink; */
  display: flex;
  flex-direction: column;
  justify-content: baseline;
}
.go-button {
  background-color: rgb(255, 199, 39);
  font-weight: bold;
}
.detail-main {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 5%;
  border: 2px solid blueviolet;
}
.card-name {
  color: black;
  font-size: 36px;
  font-weight: 800;
}
</style>