<template>
  <div class="dashboard-layout">
    
    <header class="dashboard-topbar">
      <div class="topbar-content">
        <div class="right-section">
          <span class="logo-text">AntibioticPlay</span>
        </div>
        
        <div class="stats-bar">
          <div class="stat-item" :title="'لیگ: ' + (user?.league?.name || 'برنز')">
            <font-awesome-icon 
              :icon="user?.league?.icon || 'fas fa-medal'" 
              class="flag-icon"
              :style="{ color: user?.league?.color || '#cd7f32' }" 
            />
            <span class="desktop-only">{{ user?.league?.name || 'برنز' }}</span>
          </div>

          <div class="stat-item" title="زنجیره پاسخ‌های صحیح">
            <font-awesome-icon icon="fas fa-fire" class="icon-fire" :class="{ 'animate-fire': (user?.correct_streak || 0) > 0 }" />
            <span>{{ user?.correct_streak || 0 }}</span>
          </div>

          <div class="stat-item" title="امتیاز کل">
            <font-awesome-icon icon="fas fa-star" class="icon-gem" />
            <span :class="{ 'score-pop-animation': scoreJustUpdated }">
              {{ score || 0 }}
            </span>
          </div>
        </div>

        <div class="left-section" style="display: flex; gap: 0.5rem;">
          <router-link to="/rules" class="btn-ghost" title="راهنما">
             <font-awesome-icon icon="fas fa-question-circle" />
          </router-link>
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
              <p>{{ module.description }}</p>
            </header>
            
            <div class="unit-body">
              <div class="path-node">
                <button 
                  class="node-button" 
                  :style="{ backgroundColor: getModuleColor(index) }"
                  @click="startQuiz(module.id, index)"
                >
                  <font-awesome-icon :icon="['fas', module.icon || 'star']" class="node-icon" />
                </button>
                <span class="start-label" :style="{ color: getModuleColor(index) }">شروع</span>
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
            <h3>لیگ {{ user?.league?.name || 'برنز' }}</h3>
            <router-link to="/leaderboard" class="link-text">مشاهده لیگ</router-link>
          </div>
          
          <div v-if="userRank" class="league-status">
            <div class="league-icon-large" :style="{ color: user?.league?.color || '#cd7f32' }">
              <font-awesome-icon :icon="['fas', user?.league?.icon || 'medal']" />
            </div>
            <div class="rank-info">
              <span class="rank-label">رتبه شما</span>
              <span class="rank-value">#{{ userRank }}</span>
            </div>
            <div class="xp-info">
              {{ score }} XP
            </div>
          </div>
          
          <div v-else class="league-placeholder">
            <font-awesome-icon icon="fas fa-trophy" class="league-icon-gray" />
            <p>در حال محاسبه رتبه...</p>
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
import leaderboardService from '../services/leaderboardService'; // ایمپورت سرویس لیدربورد
import { library } from '@fortawesome/fontawesome-svg-core';
import { faQuestionCircle } from '@fortawesome/free-solid-svg-icons';

library.add(faQuestionCircle);

const authStore = useAuthStore();
const quizStore = useQuizStore();
const router = useRouter();

const { user, score, level } = storeToRefs(authStore);

const earnedBadges = ref([]);
const scoreJustUpdated = ref(false);
const userRank = ref(null); // متغیر برای ذخیره رتبه

const moduleColors = ['#58cc02', '#ce82ff', '#00cd9c', '#ff9600', '#ff4b4b'];
const getModuleColor = (index) => moduleColors[index % moduleColors.length];

onMounted(async () => {
  if (authStore.triggerScoreAnimation === true) {
    scoreJustUpdated.value = true;
    authStore.resetScoreAnimationTrigger();
    setTimeout(() => { scoreJustUpdated.value = false; }, 600);
  }
  
  quizStore.fetchModules();

  try {
    const response = await badgeService.getEarnedBadges();
    earnedBadges.value = response.data;
  } catch (error) {
    console.error("Failed to fetch earned badges:", error);
  }

  // --- *** محاسبه رتبه کاربر *** ---
  try {
    // گرفتن لیگ فعلی کاربر (مثلاً 'gold')
    const currentLeagueId = authStore.userLeague?.name === 'الماس' ? 'diamond' : 
                            authStore.userLeague?.name === 'طلا' ? 'gold' :
                            authStore.userLeague?.name === 'نقره' ? 'silver' : 'bronze';
    
    // درخواست لیدربورد همان لیگ
    const lbResponse = await leaderboardService.getLeaderboard(currentLeagueId);
    const leaderboard = lbResponse.data;
    
    // پیدا کردن ایندکس کاربر
    const myIndex = leaderboard.findIndex(u => u.username === user.value.username);
    if (myIndex !== -1) {
      userRank.value = myIndex + 1;
    } else {
      userRank.value = '20+'; // اگر در ۲۰ نفر اول نبود
    }
  } catch (err) {
    console.error("Failed to fetch rank:", err);
  }
});

const handleLogout = () => {
  authStore.logout();
};

const startQuiz = async (quizId, index) => {
  await quizStore.fetchQuizDetails(quizId);
  if (!quizStore.error) {
    // رنگ تم را به عنوان کوئری به صفحه بعد می‌فرستیم
    const themeColor = getModuleColor(index);
    router.push({ 
      name: 'Quiz', 
      params: { id: quizId },
      query: { theme: themeColor } // ارسال رنگ
    });
  }
};
</script>

