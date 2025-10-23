<template>
  <div class="home-container card">
    <h1>به AntibioticPlay.ir خوش آمدید! 🧪</h1>
    <p>دانش دارویی خود را با آزمون‌های تعاملی و جذاب محک بزنید و با دیگران رقابت کنید.</p>

    <div class="actions">
      <template v-if="!authStore.isAuthenticated">
        <router-link to="/login" class="btn-primary">ورود</router-link>
        <router-link to="/register" class="btn-secondary">ثبت نام</router-link>
      </template>
      <template v-else>
        <router-link to="/dashboard" class="btn-primary">رفتن به داشبورد</router-link>
        <button @click="authStore.logout()" class="btn-danger">خروج</button>
      </template>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '../stores/auth';
const authStore = useAuthStore();
</script>

<style scoped>
.home-container {
  max-width: 600px;
  margin: 100px auto; /* Add more top margin */
  text-align: center;
  padding: 3rem !important; /* Larger padding */
}
h1 {
  color: var(--color-primary-dark);
  margin-bottom: 1.5rem;
}
p {
  font-size: 1.1rem;
  color: var(--color-text-light);
  margin-bottom: 2.5rem;
}
.actions {
  display: flex;
  justify-content: center;
  gap: 1rem;
}
/* Ensure router-links look like buttons */
.actions a {
  text-decoration: none;
}
</style>