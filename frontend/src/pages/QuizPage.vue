<template>
  <div class="quiz-layout">

    <header class="quiz-header">
      <button class="close-btn" @click="confirmExit">
        <font-awesome-icon icon="fas fa-times" />
      </button>
      
      <div class="hint-wrapper">
        <button 
          class="hint-btn" 
          @click="toggleHint" 
          :disabled="hintsRemaining <= 0 && !showHint"
          title="راهنمایی"
        >
          <font-awesome-icon icon="fas fa-lightbulb" :class="{ 'bulb-on': showHint }" />
          <span class="hint-count">{{ hintsRemaining }}</span>
        </button>
        <transition name="fade">
          <div v-if="showHint" class="hint-bubble-top">
            {{ currentQuestion?.hint || 'راهنمایی برای این سوال موجود نیست.' }}
          </div>
        </transition>
      </div>

      <div class="progress-container">
        <div class="progress-bar" :style="{ width: progressPercentage + '%' }">
          <div class="progress-highlight"></div>
        </div>
      </div>
      
      <div class="quiz-stats" v-if="currentStreak > 0">
        <font-awesome-icon icon="fas fa-fire" class="fire-icon" />
        <span>{{ currentStreak }}</span>
      </div>
    </header>

    <main class="quiz-body" ref="quizBody">
      
      <div v-if="quizStore.loading" class="loading-state">
        در حال آماده‌سازی سوالات...
      </div>

      <div v-else-if="currentQuestion" class="question-container" :class="{ 'shake-animation': applyShake }">
        <h2 class="question-title">{{ currentQuestion.title }}</h2>
        
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
      </div>
    </main>

    <transition name="slide-up">
      <div v-if="quizState === 'correct' || quizState === 'incorrect'" class="character-popup">
        <img 
          :src="quizState === 'correct' ? correctImg : incorrectImg" 
          class="character-img" 
          alt="Character"
        />
        <div class="speech-bubble" v-if="quizState === 'incorrect'">
          اوه! اشتباه بود.
        </div>
        <div class="speech-bubble correct-bubble" v-if="quizState === 'correct'">
          آفرین!
        </div>
      </div>
    </transition>

    <footer 
      class="quiz-footer" 
      :class="{ 
        'footer-correct': quizState === 'correct', 
        'footer-incorrect': quizState === 'incorrect' 
      }"
    >
      <div class="footer-content">
        
        <div v-if="quizState !== 'answering'" class="feedback-message">
          <div class="feedback-icon-circle">
            <font-awesome-icon :icon="quizState === 'correct' ? 'fas fa-check' : 'fas fa-times'" />
          </div>
          <div class="feedback-text">
            <h3 v-if="quizState === 'correct'">عالی بود!</h3>
            <h3 v-else>اشتباه بود!</h3>
            
            <p v-if="explanationText" class="explanation-text">{{ explanationText }}</p>
          </div>
        </div>

        <div class="action-button-wrapper">
          <button
            v-if="quizState === 'answering'"
            @click="checkAnswer"
            class="btn btn-primary check-btn"
            :disabled="!isAnswerComplete"
          >
            بررسی
          </button>

          <button
            v-else
            @click="handleContinue"
            class="btn continue-btn"
            :class="quizState === 'correct' ? 'btn-primary' : 'btn-danger'"
          >
            ادامه
          </button>
        </div>

      </div>
    </footer>

  </div>
</template>

<script setup>
import { ref, computed, onMounted, nextTick, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useQuizStore } from '../stores/quiz';
import { useAuthStore } from '../stores/auth';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faTimes, faCheck, faFire, faLightbulb } from '@fortawesome/free-solid-svg-icons'; // <-- Added faLightbulb

// Import Images
import correctImg from '../assets/feedback_correct.jpg';
import incorrectImg from '../assets/feedback_wrong.avif';

import DragDropMatch from '../components/DragDropMatch.vue';
import MultipleSelect from '../components/MultipleSelect.vue';
import TrueFalse from '../components/TrueFalse.vue';
import DragDropFill from '../components/DragDropFill.vue';

library.add(faTimes, faCheck, faFire, faLightbulb);

const route = useRoute();
const router = useRouter();
const quizStore = useQuizStore();
const authStore = useAuthStore();
const quizBody = ref(null);

// State Variables
const currentQuestionIndex = ref(0);
const userAnswer = ref(null);
const feedback = ref({});
const quizState = ref('answering');
const currentStreak = ref(0);
const applyShake = ref(false);
const explanationText = ref('');
const questionStartTime = ref(Date.now());

// Hint State
const hintsRemaining = ref(3);
const showHint = ref(false);

// Computed
const currentQuestion = computed(() => {
  if (quizStore.currentQuiz && quizStore.currentQuiz.questions) {
    return quizStore.currentQuiz.questions[currentQuestionIndex.value];
  }
  return null;
});

const progressPercentage = computed(() => {
  if (!quizStore.currentQuiz || !quizStore.currentQuiz.questions) return 0;
  const totalQuestions = quizStore.currentQuiz.questions.length;
  return (currentQuestionIndex.value / totalQuestions) * 100;
});

