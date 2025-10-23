<template>
  <div class="quiz-container">

    <div v-if="quizStore.loading" class="loading-message">
      در حال بارگذاری سوالات...
    </div>

    <div v-else-if="quizStore.error" class="error-message">
      {{ quizStore.error }}
    </div>

    <div v-else-if="quizStore.currentQuiz" class="quiz-content">
      <h1>آزمون: {{ quizStore.currentQuiz.title }}</h1>
      <hr>

      <div class="progress-section">
        <div class="progress-bar-container">
          <div class="progress-bar-fill" :style="{ width: progressPercentage + '%' }"></div>
        </div>
        <div v-if="currentStreak > 1" class="streak-display">
          🔥 {{ currentStreak }}
        </div>
      </div>

      <div v-if="currentQuestion" class="question-area" :class="{ 'shake-animation': applyShake }">

        <DragDropMatch
          v-if="currentQuestion.type === 'drag-drop-match' || currentQuestion.type === 'drag-drop-ordering'"
          :question="currentQuestion"
          :feedback="feedback"
          :disabled="quizState !== 'answering'"
          @update:answer="userAnswer = $event"
        />

        <MultipleSelect
          v-else-if="currentQuestion.type === 'multiple-select'"
          :question="currentQuestion"
          :feedback="feedback"
          :disabled="quizState !== 'answering'"
          @update:answer="userAnswer = $event"
        />

        <TrueFalse
          v-else-if="currentQuestion.type === 'true-false'"
          :question="currentQuestion"
          :feedback="feedback"
          :disabled="quizState !== 'answering'"
          @update:answer="userAnswer = $event"
        />

        <DragDropFill
          v-else-if="currentQuestion.type === 'drag-drop-fill'"
          :question="currentQuestion"
          :feedback="feedback"
          :disabled="quizState !== 'answering'"
          @update:answer="userAnswer = $event"
        />

        <div v-else>
          نوع سوال پشتیبانی نمی‌شود: {{ currentQuestion.type }}
        </div>

      </div>

      <footer class="quiz-footer">
        <button
          v-if="quizState === 'answering'"
          @click="checkAnswer"
          class="check-button btn-primary"
          :disabled="!isAnswerComplete"
        >
          بررسی
        </button>

        <button
          v-if="quizState === 'correct' || quizState === 'incorrect'"
          @click="handleContinue"
          class="continue-button"
          :class="quizState === 'correct' ? 'btn-primary' : 'btn-danger'"
        >
          ادامه
        </button>
      </footer>
    </div>

  </div>
</template>

<script setup>
import { ref, computed, nextTick } from 'vue';
import { useRouter } from 'vue-router';
import { useQuizStore } from '../stores/quiz';
import { useAuthStore } from '../stores/auth';
import { useNotificationStore } from '../stores/notificationStore';

import DragDropMatch from '../components/DragDropMatch.vue';
import MultipleSelect from '../components/MultipleSelect.vue';
import TrueFalse from '../components/TrueFalse.vue';
import DragDropFill from '../components/DragDropFill.vue';

const quizStore = useQuizStore();
const authStore = useAuthStore();
const notificationStore = useNotificationStore();
const router = useRouter();

const currentQuestionIndex = ref(0);
const userAnswer = ref(null);
const feedback = ref({});
const quizState = ref('answering');
const currentStreak = ref(0);
const applyShake = ref(false);

const currentQuestion = computed(() => {
  if (quizStore.currentQuiz && quizStore.currentQuiz.questions) {
    return quizStore.currentQuiz.questions[currentQuestionIndex.value];
  }
  return null;
});

const isAnswerComplete = computed(() => {
    if (!currentQuestion.value || userAnswer.value === null) return false;
    const type = currentQuestion.value.type;
    const answer = userAnswer.value;

    if (type === 'drag-drop-match' || type === 'drag-drop-ordering') {
        return answer.bank && answer.bank.length === 0;
    }
    if (type === 'multiple-select') {
        return Array.isArray(answer) && answer.length > 0;
    }
    if (type === 'true-false') {
        const statementCount = currentQuestion.value.statements.length;
        const answerCount = Object.keys(answer).length;
        return statementCount === answerCount;
    }
    if (type === 'drag-drop-fill') {
        const blankCount = currentQuestion.value.blanks.length;
        const answerCount = Object.values(answer).filter(Boolean).length;
        return blankCount === answerCount;
    }
    return true;
});

