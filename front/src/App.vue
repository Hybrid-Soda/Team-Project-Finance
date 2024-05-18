<template>
  <div>
    <RouterView />
  </div>

  <Footer />
</template>

<script setup>
  import { ref } from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  import Footer from '@/components/Footer.vue'

</script>

<style scoped>

</style>