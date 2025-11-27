<template>
  <div class="dashboard-layout">
    
    <header class="dashboard-topbar">
      <div class="topbar-content">
        <div class="right-section">
          <span class="logo-text">AntibioticPlay</span>
        </div>
        
        <div class="stats-bar">
          <div class="stat-item" title="سطح شما">
            <font-awesome-icon icon="fas fa-flag" class="flag-icon" />
            <span>سطح {{ level || 1 }}</span>
          </div>

          <div class="stat-item" title="استریک (توالی پاسخ صحیح)">
            <font-awesome-icon icon="fas fa-fire" class="icon-fire" />
            <span>{{ user?.correct_streak || 0 }}</span>
          </div>

          <div class="stat-item" title="امتیاز کل">
            <font-awesome-icon icon="fas fa-star" class="icon-gem" />
            <span :class="{ 'score-pop-animation': scoreJustUpdated }">
              {{ score || 0 }}
            </span>
          </div>
        </div>

        <div class="left-section">
          <button @click="handleLogout" class="btn-ghost">خروج</button>
        </div>
      </div>
    </header>

    <main class="dashboard-main">
      
      <div class="learning-path-column">
        <div v-if="quizStore.loading && !quizStore.modules.length" class="loading-state">
          در حال بارگذاری مسیر یادگیری...
        </div>
        
        <div v-else class="units-list">
          <div 
            v-for="(module, index) in quizStore.modules"
            :key="module.id"
            class="unit-card"
            :style="{ borderColor: getModuleColor(index) }"
          >
            <header class="unit-header" :style="{ backgroundColor: getModuleColor(index) }">
              <h3>بخش {{ index + 1 }}: {{ module.title }}</h3>
              <p>توضیحات کوتاه درباره این بخش...</p> </header>
            
            <div class="unit-body">
              <div class="path-node">
                <button 
                  class="node-button" 
                  :style="{ backgroundColor: getModuleColor(index) }"
                  @click="startQuiz(module.id)"
                >
                  <font-awesome-icon :icon="['fas', module.icon || 'star']" class="node-icon" />
                </button>
                <span class="start-label">شروع</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <aside class="sidebar-column">
        
        <div class="sidebar-widget user-widget">
          <div class="user-avatar-placeholder">
            {{ user?.username?.charAt(0).toUpperCase() }}
          </div>
          <div class="user-info">
            <h3>{{ user?.username }}</h3>
            <p>{{ user?.email }}</p>
          </div>
        </div>

        <div class="sidebar-widget leaderboard-widget">
          <div class="widget-header">
            <h3>جدول لیگ</h3>
            <router-link to="/leaderboard" class="link-text">مشاهده همه</router-link>
          </div>
          <div class="league-placeholder">
            <font-awesome-icon icon="fas fa-trophy" class="league-icon" />
            <p>در رقابت هفتگی شرکت کنید!</p>
          </div>
        </div>

        <div class="sidebar-widget badges-widget">
          <div class="widget-header">
            <h3>نشان‌های شما</h3>
          </div>
          <div v-if="earnedBadges.length > 0" class="badges-mini-grid">
            <div 
              v-for="badge in earnedBadges.slice(0, 4)" 
              :key="badge.id" 
              class="mini-badge"
              :title="badge.name"
            >
              <font-awesome-icon :icon="['fas', badge.icon.split(' ')[1]]" />
            </div>
            <div v-if="earnedBadges.length > 4" class="more-badges">
              +{{ earnedBadges.length - 4 }}
            </div>
          </div>
          <div v-else class="empty-state">
            هنوز نشانی کسب نکرده‌اید.
          </div>
        </div>

      </aside>

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

const authStore = useAuthStore();
const quizStore = useQuizStore();
const router = useRouter();

const { user, score, level } = storeToRefs(authStore);

const earnedBadges = ref([]);
const scoreJustUpdated = ref(false);

// رنگ‌های مختلف برای هر یونیت (تنوع بصری)
const moduleColors = ['#58cc02', '#ce82ff', '#00cd9c', '#ff9600', '#ff4b4b'];
const getModuleColor = (index) => moduleColors[index % moduleColors.length];

