<template>
  <div class="body">
    <Header />
    <main>
      <div class="card-page-bg">
        <div class="content">
          <div class="filter">
            <CardListFilter />
          </div>
          <div class="card-list">
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
  const slicedCard = computed(() => {
    if (cardStore.cards) {
      return cardStore.cards.slice(800, 1000)
    }
  })

  onMounted(() => {
    cardStore.readCard()
  })
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
  padding: 0 5%;
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
  padding-left: 10%;
  height: 100%;
  overflow-y: scroll;
}
</style>