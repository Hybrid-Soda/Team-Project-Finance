<template>
  <footer>
  <div class="footer-container">
    <div class="footer-logo">
      <RouterLink :to="{ name:'home' }">
        <img src="@/assets/img/PICKardº_blue.png" alt="pickard">
      </RouterLink>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2024 PICKard. All rights reserved.</p>
    </div>
    <div class="footer-contact">
      <p>Email : <a href="#">pickard2024@pickard.com</a></p>
      <p>Phone : <a href="#">+1 234 567 890</a></p>
    </div>
  </div>
</footer>
</template>

<script setup>
</script>

<style scoped>
footer {
  background-color: #333;
  color: #fff;
  padding: 20px 0;
  margin-top: 500px;
}

.footer-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
}

.footer-logo img {
  width: 100px;
}

.footer-contact p {
  margin: 5px 0;
}

.footer-contact a {
  color: #fff;
  text-decoration: none;
}

.footer-contact a:hover {
  text-decoration: underline;
}

.footer-bottom {
  margin-top: 20px;
}
</style>