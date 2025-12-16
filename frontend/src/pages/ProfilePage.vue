<template>
  <div class="page-container">
    <header class="page-header">
      <router-link to="/dashboard" class="back-btn">
        <font-awesome-icon icon="fas fa-arrow-right" /> بازگشت به داشبورد
      </router-link>
      <h1>پروفایل من</h1>
    </header>

    <div class="user-info-card card mb-4">
      <div class="current-avatar">
        <img :src="getAvatarUrl(authStore.user?.avatar_id)" alt="Avatar" class="avatar-img-lg" />
      </div>
      <div class="user-details">
        <h2>{{ authStore.user?.username }}</h2>
        <div class="stats-grid">
          <div class="stat">
            <span class="label">سطح</span>
            <span class="value">{{ authStore.user?.level || 1 }}</span>
          </div>
          <div class="stat">
            <span class="label">امتیاز کل</span>
            <span class="value">{{ authStore.user?.total_score || 0 }}</span>
          </div>
        </div>
      </div>
    </div>

    <div class="avatar-selection-section">
      <h3>انتخاب کاراکتر</h3>
      <p class="text-muted">یک دانشمند را به عنوان آواتار خود انتخاب کنید:</p>
      
      <div class="avatars-grid">
        <div 
          v-for="avatar in avatars" 
          :key="avatar.id" 
          class="avatar-item card"
          :class="{ 'selected': selectedAvatar === avatar.id }"
          @click="selectAvatar(avatar.id)"
        >
          <img :src="avatar.image" :alt="avatar.name" class="avatar-img-sm" />
          <h4>{{ avatar.name }}</h4>
          <p class="role">{{ avatar.role }}</p>
          <div v-if="selectedAvatar === avatar.id" class="check-icon">
            <font-awesome-icon icon="fas fa-check-circle" />
          </div>
        </div>
      </div>

      <div class="actions mt-4">
        <button 
          @click="saveAvatar" 
          class="btn btn-primary" 
          :disabled="isSaving || selectedAvatar === authStore.user?.avatar_id"
        >
          <span v-if="isSaving">در حال ذخیره...</span>
          <span v-else>ذخیره تغییرات</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useAuthStore } from '../stores/auth';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faArrowRight, faCheckCircle } from '@fortawesome/free-solid-svg-icons';
import api from '../services/api';

library.add(faArrowRight, faCheckCircle);

const authStore = useAuthStore();
const selectedAvatar = ref('');
const isSaving = ref(false);

// لیست دانشمندان (آواتارها)
const avatars = [
  { 
    id: 'fleming', 
    name: 'الکساندر فلمینگ', 
    role: 'کاشف پنی‌سیلین', 
    image: '/assets/avatars/avatar_fleming.png' 
  },
  { 
    id: 'waksman', 
    name: 'سلمان واکسمن', 
    role: 'کاشف استرپتومایسین', 
    image: '/assets/avatars/avatar_waksman.png' 
  },
  { 
    id: 'domagk', 
    name: 'گرهارد دماک', 
    role: 'کاشف سولفونامید', 
    image: '/assets/avatars/avatar_domagk.png' 
  },
  { 
    id: 'florey', 
    name: 'هاوارد فلوری', 
    role: 'توسعه تولید پنی‌سیلین', 
    image: '/assets/avatars/avatar_florey.png' 
  },
  { 
    id: 'hodgkin', 
    name: 'دوروتی هاجکین', 
    role: 'تعیین ساختار پنی‌سیلین', 
    image: '/assets/avatars/avatar_hodgkin.png' 
  },
  { 
    id: 'bugie', 
    name: 'الیزابت بوگی', 
    role: 'همکار در کشف استرپتومایسین', 
    image: '/assets/avatars/avatar_bugie.png' 
  },
  { 
    id: 'youyou', 
    name: 'تو یویو', 
    role: 'کاشف آرتمیسینین (ضد مالاریا)', 
    image: '/assets/avatars/avatar_youyou.png' 
  }
];

// تابع کمکی برای گرفتن آدرس عکس
const getAvatarUrl = (id) => {
  const found = avatars.find(a => a.id === id);
  // اگر پیدا نشد، عکس فلمینگ را پیش‌فرض نشان بده
  return found ? found.image : '/assets/avatars/avatar_fleming.png';
};

onMounted(() => {
  if (authStore.user) {
    selectedAvatar.value = authStore.user.avatar_id || 'fleming';
  }
});

const selectAvatar = (id) => {
  selectedAvatar.value = id;
};

const saveAvatar = async () => {
  if (!selectedAvatar.value) return;
  isSaving.value = true;
  try {
    // 1. ارسال به بک‌‌اند
    await api.post('/auth/update-avatar', { avatar_id: selectedAvatar.value });
    
    // 2. آپدیت کردن استور لوکال
    // ما دستی مقدار را در استور آپدیت می‌کنیم تا نیازی به رفرش نباشد
    if (authStore.user) {
      authStore.user.avatar_id = selectedAvatar.value;
    }
    
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
.page-container { padding: 2rem; max-width: 800px; margin: 0 auto; }
.page-header { display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem; }
.back-btn { color: var(--color-text-light); }

.user-info-card {
  display: flex;
  align-items: center;
  gap: 2rem;
  padding: 2rem;
  background: linear-gradient(135deg, var(--color-primary-light), white);
  border: 2px solid var(--color-primary);
}

.avatar-img-lg {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  border: 4px solid white;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
  background-color: #ddd; /* رنگ زمینه تا وقتی عکس لود شود */
  object-fit: cover;
}

.user-details h2 { margin: 0 0 1rem 0; color: var(--color-primary); }
.stats-grid { display: flex; gap: 2rem; }
.stat { display: flex; flex-direction: column; }
.stat .label { font-size: 0.9rem; color: var(--color-text-light); }
.stat .value { font-size: 1.2rem; font-weight: bold; }

.avatars-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 1.5rem;
  margin-top: 1.5rem;
}

.avatar-item {
  cursor: pointer;
  text-align: center;
  transition: all 0.2s;
  position: relative;
  border: 2px solid transparent;
  padding: 1rem;
}

.avatar-item:hover { transform: translateY(-5px); box-shadow: 0 8px 15px rgba(0,0,0,0.1); }
.avatar-item.selected {
  border-color: var(--color-primary);
  background-color: var(--color-primary-light);
}

.avatar-img-sm {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  margin-bottom: 0.5rem;
  object-fit: cover;
  background-color: #eee;
}

.avatar-item h4 { font-size: 1rem; margin: 0.5rem 0 0.2rem 0; }
.role { font-size: 0.8rem; color: var(--color-text-light); margin: 0; }

.check-icon {
  position: absolute;
  top: 10px;
  right: 10px;
  color: var(--color-primary);
  font-size: 1.5rem;
  background: white;
  border-radius: 50%;
  height: 24px;
  width: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.mt-4 { margin-top: 2rem; text-align: left; }

@media (max-width: 600px) {
  .user-info-card { flex-direction: column; text-align: center; }
  .stats-grid { justify-content: center; }
}
</style>