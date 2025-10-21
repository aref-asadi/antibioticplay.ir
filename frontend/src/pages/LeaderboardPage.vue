<template>
  <div class="leaderboard-container">
    <h1>🏆 جدول امتیازات 🏆</h1>
    <p>۱۰ کاربر برتر antibioticplay.ir</p>

    <div v-if="loading" class="loading-message">در حال بارگذاری...</div>
    <div v-if="error" class="error-message">{{ error }}</div>

    <ol v-if="leaderboard.length > 0" class="leaderboard-list">
      <li v-for="(user, index) in leaderboard" :key="user.username" class="leaderboard-item">
        <span class="rank">{{ index + 1 }}</span>
        <span class="username">{{ user.username }}</span>
        <span class="score">{{ user.score }} امتیاز</span>
      </li>
    </ol>

    <router-link to="/dashboard" class="back-link">بازگشت به داشبورد</router-link>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import leaderboardService from '../services/leaderboardService';

const leaderboard = ref([]);
const loading = ref(true);
const error = ref(null);

// در زمان بارگذاری کامپوننت، داده‌ها را از API دریافت کن
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
.leaderboard-container {
  max-width: 600px;
  margin: 20px auto;
  padding: 2rem;
  text-align: center;
  background-color: #fff;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

h1 {
  color: #333;
}

.leaderboard-list {
  list-style: none;
  padding: 0;
  margin-top: 2rem;
}

.leaderboard-item {
  display: flex;
  align-items: center;
  padding: 1rem;
  margin-bottom: 0.75rem;
  background-color: #f7f7f7;
  border-radius: 8px;
}

/* استایل برای سه نفر اول */
.leaderboard-item:nth-child(1) {
  background-color: #ffd700; /* Gold */
  font-weight: bold;
}
.leaderboard-item:nth-child(2) {
  background-color: #c0c0c0; /* Silver */
}
.leaderboard-item:nth-child(3) {
  background-color: #cd7f32; /* Bronze */
}

.rank {
  font-size: 1.2rem;
  font-weight: bold;
  width: 40px;
  text-align: left;
}

.username {
  flex-grow: 1;
  text-align: left;
  font-size: 1.1rem;
  padding-left: 1rem;
}

.score {
  font-size: 1.1rem;
  font-weight: bold;
  color: #42b983;
}

.back-link {
  display: inline-block;
  margin-top: 2rem;
  padding: 0.6rem 1.2rem;
  background-color: #eee;
  color: #555;
  text-decoration: none;
  border-radius: 8px;
}
.back-link:hover {
  background-color: #ddd;
}
</style>