<template>
  <div class="body">
    <Header />
    <main>
      <div class="community-bg">
        <div class="head">
          <div></div>
          <form class="filter" @submit.prevent="searchPost">
            <select name="" id="" class="form-select" style="width: 30%" v-model="searchOption">
              <option value="writer">작성자</option>
              <option value="content">글 내용</option>
            </select>
            <input type="text" class="form-control" placeholder="검색어를 입력해주세요." v-model="searchValue"/>
            <input type="submit" class="button" value="검색" />
          </form>
          <RouterLink :to="{ name: 'postCreate' }">
            <button>
              글 작성하기
            </button>
          </RouterLink>
        </div>
        <div v-if="postStore.tempPosts" class="wrap-content">
          <div class="content">
            <div class="list">
              <PostItem
                v-for="post in postStore.tempPosts"
                :key="post.id"
                :post="post"
                @click="activeDetail(post)"
                class="touch"
                />
              </div>
              <div class="detail" v-if="isActive">
              <PostDetail
              :post="selectedPost"
              @close-detail="closeDetail"/>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import PostDetail from "@/components/PostDetail.vue"
import PostItem from "@/components/PostItem.vue"
import Header from "@/components/Header.vue"
import { usePostStore } from "@/stores/post"
import { onMounted } from "vue"
import { ref } from "vue"

const postStore = usePostStore()
const selectedPost = ref(null)
const isActive = ref(false)
const searchValue = ref('')
const searchOption = ref('writer')

onMounted(() => {
  postStore.readPost()
})

const activeDetail = function (post) {
  if (post !== selectedPost.value || isActive.value === false) {
    selectedPost.value = post
    isActive.value = true
  } else {
    isActive.value = false
  }
}

const closeDetail = function () {
  isActive.value = false
}

const searchPost = function () {
  const payload = {
    searchValue: searchValue.value,
    searchOption: searchOption.value
  }
  postStore.searchPost(payload)
  searchValue.value = ''
}
</script>

<style scoped>
.post:hover {
  cursor: pointer;
}
.body {
  height: 100%;
}
main {
  height: 85%;
}
.head {
  display: flex;
  align-items: center;
  justify-content: space-around;
  width: 100%;
  margin: 3% 0;
  gap: 3%;
  width: 100%;
}
.community-bg {
  background-image: url("@/assets/img/Rectangle 3.png");
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  height: 100%;
}
.filter {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 3%;
  width: 30%;
  padding-left: 5%;
}
.create-btn {
  /* background-color: rgb(255, 199, 39); */
  color: black;
  /* font-weight: bold; */
}
.create-btn:hover {
  background-color: rgb(255, 199, 39);
}
.content {
  display: flex;
  justify-content: center;
  padding: 0 5%;
  gap: 5%;
  width: 100%;
  height: 100%;
}
.list {
  overflow-y: scroll;
  width: 40%;
  height: 90%;
}
.detail {
  width: 40%;
  height: 90%;
}
.button {
  background-color: rgba(0, 0, 0, 0);
  border: none;
}
.touch:hover {
  opacity: 0.6;
  cursor: pointer;
}
.save-btn {
  border-radius: 38px;
  padding: 10px 20px;
  border: none;
  color: white;
  background-color: rgb(33, 95, 255);
}
.wrap-content {
  width: 100%;
  height: 80%;
}
</style>