onMounted(async () => {
  // انیمیشن تغییر امتیاز
  if (authStore.triggerScoreAnimation === true) {
    scoreJustUpdated.value = true;
    authStore.resetScoreAnimationTrigger();
    setTimeout(() => { scoreJustUpdated.value = false; }, 600);
  }
  
  // دریافت آزمون‌ها
  quizStore.fetchModules();

  // دریافت نشان‌ها
  try {
    const response = await badgeService.getEarnedBadges();
    earnedBadges.value = response.data;
  } catch (error) {
    console.error("Failed to fetch earned badges:", error);
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
.dashboard-layout {
  min-height: 100vh;
  background-color: white;
  display: flex;
  flex-direction: column;
}

/* --- 1. Top Bar --- */
.dashboard-topbar {
  background-color: white;
  border-bottom: 2px solid #e5e5e5;
  position: sticky;
  top: 0;
  z-index: 100;
  padding: 0.8rem 2rem;
}
.topbar-content {
  max-width: 1050px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.logo-text {
  color: var(--color-primary);
  font-weight: 800;
  font-size: 1.5rem;
  letter-spacing: 0.5px;
}
.stats-bar {
  display: flex;
  gap: 2rem;
}
.stat-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 700;
  color: #afafaf;
  cursor: default;
}
.stat-item:hover { filter: brightness(0.9); }
.flag-icon { width: auto; height: auto; }
.icon-fire { color: #ff9600; font-size: 1.2rem; }
.icon-gem { color: #1cb0f6; font-size: 1.2rem; }
.btn-ghost {
  background: transparent;
  border: 2px solid transparent;
  color: var(--color-text-light);
  font-weight: 700;
  text-transform: uppercase;
  font-size: 0.9rem;
  padding: 0.5rem 1rem;
}
.btn-ghost:hover {
  background-color: #f0f0f0;
  border-radius: 12px;
}

/* --- 2. Main Layout --- */
.dashboard-main {
  flex: 1;
  max-width: 1050px;
  width: 100%;
  margin: 0 auto;
  padding: 2rem 1rem;
  display: flex;
  gap: 3rem;
}

/* --- Right Column: Learning Path --- */
.learning-path-column {
  flex: 1; /* Takes more space */
}

.unit-card {
  border: 2px solid; /* Color set dynamically */
  border-radius: 20px;
  overflow: hidden;
  margin-bottom: 2rem;
  text-align: right;
}
.unit-header {
  padding: 1.5rem;
  color: white;
}
.unit-header h3 { margin: 0 0 0.5rem 0; font-size: 1.4rem; }
.unit-header p { margin: 0; opacity: 0.9; font-size: 0.95rem; }

.unit-body {
  padding: 2rem;
  display: flex;
  justify-content: center;
  background-color: white;
}

.path-node {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}
.node-button {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: none;
  /* box-shadow is used for the 3D effect bottom part */
  box-shadow: 0 6px 0 rgba(0,0,0,0.2); 
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: transform 0.1s, box-shadow 0.1s;
}
.node-button:active {
  transform: translateY(4px);
  box-shadow: 0 2px 0 rgba(0,0,0,0.2);
}
.node-icon {
  font-size: 2.5rem;
  color: white;
}
.start-label {
  font-weight: 800;
  color: var(--color-text-light);
  font-size: 0.9rem;
  text-transform: uppercase;
}

/* --- Left Column: Sidebar --- */
.sidebar-column {
  width: 350px;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
/* Sidebar is hidden on mobile in typical layouts, or moved to bottom */
@media (max-width: 850px) {
  .dashboard-main { flex-direction: column-reverse; }
  .sidebar-column { width: 100%; }
}

.sidebar-widget {
  border: 2px solid #e5e5e5;
  border-radius: 16px;
  padding: 1.5rem;
  background-color: white;
}

/* User Widget */
.user-widget {
  display: flex;
  align-items: center;
  gap: 1rem;
}
.user-avatar-placeholder {
  width: 60px;
  height: 60px;
  background-color: var(--color-secondary); /* Blue */
  color: white;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.8rem;
  font-weight: bold;
  border: 2px solid black; /* Cartoon style */
}
.user-info h3 { margin: 0; font-size: 1.2rem; }
.user-info p { margin: 0; color: var(--color-text-light); font-size: 0.9rem; }

/* Leaderboard & Badges Widget */
.widget-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}
.widget-header h3 { margin: 0; color: var(--color-text); font-size: 1.1rem; }
.link-text {
  color: var(--color-secondary);
  text-decoration: none;
  font-weight: 700;
  text-transform: uppercase;
  font-size: 0.9rem;
}
.link-text:hover { text-decoration: underline; }

.league-placeholder {
  text-align: center;
  color: var(--color-text-light);
}
.league-icon { font-size: 3rem; color: #ffd700; margin-bottom: 0.5rem; }

/* Badges Grid */
.badges-mini-grid {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}
.mini-badge {
  width: 50px;
  height: 50px;
  background-color: #f7f7f7;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  color: var(--color-warning);
  font-size: 1.5rem;
}
.more-badges {
  width: 50px;
  height: 50px;
  background-color: #e5e5e5;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
  color: var(--color-text-light);
}
.empty-state { color: var(--color-text-light); font-size: 0.9rem; }
</style>