const progressPercentage = computed(() => {
  if (!quizStore.currentQuiz || !quizStore.currentQuiz.questions) return 0;
  const totalQuestions = quizStore.currentQuiz.questions.length;
  return ((currentQuestionIndex.value + 1) / totalQuestions) * 100;
});

const playSound = (soundFile) => {
  try {
    const audio = new Audio(`/${soundFile}`);
    audio.play();
  } catch (error) {
    console.error("Error playing sound:", error);
  }
};

const checkAnswer = async () => {
  if (!currentQuestion.value) return;

  applyShake.value = false;
  const isLast = currentQuestionIndex.value >= quizStore.currentQuiz.questions.length - 1;

  try {
    const response = await quizStore.submitAnswer(
      quizStore.currentQuiz.id,
      currentQuestion.value.id,
      userAnswer.value,
      isLast
    );
    const data = response.data;

    feedback.value = data.feedback;

    authStore.updateUserScore(data.newTotalScore);
    authStore.updateUserLevel(data.newLevel);
    currentStreak.value = data.isCorrect ? (currentStreak.value + 1) : 0;
    quizStore.addSessionScore(data.scoreEarned);

    if (data.newlyEarnedBadges && data.newlyEarnedBadges.length > 0) {
      quizStore.setNewlyEarnedBadges(data.newlyEarnedBadges);
    }

    if (data.isCorrect) {
      playSound('correct.mp3');
      notificationStore.showCorrectFeedback();
      quizState.value = 'correct'; // Set state after notification
    } else {
      playSound('incorrect.mp3');
      notificationStore.showIncorrectFeedback();
      applyShake.value = true;
      setTimeout(() => { applyShake.value = false; }, 500);
      quizState.value = 'incorrect'; // Set state after notification
    }

  } catch (err) {
    console.error("Error checking answer:", err);
    notificationStore.showNotification({ title: 'خطا', message: 'مشکلی در ثبت پاسخ رخ داد.' });
  }
};

const handleContinue = () => {
  notificationStore.hideNotification(); // Close any open notification
  if (currentQuestionIndex.value < quizStore.currentQuiz.questions.length - 1) {
    currentQuestionIndex.value++;
    quizState.value = 'answering';
    feedback.value = {};
    userAnswer.value = null;
    applyShake.value = false;
  } else {
    currentStreak.value = 0;
    router.push({ name: 'QuizResult' });
  }
};
</script>

<style scoped>
.quiz-container { max-width: 800px; margin: 20px auto; padding: 2rem; padding-bottom: 200px; }
.loading-message, .error-message { font-size: 1.2rem; color: var(--color-text-light); text-align: center; padding: 2rem; }
.error-message { color: var(--color-danger); }
.quiz-content { text-align: center; }
hr { margin: 1.5rem 0; border: none; border-top: 1px solid var(--color-border); }
.progress-section { display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem; /* Reduced margin */}
.progress-bar-container { flex-grow: 1; height: 15px; background-color: var(--color-border); border-radius: 10px; overflow: hidden; }
.progress-bar-fill { height: 100%; background-color: var(--color-primary); border-radius: 10px; transition: width 0.3s ease-out; }
.streak-display { font-size: 1.5rem; font-weight: bold; color: var(--color-warning); min-width: 50px; text-align: right; }
.question-area { margin-bottom: 2rem; }
.quiz-footer { position: fixed; bottom: 0; left: 0; right: 0; padding: 1rem 2rem; background-color: var(--color-background-light); border-top: 2px solid var(--color-border); display: flex; justify-content: center; align-items: center; height: 90px; z-index: 10; }
/* Button classes btn-primary/btn-danger applied in template */
.check-button, .continue-button { width: 200px; /* Ensure buttons have width */ }
/* Feedback banner styles removed as NotificationDisplay handles it */
/* Animation classes refer to global style.css */
</style>