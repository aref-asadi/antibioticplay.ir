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
          class="check-button"
          :disabled="!isAnswerComplete"
        >
          بررسی
        </button>

        <button
          v-if="quizState === 'correct' || quizState === 'incorrect'"
          @click="handleContinue"
          class="continue-button"
          :class="quizState"
        >
          ادامه
        </button>
      </footer>
    </div>

    <div v-if="quizState === 'correct'" class="feedback-banner correct slide-up-fade-in">
      <h2>✅ آفرین!</h2>
    </div>
    <div v-else-if="quizState === 'incorrect'" class="feedback-banner incorrect slide-up-fade-in">
      <h2>❌ جواب درست نبود.</h2>
    </div>

  </div>
</template>

<script setup>
import { ref, computed, nextTick } from 'vue';
import { useRouter } from 'vue-router';
import { useQuizStore } from '../stores/quiz';
import { useAuthStore } from '../stores/auth';

// --- Component Imports ---
import DragDropMatch from '../components/DragDropMatch.vue';
import MultipleSelect from '../components/MultipleSelect.vue';
import TrueFalse from '../components/TrueFalse.vue';
import DragDropFill from '../components/DragDropFill.vue';

// --- Store and Router Instances ---
const quizStore = useQuizStore();
const authStore = useAuthStore();
const router = useRouter();

// --- Local State ---
const currentQuestionIndex = ref(0); // Index of the current question
const userAnswer = ref(null); // User's answer for the current question
const feedback = ref({}); // Feedback received from the backend
const quizState = ref('answering'); // 'answering', 'correct', 'incorrect', 'loading'
const currentStreak = ref(0); // Current correct answer streak
const applyShake = ref(false);

// --- Computed Properties ---

// Gets the current question object based on the index
const currentQuestion = computed(() => {
  if (quizStore.currentQuiz && quizStore.currentQuiz.questions) {
    return quizStore.currentQuiz.questions[currentQuestionIndex.value];
  }
  return null;
});

// Determines if the "Check" button should be enabled based on question type and answer
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
    // Default for unknown types
    return true;
});

// Calculates the progress percentage for the progress bar
const progressPercentage = computed(() => {
  if (!quizStore.currentQuiz || !quizStore.currentQuiz.questions) return 0;
  const totalQuestions = quizStore.currentQuiz.questions.length;
  // Add 1 because index is 0-based
  return ((currentQuestionIndex.value + 1) / totalQuestions) * 100;
});


// --- Methods ---

// Helper function to play sound effects
const playSound = (soundFile) => {
  try {
    const audio = new Audio(`/${soundFile}`); // Assumes files are in /public
    audio.play();
  } catch (error) {
    console.error("Error playing sound:", error);
  }
};

// Submits the answer to the backend and handles the response
const checkAnswer = async () => {
  if (!currentQuestion.value) return;

  quizState.value = 'loading'; // Show loading state briefly

  const isLast = currentQuestionIndex.value >= quizStore.currentQuiz.questions.length - 1;

  try {
    const response = await quizStore.submitAnswer(
      quizStore.currentQuiz.id,
      currentQuestion.value.id,
      userAnswer.value,
      isLast // Send if it's the last question
    );

    const data = response.data;

    // Update local state based on response
    feedback.value = data.feedback;
    quizState.value = data.isCorrect ? 'correct' : 'incorrect';

    authStore.updateUserScore(data.newTotalScore);

    // Update global user state (score and level)
    authStore.updateUserLevel(data.newLevel); // آپدیت سطح
    quizStore.addSessionScore(data.scoreEarned);

    // Update local streak count
    currentStreak.value = data.isCorrect ? (currentStreak.value + 1) : 0;

    // Add score earned in this question to the session total
    quizStore.addSessionScore(data.scoreEarned);

    // Store any newly earned badges from this submission
    if (data.newlyEarnedBadges && data.newlyEarnedBadges.length > 0) {
      quizStore.setNewlyEarnedBadges(data.newlyEarnedBadges);
    }

    // Play the appropriate sound effect
    if (data.isCorrect) {
      playSound('correct.mp3');
    } else {
      playSound('incorrect.mp3');
      // --- *** Apply Shake Animation *** ---
      applyShake.value = true;
      // Reset after animation finishes (500ms duration)
      setTimeout(() => {
        applyShake.value = false;
      }, 500);
      // --- *** End Shake Animation *** ---
    }

  } catch (err) {
    console.error("Error checking answer:", err);
    quizState.value = 'answering'; // Revert state on error
  }
};

