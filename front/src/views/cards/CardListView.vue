<template>
  <div class="body">
    <Header />
    <main>
      <div class="card-page-bg">
        <div class="content">
          <div class="filter">
            <CardListFilter
            @sort-name="sortName"
            @sort-record="sortRecord"
            @sort-annual-fee="sortAnnualFee"
            @filter-cards="filterCards"
            />
          </div>
          <div class="card-list">
            <div class="loading-box" v-if="!slicedCard">
              <div id="loading"></div>
            </div>
            <CardListItem
            v-for="card in slicedCard"
            :key="card.id"
            :card="card"
            />
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import CardListFilter from '@/components/CardListFilter.vue'
import CardListItem from '@/components/CardListItem.vue'
import Header from '@/components/Header.vue'

import { ref, onMounted, computed } from 'vue'
import { useCardStore } from '@/stores/card'

const cardStore = useCardStore()
const slicedCard = ref(null)
// const slicedCard = computed(() => {
//   if (cardStore.cards) {
//     return cardStore.cards.slice(800, 2000)
//   }
// })

onMounted(() => {
  cardStore.readCard()
  setTimeout(() => {
    slicedCard.value = cardStore.cards.slice(800, 2000)
  }, 2000)
})

const sortName = () => slicedCard.value.sort((a, b) => a.name.localeCompare(b.name))
const sortRecord = () => slicedCard.value.sort((a, b) => a.record - b.record)
const sortAnnualFee = () => slicedCard.value.sort((a, b) => a.annual_fee1 - b.annual_fee1)

const filterCards = (filters) => {
  slicedCard.value = cardStore.cards.filter(card => {
    let matchBrand = filters.brands.includes(card.brand)
    if (filters.brands.length === 0) {
      matchBrand = true
    }

    let matchRecord = false
    if (filters.record <= 50) {
      matchRecord = card.record >= filters.record
    } else {
      matchRecord = card.record <= filters.record
    }

    let matchAnnualFee = false
    if (filters.annualFee >= 100000) {
      matchAnnualFee = card.annual_fee1 >= filters.annualFee
    } else {
      matchAnnualFee = card.annual_fee1 <= filters.annualFee
    }
    return matchBrand && matchRecord && matchAnnualFee
  })
}
</script>

<style scoped>
/* .card-page-bg {
  width: 100%;
  height: 1000px;
  border-radius: 50px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
  margin-top: 40px;
} */
.card-page-bg {
  background-image: url("@/assets/img/Rectangle 3.png");
}
.content {
  display: flex;
  justify-content: center;
  padding: 0 3%;
  padding-top: 2%;
  align-items: center;
  height: 800px;
}
.filter {
  width: 10%;
  height: 50%;
  /* border: 3px solid red; */
  display: flex;
  align-items: center;
  padding-bottom: 2%;
}
.card-list {
  /* border: 3px solid blue; */
  width: 90%;
  margin-left: 10%;
  height: 100%;
  overflow-y: scroll;
}
.loading-box {
  width: 100%;
  height: 100%;
  display: flex;  
  justify-content: center;
  align-items: center;
}
</style>