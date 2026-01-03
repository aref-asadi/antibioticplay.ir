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
          :disabled="hintsRemaining <= 0"
          title="راهنمایی"
          :style="hintButtonStyle"
        >
          <font-awesome-icon icon="fas fa-lightbulb" />
          <span class="hint-count" :style="{ backgroundColor: themeColor }">{{ hintsRemaining }}</span>
        </button>
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

    <footer class="quiz-footer" v-if="quizState === 'answering'">
      <div class="footer-content">
        <button
          @click="checkAnswer"
          class="btn check-btn"
          :style="checkButtonStyle"
          :disabled="!isAnswerComplete"
        >
          بررسی
        </button>
      </div>
    </footer>

    <Transition name="fade">
      <div v-if="showHintModal" class="modal-overlay" @click.self="showHintModal = false">
        <div class="modal-card hint-card">
          <button class="modal-close-icon" @click="showHintModal = false">
            <font-awesome-icon icon="fas fa-times" />
          </button>
          
          <div class="modal-header">
            <font-awesome-icon icon="fas fa-lightbulb" class="modal-icon-hint" />
            <h3>راهنمایی</h3>
          </div>
          
          <div class="modal-body">
            <div v-if="isImageHint" class="hint-image-wrapper">
              <img :src="currentQuestion.hint" alt="Hint Image" class="hint-img-content" />
            </div>
            
            <p v-else>
              {{ currentQuestion?.hint || 'راهنمایی برای این سوال موجود نیست.' }}
            </p>
          </div>
        </div>
      </div>
    </Transition>

    <Transition name="pop-up">
      <div v-if="quizState !== 'answering'" class="modal-overlay">
        <div class="modal-card feedback-card" :class="quizState === 'correct' ? 'card-correct' : 'card-incorrect'">
          
          <div class="feedback-image-wrapper">
             <img 
              :src="quizState === 'correct' ? correctImg : incorrectImg" 
              class="feedback-character-img" 
              alt="Character"
            />
          </div>

          <div class="feedback-content">
            <h2 class="feedback-title">
              {{ quizState === 'correct' ? 'عالی بود!' : 'اشتباه بود!' }}
            </h2>
            
            <div class="feedback-text-scroll">
               <p v-if="explanationText" class="explanation-text">{{ explanationText }}</p>
            </div>
          </div>

          <div class="feedback-actions">
            <button
              @click="handleContinue"
              class="btn continue-btn"
              :class="quizState === 'correct' ? 'btn-primary' : 'btn-danger'"
            >
              ادامه
            </button>
          </div>

        </div>
      </div>
    </Transition>

    <Confetti v-if="quizState === 'correct'" />

  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue';
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
const showHintModal = ref(false);
const isImageHint = computed(() => {
  const hint = currentQuestion.value?.hint;
  if (!hint) return false;
  const imageExtensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'];
  return imageExtensions.some(ext => hint.toLowerCase().endsWith(ext));
});

// --- Theme & Style Logic ---
const themeColor = computed(() => route.query.theme || '#58cc02');

