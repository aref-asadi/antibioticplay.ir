<template>
  <div class="page-container">
    <header class="page-header">
      <router-link to="/dashboard" class="back-btn">
        <font-awesome-icon icon="fas fa-arrow-right" /> بازگشت به داشبورد
      </router-link>
      <h1>پروفایل کاربری</h1>
    </header>

    <div class="profile-header-card card">
      <div class="profile-avatar-section">
        <img :src="currentAvatarUrl" alt="Avatar" class="avatar-img-lg" />
        <div class="profile-names">
          <h2>{{ authStore.user?.username }}</h2>
          <span class="email-text">{{ authStore.user?.email }}</span>
        </div>
      </div>
      
      <div class="stats-overview">
        <div class="stat-box">
          <span class="stat-label">سطح</span>
          <span class="stat-value">{{ authStore.user?.level || 1 }}</span>
        </div>
        <div class="stat-box">
          <span class="stat-label">امتیاز کل</span>
          <span class="stat-value">{{ authStore.user?.score || 0 }}</span>
        </div>
        <div class="stat-box">
          <span class="stat-label">آزمون‌ها</span>
          <span class="stat-value">{{ authStore.user?.quizzes_completed || 0 }}</span>
        </div>
      </div>
    </div>

    <div class="content-grid">
      <div class="info-column">
        
        <div class="info-card card league-card">
          <h3>وضعیت لیگ</h3>
          <div class="league-details">
            <font-awesome-icon 
              :icon="authStore.userLeague?.icon || 'fas fa-medal'" 
              class="league-icon-big"
              :style="{ color: authStore.userLeague?.color || '#cd7f32' }" 
            />
            <div class="league-text">
              <span class="league-name" :style="{ color: authStore.userLeague?.color }">
                لیگ {{ authStore.userLeague?.name }}
              </span>
              <div class="rank-display">
                <span class="label">رتبه شما:</span>
                <span class="value" v-if="userRank">#{{ userRank }}</span>
                <span class="value" v-else>...</span>
              </div>
            </div>
          </div>
        </div>

        <div class="info-card card badges-card">
          <h3>نشان‌های افتخار</h3>
          <div v-if="earnedBadgesList.length > 0" class="badges-grid-profile">
            <div 
              v-for="badge in earnedBadgesList" 
              :key="badge.id" 
              class="badge-item"
              :title="badge.name + ': ' + badge.description"
            >
              <div class="badge-icon-wrapper">
                 <font-awesome-icon :icon="['fas', badge.icon.split(' ')[1]]" />
              </div>
              <span class="badge-name">{{ badge.name }}</span>
            </div>
          </div>
          <div v-else class="empty-badges">
            <p>هنوز نشانی کسب نکرده‌اید.</p>
            <router-link to="/dashboard" class="btn-text">شروع یادگیری</router-link>
          </div>
        </div>
      </div>

      <div class="avatar-selection-column">
        <div class="card selection-card">
          <h3>تغییر کاراکتر</h3>
          <p class="text-muted">دانشمند مورد علاقه خود را انتخاب کنید:</p>
          
          <div class="avatars-grid">
            <div 
              v-for="avatar in avatars" 
              :key="avatar.id" 
              class="avatar-item"
              :class="{ 'selected': selectedAvatar === avatar.id }"
              @click="selectAvatar(avatar.id)"
            >
              <img :src="avatar.image" :alt="avatar.name" class="avatar-img-sm" />
              <div class="avatar-meta">
                <h4>{{ avatar.name }}</h4>
                <p>{{ avatar.role }}</p>
              </div>
              <div v-if="selectedAvatar === avatar.id" class="check-icon">
                <font-awesome-icon icon="fas fa-check-circle" />
              </div>
            </div>
          </div>

          <div class="actions">
            <button 
              @click="saveAvatar" 
              class="btn btn-primary btn-block" 
              :disabled="isSaving || selectedAvatar === authStore.user?.avatar_id"
            >
              <span v-if="isSaving">در حال ذخیره...</span>
              <span v-else>ذخیره تغییرات</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useAuthStore } from '../stores/auth';
import api from '../services/api';
import badgeService from '../services/badgeService';
import leaderboardService from '../services/leaderboardService';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faArrowRight, faCheckCircle, faMedal, faTrophy, faGem } from '@fortawesome/free-solid-svg-icons';

