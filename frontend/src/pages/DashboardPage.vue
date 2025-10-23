<template>
  <div class="dashboard-container">

    <header class="dashboard-header">
      <h1 v-if="user">
        خوش آمدید، {{ user.username }}!
      </h1>
      <button @click="handleLogout" class="logout-button">خروج</button>
    </header>

    <main class="dashboard-content">

      <div class="stats-and-leaderboard">
        <div class="stats">
            <div class="stat-card">
                <h3>امتیاز</h3>
                <p>
                  <span :class="{ 'score-pop-animation': scoreJustUpdated }">
                    {{ score || 0 }}
                  </span>
                </p>
            </div>
            <div class="stat-card">
                <h3>سطح</h3>
                <p>{{ level || 1 }}</p>
            </div>
        </div>

        <router-link to="/leaderboard" class="leaderboard-link">
          <span>🏆</span>
          مشاهده جدول امتیازات
        </router-link>
      </div>

      <div v-if="earnedBadges.length > 0" class="badges-section">
        <h2>🏆 نشان‌های شما 🏆</h2>
        <div v-if="loadingBadges" class="loading-message">در حال بارگذاری نشان‌ها...</div>
        <div v-else class="badges-grid">
          <BadgeDisplay
            v-for="badge in earnedBadges"
            :key="badge.id"
            :badge="badge"
          />
        </div>
      </div>

      <hr class="divider">

      <div class="quiz-selection">
        <h2>یک آزمون را انتخاب کنید</h2>
        <div v-if="quizStore.loading && !quizStore.modules.length" class="loading-message">در حال بارگذاری آزمون‌ها...</div>
        <div v-if="quizStore.error" class="error-message">{{ quizStore.error }}</div>
        <div v-if="!quizStore.loading && quizStore.modules.length > 0" class="modules-grid">
          <div
            v-for="module in quizStore.modules"
            :key="module.id"
            class="module-card"
          >
            <font-awesome-icon :icon="['fas', module.icon || 'question']" class="module-icon" />
            <h3>{{ module.title }}</h3>
            <button @click="startQuiz(module.id)">شروع آزمون</button>
          </div>
        </div>
      </div>

    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { storeToRefs } from 'pinia';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';
import { useQuizStore } from '../stores/quiz';
import badgeService from '../services/badgeService';
import BadgeDisplay from '../components/BadgeDisplay.vue';

const authStore = useAuthStore();
const quizStore = useQuizStore();
const router = useRouter();

const { user, score, level } = storeToRefs(authStore);

const earnedBadges = ref([]);
const loadingBadges = ref(false);
const scoreJustUpdated = ref(false);

onMounted(async () => {
  if (authStore.triggerScoreAnimation === true) {
    scoreJustUpdated.value = true;
    authStore.resetScoreAnimationTrigger();

    setTimeout(() => {
      scoreJustUpdated.value = false;
    }, 600);
  }
  
  quizStore.fetchModules();

  loadingBadges.value = true;
  try {
    const response = await badgeService.getEarnedBadges();
    earnedBadges.value = response.data;
  } catch (error) {
    console.error("Failed to fetch earned badges:", error);
  } finally {
    loadingBadges.value = false;
  }
});

const handleLogout = () => {
  authStore.logout();
};

const startQuiz = async (quizId) => {
  await quizStore.fetchQuizDetails(quizId);
  if (!quizStore.error) {
    router.push({ name: 'Quiz', params: { id: quizId } });
  }
};
</script>

<style scoped>
  .dashboard-container { max-width: 900px; margin: 20px auto; padding: 2rem; text-align: center; }
  .dashboard-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; padding-bottom: 1rem; border-bottom: 1px solid var(--color-border); }
  .stats-and-leaderboard { display: flex; justify-content: space-between; align-items: center; gap: 1.5rem; flex-wrap: wrap; margin-bottom: 1rem; }
  .stats { flex-grow: 1; display: flex; justify-content: center; gap: 1rem; }
  .stat-card { min-width: 110px; padding: 1rem 1.5rem !important; /* Override card padding slightly */ }
  .stats p span { display: inline-block; }
  .leaderboard-link { display: inline-flex; align-items: center; gap: 0.5rem; text-decoration: none; }
  .badges-section { margin-top: 2.5rem; padding-top: 2rem; border-top: 1px solid var(--color-border); }
  .badges-section h2 { margin-bottom: 1.5rem; color: var(--color-text); }
  .badges-grid { display: flex; flex-wrap: wrap; justify-content: center; gap: 1rem; }
  .divider { margin: 2.5rem 0; border: none; border-top: 1px solid var(--color-border); }
  .quiz-selection h2 { margin-bottom: 1.5rem; color: var(--color-text); }
  .modules-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 1.5rem; }
  .module-card { display: flex; flex-direction: column; align-items: center; justify-content: space-between; }
  .module-icon { font-size: 3rem; color: var(--color-primary); margin-bottom: 1rem; }
  .module-card h3 { margin-top: 0; margin-bottom: 1.5rem; color: var(--color-text); text-align: center; font-size: 1.1rem; }
  .loading-message { font-size: 1.2rem; color: var(--color-text-light); }
  .error-message { font-size: 1.2rem; color: var(--color-danger); }
</style>