<template>
  <div class="body">
    <Header />
    <main @scroll="handleScroll" ref="scrollContainer">
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
            <div class="loading-box" v-if="!slicedCard.length">
              <div id="loading"></div>
            </div>
            <CardListItem
            v-for="card in slicedCard"
            :key="card.id"
            :card="card"
            />
            <div v-if="isLoading">
              <div class="search-result--loading-card" v-for="_ in 3">
                <div class="search-result--loading-img"></div>
                <div class="search-result--loading-text">
                  <h2 class="search-result--loading-cardName"></h2>
                  <p class="search-result--loading-cardContent"></p>
                  <p class="search-result--loading-cardContent"></p>
                  <p class="search-result--loading-cardContent"></p>
                </div>
              </div><hr>
            </div>
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
import '@/assets/loader.css'

import { ref, onMounted, computed } from 'vue'
import { useCardStore } from '@/stores/card'

const cardStore = useCardStore()
const isLoading = ref(false)
const batchSize = 20
const slicedCard = ref([])
const loadedCount = ref(0)
const scrollContainerRef = ref(null)

const loadMoreCards = () => {
  if (isLoading.value) return
  isLoading.value = true
  setTimeout(() => {
    const start = loadedCount.value
    const end = loadedCount.value + batchSize
    slicedCard.value.push(...cardStore.cards.slice(start, end))
    loadedCount.value += batchSize
    isLoading.value = false
  }, 1000)
}

const handleScroll = () => {
  const scrollContainer = scrollContainerRef.value
  console.log(scrollContainer)
  if (scrollContainer.scrollTop + scrollContainer.clientHeight >= scrollContainer.scrollHeight - 10) {
    loadMoreCards()
  }
}

onMounted(() => {
  cardStore.readCard()
  loadMoreCards()
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