const isAnswerComplete = computed(() => {
    if (!currentQuestion.value || userAnswer.value === null) return false;
    const type = currentQuestion.value.type;
    const answer = userAnswer.value;

    if (type === 'drag-drop-match' || type === 'drag-drop-ordering') return answer.bank && answer.bank.length === 0;
    if (type === 'multiple-select') return Array.isArray(answer) && answer.length > 0;
    if (type === 'true-false') return currentQuestion.value.statements.length === Object.keys(answer).length;
    if (type === 'drag-drop-fill') return currentQuestion.value.blanks.length === Object.values(answer).filter(Boolean).length;
    return true;
});

// Watchers
watch(currentQuestion, () => {
  questionStartTime.value = Date.now();
  showHint.value = false; // مخفی کردن راهنما برای سوال جدید
});

onMounted(() => {
  const quizId = route.params.id;
  if (quizId) {
    quizStore.fetchQuizDetails(quizId);
  }
});

// Methods
const toggleHint = () => {
  if (showHint.value) {
    showHint.value = false;
  } else if (hintsRemaining.value > 0) {
    hintsRemaining.value--;
    showHint.value = true;
  }
};

const playSound = (soundFile) => {
  try {
    const audio = new Audio(`/${soundFile}`);
    audio.play();
  } catch (error) {
    console.error("Error playing sound:", error);
  }
};

const scrollToBottom = () => {
  nextTick(() => {
    if (quizBody.value) {
      quizBody.value.scrollTop = quizBody.value.scrollHeight;
    }
  });
};

const checkAnswer = async () => {
  if (!currentQuestion.value) return;

  const timeTaken = Math.floor((Date.now() - questionStartTime.value) / 1000);
  const isLast = currentQuestionIndex.value >= quizStore.currentQuiz.questions.length - 1;

  try {
    const response = await quizStore.submitAnswer(
      quizStore.currentQuiz.id,
      currentQuestion.value.id,
      userAnswer.value,
      isLast,
      timeTaken
    );
    
    const data = response.data;
    feedback.value = data.feedback;
    explanationText.value = data.explanation;

    authStore.updateUserScore(data.newTotalScore);
    authStore.updateUserLevel(data.newLevel);
    quizStore.addSessionScore(data.scoreEarned);

    if (data.newlyEarnedBadges && data.newlyEarnedBadges.length > 0) {
        quizStore.setNewlyEarnedBadges(data.newlyEarnedBadges);
    }

    if (data.isCorrect) {
      playSound('correct.mp3');
      quizState.value = 'correct';
      currentStreak.value++;
    } else {
      playSound('incorrect.mp3');
      quizState.value = 'incorrect';
      currentStreak.value = 0;
      applyShake.value = true;
      setTimeout(() => { applyShake.value = false; }, 500);
    }
    
    scrollToBottom();

  } catch (err) {
    console.error("Error checking answer:", err);
  }
};

const handleContinue = () => {
  if (currentQuestionIndex.value < quizStore.currentQuiz.questions.length - 1) {
    currentQuestionIndex.value++;
    quizState.value = 'answering';
    feedback.value = {};
    userAnswer.value = null;
    explanationText.value = '';
  } else {
    currentStreak.value = 0;
    router.push({ name: 'QuizResult' });
  }
};

const confirmExit = () => {
  if (confirm('آیا مطمئنید می‌خواهید آزمون را ترک کنید؟')) router.push('/dashboard');
};
</script>

<style scoped>
/* Layout */
.quiz-layout {
  display: flex; flex-direction: column; height: 100vh; height: 100dvh; background-color: white; overflow: hidden;
}

