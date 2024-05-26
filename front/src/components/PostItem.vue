<template>
  <div class="wrap">
    <div class="headerImage">
      <img
        v-if="post.image"
        class="postImage mt-3"
        :src="`${postStore.API_URL}${post.image}`"
        alt="image">
    </div>
    <div class="header">
      <p>{{ post.title }}</p>
      <p>{{ post.user.nickname }}</p>
    </div>
    <div class="main">
      <p>{{ post.content.slice(0, 20) }}<span v-if="post.content.length > 20">...</span></p>
      <p>&hearts; {{ likeLength }}</p>
    </div>
    <hr>
  </div>
</template>

<script setup>
import { ref, computed, defineProps } from 'vue'
import { usePostStore } from '@/stores/post'

const props = defineProps({
  post: {
    type: Object,
    required: true
  }
})

const postStore = usePostStore()
const likeLength = computed(() => {
  return postStore.tempPosts.find(post => post.id === props.post.id).like_users.length
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
.headerImage {
  text-align: center;
  margin-bottom: 5%;
}
.postImage {
  max-width: 50%;
  max-height: fit-content;
}
</style>