<style scoped>
.dashboard-layout { min-height: 100vh; background-color: white; display: flex; flex-direction: column; }

/* Top Bar */
.dashboard-topbar { background-color: white; border-bottom: 2px solid #e5e5e5; position: sticky; top: 0; z-index: 100; padding: 0.8rem 2rem; }
.topbar-content { max-width: 1050px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; }

.logo-text { color: var(--color-primary); font-weight: 800; font-size: 1.5rem; letter-spacing: 0.5px; }

/* Left Section Adjustment */
.left-section {
  display: flex; 
  gap: 0.5rem; 
  /* --- FIX: وسط‌چین کردن عمودی آیتم‌ها (دکمه خروج و راهنما) --- */
  align-items: center; 
}

.stats-bar { display: flex; gap: 1.5rem; }
.stat-item { display: flex; align-items: center; gap: 0.5rem; font-weight: 700; color: #afafaf; cursor: default; }
.stat-item:hover { filter: brightness(0.9); }
.icon-fire { color: #ff9600; font-size: 1.2rem; }
.icon-gem { color: #1cb0f6; font-size: 1.2rem; }
.flag-icon { font-size: 1.2rem; }

/* Main Layout */
.dashboard-main { flex: 1; max-width: 1050px; width: 100%; margin: 0 auto; padding: 2rem 1rem; display: flex; gap: 3rem; }
.learning-path-column { flex: 1; }

/* Unit Cards */
.unit-card { border: 2px solid; border-radius: 20px; overflow: hidden; margin-bottom: 2rem; text-align: right; }
.unit-header { padding: 1.5rem; color: white; }
.unit-header h3 { margin: 0 0 0.5rem 0; font-size: 1.4rem; }
.unit-header p { margin: 0; opacity: 0.9; font-size: 0.95rem; }
.unit-body { padding: 2rem; display: flex; justify-content: center; background-color: white; }
.path-node { display: flex; flex-direction: column; align-items: center; gap: 0.5rem; }
.node-button { width: 80px; height: 80px; border-radius: 50%; border: none; box-shadow: 0 6px 0 rgba(0,0,0,0.2); display: flex; align-items: center; justify-content: center; cursor: pointer; transition: transform 0.1s, box-shadow 0.1s; }
.node-button:active { transform: translateY(4px); box-shadow: 0 2px 0 rgba(0,0,0,0.2); }
.node-icon { font-size: 2.5rem; color: white; }
.start-label { font-weight: 800; font-size: 0.9rem; text-transform: uppercase; }

/* Sidebar */
.sidebar-column { width: 350px; display: flex; flex-direction: column; gap: 1.5rem; }
.sidebar-widget { border: 2px solid #e5e5e5; border-radius: 16px; padding: 1.5rem; background-color: white; }

/* User Widget */
.user-widget { display: flex; align-items: center; gap: 1rem; }
.user-avatar-placeholder { width: 60px; height: 60px; background-color: var(--color-secondary); color: white; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-size: 1.8rem; font-weight: bold; border: 2px solid rgba(0,0,0,0.1); }
.user-info h3 { margin: 0; font-size: 1.2rem; }
.user-info p { margin: 0; color: var(--color-text-light); font-size: 0.9rem; }

/* Leaderboard Widget */
.league-status { display: flex; align-items: center; gap: 1rem; }
.league-icon-large { font-size: 3rem; display: flex; align-items: center; }
.rank-info { flex: 1; display: flex; flex-direction: column; }
.rank-label { font-size: 0.8rem; color: var(--color-text-light); font-weight: 700; text-transform: uppercase; }
.rank-value { font-size: 1.8rem; font-weight: 800; color: var(--color-text); }
.xp-info { font-weight: 700; color: var(--color-text-light); background: #f0f0f0; padding: 0.2rem 0.6rem; border-radius: 8px; font-size: 0.9rem; }
.league-placeholder { text-align: center; color: var(--color-text-light); }
.league-icon-gray { font-size: 3rem; color: #e5e5e5; margin-bottom: 0.5rem; }

.widget-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; }
.widget-header h3 { margin: 0; color: var(--color-text); font-size: 1.1rem; }
.link-text { color: var(--color-secondary); text-decoration: none; font-weight: 700; text-transform: uppercase; font-size: 0.9rem; }
.link-text:hover { text-decoration: underline; }

/* Badges */
.badges-mini-grid { display: flex; gap: 0.5rem; flex-wrap: wrap; }
.mini-badge { width: 50px; height: 50px; background-color: #f7f7f7; border-radius: 50%; display: flex; justify-content: center; align-items: center; color: var(--color-warning); font-size: 1.5rem; }
.more-badges { width: 50px; height: 50px; background-color: #e5e5e5; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-weight: bold; color: var(--color-text-light); }
.empty-state { color: var(--color-text-light); font-size: 0.9rem; }

@media (max-width: 850px) {
  .dashboard-main { flex-direction: column-reverse; padding-bottom: 100px; }
  .sidebar-column { width: 100%; }
  .desktop-only { display: none; }
  
  /* --- FIX: مخفی کردن لوگو در هدر موبایل --- */
  .logo-text { display: none; }
  /* تنظیم فاصله هدر در موبایل */
  .dashboard-topbar { padding: 0.8rem 1rem; }
}
</style>