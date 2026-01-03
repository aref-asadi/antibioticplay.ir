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
        
        <div style="display: flex; gap: 1rem;">
          <div class="input-group">
            <input 
              type="text" 
              class="duo-input" 
              placeholder="نام" 
              v-model="firstName" 
              required 
            />
          </div>
          <div class="input-group">
            <input 
              type="text" 
              class="duo-input" 
              placeholder="نام خانوادگی" 
              v-model="lastName" 
              required 
            />
          </div>
        </div>

        <div class="input-group">
          <input 
            type="text" 
            class="duo-input" 
            placeholder="نام کاربری (انگلیسی)" 
            v-model="username" 
            required 
            dir="ltr"
          />
        </div>

        <div class="input-group">
          <input 
            type="email" 
            class="duo-input" 
            placeholder="ایمیل" 
            v-model="email" 
            required 
            dir="ltr"
          />
        </div>

        <div class="input-group">
          <input 
            type="password" 
            class="duo-input" 
            placeholder="رمز عبور" 
            v-model="password" 
            required 
            dir="ltr"
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
const firstName = ref('');
const lastName = ref('');
const username = ref('');
const email = ref('');
const password = ref('');
const loading = ref(false);
const error = ref(null);

const handleRegister = async () => {
  loading.value = true;
  error.value = null;
  try {
    await authStore.register(username.value, email.value, password.value, firstName.value, lastName.value);
  } catch (err) {
    if (err.response && err.response.status === 409) {
       error.value = 'این نام کاربری یا ایمیل قبلاً ثبت شده است.';
    } else {
       error.value = 'خطا در برقراری ارتباط با سرور.';
    }
  } finally {
    loading.value = false;
  }
};
</script>