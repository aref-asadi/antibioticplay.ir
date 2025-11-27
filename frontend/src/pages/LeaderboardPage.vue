<template>
  <div class="leaderboard-layout" :style="{ backgroundColor: currentLeagueColor }">
    
    <header class="league-header">
      <div class="header-content">
        <router-link to="/dashboard" class="back-btn">بازگشت</router-link>
        
        <div class="league-tabs">
          <button 
            v-for="league in leagues" 
            :key="league.id"
            class="league-tab-btn"
            :class="{ active: selectedLeague === league.id }"
            @click="changeLeague(league.id)"
          >
            <font-awesome-icon :icon="['fas', league.icon]" />
            <span class="tab-label">{{ league.name }}</span>
          </button>
        </div>

        <div class="spacer"></div>
      </div>
      
      <div class="league-info-text">
        <h1 class="league-title">{{ currentLeagueTitle }}</h1>
        <p class="league-subtitle">رتبه‌بندی بر اساس امتیاز کل</p>
      </div>
    </header>

    <main class="leaderboard-body">
      <div class="leaderboard-card">
        
        <div class="list-header">
          <span class="col-rank">رتبه</span>
          <span class="col-user">کاربر</span>
          <span class="col-score">امتیاز</span>
        </div>

        <div v-if="loading" class="loading-state">در حال بارگذاری...</div>
        <div v-else-if="leaderboard.length === 0" class="empty-state">
          هنوز کسی به این لیگ نرسیده است! اولین نفر باشید.
        </div>

        <div v-else class="ranking-list">
          <div 
            v-for="(user, index) in leaderboard" 
            :key="user.username" 
            class="ranking-item"
            :class="{ 'is-me': isCurrentUser(user.username) }"
          >
            <div class="col-rank">
              <div v-if="index < 3" class="medal-icon" :class="'rank-' + (index+1)">
                <font-awesome-icon icon="fas fa-trophy" />
              </div>
              <span v-else class="rank-number">{{ index + 1 }}</span>
            </div>

            <div class="col-user">
              <div class="avatar-circle" :style="{ backgroundColor: currentLeagueColor }">
                {{ user.username.charAt(0).toUpperCase() }}
              </div>
              <div class="user-details">
                <span class="username-text">{{ user.username }}</span>
                <span v-if="isCurrentUser(user.username)" class="me-badge">شما</span>
              </div>
            </div>

            <div class="col-score">{{ user.score }}</div>
          </div>
        </div>

      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue';
import { useAuthStore } from '../stores/auth';
import leaderboardService from '../services/leaderboardService';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faTrophy, faMedal, faGem } from '@fortawesome/free-solid-svg-icons';

library.add(faTrophy, faMedal, faGem);

const authStore = useAuthStore();
const leaderboard = ref([]);
const loading = ref(false);
const selectedLeague = ref('diamond'); // پیش‌فرض

const leagues = [
  { id: 'bronze', name: 'برنز', color: '#cd7f32', icon: 'medal' },
  { id: 'silver', name: 'نقره', color: '#a0a0a0', icon: 'medal' }, // کمی تیره‌تر برای دیده شدن روی سفید
  { id: 'gold', name: 'طلا', color: '#e6c200', icon: 'trophy' }, // طلایی تیره‌تر
  { id: 'diamond', name: 'الماس', color: '#ce82ff', icon: 'gem' } // بنفش
];

// تشخیص لیگ فعلی کاربر برای انتخاب پیش‌فرض
onMounted(() => {
  // اگر کاربر لیگ مشخصی دارد، همان را انتخاب کن، وگرنه الماس
  const userLeagueName = authStore.userLeague?.name;
  if (userLeagueName) {
    const found = leagues.find(l => l.name === userLeagueName);
    if (found) selectedLeague.value = found.id;
  }
  fetchData();
});

const currentLeagueColor = computed(() => {
  return leagues.find(l => l.id === selectedLeague.value)?.color || '#ce82ff';
});