library.add(faArrowRight, faCheckCircle, faMedal, faTrophy, faGem);

const authStore = useAuthStore();
const selectedAvatar = ref('');
const isSaving = ref(false);
const earnedBadgesList = ref([]);
const userRank = ref(null);

// لیست دانشمندان (آواتارها) - با مسیر صحیح
const avatars = [
  { id: 'fleming', name: 'الکساندر فلمینگ', role: 'کاشف پنی‌سیلین', image: '/avatars/avatar_fleming.png' },
  { id: 'waksman', name: 'سلمان واکسمن', role: 'کاشف استرپتومایسین', image: '/avatars/avatar_waksman.png' },
  { id: 'domagk', name: 'گرهارد دماک', role: 'کاشف سولفونامید', image: '/avatars/avatar_domagk.png' },
  { id: 'florey', name: 'هاوارد فلوری', role: 'توسعه تولید پنی‌سیلین', image: '/avatars/avatar_florey.png' },
  { id: 'hodgkin', name: 'دوروتی هاجکین', role: 'تعیین ساختار پنی‌سیلین', image: '/avatars/avatar_hodgkin.png' },
  { id: 'bugie', name: 'الیزابت بوگی', role: 'همکار در کشف استرپتومایسین', image: '/avatars/avatar_bugie.png' },
  { id: 'youyou', name: 'تو یویو', role: 'کاشف آرتمیسینین', image: '/avatars/avatar_youyou.png' }
];

const currentAvatarUrl = computed(() => {
  const id = authStore.user?.avatar_id || 'fleming';
  const found = avatars.find(a => a.id === id);
  return found ? found.image : '/avatars/avatar_fleming.png';
});

onMounted(async () => {
  // 1. تنظیم آواتار فعلی در متغیر لوکال
  if (authStore.user) {
    selectedAvatar.value = authStore.user.avatar_id || 'fleming';
  }

  // 2. دریافت مجدد پروفایل برای اطمینان از سینک بودن داده‌ها
  await authStore.fetchUser();

  // 3. دریافت نشان‌ها
  try {
    // اگر در بک‌اند لیست نشان‌ها را در آبجکت کاربر برگرداندیم که عالی است
    // اما برای اطمینان از badgeService هم استفاده می‌کنیم تا جزئیات (icon, name) را داشته باشیم
    const response = await badgeService.getEarnedBadges();
    earnedBadgesList.value = response.data;
  } catch (error) {
    console.error('Error fetching badges:', error);
  }

  // 4. دریافت رتبه کاربر
  try {
    const currentLeagueId = authStore.userLeague?.name === 'الماس' ? 'diamond' : 
                            authStore.userLeague?.name === 'طلا' ? 'gold' :
                            authStore.userLeague?.name === 'نقره' ? 'silver' : 'bronze';
    
    const lbResponse = await leaderboardService.getLeaderboard(currentLeagueId);
    const leaderboard = lbResponse.data;
    const myIndex = leaderboard.findIndex(u => u.username === authStore.username);
    
    if (myIndex !== -1) {
      userRank.value = myIndex + 1;
    } else {
      userRank.value = '20+';
    }
  } catch (err) {
    console.error("Failed to fetch rank:", err);
  }
});

const selectAvatar = (id) => {
  selectedAvatar.value = id;
};

const saveAvatar = async () => {
  if (!selectedAvatar.value) return;
  isSaving.value = true;
  try {
    await api.post('/auth/update-avatar', { avatar_id: selectedAvatar.value });
    if (authStore.user) {
      authStore.user.avatar_id = selectedAvatar.value;
    }
    // آپدیت کردن لوکال استوریج
    localStorage.setItem('user', JSON.stringify(authStore.user));
    alert('آواتار شما با موفقیت تغییر کرد!');
  } catch (error) {
    console.error('Error updating avatar:', error);
    alert('خطا در ذخیره آواتار.');
  } finally {
    isSaving.value = false;
  }
};
</script>

<style scoped>
.page-container { padding: 2rem; max-width: 1000px; margin: 0 auto; min-height: 100vh; }
.page-header { display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem; }
.back-btn { color: var(--color-text-light); text-decoration: none; font-weight: bold; }
h1 { margin: 0; font-size: 1.8rem; color: var(--color-text); }