// Moves to the next question or finishes the quiz
const handleContinue = () => {
  // Check if there are more questions
  if (currentQuestionIndex.value < quizStore.currentQuiz.questions.length - 1) {
    // Move to the next question
    currentQuestionIndex.value++;

    // Reset state for the new question
    quizState.value = 'answering';
    feedback.value = {};
    userAnswer.value = null;
    // Ensure shake is reset if user continues quickly
    applyShake.value = false;
    // Streak is updated in checkAnswer, no need to reset here explicitly unless starting fresh
  } else {
    // Quiz finished, reset streak and navigate to results
    currentStreak.value = 0;
    router.push({ name: 'QuizResult' });
  }
};
</script>

<style scoped>
.quiz-container {
  max-width: 800px;
  margin: 20px auto;
  padding: 2rem;
  padding-bottom: 200px; /* Space for footer and banners */
}

.loading-message, .error-message {
  font-size: 1.2rem;
  color: var(--color-text-light); /* Use global variable */
  text-align: center;
  padding: 2rem;
}
.error-message {
  color: var(--color-danger); /* Use global variable */
}

.quiz-content {
  text-align: center;
}

hr {
  margin: 1.5rem 0;
  border: none;
  border-top: 1px solid var(--color-border); /* Use global variable */
}

/* --- Progress Section Styles --- */
.progress-section {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 2rem;
}

.progress-bar-container {
  flex-grow: 1;
  height: 15px;
  background-color: var(--color-border); /* Use global variable */
  border-radius: 10px;
  overflow: hidden;
}

.progress-bar-fill {
  height: 100%;
  background-color: var(--color-primary); /* Use global variable */
  border-radius: 10px;
  transition: width 0.3s ease-out;
}

.streak-display {
  font-size: 1.5rem;
  font-weight: bold;
  color: var(--color-warning); /* Use global variable */
  min-width: 50px;
  text-align: right;
}
/* --- End Progress Section Styles --- */

.question-area {
  margin-bottom: 2rem;
}

/* --- Footer --- */
.quiz-footer {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 1rem 2rem;
  background-color: var(--color-background-light); /* Use global variable */
  border-top: 2px solid var(--color-border); /* Use global variable */
  display: flex;
  justify-content: center;
  align-items: center;
  height: 90px;
  z-index: 10;
}

/* Remove button base styles - they come from style.css now */
/* Add button classes directly in template: btn-primary, btn-danger */

/* --- Feedback Banners --- */
.feedback-banner {
  position: fixed;
  bottom: 90px; /* Position above footer */
  left: 0;
  right: 0;
  padding: 1.5rem;
  text-align: center;
  z-index: 9;
}
.feedback-banner h2 {
  margin: 0;
  font-size: 1.3rem;
  font-weight: bold;
}

.feedback-banner.correct {
  background-color: #d7ffb8; /* Keep specific light background */
  color: var(--color-primary-dark); /* Use global variable */
}
.feedback-banner.incorrect {
  background-color: #ffdfe0; /* Keep specific light background */
  color: var(--color-danger-dark); /* Use global variable */
}

/* Animation class refers to global style.css */
/* .slide-up-fade-in { ... } */
/* .shake-animation { ... } */

</style>