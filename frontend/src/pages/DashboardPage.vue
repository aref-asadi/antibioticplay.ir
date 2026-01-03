<template>
  <div class="dashboard-layout">
    
    <header class="dashboard-topbar">
      <div class="topbar-content">
        <div class="right-section">
          <router-link to="/" class="dashboard-logo-link">
            <div class="logo-container">
              <font-awesome-icon icon="fas fa-microscope" class="logo-icon" />
              <h2 class="logo-text">AntibioticPlay</h2>
            </div>
          </router-link>
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

          <div class="stat-item" title="پاسخ صحیح متوالی">
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
          <a href="https://survey.porsline.ir/s/JLf6Akmc" target="_blank" class="btn-ghost header-btn" title="تکمیل پرسشنامه">
             <font-awesome-icon icon="fas fa-clipboard-list" />
             <span class="btn-label">پرسشنامه</span>
          </a>

          <router-link to="/rules" class="btn-ghost header-btn" title="راهنما">
             <font-awesome-icon icon="fas fa-question-circle" />
             <span class="btn-label">راهنما</span>
          </router-link>
          <button @click="handleLogout" class="btn-ghost">خروج</button>
        </div>
      </div>
    </header>

    <main class="dashboard-main">
      
      <div class="learning-path-column">
        
        <div v-for="(unit, unitIndex) in quizStore.modules" :key="unit.id" class="unit-section">
          
          <header class="unit-header" :style="{ backgroundColor: unit.color }">
            <div class="unit-info">
              <h3>{{ unit.title }}</h3>
              <p>{{ unit.description }}</p>
            </div>
          </header>
          
          <div class="unit-levels">
            <div 
              v-for="(level, index) in unit.levels" 
              :key="level.id" 
              class="level-node-wrapper"
              :class="{ 
                'completed': level.is_completed,
                'locked': level.is_locked 
              }"
            >
              <button 
                class="level-button" 
                :style="getLevelButtonStyle(level, unit.color)"
                @click="startQuiz(level)"
                :disabled="level.is_locked"
              >
                <font-awesome-icon v-if="level.is_completed" icon="fas fa-check" class="check-icon" />
                <font-awesome-icon v-else-if="level.is_locked" icon="fas fa-lock" class="lock-icon" />
                <font-awesome-icon v-else :icon="['fas', level.icon || 'star']" class="level-icon" />
              </button>
              
              <span class="level-title">{{ level.title }}</span>
            </div>
          </div>

        </div>

      </div>

      <aside class="sidebar-column">
        
        <div class="sidebar-widget user-widget">
          <div class="user-avatar-img-container">
            <img :src="userAvatar" alt="Avatar" class="sidebar-avatar" />
          </div>
          <div class="user-info">
            <h3>{{ authStore.fullName }}</h3>
            <p class="user-email">{{ user?.email }}</p>
            
            <router-link to="/profile" class="profile-link-btn">
              <font-awesome-icon icon="fas fa-user-pen" />
              ویرایش پروفایل
            </router-link>
          </div>
        </div>

        <div class="sidebar-widget review-widget">
          <div class="widget-header">
            <h3>مرور</h3>
          </div>
          <router-link to="/review" class="btn btn-outline review-link-btn" style="width: 100%; color: var(--color-secondary); border-color: var(--color-border);">
            <font-awesome-icon icon="fas fa-bookmark" />
            سوالات نشان‌دار
          </router-link>
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
import { ref, onMounted, computed } from 'vue';
import { storeToRefs } from 'pinia';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';
import { useQuizStore } from '../stores/quiz';
import badgeService from '../services/badgeService';
import leaderboardService from '../services/leaderboardService'; // ایمپورت سرویس لیدربورد
import { library } from '@fortawesome/fontawesome-svg-core';
import { faQuestionCircle, faUserPen, faLock, faMicroscope, faClipboardList } from '@fortawesome/free-solid-svg-icons';

library.add(faQuestionCircle, faUserPen, faLock, faMicroscope, faClipboardList);

const authStore = useAuthStore();
const quizStore = useQuizStore();
const router = useRouter();

const { user, score, level } = storeToRefs(authStore);

const earnedBadges = ref([]);
const scoreJustUpdated = ref(false);
const userRank = ref(null); // متغیر برای ذخیره رتبه

const moduleColors = ['#0288d1', '#009688', '#5e35b1', '#43a047', '#e53935'];
const getModuleColor = (index) => moduleColors[index % moduleColors.length];

const userAvatar = computed(() => {
  const avatarId = authStore.user?.avatar_id || 'fleming';
  // اصلاح مسیر: فایل‌ها در پوشه public/avatars هستند
  return `/avatars/avatar_${avatarId}.png`;
})

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

