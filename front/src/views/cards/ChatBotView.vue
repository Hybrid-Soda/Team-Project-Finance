<template>
  <div>
    <div v-for="message in chatLog">
      <p>{{ message.role }} - {{ message.content }}</p>
    </div>

    <form @submit.prevent="chatReceive">
      <div class="form-floating">
        <input type="chat" class="form-control" id="chat" placeholder="" v-model.trim="userMsg"/>
        <label for="chat">질문을 입력해 주세요</label>
        <input type="submit" class="btn btn-outline-success" />
      </div>
    </form>
  </div>
</template>

<script setup>
import OpenAI from "openai"
import { ref } from "vue"
import axios from "axios"

const userMsg = ref("")
const chatLog = ref([])

const chatReceive = async () => {
  chatLog.value.push({
    role: "user",
    content: userMsg.value,
  })

  try {
    const openai = new OpenAI({
        apiKey: import.meta.env.VITE_API_KEY,
        dangerouslyAllowBrowser: true
    })

    const response = await openai.chat.completions.create({
      messages: chatLog.value,
      model: "davinci-002",
      // model: "gpt-3.5-turbo",
      max_tokens: 5
    })

    if (response && response.choices && response.choices.length > 0) {
      chatLog.value.push({
        role: "system",
        content: response.choices[0].message.content
      })
    } else {
      console.error('Invalid response:', response);
    }

    userMsg.value = ""

  } catch (err) {
    console.error('Error fetching data:', err)
  }
}
</script>

<style scoped></style>