const currentLeagueTitle = computed(() => {
  return 'لیگ ' + (leagues.find(l => l.id === selectedLeague.value)?.name || 'الماس');
});

const isCurrentUser = (username) => authStore.user?.username === username;

const changeLeague = (leagueId) => {
  selectedLeague.value = leagueId;
  fetchData();
};

const fetchData = async () => {
  loading.value = true;
  leaderboard.value = [];
  try {
    const response = await leaderboardService.getLeaderboard(selectedLeague.value);
    leaderboard.value = response.data;
  } catch (err) {
    console.error(err);
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
.leaderboard-layout {
  min-height: 100vh;
  transition: background-color 0.5s ease; /* انیمیشن تغییر رنگ */
  display: flex;
  flex-direction: column;
}

.league-header {
  padding: 1rem;
  background-color: rgba(0, 0, 0, 0.15);
  color: white;
}
.header-content {
  max-width: 800px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
}
.back-btn {
  color: white; text-decoration: none; font-weight: 700;
  background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 12px;
}

/* Tabs */
.league-tabs {
  display: flex;
  background: rgba(0,0,0,0.2);
  border-radius: 16px;
  padding: 4px;
  overflow-x: auto; /* اسکرول در موبایل */
}
.league-tab-btn {
  background: transparent;
  border: none;
  color: rgba(255,255,255,0.6);
  padding: 0.6rem 1rem;
  border-radius: 12px;
  cursor: pointer;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s;
  white-space: nowrap;
}
.league-tab-btn.active {
  background: white;
  color: var(--color-text); /* متن تیره روی تب سفید */
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.league-tab-btn:hover:not(.active) { color: white; }

.league-info-text { text-align: center; margin-top: 1.5rem; margin-bottom: 1rem; }
.league-title { margin: 0; font-size: 2rem; font-weight: 900; text-shadow: 0 2px 4px rgba(0,0,0,0.1); }
.league-subtitle { margin: 0; opacity: 0.9; }

.leaderboard-body { flex: 1; display: flex; justify-content: center; padding: 0 1rem 2rem; }
.leaderboard-card { width: 100%; max-width: 800px; background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1); min-height: 300px; display: flex; flex-direction: column; }

/* List Styles (Same as before with minor tweaks) */
.list-header { display: flex; padding: 1rem 1.5rem; background: #f9f9f9; color: #777; font-weight: 700; font-size: 0.9rem; }
.ranking-list { flex: 1; overflow-y: auto; }
.ranking-item { display: flex; align-items: center; padding: 1rem 1.5rem; border-bottom: 1px solid #f0f0f0; }
.ranking-item.is-me { background-color: #f0faff; border-left: 4px solid var(--color-secondary); }

.col-rank { width: 50px; text-align: center; font-weight: 700; color: #777; }
.col-user { flex: 1; display: flex; align-items: center; gap: 1rem; padding: 0 1rem; }
.col-score { width: 80px; text-align: left; font-weight: 800; color: #444; }

.medal-icon { font-size: 1.4rem; }
.rank-1 { color: #ffd700; }
.rank-2 { color: #c0c0c0; }
.rank-3 { color: #cd7f32; }

.avatar-circle { width: 40px; height: 40px; color: white; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-weight: bold; }
.username-text { font-weight: 700; }
.me-badge { font-size: 0.7rem; background: var(--color-secondary); color: white; padding: 2px 6px; border-radius: 6px; margin-right: 0.5rem; }

.loading-state, .empty-state { padding: 3rem; text-align: center; color: #999; }

@media (max-width: 600px) {
  .header-content { flex-direction: column; }
  .league-tabs { width: 100%; justify-content: space-between; }
  .league-tab-btn { flex: 1; justify-content: center; padding: 0.6rem 0.5rem; font-size: 0.9rem; }
  .tab-label { display: none; } /* فقط آیکون در موبایل برای جا شدن */
  .active .tab-label { display: inline; } /* تب فعال متن داشته باشد */
}
</style>