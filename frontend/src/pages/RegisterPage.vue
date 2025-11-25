<template>
  <div class="auth-wrapper">
    
    <header class="auth-header">
      <router-link to="/" class="close-btn">
        <font-awesome-icon icon="fas fa-times" />
      </router-link>
      <router-link to="/login" class="btn btn-outline" style="color: var(--color-secondary); border-color: var(--color-border);">
        ورود
      </router-link>
    </header>

    <div class="auth-content">
      <h2 class="auth-title">ایجاد حساب کاربری</h2>

      <form @submit.prevent="handleRegister" class="duo-form">
        
        <div class="input-group">
          <input 
            type="text" 
            class="duo-input" 
            placeholder="نام (نام کاربری)" 
            v-model="username" 
            required 
          />
        </div>

        <div class="input-group">
          <input 
            type="email" 
            class="duo-input" 
            placeholder="ایمیل" 
            v-model="email" 
            required 
          />
        </div>

        <div class="input-group">
          <input 
            type="password" 
            class="duo-input" 
            placeholder="رمز عبور" 
            v-model="password" 
            required 
          />
        </div>

        <div v-if="error" class="error-message text-center" style="color: var(--color-danger); margin-top: 0.5rem;">
          {{ error }}
        </div>

        <button type="submit" class="btn btn-submit" :disabled="loading">
          {{ loading ? 'در حال ساخت حساب...' : 'ایجاد حساب' }}
        </button>

      </form>

      <p class="auth-footer-text">
        با ثبت نام در AntibioticPlay، شما با <strong>شرایط</strong> و <strong>حریم خصوصی</strong> ما موافقت می‌کنید.
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
const email = ref('');
const password = ref('');
const loading = ref(false);
const error = ref(null);

const handleRegister = async () => {
  loading.value = true;
  error.value = null;
  try {
    await authStore.register(username.value, email.value, password.value);
  } catch (err) {
    error.value = 'ثبت نام ناموفق بود. ممکن است این نام کاربری قبلاً گرفته شده باشد.';
  } finally {
    loading.value = false;
  }
};
</script>