<template>
  <div>
    <div class="card-list-content">
          <div>
            <ul class="filter-list">
              <li class="filter-comp">
                <a href="">
                    카드사
                </a>
              </li>
              <li class="filter-comp">
                <label for="customRange3" class="form-label">실적</label>
                <input type="range" class="form-range" min="0" max="5" step="0.5" id="customRange3">
              </li>
              <li class="filter-comp">
                <label for="customRange3" class="form-label">연회비</label>
                <input type="range" class="form-range" min="0" max="5" step="0.5" id="customRange3">
              </li>
              <li class="isActivate filter-comp">
                <a href="#">
                  인기순 정렬
                </a>
              </li>
              <li class="filter-comp">
                <a href="#">
                  이름순 정렬
                </a>
              </li>
            </ul>
          </div>
        </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'


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
</style>