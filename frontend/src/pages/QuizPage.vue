<template>
  <div class="quiz-layout" :style="layoutStyles">
    <div class="bg-pattern-overlay"></div>

    <header class="quiz-header">
      <button class="close-btn" @click="confirmExit">
        <font-awesome-icon icon="fas fa-times" />
      </button>
      
      <button 
        class="icon-btn" 
        @click="handleBookmark"
        :class="{ 'active': isBookmarked }"
        title="ذخیره برای مرور"
        :style="bookmarkButtonStyle"
      >
        <font-awesome-icon :icon="isBookmarked ? 'fas fa-bookmark' : 'far fa-bookmark'" />
      </button>

      <div class="hint-wrapper">
        <button 
          class="hint-btn icon-btn" 
          @click="toggleHint" 
          :disabled="hintsRemaining <= 0 && !showHint"
          title="راهنمایی"
          :style="hintButtonStyle"
        >
          <font-awesome-icon icon="fas fa-lightbulb" :class="{ 'bulb-on': showHint }" />
          <span class="hint-count" :style="{ backgroundColor: themeColor }">{{ hintsRemaining }}</span>
        </button>
        
        <transition name="fade">
          <div v-if="showHint" class="hint-bubble-top">
            {{ currentQuestion?.hint || 'راهنمایی برای این سوال موجود نیست.' }}
          </div>
        </transition>
      </div>

      <div class="progress-container">
        <div class="progress-bar" :style="{ width: progressPercentage + '%', backgroundColor: themeColor }">
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

        <div v-if="currentQuestion.question_image && currentQuestion.type !== 'image-labeling'" class="question-image-container">
          <img :src="currentQuestion.question_image" alt="Question Image" />
        </div>
        
        <component 
          :is="getComponentType(currentQuestion.type)"
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
        <div class="speech-bubble" :class="{ 'correct-bubble': quizState === 'correct' }">
          {{ quizState === 'correct' ? 'آفرین!' : 'اوه! اشتباه بود.' }}
        </div>
      </div>
    </transition>

    <Confetti v-if="quizState === 'correct'" />

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
            class="btn check-btn"
            :style="checkButtonStyle"
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
import { useBookmarkStore } from '../stores/bookmarkStore';
import { library } from '@fortawesome/fontawesome-svg-core';
import { 
  faTimes, faCheck, faFire, faLightbulb, 
  faBookmark as fasBookmark 
} from '@fortawesome/free-solid-svg-icons';
import { faBookmark as farBookmark } from '@fortawesome/free-regular-svg-icons';

// Import Images
import correctImg from '../assets/feedback_correct.jpg';
import incorrectImg from '../assets/feedback_wrong.avif';

// Import Components
import DragDropMatch from '../components/DragDropMatch.vue';
import MultipleSelect from '../components/MultipleSelect.vue';
import TrueFalse from '../components/TrueFalse.vue';
import DragDropFill from '../components/DragDropFill.vue';
import ImageLabeling from '../components/ImageLabeling.vue';

import Confetti from '../components/Confetti.vue';

// Register Icons
library.add(faTimes, faCheck, faFire, faLightbulb, fasBookmark, farBookmark);

const route = useRoute();
const router = useRouter();
const quizStore = useQuizStore();
const authStore = useAuthStore();
const bookmarkStore = useBookmarkStore();
const quizBody = ref(null);

// --- State Variables ---
const currentQuestionIndex = ref(0);
const userAnswer = ref(null);
const feedback = ref({});
const quizState = ref('answering'); // 'answering', 'correct', 'incorrect'
const currentStreak = ref(0);
const applyShake = ref(false);
const explanationText = ref('');
const questionStartTime = ref(Date.now());
const hintsRemaining = ref(3);
const showHint = ref(false);

// --- Theme & Style Logic ---
const themeColor = computed(() => route.query.theme || '#58cc02');

const layoutStyles = computed(() => {
  const svgPattern = `data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%239C92AC' fill-opacity='0.08'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E`;
  return {
    backgroundColor: `${themeColor.value}1a`, // 10% opacity hex
    backgroundImage: `url("${svgPattern}")`
  };
});

const checkButtonStyle = computed(() => ({
  backgroundColor: themeColor.value,
  color: 'white',
  borderBottomColor: adjustColor(themeColor.value, -20)
}));

const hintButtonStyle = computed(() => ({
  borderColor: themeColor.value, 
  color: themeColor.value
}));

const bookmarkButtonStyle = computed(() => ({
  color: isBookmarked.value ? themeColor.value : '#e5e5e5',
  borderColor: isBookmarked.value ? themeColor.value : '#e5e5e5'
}));

