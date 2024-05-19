<template>
  <div class="wrap">
    <div style="width: 90%; height: 100%;">
      <header>
        <div class="title">여기는 제목입니다.</div>
        <div class="user">user01</div>
      </header>
      <main>
        <div class="content">
          <img src="@/assets/img/404Error.png" alt=""><br>
          여기는 content입니다.<br>
          여기는 content입니다.<br>
          여기는 content입니다.<br>
          여기는 content입니다.<br>
          여기는 content입니다.<br>
          여기는 content입니다.<br>
          여기는 content입니다.<br>
          여기는 content입니다.<br>
          여기는 content입니다.<br>
          여기는 content입니다.<br>
          여기는 content입니다.<br>
          여기는 content입니다.<br>
          여기는 content입니다.<br>
          여기는 content입니다.<br>
          여기는 content입니다.<br>
          여기는 content입니다.<br>
          여기는 content입니다.<br>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
.wrap {
  overflow-y: scroll;
  width: 100%;
  height: 100%
}
header {
  padding-bottom: 2%;
  border-bottom: 3px solid rgb(224, 224, 224);
}
.title {
  font-size: x-large;
  color: black;
  font-weight: bold;
}
img {
  width: 300px;
}
main {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.content {
  width: 100%;
  display: block;
  margin-top: 3%;
}
</style>