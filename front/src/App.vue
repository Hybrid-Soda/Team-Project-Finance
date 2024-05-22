<template>
  <div style="height: 100%;">
    <RouterView />
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useRoute, useRouter } from 'vue-router'

  !function(w, d, s, ...args){
    var div = d.createElement('div');
    div.id = 'aichatbot';
    d.body.appendChild(div);
    w.chatbotConfig = args;
    var f = d.getElementsByTagName(s)[0],
    j = d.createElement(s);
    j.defer = true;
    j.type = 'module';
    j.src = 'https://aichatbot.sendbird.com/index.js';
    f.parentNode.insertBefore(j, f);
  }(window, document, 'script', 'C70DB29C-C1EF-407A-98F7-175C6AA6BBC6', 'onboarding_bot', {
    apiHost: 'https://api-cf-ap-2.sendbird.com',
  });
</script>

<style scoped>
</style>