/* Header */
.quiz-header {
  flex: 0 0 auto; padding: 1.5rem 2rem; display: flex; align-items: center; gap: 1.5rem; background-color: white; z-index: 20; border-bottom: 1px solid #f0f0f0;
}
.close-btn { background: none; border: none; color: #e5e5e5; font-size: 1.5rem; cursor: pointer; padding: 0; min-width: auto; border-bottom: none; }
.close-btn:hover { color: var(--color-text-light); }

/* Hint Styles */
.hint-wrapper { position: relative; }
.hint-btn {
  background: none; border: 2px solid #e5e5e5; border-radius: 50%; width: 40px; height: 40px;
  display: flex; justify-content: center; align-items: center; cursor: pointer; color: #e5e5e5;
  transition: all 0.2s; position: relative; border-bottom-width: 4px; padding: 0; min-width: auto;
}
.hint-btn:not(:disabled) { border-color: #ffd700; color: #ffd700; background: #fffdf0; }
.hint-btn:active:not(:disabled) { transform: translateY(2px); border-bottom-width: 2px; }
.bulb-on { color: #ffc800; filter: drop-shadow(0 0 5px #ffd700); }
.hint-count {
  position: absolute; top: -5px; right: -5px; background: var(--color-primary); color: white;
  font-size: 0.7rem; width: 18px; height: 18px; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-weight: bold;
}
.hint-bubble-top {
  position: absolute; top: 120%; right: -20px; width: 250px; background: #333; color: white;
  padding: 1rem; border-radius: 12px; font-size: 0.9rem; z-index: 30; text-align: right; box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}
.hint-bubble-top::after {
  content: ''; position: absolute; top: -6px; right: 30px; width: 12px; height: 12px; background: #333; transform: rotate(45deg);
}

.progress-container { flex-grow: 1; height: 16px; background-color: #e5e5e5; border-radius: 10px; overflow: hidden; }
.progress-bar { height: 100%; background-color: var(--color-primary); border-radius: 10px; position: relative; transition: width 0.5s cubic-bezier(0.4, 0, 0.2, 1); }
.progress-highlight { position: absolute; top: 20%; left: 5%; right: 5%; height: 30%; background-color: rgba(255,255,255,0.3); border-radius: 10px; }
.quiz-stats { display: flex; align-items: center; gap: 0.5rem; color: #ff9600; font-weight: bold; font-size: 1.2rem; }

/* Main Body */
.quiz-body {
  flex: 1 1 auto; overflow-y: auto; padding: 1rem 2rem; padding-bottom: 2rem; display: flex; justify-content: center; position: relative; scroll-behavior: smooth;
}
.question-container { width: 100%; max-width: 800px; text-align: center; margin-top: 1rem; }
.question-title { font-size: 1.8rem; color: var(--color-text); margin-bottom: 2rem; text-align: right; }

/* Styles for Question Cards (Visual Polish) */
.question-container {
  background: white; /* یا #ffffff اگر پس زمینه صفحه رنگی باشد */
  /* برای برجسته شدن کارت */
  /* border: 2px solid #e5e5e5; */ /* اختیاری: اگر می‌خواهید کادر داشته باشد */
  /* border-radius: 20px; */
  /* padding: 2rem; */
  /* box-shadow: 0 4px 0 #e5e5e5; */ /* حالت سه‌بعدی */
}

/* Character Animation */
.character-popup { position: fixed; bottom: 140px; right: 20px; z-index: 90; display: flex; align-items: flex-end; gap: 10px; pointer-events: none; }
.character-img { width: 120px; height: auto; filter: drop-shadow(0 5px 15px rgba(0,0,0,0.2)); }
.speech-bubble { background: white; border: 2px solid #e5e5e5; padding: 0.8rem 1.2rem; border-radius: 20px 20px 0 20px; font-weight: bold; color: var(--color-danger); margin-bottom: 20px; animation: popIn 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
.correct-bubble { color: var(--color-primary); border-color: var(--color-primary); }

/* Footer */
.quiz-footer { flex: 0 0 auto; width: 100%; padding: 2rem; border-top: 2px solid #e5e5e5; background-color: white; transition: background-color 0.2s, border-color 0.2s; z-index: 100; position: relative; }
.footer-content { max-width: 1000px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; }
.feedback-message { display: flex; align-items: center; gap: 1rem; animation: slideRight 0.3s ease-out; }
@keyframes slideRight { from { opacity: 0; transform: translateX(-20px); } to { opacity: 1; transform: translateX(0); } }
.feedback-icon-circle { width: 60px; height: 60px; border-radius: 50%; background-color: white; display: flex; justify-content: center; align-items: center; font-size: 1.8rem; }
.footer-correct .feedback-icon-circle { color: var(--color-primary); }
.footer-incorrect .feedback-icon-circle { color: var(--color-danger); }
.feedback-text h3 { margin: 0; font-size: 1.5rem; font-weight: 800; }
.footer-correct .feedback-text { color: var(--color-primary-dark); }
.footer-incorrect .feedback-text { color: var(--color-danger-dark); }
.explanation-text { font-size: 0.95rem; color: #555; margin-top: 0.5rem; max-width: 600px; line-height: 1.5; text-align: right; }
.action-button-wrapper { margin-right: auto; }
.check-btn, .continue-btn { min-width: 150px; padding: 1rem 2rem; font-size: 1.1rem; width: 100%; }

/* Mobile Adjustments */
@media (max-width: 600px) {
  .footer-content { flex-direction: column; gap: 1rem; align-items: stretch; }
  .action-button-wrapper { width: 100%; margin: 0; }
  .feedback-message { margin-bottom: 0.5rem; justify-content: center; flex-direction: column; text-align: center; }
  .character-popup { bottom: 180px; right: 50%; transform: translateX(50%); }
  .character-img { width: 100px; }
  .explanation-text { text-align: center; }
}

/* Colors & Transitions */
.footer-correct { background-color: #d7ffb8; border-color: #d7ffb8; }
.footer-incorrect { background-color: #ffdfe0; border-color: #ffdfe0; }
.slide-up-enter-active, .slide-up-leave-active { transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
.slide-up-enter-from, .slide-up-leave-to { opacity: 0; transform: translateY(100px); }
.fade-enter-active, .fade-leave-active { transition: opacity 0.2s; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
@keyframes popIn { from { opacity: 0; transform: scale(0.5); } to { opacity: 1; transform: scale(1); } }
.shake-animation { animation: shake 0.5s ease-in-out; }
@keyframes shake { 0%, 100% { transform: translateX(0); } 25% { transform: translateX(-5px); } 75% { transform: translateX(5px); } }
</style>