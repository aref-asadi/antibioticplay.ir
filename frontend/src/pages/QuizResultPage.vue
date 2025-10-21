<template>
  <div class="result-container">
    <div class="result-card">
      <h1>🎉 آزمون کامل شد! 🎉</h1>

      <div v-if="didLevelUp" class="level-up-banner">
        <h2>🥳 تبریک! سطح شما بالا رفت!</h2>
        <p>شما به سطح <span class="new-level">{{ authStore.level }}</span> رسیدید.</p>
      </div>
      <p class="result-summary">
        شما در این آزمون <span class="highlight">{{ quizStore.currentSessionScore }}</span> امتیاز کسب کردید.
      </p>

      <div class="total-score">
        امتیاز کل شما: <span class="highlight-total">{{ authStore.score }}</span>
      </div>

      <router-link to="/dashboard" class="back-button">بازگشت به داشبورد</router-link>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useQuizStore } from '../stores/quiz';
import { useAuthStore } from '../stores/auth';

const quizStore = useQuizStore();
const authStore = useAuthStore();

// چک می‌کنیم که آیا در آخرین پاسخ، پرچم levelUp=true بوده یا نه
const didLevelUp = computed(() => {
  return quizStore.lastSubmissionResult && quizStore.lastSubmissionResult.levelUp;
});
</script>

<style scoped>
.result-container {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 80vh;
  text-align: center;
}
.result-card {
  background-color: #fff;
  padding: 3rem;
  border-radius: 16px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.1);
}
h1 {
  color: #333;
  margin-bottom: 2rem;
}
.result-summary {
  font-size: 1.5rem;
  color: #555;
  margin-bottom: 1rem;
}
.total-score {
  font-size: 1.2rem;
  color: #777;
  margin-bottom: 2.5rem;
}
.highlight {
  font-weight: bold;
  color: #42b983; /* Green */
  font-size: 1.8rem;
}
.highlight-total {
  font-weight: bold;
  color: #333;
}
.back-button {
  display: inline-block;
  padding: 0.8rem 1.5rem;
  background-color: #42b983;
  color: white;
  text-decoration: none;
  border-radius: 8px;
  font-size: 1.1rem;
  font-weight: bold;
  transition: background-color 0.2s;
}
.back-button:hover {
  background-color: #369d6e;
}

.level-up-banner {
  background-color: #fffbeb; /* Light yellow */
  border: 2px solid #fde047; /* Yellow */
  border-radius: 12px;
  padding: 1rem;
  margin-bottom: 2rem;
}
.level-up-banner h2 {
  color: #ca8a04; /* Dark Yellow */
  margin-top: 0;
}
.new-level {
  font-weight: bold;
  font-size: 1.2em;
}

.result-summary {
  font-size: 1.5rem;
  color: #555;
  margin-bottom: 1rem;
}
</style>