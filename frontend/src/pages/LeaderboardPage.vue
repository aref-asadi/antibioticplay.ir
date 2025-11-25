<template>
  <div class="leaderboard-layout">
    
    <header class="league-header">
      <div class="header-content">
        <router-link to="/dashboard" class="back-btn">بازگشت</router-link>
        <div class="league-info">
          <h1 class="league-title">لیگ الماس</h1>
          <p class="league-subtitle">۱۰ نفر برتر این هفته</p>
        </div>
        <div class="spacer"></div> </div>
    </header>

    <main class="leaderboard-body">
      <div class="leaderboard-card">
        
        <div class="list-header">
          <span class="col-rank">رتبه</span>
          <span class="col-user">کاربر</span>
          <span class="col-score">امتیاز</span>
        </div>

        <div v-if="loading" class="loading-state">
          در حال بارگذاری نتایج...
        </div>
        <div v-if="error" class="error-message">{{ error }}</div>

        <div v-if="!loading && leaderboard.length > 0" class="ranking-list">
          <div 
            v-for="(user, index) in leaderboard" 
            :key="user.username" 
            class="ranking-item"
            :class="{ 
              'is-me': isCurrentUser(user.username),
              'rank-1': index === 0,
              'rank-2': index === 1,
              'rank-3': index === 2
            }"
          >
            <div class="col-rank">
              <div v-if="index < 3" class="medal-icon">
                <font-awesome-icon icon="fas fa-trophy" />
              </div>
              <span v-else class="rank-number">{{ index + 1 }}</span>
            </div>

            <div class="col-user">
              <div class="avatar-circle">
                {{ user.username.charAt(0).toUpperCase() }}
              </div>
              <div class="user-details">
                <span class="username-text">{{ user.username }}</span>
                <span v-if="isCurrentUser(user.username)" class="me-badge">شما</span>
              </div>
            </div>

            <div class="col-score">
              {{ user.score }} XP
            </div>
          </div>
        </div>

      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useAuthStore } from '../stores/auth';
import leaderboardService from '../services/leaderboardService';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faTrophy } from '@fortawesome/free-solid-svg-icons';

library.add(faTrophy);

const leaderboard = ref([]);
const loading = ref(true);
const error = ref(null);
const authStore = useAuthStore();

// تابع تشخیص کاربر فعلی
const isCurrentUser = (username) => {
  return authStore.user && authStore.user.username === username;
};

onMounted(async () => {
  try {
    const response = await leaderboardService.getLeaderboard();
    leaderboard.value = response.data;
  } catch (err) {
    console.error(err);
    error.value = 'خطا در دریافت جدول امتیازات.';
  } finally {
    loading.value = false;
  }
});
</script>

<style scoped>
.leaderboard-layout {
  min-height: 100vh;
  background-color: #ce82ff; /* Amethyst League Color */
  display: flex;
  flex-direction: column;
}

/* --- Header --- */
.league-header {
  padding: 1.5rem 2rem;
  background-color: rgba(0, 0, 0, 0.1); /* کمی تیره‌تر از پس‌زمینه */
  color: white;
}
.header-content {
  max-width: 800px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.back-btn {
  color: white;
  text-decoration: none;
  font-weight: 700;
  background: rgba(255, 255, 255, 0.2);
  padding: 0.5rem 1rem;
  border-radius: 12px;
  transition: background 0.2s;
}
.back-btn:hover { background: rgba(255, 255, 255, 0.3); }

.league-info { text-align: center; }
.league-title { margin: 0; font-size: 1.8rem; font-weight: 900; }
.league-subtitle { margin: 0; opacity: 0.8; font-size: 0.9rem; }
.spacer { width: 80px; } /* برای بالانس کردن دکمه بازگشت */

/* --- Body --- */
.leaderboard-body {
  flex: 1;
  display: flex;
  justify-content: center;
  padding: 2rem 1rem;
}

.leaderboard-card {
  width: 100%;
  max-width: 800px;
  background: white;
  border-radius: 20px;
  padding: 0; /* پدینگ داخلی لیست هندل می‌کند */
  box-shadow: 0 8px 0 rgba(0, 0, 0, 0.1);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.list-header {
  display: flex;
  padding: 1rem 1.5rem;
  border-bottom: 2px solid #e5e5e5;
  color: var(--color-text-light);
  font-weight: 700;
  font-size: 0.9rem;
}

.ranking-list {
  flex: 1;
  overflow-y: auto;
}

.ranking-item {
  display: flex;
  align-items: center;
  padding: 1rem 1.5rem;
  border-bottom: 1px solid #f0f0f0;
  transition: background-color 0.2s;
}
.ranking-item:hover { background-color: #f9f9f9; }
.ranking-item:last-child { border-bottom: none; }

/* Highlight Current User */
.ranking-item.is-me {
  background-color: #e5f6ff; /* آبی خیلی روشن */
  border: 2px solid var(--color-secondary);
  border-radius: 12px;
  margin: 0.5rem;
  position: relative;
  z-index: 1;
}

/* --- Columns --- */
.col-rank { width: 60px; text-align: center; display: flex; justify-content: center; align-items: center; }
.col-user { flex: 1; display: flex; align-items: center; gap: 1rem; padding: 0 1rem; }
.col-score { width: 100px; text-align: left; font-weight: 700; color: var(--color-text); }

/* Ranks Styling */
.rank-number { font-weight: 700; color: var(--color-text-light); }
.medal-icon { font-size: 1.5rem; }
.rank-1 .medal-icon { color: #ffd700; } /* Gold */
.rank-2 .medal-icon { color: #c0c0c0; } /* Silver */
.rank-3 .medal-icon { color: #cd7f32; } /* Bronze */

/* User Avatar */
.avatar-circle {
  width: 45px;
  height: 45px;
  background-color: var(--color-secondary);
  color: white;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
  font-size: 1.2rem;
  border: 2px solid rgba(0,0,0,0.1);
}
.rank-1 .avatar-circle { background-color: #ffd700; border-color: #e6c200; }
.rank-2 .avatar-circle { background-color: #c0c0c0; border-color: #a8a8a8; }
.rank-3 .avatar-circle { background-color: #cd7f32; border-color: #b56e2b; }

.user-details { display: flex; flex-direction: column; align-items: flex-start; }
.username-text { font-weight: 700; color: var(--color-text); }
.me-badge {
  font-size: 0.7rem;
  background-color: var(--color-secondary);
  color: white;
  padding: 0.1rem 0.4rem;
  border-radius: 8px;
}

/* Responsive */
@media (max-width: 600px) {
  .header-content { flex-direction: column; gap: 1rem; text-align: center; }
  .back-btn { align-self: flex-start; }
  .spacer { display: none; }
}
</style>