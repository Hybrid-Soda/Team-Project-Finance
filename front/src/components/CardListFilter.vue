<template>
  <div>
    <div class="card-list-content">
      <div class="filter-wrap">
        <ul class="filter-list">
          <div class="category">정렬</div>
          <li
            class="filter-sort"
            :class="{ isActivate: activeSort === 'nameSort' }"
            @click="sortBy('nameSort')"
          >
            <a href="#">이름순</a>
          </li>
          <li
            class="filter-sort"
            :class="{ isActivate: activeSort === 'recordSort' }"
            @click="sortBy('recordSort')"
          >
            <a href="#">전월실적순</a>
          </li>
          <li
            class="filter-sort"
            :class="{ isActivate: activeSort === 'annualFeeSort' }"
            @click="sortBy('annualFeeSort')"
          >
            <a href="#">연회비순</a>
          </li>
        </ul>
        <br/>
        <ul>
          <div class="category">필터</div>
          <li class="filter-comp">
            <label for="">카드사</label>
            <div class="card-brand-list">
              <div class="form-check" v-for="brand in store.brands" :key="brand">
                <input class="form-check-input" type="checkbox" :value="brand" :id="brand" v-model="selectedBrands"/>
                <label class="form-check-label" :for="brand">{{ brand }}</label>
              </div>
            </div>
          </li>
          <li class="filter-comp" style="margin-top: 10px">
            <label for="customRange3" class="form-label">
              <span v-if="recordValue < 50">실적 : {{ recordValue }}만원 이하</span>
              <span v-else>실적 : {{ recordValue }}만원 이상</span>
            </label>
            <input type="range" class="form-range" min="0" max="50" step="5" id="customRange3" v-model="recordValue"/>
          </li>
          <li class="filter-comp">
            <label for="customRangeMin" class="form-label">
              <span v-if="annualFeeValue < 100000"
                >연회비 : {{ annualFeeValue }}원 이하</span
              >
              <span v-else>연회비 : {{ annualFeeValue }}원 이상</span>
            </label>
            <input type="range" class="form-range" min="0" max="100000" step="10000" id="customRangeMin" v-model="annualFeeValue"/>
          </li>
          <button @click="applyFilters" class="filter-button">조회하기</button>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, defineEmits } from "vue"
import { useCardStore } from "@/stores/card"

const store = useCardStore()

const recordValue = ref(0)
const annualFeeValue = ref(0)
const selectedBrands = ref([])
const activeSort = ref("nameSort")

const emit = defineEmits([
  "sortName",
  "sortRecord",
  "sortAnnualFee",
  "filterCards",
])


const sortBy = (criteria) => {
  activeSort.value = criteria
  switch(criteria) {
    case 'nameSort':
      emit('sortName')
      break
    case 'recordSort':
      emit('sortRecord')
      break
    case 'annualFeeSort':
      emit('sortAnnualFee')
      break
  }
}

const applyFilters = () => {
  emit("filterCards", {
    brands: selectedBrands.value,
    record: Number(recordValue.value),
    annualFee: Number(annualFeeValue.value),
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
.filter-sort a {
  text-decoration: none;
  color: inherit;
}
.filter-sort a:active {
  color: rgb(255, 199, 39);
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
