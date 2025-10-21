<template>
  <div class="dashboard-container">
    
    <header class="dashboard-header">
      <h1 v-if="authStore.user">
        خوش آمدید، {{ authStore.user.username }}!
      </h1>
      <button @click="handleLogout" class="logout-button">خروج</button>
    </header>

    <main class="dashboard-content">

      <div class="stats-and-leaderboard">
        <div class="stats">
            <div class="stat-card">
                <h3>امتیاز</h3>
                <p>{{ authStore.user.score || 0 }}</p>
            </div>
            <div class="stat-card">
                <h3>سطح</h3>
                <p>{{ authStore.user.level || 1 }}</p>
            </div>
        </div>

        <router-link to="/leaderboard" class="leaderboard-link">
          <span>🏆</span>
          مشاهده جدول امتیازات
        </router-link>
      </div>
      <hr class="divider">
      
      <div class="quiz-selection">
        <h2>یک آزمون را انتخاب کنید</h2>
        
        <div v-if="quizStore.loading" class="loading-message">
          در حال بارگذاری آزمون‌ها...
        </div>
        <div v-if="quizStore.error" class="error-message">
          {{ quizStore.error }}
        </div>
        
        <div v-if="!quizStore.loading && quizStore.modules.length > 0" class="modules-grid">
          <div 
            v-for="module in quizStore.modules" 
            :key="module.id" 
            class="module-card"
          >
            <h3>{{ module.title }}</h3>
            <button @click="startQuiz(module.id)">شروع آزمون</button>
          </div>
        </div>
      </div>

    </main>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';
import { useQuizStore } from '../stores/quiz';

// نمونه‌سازی از storeها و روتر
const authStore = useAuthStore();
const quizStore = useQuizStore();
const router = useRouter();

// دریافت لیست ماژول‌های آزمون به محض باز شدن صفحه
onMounted(() => {
  quizStore.fetchModules();
});

// تابع برای خروج از سیستم
const handleLogout = () => {
  authStore.logout();
};

// تابع برای شروع آزمون
const startQuiz = async (quizId) => {
  // ۱. دریافت سوالات آزمون از سرور
  await quizStore.fetchQuizDetails(quizId);
  
  // ۲. اگر خطایی وجود نداشت، کاربر را به صفحه آزمون هدایت کن
  if (!quizStore.error) {
    router.push({ name: 'Quiz', params: { id: quizId } });
  }
};
</script>

<style scoped>
.dashboard-container {
  max-width: 900px;
  margin: 20px auto;
  padding: 2rem;
  text-align: center;
}

.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #eee;
}

.logout-button {
  padding: 0.5rem 1rem;
  background-color: #e74c3c; /* Red */
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.9rem;
}
.logout-button:hover {
    background-color: #c0392b;
}

.stats {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-top: 1rem;
}

.stat-card {
    padding: 1rem 2rem;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    min-width: 120px;
}

.divider {
  margin: 2.5rem 0;
  border: none;
  border-top: 1px solid #eee;
}

.quiz-selection h2 {
  margin-bottom: 1.5rem;
}

.modules-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.module-card {
  padding: 1.5rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  transition: transform 0.2s, box-shadow 0.2s;
  background-color: #fff;
}
.module-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.module-card h3 {
  margin-top: 0;
  margin-bottom: 1.5rem;
  color: #333;
}

.module-card button {
  padding: 0.6rem 1.2rem;
  background-color: #42b983; /* Green */
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: bold;
}
.module-card button:hover {
  background-color: #369d6e;
}

.loading-message {
  font-size: 1.2rem;
  color: #777;
}

.error-message {
  font-size: 1.2rem;
  color: #e74c3c;
}
</style>