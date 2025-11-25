<template>
  <div class="auth-wrapper">
    
    <header class="auth-header">
      <router-link to="/" class="close-btn">
        <font-awesome-icon icon="fas fa-times" />
      </router-link>
      <router-link to="/register" class="btn btn-outline" style="color: var(--color-secondary); border-color: var(--color-border);">
        ثبت نام
      </router-link>
    </header>

    <div class="auth-content">
      <h2 class="auth-title">ورود</h2>

      <form @submit.prevent="handleLogin" class="duo-form">
        
        <div class="input-group">
          <input 
            type="text" 
            class="duo-input" 
            :class="{ 'error': error }"
            placeholder="نام کاربری یا ایمیل" 
            v-model="username" 
            required 
          />
        </div>

        <div class="input-group">
          <input 
            type="password" 
            class="duo-input" 
            :class="{ 'error': error }"
            placeholder="رمز عبور" 
            v-model="password" 
            required 
          />
          <router-link to="/forgot-password" class="forgot-link">فراموشی؟</router-link>
        </div>

        <div v-if="error" class="error-message text-center" style="color: var(--color-danger); margin-top: 0.5rem;">
          {{ error }}
        </div>

        <button type="submit" class="btn btn-submit" :disabled="loading">
          {{ loading ? 'در حال ورود...' : 'ورود' }}
        </button>

      </form>

      <p class="auth-footer-text">
        با ورود به AntibioticPlay، شما با <strong>شرایط</strong> و <strong>حریم خصوصی</strong> ما موافقت می‌کنید.
      </p>
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '../stores/auth';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faTimes } from '@fortawesome/free-solid-svg-icons';

library.add(faTimes);

const authStore = useAuthStore();
const username = ref('');
const password = ref('');
const loading = ref(false);
const error = ref(null);

const handleLogin = async () => {
  loading.value = true;
  error.value = null;
  try {
    await authStore.login(username.value, password.value);
  } catch (err) {
    error.value = 'نام کاربری یا رمز عبور اشتباه است.';
  } finally {
    loading.value = false;
  }
};
</script>