<template>
  <div class="body">
    <Header/>
    <main>
      <div class="community-bg">
        <div class="head">
          <div></div>
          <form class="filter">
            <select name="" id="" class="form-select" style="width: 30%;">
              <option value="작성자">작성자</option>
              <option value="글 내용">글 내용</option>
            </select>
            <input type="text" class="form-control" placeholder="검색어를 입력해주세요.">
            <input type="submit" class="button" value="검색">
          </form>
          <button class="create-btn" data-bs-toggle="modal" data-bs-target="#exampleModal">글 작성하기</button>
        </div>
        <div class="wrap-content">
          <div class="content">
            <div class="list">
              <CommunityItem  @click="activeDetail" class="touch"/>
              <CommunityItem  @click="activeDetail" class="touch"/>
            </div>
            <div class="detail" v-if="isActive">
              <CommunityItemDetail />
            </div>
          </div>
        </div>
      </div>
    </main>
    <!-- <div class="d-flex justify-space-between">
      <h1 class="me-auto">금융상품 자유 게시판</h1>
      <RouterLink v-if="userStore.isLogIn" :to="{ name: 'postCreate' }">
        <button>글 쓰기</button>
      </RouterLink>
    </div><br>

    <table class="table">
      <thead>
        <tr>
          <th scope="col">글 번호</th>
          <th scope="col">제목</th>
          <th scope="col">작성자</th>
          <th scope="col">작성일자</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="post in postStore.posts" :key="post.id" @click="goDetail(post.id)" class="post">
          <th scope="row">{{ post.id }}</th>
          <td>{{ post.title }}</td>
          <td>{{ post.user.nickname }}</td>
          <td>{{ post.created_at.slice(0, 10) }}</td>
        </tr>
      </tbody>
    </table> -->
  </div>
    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">글 작성하기</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form>
            <label for="title">
              <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">Email address</label>
                <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
              </div>
              <div class="mb-3">
                <label for="exampleFormControlTextarea1" class="form-label">Example textarea</label>
                <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
              </div>
            </label>
          </form>
        </div>
        <div class="modal-footer">
          <button data-bs-dismiss="modal">Close</button>
          <input type="submit" class="save-btn" value="Save">
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter, RouterLink } from 'vue-router'
import { usePostStore } from '@/stores/post'
import { useUserStore } from '@/stores/user'
import { onMounted } from 'vue'
import Header from '@/components/Header.vue'
import { ref } from 'vue'
import PostDetailView from './PostDetailView.vue'
import CommunityItem from '@/components/CommunityItem.vue'
import CommunityItemDetail from '@/components/CommunityItemDetail.vue'

const router = useRouter()
const postStore = usePostStore()
const userStore = useUserStore()

onMounted(() => {
  postStore.readPost()
})

const goDetail = (id) => {
  router.push({ name: 'postDetail', params: { id } })
}

const isActive = ref(false)
  const activeDetail = function() {
    isActive.value = !isActive.value
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
  opacity: .6;
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