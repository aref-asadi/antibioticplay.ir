<template>
  <div id="main-container">
    <router-view />

    <BottomNav v-if="showBottomNav" />

    <NotificationDisplay
      :badge="quizStore.badgeToShowNotification"
      @close="quizStore.clearBadgeNotification"
    />
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import { useQuizStore } from './stores/quiz';
import NotificationDisplay from './components/NotificationDisplay.vue';
// 1. ایمپورت کامپوننت جدید
import BottomNav from './components/BottomNav.vue';

const quizStore = useQuizStore();
const route = useRoute();

// 2. شرط نمایش نوار پایین
const showBottomNav = computed(() => {
  // لیست صفحاتی که نوار پایین باید در آن‌ها دیده شود
  const allowedRoutes = ['Dashboard', 'Leaderboard'];
  return allowedRoutes.includes(route.name);
});
</script>

<style>
#main-container {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  min-height: 100vh;
  box-sizing: border-box;
  /* حذف padding سراسری چون صفحات خودشان مدیریت می‌کنند */
  padding: 0; 
}
</style>