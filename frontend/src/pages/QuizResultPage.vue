<template>
  <div class="result-container">
    <div class="result-card card">
      <h1>🎉 آزمون کامل شد! 🎉</h1>

      <div v-if="didLevelUp" class="level-up-banner">
         <h2>🥳 تبریک! سطح شما بالا رفت!</h2>
         <p>شما به سطح <span class="new-level">{{ authStore.level }}</span> رسیدید.</p>
      </div>

      <p class="result-summary">
        شما در این آزمون <span class="highlight">{{ quizStore.currentSessionScore }}</span> امتیاز کسب کردید.
      </p>

      <div class="total-score">
        امتیاز کل شما: <span class="highlight-total">{{ finalTotalScore }}</span>
      </div>

      <router-link to="/dashboard" class="back-button btn-primary">بازگشت به داشبورد</router-link>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue';
import { useQuizStore } from '../stores/quiz';
import { useAuthStore } from '../stores/auth';
import { useNotificationStore } from '../stores/notificationStore';

const quizStore = useQuizStore();
const authStore = useAuthStore();
const notificationStore = useNotificationStore();

onMounted(() => {
  const sessionScore = quizStore.currentSessionScore;
  const totalScore = finalTotalScore.value;
  const possibleScore = quizStore.currentQuiz?.total_possible_score;

  console.log(`[QuizResultPage] Possible score for this quiz: ${possibleScore}`); // <-- لاگ جدید
  
  if (possibleScore && sessionScore >= possibleScore / 2) {
      notificationStore.showGoodResult(sessionScore, totalScore);
      console.log('[QuizResultPage] Showing GOOD result notification.'); // <-- لاگ جدید
  } else {
      notificationStore.showBadResult(sessionScore, totalScore);
      console.log('[QuizResultPage] Showing BAD result notification.'); // <-- لاگ جدید
  }
});

const finalTotalScore = computed(() => {
  return quizStore.lastSubmissionResult?.newTotalScore ?? authStore.score;
});

const didLevelUp = computed(() => {
  return quizStore.lastSubmissionResult && quizStore.lastSubmissionResult.levelUp;
});

</script>

<style scoped>
.result-container { display: flex; align-items: center; justify-content: center; min-height: 80vh; text-align: center; }
.result-card { /* Base styles from .card in style.css */ padding: 3rem !important; }
h1 { color: var(--color-text); margin-bottom: 2rem; }
.level-up-banner { background-color: #fffbeb; border: 2px solid var(--color-warning); border-radius: 12px; padding: 1rem; margin-bottom: 2rem; }
.level-up-banner h2 { color: var(--color-warning-dark); margin-top: 0; }
.new-level { font-weight: bold; font-size: 1.2em; }
.result-summary { font-size: 1.5rem; color: var(--color-text-light); margin-bottom: 1rem; }
.total-score { font-size: 1.2rem; color: var(--color-text-light); margin-bottom: 2.5rem; }
.highlight { font-weight: bold; color: var(--color-primary); font-size: 1.8rem; }
.highlight-total { font-weight: bold; color: var(--color-text); }
.back-button { text-decoration: none; } /* Base styles from .btn-primary */
</style>