<template>
  <div class="wrap">
    <div class="header">
      <p>{{ post.title }}</p>
      <p>{{ post.user.nickname }}</p>
    </div>
    <div class="main">
      <p>{{ post.content.slice(0, 20) }}...</p>
      <p>&hearts; {{ likeLength }}</p>
    </div>
    <hr>
  </div>
</template>

<script setup>
import { ref, computed, defineProps } from 'vue'

const props = defineProps({
  post: {
    type: Object,
    required: true
  }
})

const likeLength = computed(() => {
  return props.post.like_users.length
})
</script>

<style scoped>
.wrap {
  padding: 0 3%;
}
.header {
  display: flex;
  justify-content: space-between;
  font-weight: 700;
}
.main {
  display: flex;
  justify-content: space-between;
}
</style>