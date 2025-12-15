<template>
  <div class="result-page">
    
    <div class="result-header">
      <h1 class="completion-title">درس تمام شد!</h1>
      <div class="result-image-wrapper">
        <img :src="resultImage" class="result-img" alt="Result" />
      </div>
    </div>

    <div class="stats-grid">
      
      <div class="stat-card xp-card">
        <div class="stat-label">XP دریافتی</div>
        <div class="stat-value text-warning">
          <font-awesome-icon icon="fas fa-plus" class="small-icon" />
          {{ xpGainedDisplay }}
        </div>
      </div>

      <div class="stat-card streak-card">
        <div class="stat-label">پاسخ صحیح متوالی</div>
        <div class="stat-value text-fire">
          <font-awesome-icon icon="fas fa-fire" />
          {{ authStore.user?.correct_streak || 0 }}
        </div>
      </div>

      <div class="stat-card feedback-card">
        <div class="stat-label">عملکرد</div>
        <div class="stat-value text-primary">
          {{ performanceLabel }}
        </div>
      </div>

    </div>

    <div v-if="didLevelUp" class="level-up-banner slide-up-animation">
      <div class="level-content">
        <font-awesome-icon icon="fas fa-arrow-up" class="level-icon" />
        <div>
          <h3>ارتقای سطح!</h3>
          <p>تبریک! شما به سطح {{ authStore.level }} رسیدید.</p>
        </div>
      </div>
    </div>

    <footer class="result-footer">
      <router-link to="/dashboard" class="btn btn-primary continue-btn">
        ادامه
      </router-link>
    </footer>

  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue';
import { useQuizStore } from '../stores/quiz';
import { useAuthStore } from '../stores/auth';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faFire, faPlus, faArrowUp } from '@fortawesome/free-solid-svg-icons';

// Import images
import resultGoodImg from '../assets/result_good.jpg';
import resultBadImg from '../assets/result_bad.jpg';

library.add(faFire, faPlus, faArrowUp);

const quizStore = useQuizStore();
const authStore = useAuthStore();

const xpGainedDisplay = computed(() => {
  // این مقدار را باید از آخرین پاسخ سرور بگیریم
  // اگر مقدار وجود نداشت (مثلا رفرش صفحه)، صفر نشان بده
  return quizStore.lastSubmissionResult?.xpGained || 0;
});

// تعیین تصویر و متن بر اساس عملکرد
const performanceLabel = computed(() => {
  const score = quizStore.currentSessionScore;
  const possible = quizStore.currentQuiz?.total_possible_score || 10;
  const percentage = (score / possible) * 100;

  if (percentage >= 80) return 'عالی!';
  if (percentage >= 50) return 'خوب';
  return 'تلاش بیشتر';
});

const resultImage = computed(() => {
  const score = quizStore.currentSessionScore;
  const possible = quizStore.currentQuiz?.total_possible_score || 10;
  // اگر بیش از نصف نمره را گرفته باشد، تصویر خوشحال
  return (score >= possible / 2) ? resultGoodImg : resultBadImg;
});

const didLevelUp = computed(() => {
  return quizStore.lastSubmissionResult && quizStore.lastSubmissionResult.levelUp;
});

// حذف لاجیک نوتیفیکیشن پاپ‌آپ از اینجا
</script>

<style scoped>
.result-page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: white;
  padding: 2rem;
  text-align: center;
}

/* --- Header --- */
.result-header {
  margin-top: 2rem;
  margin-bottom: 3rem;
}
.completion-title {
  color: var(--color-warning); /* Gold/Yellow color */
  font-size: 2.5rem;
  font-weight: 900;
  margin-bottom: 1rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}
.result-image-wrapper {
  width: 200px;
  height: 200px;
  margin: 0 auto;
}
.result-img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  /* Add a subtle float animation */
  animation: float 3s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

/* --- Stats Grid --- */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  width: 100%;
  max-width: 600px;
  margin-bottom: 2rem;
}

.stat-card {
  background-color: #fff;
  border: 2px solid var(--color-border);
  border-radius: 16px;
  padding: 1rem 0.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 0 var(--color-border); /* 3D effect */
}

.stat-label {
  font-size: 0.9rem;
  color: var(--color-text-light);
  margin-bottom: 0.5rem;
  font-weight: 700;
}

.stat-value {
  font-size: 1.5rem;
  font-weight: 900;
  display: flex;
  align-items: center;
  gap: 0.3rem;
}

/* Colors */
.text-warning { color: var(--color-warning); }
.text-fire { color: #ff9600; }
.text-primary { color: var(--color-primary); }
.small-icon { font-size: 1rem; }

/* --- Level Up Banner --- */
.level-up-banner {
  background-color: #d7ffb8;
  border: 2px solid var(--color-primary);
  border-radius: 16px;
  padding: 1rem 2rem;
  margin-bottom: 2rem;
  width: 100%;
  max-width: 600px;
  box-sizing: border-box;
}
.level-content {
  display: flex;
  align-items: center;
  gap: 1rem;
  text-align: right;
}
.level-icon {
  font-size: 2rem;
  color: var(--color-primary);
  background: white;
  padding: 10px;
  border-radius: 50%;
}
.level-content h3 { margin: 0 0 0.2rem 0; color: var(--color-primary-dark); }
.level-content p { margin: 0; color: var(--color-text); font-size: 0.95rem; }

/* --- Footer --- */
.result-footer {
  margin-top: auto; /* Push to bottom */
  width: 100%;
  max-width: 600px;
  padding-bottom: 2rem;
}
.continue-btn {
  width: 100%;
  padding: 1rem;
  font-size: 1.2rem;
}

/* --- Animations --- */
.slide-up-animation {
  animation: slideUp 0.5s ease-out;
}
@keyframes slideUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Mobile Responsive */
@media (max-width: 600px) {
  .stats-grid {
    grid-template-columns: 1fr; /* Stack cards on mobile */
  }
  .stat-card {
    flex-direction: row;
    justify-content: space-between;
    padding: 1rem 2rem;
  }
  .stat-label { margin-bottom: 0; }
}
</style>