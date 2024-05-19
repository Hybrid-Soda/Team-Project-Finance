<template>
  <div>
    <div class="card-list-content">
          <div>
            <ul class="filter-list">
              <div class="category">정렬</div>
              <li class="isActivate filter-sort">
                <a href="#">
                  인기순 정렬
                </a>
              </li>
              <li class="filter-sort">
                <a href="#">
                  이름순 정렬
                </a>
              </li>
            </ul>
            <br>
            <ul>
              <div class="category">필터</div>
              <li class="filter-comp">
                <label for="">카드사</label>
                <div class="card-brand-list">
                  <div class="form-check" v-for="brand in store.brands">
                    <input class="form-check-input" type="checkbox" value="신한카드" :id="brand">
                    <label class="form-check-label" :for="brand">
                      {{ brand }}
                    </label>
                  </div>
                </div>
              </li>
              <li class="filter-comp" style="margin-top: 10px;">
                <label for="customRange3" class="form-label">실적</label>
                <input type="range" class="form-range" min="0" max="5" step="0.5" id="customRange3">
              </li>
              <li class="filter-comp">
                <label for="customRange3" class="form-label">연회비</label>
                <input type="range" class="form-range" min="0" max="5" step="0.5" id="customRange3">
              </li>
              <a href=""><div class="filter-button">
                조회하기
                <!-- <input type="submit" class="filter-button" value="조회하기"> -->
              </div></a>
            </ul>
          </div>
          
        </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useCardStore } from '@/stores/card';
  const store = useCardStore()


</script>

<style scoped>
.isActivate {
  color: rgb(255, 199, 39)
}
.filter-comp {
  margin: 15px auto;
  font-size: large;
  font-weight: 500;
}
.form-range-thumb {
  background-color: rgb(255, 199, 39);
}
.card-brand-list {
  /* border: 2px solid red; */
 height: 150px;
 padding: 10px;
 overflow-y: scroll; 
}
.category {
  text-align: center;
  /* color: rgb(204, 204, 204); */
  font-weight: 700;
  padding: 5px;
  margin-bottom: 5px;
  background-color: white;
  border-bottom: 2px solid rgb(219, 219, 219);
  /* border-radius: 37px; */
  cursor: default;
}
.filter-list {
  /* border: 1px solid blue; */
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}
.filter-sort {
  font-size: large;
  font-weight: 500;
  margin-top: 5px;
}
.filter-button {
  text-align: center;
  color: black;
  font-weight: 700;
  padding: 5px;
  border: 2px solid rgb(255, 199, 39);
  /* border: none; */
  border-radius: 37px;
  background-color: rgba(0, 0, 0, 0);
  color: rgb(255, 199, 39);
  text-align: center;
}
.card-list-content {
  display: flex;
  flex-direction: column;
  align-items: end;
}
</style>