const adjustColor = (color, amount) => {
    return '#' + color.replace(/^#/, '').replace(/../g, color => ('0'+Math.min(255, Math.max(0, parseInt(color, 16) + amount)).toString(16)).substr(-2));
}

const getLevelButtonStyle = (level, unitColor) => {
  if (level.is_locked) {
    return {
      backgroundColor: '#e5e5e5',
      boxShadow: 'none',
      cursor: 'not-allowed',
      color: '#afafaf'
    };
  }
  
  if (level.is_completed) {
    return {
      backgroundColor: '#ffc107',
      boxShadow: '0 6px 0 #d39e00',
      color: 'white'
    };
  }

  return {
    backgroundColor: unitColor,
    boxShadow: `0 6px 0 ${adjustColor(unitColor, -40)}`,
    color: 'white'
  };
};

const startQuiz = (level, unitIndex = 0) => {
  if (!level || level.is_locked) return;

  const quizId = level.id;
  // prefer unit color if passed on level, otherwise derive from module index
  const themeColor = level.unitColor || getModuleColor(unitIndex);

  router.push({
    name: 'Quiz',
    params: { id: quizId },
    query: { theme: themeColor }
  });
};
</script>

<style scoped>
.dashboard-layout { min-height: 100vh; background-color: white; display: flex; flex-direction: column; }

/* Top Bar */
.dashboard-topbar { background-color: white; border-bottom: 2px solid #e5e5e5; position: sticky; top: 0; z-index: 100; padding: 0.8rem 2rem; }
.topbar-content { max-width: 1050px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; }

.dashboard-logo-link {
  text-decoration: none;
  display: inline-block;
  margin-right: auto; /* برای هل دادن بقیه آیتم‌ها به چپ (در حالت RTL) */
}

.logo-container {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.logo-icon {
  font-size: 1.4rem;
  color: var(--color-primary);
}

.logo-text {
  background: linear-gradient(45deg, var(--color-primary), #2c3e50);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 800;
  font-size: 1.4rem;
  margin: 0;
  letter-spacing: 0.5px;
}
/* Left Section Adjustment */
.left-section {
  display: flex; 
  gap: 0.5rem; 
  /* --- FIX: وسط‌چین کردن عمودی آیتم‌ها (دکمه خروج و راهنما) --- */
  align-items: center; 
}

/* استایل دکمه‌های هدر */
.header-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 0.8rem;
  border-radius: 12px;
  transition: background-color 0.2s;
  color: var(--color-text-light);
  font-weight: 600;
  text-decoration: none;
}

.header-btn:hover {
  background-color: #f0f0f0;
  color: var(--color-text);
}

.btn-label {
  font-size: 0.9rem;
}

.logout-btn {
  color: var(--color-danger);
}
.logout-btn:hover {
  background-color: var(--color-danger-light);
  color: var(--color-danger);
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
.unit-section { margin-bottom: 3rem; }

.unit-header {
  border-radius: 16px; padding: 1.5rem 2rem; color: white;
  display: flex; justify-content: space-between; align-items: center;
  margin-bottom: 2rem; position: sticky; top: 80px; z-index: 10;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}
.unit-info h3 { margin: 0 0 0.5rem 0; font-size: 1.5rem; }
.unit-info p { margin: 0; opacity: 0.9; }

.unit-levels {
  display: flex; flex-direction: column; align-items: center; gap: 2rem;
  padding: 1rem 0;
}

.level-button {
  width: 70px; height: 70px; border-radius: 50%; border: none;
  cursor: pointer; display: flex; justify-content: center; align-items: center;
  font-size: 2rem; color: white; transition: transform 0.1s;
  position: relative; z-index: 1;
}
.level-button:active { transform: translateY(4px); box-shadow: none !important; }

.level-title {
  margin-top: 0.5rem; font-weight: bold; color: #777; font-size: 0.9rem;
  background: white; padding: 0.2rem 0.6rem; border-radius: 10px; border: 2px solid #eee;
}

.level-node-wrapper {
  display: flex; flex-direction: column; align-items: center;
}

.level-node-wrapper:nth-child(odd) { transform: translateX(-30px); }
.level-node-wrapper:nth-child(even) { transform: translateX(30px); }

.level-node-wrapper.locked .level-button {
  background-color: #e5e5e5 !important; /* اجبار رنگ خاکستری */
  box-shadow: 0 4px 0 #ccc !important;
  transform: none !important; /* حذف انیمیشن کلیک */
}

.level-node-wrapper.locked .level-title {
  color: #aaa;
  border-color: #eee;
}

.lock-icon {
  font-size: 1.5rem;
  opacity: 0.6;
}

/* Sidebar */
.sidebar-column { width: 350px; display: flex; flex-direction: column; gap: 1.5rem; }
.sidebar-widget { border: 2px solid #e5e5e5; border-radius: 16px; padding: 1.5rem; background-color: white; }

/* User Widget */
.user-widget { display: flex; align-items: center; gap: 1rem; }
/* استایل جدید برای عکس آواتار در سایدبار */
.user-avatar-img-container {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  overflow: hidden;
  border: 3px solid var(--color-primary);
  background-color: white;
  flex-shrink: 0;
}
.sidebar-avatar {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.user-info h3 { margin: 0; font-size: 1.2rem; }
.user-info p { margin: 0; color: var(--color-text-light); font-size: 0.9rem; }
.user-info {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.user-email {
  margin: 0 0 0.5rem 0; /* کمی فاصله پایین ایمیل */
  color: var(--color-text-light);
  font-size: 0.9rem;
}

.profile-link-btn {
  font-size: 0.85rem;
  color: var(--color-secondary); /* یا color-primary بسته به سلیقه */
  text-decoration: none;
  font-weight: bold;
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  transition: opacity 0.2s;
}

.profile-link-btn:hover {
  opacity: 0.8;
  text-decoration: underline;
}

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
  .btn-label { display: none; }
  .logo-container { display: none; }
  .dashboard-topbar { padding: 0.8rem 1rem; }
}
</style>