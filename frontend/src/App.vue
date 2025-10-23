<template>
  <div id="main-container">
    <router-view />

    <NotificationDisplay
      :badge="quizStore.badgeToShowNotification"
      @close="quizStore.clearBadgeNotification"
    />
    </div>
</template>

<script setup>
import { useQuizStore } from './stores/quiz';
// --- *** استفاده از نام صحیح کامپوننت *** ---
import NotificationDisplay from './components/NotificationDisplay.vue';
// --- *** پایان تغییر *** ---

const quizStore = useQuizStore();
</script>

<style>
/* ... (استایل‌های قبلی App.vue) ... */
#main-container {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  padding: 1rem;
  min-height: 100vh;
  box-sizing: border-box;
}
</style>