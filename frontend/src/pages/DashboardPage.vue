<template>
  <div class="dashboard-container">
    <header class="dashboard-header">
      <h1 v-if="authStore.user">خوش آمدید، {{ authStore.user.username }}!</h1>
      <button @click="handleLogout" class="logout-button">خروج</button>
    </header>

    <main class="dashboard-content">
      <div v-if="authStore.user" class="stats">
          </div>

      <hr class="divider">

      <div class="quiz-selection">
        <h2>یک آزمون را انتخاب کنید</h2>
        <div v-if="quizStore.loading" class="loading-message">در حال بارگذاری آزمون‌ها...</div>
        <div v-if="quizStore.error" class="error-message">{{ quizStore.error }}</div>
        <div v-if="!quizStore.loading && quizStore.modules.length > 0" class="modules-grid">
          <div v-for="module in quizStore.modules" :key="module.id" class="module-card">
            <h3>{{ module.title }}</h3>
            <button @click="startQuiz(module.id)">شروع آزمون</button>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
// File: frontend/src/pages/DashboardPage.vue -> <script setup>

import { onMounted } from 'vue';
import { useRouter } from 'vue-router'; // <-- ایمپورت useRouter
import { useAuthStore } from '../stores/auth';
import { useQuizStore } from '../stores/quiz';

const authStore = useAuthStore();
const quizStore = useQuizStore();
const router = useRouter(); // <-- استفاده از روتر

onMounted(() => {
  quizStore.fetchModules();
});

const handleLogout = () => {
  authStore.logout();
};

// --- تابع آپدیت شده ---
const startQuiz = async (quizId) => {
  // ابتدا سوالات آزمون را دریافت می‌کنیم
  await quizStore.fetchQuizDetails(quizId);

  // اگر دریافت موفقیت‌آمیز بود، به صفحه آزمون می‌رویم
  if (!quizStore.error) {
    router.push({ name: 'Quiz', params: { id: quizId } });
  }
};
</script>

<style scoped>
.dashboard-container {
  max-width: 800px;
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
  background-color: #e74c3c; /* Red color for logout */
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
    margin-top: 2rem;
}

.stat-card {
    padding: 1rem 2rem;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.divider {
  margin: 2rem 0;
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
}
.module-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.module-card h3 {
  margin-bottom: 1rem;
}
.module-card button {
  padding: 0.6rem 1.2rem;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>