const layoutStyles = computed(() => {
  const svgPattern = `data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%239C92AC' fill-opacity='0.08'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E`;
  return {
    backgroundColor: `${themeColor.value}1a`,
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
    if (type === 'image-labeling') {
        if (!answer || typeof answer !== 'object') return false;
        const placedItemsCount = Object.values(answer).reduce((count, items) => count + (Array.isArray(items) ? items.length : 0), 0);
        const totalOptions = currentQuestion.value.options ? currentQuestion.value.options.length : 0;
        return totalOptions > 0 ? placedItemsCount === totalOptions : placedItemsCount > 0;
    }
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
  showHintModal.value = false;
  userAnswer.value = null;
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
  if (hintsRemaining.value > 0) {
    hintsRemaining.value--;
    showHintModal.value = true;
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
  height: 100vh; height: 100dvh; 
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
.hint-count {
  position: absolute; top: -5px; right: -5px; color: white;
  font-size: 0.75rem; width: 20px; height: 20px; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-weight: bold;
}

.hint-image-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  margin-top: 0.5rem;
}

.hint-img-content {
  max-width: 100%;
  max-height: 300px; /* محدودیت ارتفاع برای جلوگیری از اسکرول زیاد */
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  object-fit: contain;
}

/* Progress Bar */
.progress-container { flex-grow: 1; height: 16px; background-color: rgba(0,0,0,0.1); border-radius: 10px; overflow: hidden; margin-left: 1rem; margin-right: 1rem; }
.progress-bar { height: 100%; border-radius: 10px; position: relative; transition: width 0.5s cubic-bezier(0.4, 0, 0.2, 1); }
.progress-highlight { position: absolute; top: 20%; left: 5%; right: 5%; height: 30%; background-color: rgba(255,255,255,0.3); border-radius: 10px; }
.quiz-stats { display: flex; align-items: center; gap: 0.5rem; color: #ff9600; font-weight: bold; font-size: 1.2rem; }

/* Main Body */
.quiz-body {
  flex: 1 1 auto; 
  overflow-y: auto; 
  padding: 1rem 2rem;
  padding-bottom: 2rem; 
  display: flex; justify-content: center; position: relative; scroll-behavior: smooth; z-index: 10;
}
.question-container { width: 100%; max-width: 800px; text-align: center; margin-top: 1rem; }
.question-title { font-size: 1.8rem; color: var(--color-text); margin-bottom: 2rem; text-align: right; font-weight: 800; }
.question-image-container { margin-bottom: 2rem; text-align: center; }
.question-image-container img { max-width: 100%; max-height: 300px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }

/* Footer */
.quiz-footer {
  flex: 0 0 auto; 
  width: 100%; padding: 1.5rem 2rem; border-top: 2px solid rgba(0,0,0,0.05); background-color: white; 
  z-index: 100;
}
.footer-content { max-width: 1000px; margin: 0 auto; display: flex; justify-content: flex-end; }
.check-btn { min-width: 180px; padding: 1rem 2rem; font-size: 1.2rem; width: auto; transition: filter 0.2s; box-shadow: 0 4px 0 rgba(0,0,0,0.1); border-radius: 16px; color: white; border: none; cursor: pointer; border-bottom: 4px solid rgba(0,0,0,0.2); }
.check-btn:disabled { background-color: #e5e5e5 !important; border-bottom-color: #d4d4d4 !important; color: #afafaf !important; cursor: not-allowed; box-shadow: none; }
.check-btn:hover:not(:disabled) { filter: brightness(1.1); }
.check-btn:active:not(:disabled) { transform: translateY(2px); border-bottom-width: 2px; }

/* --- MODAL STYLES --- */
.modal-overlay {
  position: fixed; top: 0; left: 0; right: 0; bottom: 0;
  background-color: rgba(0, 0, 0, 0.6);
  z-index: 1000;
  display: flex; justify-content: center; align-items: center;
  padding: 1rem;
  backdrop-filter: blur(4px);
}

.modal-card {
  background: white;
  border-radius: 20px;
  width: 100%;
  max-width: 450px;
  position: relative;
  display: flex;
  flex-direction: column;
  box-shadow: 0 10px 25px rgba(0,0,0,0.2);
  animation: popIn 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.modal-close-icon {
  position: absolute; top: 10px; left: 10px;
  background: #f0f0f0; border: none; width: 32px; height: 32px; border-radius: 50%;
  cursor: pointer; color: #666; display: flex; justify-content: center; align-items: center;
  font-size: 1rem; transition: background 0.2s; z-index: 10;
  min-width: auto !important;
}
.modal-close-icon:hover { background: #e0e0e0; }

/* Hint Modal */
.hint-card { padding: 2rem; text-align: center; border-bottom: 4px solid #e5e5e5; }
.modal-header { margin-bottom: 1rem; color: #fbc02d; display: flex; flex-direction: column; align-items: center; gap: 0.5rem; }
.modal-icon-hint { font-size: 3rem; }
.modal-header h3 { font-size: 1.5rem; font-weight: 800; color: #333; margin: 0; }
.modal-body {
  font-size: 1.1rem;
  line-height: 1.6;
  color: #555;
  
  /* --- اضافه شده برای حل مشکل اسکرول --- */
  max-height: 50vh;       /* حداکثر ارتفاع: 50 درصد ارتفاع صفحه */
  overflow-y: auto;       /* اگر متن بیشتر بود، اسکرول عمودی فعال شود */
  padding: 0 0.5rem;      /* کمی فاصله از بغل برای زیبایی اسکرول‌بار */
  width: 100%;            /* اطمینان از عرض کامل */
  
  /* استایل برای اسکرول‌بار (اختیاری ولی زیباتر) */
  scrollbar-width: thin;
  scrollbar-color: #ccc transparent;
}

/* استایل اسکرول‌بار برای کروم و سافاری */
.modal-body::-webkit-scrollbar {
  width: 6px;
}
.modal-body::-webkit-scrollbar-track {
  background: transparent;
}
.modal-body::-webkit-scrollbar-thumb {
  background-color: #ccc;
  border-radius: 20px;
}

/* Feedback Modal */
.feedback-card { overflow: hidden; padding-bottom: 1.5rem; text-align: center; }
.card-correct { border: 2px solid #84d8ff; background: #f0faff; }
.card-incorrect { border: 2px solid #ffb8b8; background: #fff5f5; }

.feedback-image-wrapper { width: 100%; height: 180px; overflow: hidden; background: white; display: flex; justify-content: center; align-items: flex-end; }
.feedback-character-img { width: 140px; height: auto; }

.feedback-content { padding: 1rem 1.5rem; }
.feedback-title { font-size: 2rem; margin: 0.5rem 0; font-weight: 900; }
.card-correct .feedback-title { color: #1cb0f6; }
.card-incorrect .feedback-title { color: #ea2b2b; }

.feedback-text-scroll { max-height: 150px; overflow-y: auto; margin-bottom: 1.5rem; padding: 0 0.5rem; }
.explanation-text { font-size: 1rem; color: #555; line-height: 1.6; margin: 0; }

.feedback-actions { padding: 0 1.5rem; }
.continue-btn { width: 100%; padding: 0.8rem; border-radius: 12px; font-weight: 700; font-size: 1.1rem; cursor: pointer; border: none; border-bottom: 4px solid transparent; color: white; transition: all 0.2s; }
.continue-btn:active { transform: translateY(2px); border-bottom-width: 2px; }
.btn-primary { background-color: #1cb0f6; border-bottom-color: #1899d6; }
.btn-primary:hover { background-color: #1899d6; }
.btn-danger { background-color: #ff4b4b; border-bottom-color: #d40000; }
.btn-danger:hover { background-color: #d40000; }

/* Transitions */
.fade-enter-active, .fade-leave-active { transition: opacity 0.2s; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
.pop-up-enter-active { animation: popIn 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
.pop-up-leave-active { transition: opacity 0.2s; }
.pop-up-leave-to { opacity: 0; }
@keyframes popIn { from { opacity: 0; transform: scale(0.8); } to { opacity: 1; transform: scale(1); } }
.shake-animation { animation: shake 0.5s ease-in-out; }
@keyframes shake { 0%, 100% { transform: translateX(0); } 25% { transform: translateX(-5px); } 75% { transform: translateX(5px); } }

/* Mobile Adjustments */
@media (max-width: 600px) {
  .quiz-header { padding: 0.8rem 1rem; gap: 0.8rem; }
  .icon-btn { width: 40px; height: 40px; }
  .check-btn { width: 100%; }
}
</style>