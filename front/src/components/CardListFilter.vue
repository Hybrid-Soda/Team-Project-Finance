<template>
  <div>
    <div class="card-list-content">
      <div class="filter-wrap">
        <ul class="filter-list">
          <div class="category">정렬</div>
          <li class="isActivate filter-sort">
            <a href="#">인기순</a>
          </li>
          <li class="filter-sort">
            <a href="#" @click="sortName">이름순</a>
          </li>
          <li class="filter-sort">
            <a href="#" @click="sortRecord">전월실적순</a>
          </li>
          <li class="filter-sort">
            <a href="#" @click="sortAnnualFee">연회비순</a>
          </li>
        </ul>
        <br/>
        <ul>
          <div class="category">필터</div>
          <li class="filter-comp">
            <label for="">카드사</label>
            <div class="card-brand-list">
              <div class="form-check" v-for="brand in store.brands" :key="brand">
                <input 
                class="form-check-input" 
                type="checkbox" 
                :value="brand" 
                :id="brand" 
                v-model="selectedBrands"
                />
                <label class="form-check-label" :for="brand">{{ brand }}</label>
              </div>
            </div>
          </li>
          <li class="filter-comp" style="margin-top: 10px">
            <label for="customRange3" class="form-label">실적</label>
            <input type="range" class="form-range" min="0" max="5" step="0.5" id="customRange3"/>
          </li>
          <li class="filter-comp">
            <label for="customRange3" class="form-label">연회비</label>
            <input type="range" class="form-range" min="0" max="5" step="0.5" id="customRange3"/>
          </li>
          <button @click="applyFilters" class="filter-button">
            조회하기
          </button>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, defineEmits } from "vue"
import { useCardStore } from "@/stores/card"

const store = useCardStore()

const selectedBrands = ref([])
const performance = ref(0)
const annualFee = ref(0)
const emit = defineEmits(["sortName", "sortRecord", "sortAnnualFee", "filterCards"])

const sortName = (_) => emit("sortName")
const sortRecord = (_) => emit("sortRecord")
const sortAnnualFee = (_) => emit("sortAnnualFee")

const applyFilters = () => {
  emit.filterCards({
    brands: selectedBrands.value,
    performance: performance.value,
    annualFee: annualFee.value
  })
}
</script>

<style scoped>
.isActivate {
  color: rgb(255, 199, 39);
}
.filter-wrap {
  width: 14vw;
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
  width: 100%;
  text-align: center;
  font-weight: 700;
  padding: 5px;
  border: 2px solid rgb(255, 199, 39);
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
.filter-button:hover {
  background-color: rgb(255, 199, 39);
  color: rgb(255, 255, 255);
}
</style>