.card { background: white; border: 2px solid #e5e5e5; border-radius: 16px; padding: 1.5rem; }

/* --- Profile Header --- */
.profile-header-card { display: flex; flex-direction: column; gap: 2rem; margin-bottom: 2rem; background: linear-gradient(135deg, white, #f0f7ff); border-color: var(--color-primary-light); }

.profile-avatar-section { display: flex; align-items: center; gap: 1.5rem; }
.avatar-img-lg { width: 100px; height: 100px; border-radius: 50%; border: 4px solid white; box-shadow: 0 4px 10px rgba(0,0,0,0.1); background-color: #eee; object-fit: cover; }
.profile-names h2 { margin: 0; font-size: 1.8rem; color: var(--color-primary); }
.email-text { color: var(--color-text-light); font-size: 1rem; }

.stats-overview { display: flex; gap: 3rem; padding-top: 1rem; border-top: 2px solid rgba(0,0,0,0.05); }
.stat-box { display: flex; flex-direction: column; gap: 0.3rem; }
.stat-label { font-size: 0.9rem; color: var(--color-text-light); font-weight: bold; }
.stat-value { font-size: 1.4rem; font-weight: 800; color: var(--color-text); }

/* --- Grid Layout --- */
.content-grid { display: grid; grid-template-columns: 1fr 1.5fr; gap: 2rem; }

.info-column { display: flex; flex-direction: column; gap: 2rem; }
.info-card h3 { margin: 0 0 1rem 0; font-size: 1.1rem; color: var(--color-text-light); text-transform: uppercase; letter-spacing: 0.5px; }

/* League Card */
.league-details { display: flex; align-items: center; gap: 1rem; }
.league-icon-big { font-size: 3.5rem; }
.league-text { display: flex; flex-direction: column; }
.league-name { font-size: 1.4rem; font-weight: 900; }
.rank-display { margin-top: 0.2rem; font-size: 1rem; color: var(--color-text); }
.rank-display .value { font-weight: bold; margin-right: 0.3rem; font-size: 1.2rem; }

/* Badges Card */
.badges-grid-profile { display: grid; grid-template-columns: repeat(auto-fill, minmax(80px, 1fr)); gap: 1rem; }
.badge-item { display: flex; flex-direction: column; align-items: center; text-align: center; gap: 0.5rem; }
.badge-icon-wrapper { width: 60px; height: 60px; background-color: #fff9c4; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.8rem; color: #fbc02d; border: 2px solid #fbc02d; }
.badge-name { font-size: 0.8rem; color: var(--color-text); font-weight: bold; }
.empty-badges { text-align: center; padding: 1rem; color: var(--color-text-light); }

/* Avatar Selection */
.selection-card h3 { margin-top: 0; }
.avatars-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 1rem; margin-top: 1.5rem; max-height: 500px; overflow-y: auto; padding-right: 0.5rem; }

.avatar-item { cursor: pointer; border: 2px solid transparent; border-radius: 12px; padding: 1rem; text-align: center; position: relative; transition: all 0.2s; background: #f9f9f9; }
.avatar-item:hover { background: #fff; box-shadow: 0 4px 12px rgba(0,0,0,0.08); transform: translateY(-2px); }
.avatar-item.selected { border-color: var(--color-primary); background-color: var(--color-primary-light); }

.avatar-img-sm { width: 70px; height: 70px; border-radius: 50%; object-fit: cover; margin-bottom: 0.5rem; border: 2px solid white; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
.avatar-meta h4 { font-size: 0.9rem; margin: 0.5rem 0 0.2rem 0; color: var(--color-text); }
.avatar-meta p { font-size: 0.75rem; color: var(--color-text-light); margin: 0; line-height: 1.2; }

.check-icon { position: absolute; top: 8px; right: 8px; color: var(--color-primary); font-size: 1.2rem; background: white; border-radius: 50%; width: 20px; height: 20px; display: flex; alignItems: center; justifyContent: center; }

.actions { margin-top: 2rem; }
.btn-block { width: 100%; padding: 0.8rem; font-size: 1rem; }

@media (max-width: 850px) {
  .content-grid { grid-template-columns: 1fr; }
  .profile-header-card { flex-direction: column; align-items: center; text-align: center; }
  .profile-avatar-section { flex-direction: column; text-align: center; }
  .stats-overview { justify-content: center; width: 100%; }
}
</style>