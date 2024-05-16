<template>
  <div>
    <Header />
    <div style="height: 843px; overflow: hidden;">
      <div class="card-page-bg">
        <div class="content">
          <div class="filter">
            <CardListFilter />
          </div>
          <div class="card-list">
            <CardListItem />
            <CardListItem />
            <CardListItem />
            <CardListItem />
            <CardListItem />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import CardListFilter from '@/components/CardListFilter.vue';
  import Header from '@/components/Header.vue';
  import CardListItem from '@/components/CardListItem.vue';

</script>

<style scoped>
.card-page-bg {
  width: 100%;
  height: 1000px;
  border-radius: 50px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
  margin-top: 40px;
}
.content {
  display: flex;
  justify-content: center;
  padding: 0 5%;
  padding-top: 2%;
  height: 75%;
  align-items: center;
}
.filter {
  width: 10%;
  height: 50%;
  /* border: 3px solid red; */
  display: flex;
  align-items: center;
  padding-bottom: 5%;
}
.card-list {
  /* border: 3px solid blue; */
  width: 90%;
  padding-left: 10%;
  height: 100%;
  overflow: scroll;
}
.card-list::-webkit-scrollbar {
    display: none; /* Chrome, Safari, Opera*/
}
</style>