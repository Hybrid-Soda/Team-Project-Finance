<template>
  <div class="wrap">
    <header>
      <img src="../assets/img/example_card.png" alt="">
      <div class="title">신한카드 Point Plan</div>
    </header>
    <main>
      <p>혜택</p>
      <p>실적</p>
    </main>
  </div>
</template>

<script setup>

</script>

<style scoped>
.wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}
header, main {
  display: flex;
  flex-direction: column;
  align-items: center;
}
header {
  gap: 20px;
}
img {
  width: 50%;
}
.title {
  font-size: 24px;
  color: black;
  font-weight: bold;
}
</style>