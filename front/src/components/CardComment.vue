<template>
  <div class="container body">
    <div class="content">
      <form>
        <div class="form-floating mb-3">
          <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
          <label for="floatingInput">제목</label>
        </div>
        <div class="form-floating mb-3">
          <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
          <label for="floatingInput">내용</label>
        </div>
        <input type="submit" value="작성하기">
      </form>
      <div class="detail">
        <div class="head">
          <div class="title">안녕하세요</div>
          <div class="user">user1</div>
        </div>
        <div class="text">이 카드는 ~~~ 암튼 조아요<br>이 카드는 ~~~ 암튼 조아요</div>
      </div>
      <div class="detail">
        <div class="head">
          <div class="title">안녕하세요</div>
          <div class="user">user1</div>
        </div>
        <div class="text">이 카드는 ~~~ 암튼 조아요<br>이 카드는 ~~~ 암튼 조아요</div>
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
form {
  display: flex;
  gap: 2%;
}
.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 80%;
  height: 80%;
  margin: 2% 0;
  gap: 5%;
  overflow: scroll;
}
.d-img {
  width: 15%;
  opacity: .7;
}
.detail {
  width: 100%;
  margin: 1% 0;
}
.title {
  color: black;
  font-size: 24px;
  font-weight: 800;
}
.head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 2%;
}
.user {
  font-size: 18px;
}
</style>