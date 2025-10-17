<template>
  <div class="quiz-container">
    <div v-if="quizStore.loading">در حال بارگذاری سوالات...</div>
    <div v-else-if="quizStore.error">{{ quizStore.error }}</div>
    <div v-else-if="quizStore.currentQuiz">
      <h1>آزمون: {{ quizStore.currentQuiz.title }}</h1>
      <hr>
      </div>
  </div>
</template>

<script setup>
import { useQuizStore } from '../stores/quiz';
const quizStore = useQuizStore();
</script>

<style scoped>
.quiz-container {
  max-width: 800px;
  margin: 20px auto;
  padding: 2rem;
}
</style>