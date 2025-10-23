<template>
  <div id="main-container">
    <router-view />

    <NewBadgeNotification
      :badge="quizStore.badgeToShowNotification"
      @close="quizStore.clearBadgeNotification"
    />
    </div>
</template>

<script setup>
import { useQuizStore } from './stores/quiz'; // <-- *** ایمپورت quizStore ***
import NewBadgeNotification from './components/NewBadgeNotification.vue'; // <-- *** ایمپورت کامپوننت ***

const quizStore = useQuizStore(); // <-- *** استفاده از store ***
</script>

<style>
/* ... (استایل‌های قبلی App.vue) ... */
#main-container {
  /* font-family and text-align are inherited from style.css */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  /* margin-top: 60px; */ /* Removed margin-top for potentially full-page layouts */
  padding: 1rem;
  min-height: 100vh; /* Ensure container takes full height */
  box-sizing: border-box;
}
</style>