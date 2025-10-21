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
      
      <div v-if="currentQuestion" class="question-area">
        
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

    <div v-if="quizState === 'correct'" class="feedback-banner correct">
      <h2>✅ آفرین!</h2>
    </div>
    <div v-else-if="quizState === 'incorrect'" class="feedback-banner incorrect">
      <h2>❌ جواب درست نبود.</h2>
    </div>

  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useQuizStore } from '../stores/quiz';
import { useAuthStore } from '../stores/auth';

// --- ایمپورت‌های کامپوننت ---
import DragDropMatch from '../components/DragDropMatch.vue'; 
import MultipleSelect from '../components/MultipleSelect.vue';
import TrueFalse from '../components/TrueFalse.vue';
import DragDropFill from '../components/DragDropFill.vue';

// نمونه‌سازی از storeها و روتر
const quizStore = useQuizStore();
const authStore = useAuthStore();
const router = useRouter();

// --- State های محلی ---
const currentQuestionIndex = ref(0); // شماره سوال فعلی
const userAnswer = ref(null); // جوابی که کاربر انتخاب کرده (از کامپوننت فرزند میاد)
const feedback = ref({}); // بازخوردی که از سرور میاد
const quizState = ref('answering'); // 'answering', 'correct', 'incorrect', 'loading'

// --- Computed Properties ---

// آبجکت سوال فعلی را بر اساس ایندکس برمی‌گرداند
const currentQuestion = computed(() => {
  if (quizStore.currentQuiz && quizStore.currentQuiz.questions) {
    return quizStore.currentQuiz.questions[currentQuestionIndex.value];
  }
  return null;
});

// دکمه "بررسی" را فقط زمانی فعال می‌کند که جوابی وارد شده باشد
const isAnswerComplete = computed(() => {
    if (!currentQuestion.value || userAnswer.value === null) return false;
    
    const type = currentQuestion.value.type;
    const answer = userAnswer.value;

    if (type === 'drag-drop-match' || type === 'drag-drop-ordering') {
        // برای درگ/دراپ، بانک باید خالی باشد
        return answer.bank && answer.bank.length === 0;
    }
    
    if (type === 'multiple-select') {
        // برای چندانتخابی، حداقل یک گزینه باید انتخاب شده باشد
        return Array.isArray(answer) && answer.length > 0;
    }

    if (type === 'true-false') {
        // چک می‌کند که آیا تعداد جواب‌های کاربر با تعداد گزاره‌های سوال برابر است
        const statementCount = currentQuestion.value.statements.length;
        const answerCount = Object.keys(answer).length;
        return statementCount === answerCount;
    }

    if (type === 'drag-drop-fill') {
        // چک می‌کند که آیا تعداد جواب‌های کاربر با تعداد جاهای خالی برابر است
        const blankCount = currentQuestion.value.blanks.length;
        // آرایه‌ای از جواب‌های غیر خالی (non-empty) می‌سازد
        const answerCount = Object.values(answer).filter(Boolean).length; 
        return blankCount === answerCount;
    }
    
    // اگر نوع سوالی را نمی‌شناسیم، فعلا دکمه را فعال کن
    return true;
});

// --- Methods ---

// تابع اصلی بررسی جواب
const checkAnswer = async () => {
  if (!currentQuestion.value) return;

  quizState.value = 'loading';
  
  try {
    const response = await quizStore.submitAnswer(
      quizStore.currentQuiz.id,
      currentQuestion.value.id,
      userAnswer.value
    );

    const data = response.data;
    feedback.value = data.feedback;
    quizState.value = data.isCorrect ? 'correct' : 'incorrect';
    
    // آپدیت امتیاز کل کاربر
    authStore.updateUserScore(data.newTotalScore);

    authStore.updateUserLevel(data.newLevel);
    
    // --- *** خط جدید *** ---
    // اضافه کردن امتیاز کسب شده از این سوال به حافظه موقت آزمون
    quizStore.addSessionScore(data.scoreEarned);
    
  } catch (err) {
    console.error("Error checking answer:", err);
    quizState.value = 'answering';
  }
};

// تابع برای رفتن به سوال بعدی یا اتمام آزمون
const handleContinue = () => {
  // چک می‌کنیم آیا سوال دیگری باقی مانده است
  if (currentQuestionIndex.value < quizStore.currentQuiz.questions.length - 1) {
    // رفتن به سوال بعدی
    currentQuestionIndex.value++;
    
    // ریست کردن state ها برای سوال بعدی
    quizState.value = 'answering';
    feedback.value = {};
    userAnswer.value = null;
  } else {
    // --- *** بخش آپدیت شده *** ---
    // آزمون تمام شده است
    // به جای alert، کاربر را به صفحه نتایج هدایت می‌کنیم
    router.push({ name: 'QuizResult' });
  }
};
</script>

<style scoped>
.quiz-container {
  max-width: 800px;
  margin: 20px auto;
  padding: 2rem;
  /* ایجاد فضا در پایین صفحه برای دکمه‌ها و بنرها */
  padding-bottom: 200px; 
}

.loading-message, .error-message {
  font-size: 1.2rem;
  color: #777;
  text-align: center;
}
.error-message {
  color: #e74c3c;
}

.quiz-content {
  text-align: center;
}

hr {
  margin: 1.5rem 0;
  border: none;
  border-top: 1px solid #eee;
}

/* --- Footer --- */
.quiz-footer {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 1rem 2rem;
  background-color: #fff;
  border-top: 2px solid #e5e5e5;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 90px; /* ارتفاع ثابت */
  z-index: 10;
}

.check-button, .continue-button {
  border: none;
  padding: 1rem 2.5rem;
  font-size: 1.2rem;
  font-weight: bold;
  color: white;
  border-radius: 12px;
  cursor: pointer;
  width: 200px;
  transition: background-color 0.2s;
}

/* دکمه بررسی */
.check-button {
  background-color: #58a700; /* Duolingo Green */
}
.check-button:disabled {
  background-color: #e5e5e5;
  color: #afafaf;
  cursor: not-allowed;
}

/* دکمه ادامه (بر اساس وضعیت) */
.continue-button.correct {
  background-color: #58a700;
}
.continue-button.incorrect {
  background-color: #ff4b4b; /* Duolingo Red */
}

/* --- Feedback Banners --- */
.feedback-banner {
  position: fixed;
  bottom: 90px; /* دقیقا بالای فوتر */
  left: 0;
  right: 0;
  padding: 1.5rem;
  color: white;
  text-align: center;
  z-index: 9;
}
.feedback-banner h2 {
  margin: 0;
  font-size: 1.3rem;
  font-weight: bold;
}

.feedback-banner.correct {
  background-color: #d7ffb8; /* Light Green */
  color: #58a700; /* Dark Green */
}
.feedback-banner.incorrect {
  background-color: #ffdfe0; /* Light Red */
  color: #ff4b4b; /* Dark Red */
}
</style>