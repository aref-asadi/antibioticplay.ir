<template>
  <div class="result-container">
    <div class="result-card">
      <h1>🎉 آزمون کامل شد! 🎉</h1>

      <div v-if="didLevelUp" class="level-up-banner">
         </div>

      <p class="result-summary">
        شما در این آزمون <span class="highlight">{{ quizStore.currentSessionScore }}</span> امتیاز کسب کردید.
      </p>

      <div class="total-score">
        امتیاز کل شما: <span class="highlight-total">{{ finalTotalScore }}</span>
      </div>

      <router-link to="/dashboard" class="btn-primary">بازگشت به داشبورد</router-link>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'; // Import computed
import { useQuizStore } from '../stores/quiz';
import { useAuthStore } from '../stores/auth';

const quizStore = useQuizStore();
const authStore = useAuthStore(); // Keep authStore for level display if needed

onMounted(() => {
  // Keep logs for now if you want
  console.log('[QuizResultPage] Mounted.');
  console.log('[QuizResultPage] quizStore.currentSessionScore:', quizStore.currentSessionScore);
  console.log('[QuizResultPage] quizStore.lastSubmissionResult:', JSON.parse(JSON.stringify(quizStore.lastSubmissionResult)));
  console.log('[QuizResultPage] authStore.score (getter at mount):', authStore.score);
});

// --- *** Get final score from quizStore *** ---
const finalTotalScore = computed(() => {
  // Use the total score reported by the backend after the LAST submission
  return quizStore.lastSubmissionResult?.newTotalScore ?? authStore.score;
  // Fallback to authStore.score just in case lastSubmissionResult isn't set
});
// ---------------------------------------------

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
  color: var(--color-primary); /* Green */
  font-size: 1.8rem;
}
.highlight-total {
  font-weight: bold;
  color: var(--color-text); /* Use default text color */
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