// Helper to darken color
function adjustColor(color, amount) {
    return '#' + color.replace(/^#/, '').replace(/../g, color => ('0'+Math.min(255, Math.max(0, parseInt(color, 16) + amount)).toString(16)).substr(-2));
}

// --- Question Logic ---
const currentQuestion = computed(() => {
  if (quizStore.currentQuiz && quizStore.currentQuiz.questions) {
    return quizStore.currentQuiz.questions[currentQuestionIndex.value];
  }
  return null;
});

const getComponentType = (type) => {
  if (type === 'drag-drop-match' || type === 'drag-drop-ordering') return DragDropMatch;
  if (type === 'multiple-select') return MultipleSelect;
  if (type === 'true-false') return TrueFalse;
  if (type === 'drag-drop-fill') return DragDropFill;
  if (type === 'image-labeling') return ImageLabeling;
  return null;
};

const progressPercentage = computed(() => {
  if (!quizStore.currentQuiz?.questions) return 0;
  return (currentQuestionIndex.value / quizStore.currentQuiz.questions.length) * 100;
});

const isAnswerComplete = computed(() => {
    if (!currentQuestion.value || userAnswer.value === null) return false;
    const type = currentQuestion.value.type;
    const answer = userAnswer.value;

    if (type === 'drag-drop-match' || type === 'drag-drop-ordering') return answer.bank && answer.bank.length === 0;
    if (type === 'multiple-select') return Array.isArray(answer) && answer.length > 0;
    if (type === 'true-false') return currentQuestion.value.statements.length === Object.keys(answer).length;
    if (type === 'drag-drop-fill') return currentQuestion.value.blanks.length === Object.values(answer).filter(Boolean).length;
    if (type === 'image-labeling') return currentQuestion.value.drop_zones.length === Object.keys(answer).length;
    return true;
});

// --- Bookmark Logic ---
const isBookmarked = computed(() => {
  if (!currentQuestion.value) return false;
  return bookmarkStore.isBookmarked(quizStore.currentQuiz.id, currentQuestion.value.id);
});

const handleBookmark = async () => {
  if (!currentQuestion.value) return;
  await bookmarkStore.toggleBookmark(quizStore.currentQuiz.id, currentQuestion.value.id);
};

// --- Watchers ---
watch(currentQuestion, () => {
  questionStartTime.value = Date.now();
  showHint.value = false;
  userAnswer.value = null; // Reset answer
});

// --- Lifecycle ---
onMounted(() => {
  const quizId = route.params.id;
  if (quizId) {
    quizStore.fetchQuizDetails(quizId);
  }
});

// --- Interaction Methods ---
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
      // اسکرول نرم به پایین‌ترین نقطه
      quizBody.value.scrollTo({
        top: quizBody.value.scrollHeight,
        behavior: 'smooth'
      });
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

    if (data.newlyEarnedBadges?.length > 0) {
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
  display: flex; flex-direction: column; 
  height: 100vh; height: 100dvh; /* Mobile viewport fix */
  background-color: white; 
  overflow: hidden;
  position: relative;
}

.bg-pattern-overlay {
  position: absolute; top: 0; left: 0; right: 0; bottom: 0; pointer-events: none; z-index: 0;
}

/* Header */
.quiz-header {
  flex: 0 0 auto; padding: 1rem 2rem; display: flex; align-items: center; gap: 1rem;
  background-color: transparent; z-index: 20;
}
.close-btn { background: none; border: none; color: rgba(0,0,0,0.3); font-size: 1.5rem; cursor: pointer; padding: 0; min-width: auto; border-bottom: none; }
.close-btn:hover { color: rgba(0,0,0,0.6); }

/* Buttons in Header (Hint & Bookmark) */
.icon-btn {
  background: white; border: 2px solid; border-radius: 50%; width: 45px; height: 45px;
  display: flex; justify-content: center; align-items: center; cursor: pointer;
  transition: all 0.2s; border-bottom-width: 4px; padding: 0; min-width: auto;
  font-size: 1.2rem;
  box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}
.icon-btn:active:not(:disabled) { transform: translateY(2px); border-bottom-width: 2px; }
.icon-btn.active { background-color: #fffdf0; }

.hint-wrapper { position: relative; }
.bulb-on { filter: drop-shadow(0 0 5px currentColor); }
.hint-count {
  position: absolute; top: -5px; right: -5px; color: white;
  font-size: 0.75rem; width: 20px; height: 20px; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-weight: bold;
}
.hint-bubble-top {
  position: absolute; top: 130%; right: -10px; width: 260px; background: #3c3c3c; color: white;
  padding: 1rem; border-radius: 12px; font-size: 0.95rem; z-index: 30; text-align: right; box-shadow: 0 4px 15px rgba(0,0,0,0.2); line-height: 1.5;
}
.hint-bubble-top::after {
  content: ''; position: absolute; top: -6px; right: 25px; width: 12px; height: 12px; background: #3c3c3c; transform: rotate(45deg);
}

/* Progress Bar */
.progress-container { flex-grow: 1; height: 16px; background-color: rgba(0,0,0,0.1); border-radius: 10px; overflow: hidden; margin-left: 1rem; margin-right: 1rem; }
.progress-bar { height: 100%; border-radius: 10px; position: relative; transition: width 0.5s cubic-bezier(0.4, 0, 0.2, 1); }
.progress-highlight { position: absolute; top: 20%; left: 5%; right: 5%; height: 30%; background-color: rgba(255,255,255,0.3); border-radius: 10px; }

.quiz-stats { display: flex; align-items: center; gap: 0.5rem; color: #ff9600; font-weight: bold; font-size: 1.2rem; }

/* Main Body */
.quiz-body {
  flex: 1 1 auto; /* Fill space */
  overflow-y: auto; /* Scrollable */
  padding: 1rem 2rem;
  padding-bottom: 2rem; /* Normal padding */
  display: flex; justify-content: center; position: relative; scroll-behavior: smooth; z-index: 10;
}
.question-container { width: 100%; max-width: 800px; text-align: center; margin-top: 1rem; }
.question-title { font-size: 1.8rem; color: var(--color-text); margin-bottom: 2rem; text-align: right; font-weight: 800; }
.question-image-container {
  margin-bottom: 2rem;
  text-align: center;
}
.question-image-container img {
  max-width: 100%;
  max-height: 300px;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

/* Character Animation */
.character-popup { position: fixed; bottom: 160px; right: 20px; z-index: 90; display: flex; align-items: flex-end; gap: 10px; pointer-events: none; }
.character-img { width: 130px; height: auto; filter: drop-shadow(0 5px 15px rgba(0,0,0,0.15)); }
.speech-bubble { background: white; border: 2px solid #e5e5e5; padding: 1rem 1.5rem; border-radius: 20px 20px 0 20px; font-weight: 800; color: var(--color-danger); margin-bottom: 30px; animation: popIn 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); font-size: 1.1rem; }
.correct-bubble { color: var(--color-primary); border-color: var(--color-primary-light); background-color: #fafff5; }

/* Footer */
.quiz-footer {
  flex: 0 0 auto; /* Fixed height based on content */
  width: 100%; padding: 2rem; border-top: 2px solid rgba(0,0,0,0.05); background-color: white; 
  transition: background-color 0.2s, border-color 0.2s; z-index: 100; position: relative;
}
.footer-content { max-width: 1000px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; }

/* Feedback */
.feedback-message { display: flex; align-items: flex-start; gap: 1rem; animation: slideRight 0.3s ease-out; flex: 1; }
@keyframes slideRight { from { opacity: 0; transform: translateX(-20px); } to { opacity: 1; transform: translateX(0); } }

.feedback-icon-circle { width: 70px; height: 70px; border-radius: 50%; background-color: white; display: flex; justify-content: center; align-items: center; font-size: 2rem; flex-shrink: 0; }
.footer-correct .feedback-icon-circle { color: var(--color-primary); }
.footer-incorrect .feedback-icon-circle { color: var(--color-danger); }

.feedback-text { display: flex; flex-direction: column; align-items: flex-start; text-align: right; }
.feedback-text h3 { margin: 0; font-size: 1.6rem; font-weight: 900; margin-bottom: 0.5rem; }
.footer-correct .feedback-text h3 { color: var(--color-primary-dark); }
.footer-incorrect .feedback-text h3 { color: var(--color-danger-dark); }

.explanation-text { font-size: 1rem; color: #4b4b4b; margin: 0; line-height: 1.6; max-width: 650px; }

/* Actions */
.action-button-wrapper { margin-right: 2rem; }
.check-btn, .continue-btn { min-width: 180px; padding: 1rem 2rem; font-size: 1.2rem; width: auto; transition: filter 0.2s; box-shadow: 0 4px 0 rgba(0,0,0,0.1); }
.check-btn:hover { filter: brightness(1.1); }

/* Mobile Adjustments */
@media (max-width: 600px) {
  .footer-content { flex-direction: column; gap: 1.5rem; align-items: stretch; }
  .action-button-wrapper { width: 100%; margin: 0; }
  .check-btn, .continue-btn { width: 100%; }
  
  .feedback-message { margin-bottom: 0.5rem; flex-direction: row; align-items: center; }
  .feedback-text h3 { font-size: 1.4rem; }
  .feedback-text { width: 100%; }
  .explanation-text { font-size: 0.9rem; }
  
  .character-popup { bottom: 180px; right: 50%; transform: translateX(50%); }
  .character-img { width: 110px; }
  
  .quiz-header { padding: 0.8rem 1rem; gap: 0.8rem; }
  .icon-btn { width: 40px; height: 40px; }
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