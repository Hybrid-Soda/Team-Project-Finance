<template>
  <div class="body">
    <Header />
    <main>
      <main class="card-page-bg">
        <div class="content">
          <div class="filter">
            <CardListFilter />
          </div>
          <div class="card-list">
            <div class="loading-box" v-if="!cardStore.tempCards.length">
              <div id="loading"></div>
            </div>
            <CardListItem v-for="card in cardStore.tempCards" :key="card.id" :card="card"/>
            <div ref="trigger" id="trigger">
              <div id="loading"></div>
            </div>
          </div>
        </div>
      </main>
    </main>
  </div>
</template>

<script setup>
import CardListFilter from "@/components/CardListFilter.vue"
import CardListItem from "@/components/CardListItem.vue"
import Header from "@/components/Header.vue"
import "@/assets/loader.css"

import { ref, onMounted, computed } from "vue"
import { useCardStore } from "@/stores/card"

const cardStore = useCardStore()
const cardLength = computed(() => cardStore.tempCards.length)
const loading = ref(false)
const trigger = ref(null)

const loadCard = () => {
  if (cardStore.tempCards.length >= cardStore.cards.length) return
  loading.value = true
  const nextCards = cardStore.cards.slice(cardLength.value, cardLength.value + 40)
  cardStore.tempCards.push(...nextCards)
  loading.value = false
}

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting && !loading.value) {
      loadCard()
    }
  })
})

onMounted(() => {
  cardStore.readCard()
  observer.observe(trigger.value)
})
</script>

<style scoped>
.card-page-bg {
  background-image: url("@/assets/img/Rectangle 3.png");
}
.content {
  display: flex;
  padding: 0 5%;
  height: 800px;
  padding-top: 2%;
  align-items: center;
  justify-content: center;
}
.filter {
  width: 20%;
  display: flex;
  padding-bottom: 2%;
  align-items: center;
}
.card-list {
  width: 90%;
  height: 100%;
  margin-left: 6%;
  overflow-y: scroll;
}
.loading-box {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
#trigger {
  display: flex;
  justify-content: center;
}
</style>