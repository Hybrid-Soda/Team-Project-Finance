<template>
  <div class="filter-container">
    <ul class="filter-list">
      <input type="text" class="form-control" v-model="search" placeholder="검색어를 입력하세요." style="margin-bottom: 4%;">
      <button class="filter-button" @click="searchCard">검색</button>
    </ul>

    <ul class="filter-list">
      <div class="category">정렬</div>
      <button class="sort-item" @click="store.sortCard('sortName')">이름순</button>
      <button class="sort-item" @click="store.sortCard('sortRecord')">전월실적순</button>
      <button class="sort-item" @click="store.sortCard('sortAnnualFee')">연회비순</button>
    </ul>

    <ul class="filter-list">
      <div class="category">필터</div>
      <label class="label">카드사</label>
      <div class="card-brand-list">
        <div class="form-check" v-for="brand in store.brands" :key="brand">
          <input class="form-check-input" type="checkbox" :value="brand" :id="brand" v-model.number="condA"/>
          <label class="form-check-label" :for="brand">{{ brand }}</label>
        </div>
      </div>
      <li class="filter-comp mt-3">
        <label for="range1" class="form-label">
          <span v-if="condB < 50">실적 : {{ condB }}만원 이하</span>
          <span v-else>실적 : {{ condB }}만원 이상</span>
        </label>
        <input type="range" class="form-range" min="0" max="50" step="5" id="range1" v-model.number="condB"/>
      </li>
      <li class="filter-comp">
        <label for="range2" class="form-label">
          <span v-if="condC < 100000">연회비 : {{ condC }}원 이하</span>
          <span v-else>연회비 : {{ condC }}원 이상</span>
        </label>
        <input type="range" class="form-range" min="0" max="100000" step="10000" id="range2" v-model="condC"/>
      </li>

      <button class="filter-button" @click="filterCard">조회하기</button>
    </ul>
  </div>
</template>

<script setup>
import { ref } from "vue"
import { useCardStore } from "@/stores/card"

const store = useCardStore()
const condA = ref([])
const condB = ref(0)
const condC = ref(0)
const search = ref('')

const filterCard = () => {
  store.filterCard({
    brands: condA.value,
    record: condB.value,
    annualFee: condC.value,
  })
}

const searchCard = function () {
  store.tempCards = store.cards.filter(card => 
    card.name.includes(search.value)
  )
  search.value = ''
}
</script>

<style scoped>
.filter-container {
  width: 14vw;
  display: flex;
  flex-direction: column;
}
.filter-list {
  padding: 0;
  display: flex;
  font-size: large;
  font-weight: 500;
  text-align: center;
  flex-direction: column;
}
.form-check {
  text-align: start;
}
.sort-item {
  padding: 0;
  margin-block: 3px;
  background-color: white;
}
.sort-item:focus {
  color: rgb(255, 199, 39);
}
.category {
  padding: 5px;
  cursor: default;
  font-weight: 700;
  text-align: center;
  margin-bottom: 5px;
  background-color: white;
  border-bottom: 2px solid rgb(219, 219, 219);
}
.label {
  text-align: start;
  padding: 0 10px;
}
.card-brand-list {
  height: 160px;
  padding: 10px;
  overflow-y: scroll;
}
.filter-button {
  width: 100%;
  padding: 5px;
  font-weight: 600;
  text-align: center;
  border-radius: 37px;
  color: rgb(255, 199, 39);
  border: 2px solid rgb(255, 199, 39);
  background-color: rgba(0, 0, 0, 0);
}
.filter-button:hover {
  color: rgb(255, 255, 255);
  background-color: rgb(255, 199, 39);
}
</style>
