<template>
  <div class="forgot-password-page">
    
    <header class="duo-header">
      <div class="header-content">
        <router-link to="/" class="logo-text">AntibioticPlay</router-link>
        <div class="header-actions">
          <router-link to="/login" class="btn btn-white">ورود</router-link>
          <router-link to="/register" class="btn btn-primary">شروع کنید</router-link>
        </div>
      </div>
    </header>

    <div class="forgot-content">
      <div class="form-container">
        <h2 class="title">فراموشی رمز عبور</h2>
        <p class="description">
          دستورالعمل‌های بازنشانی رمز عبور را به ایمیل شما ارسال خواهیم کرد.
        </p>

        <form @submit.prevent="handleSubmit" class="forgot-form">
          <div class="input-group">
            <input 
              type="email" 
              class="duo-input" 
              placeholder="ایمیل" 
              v-model="email" 
              required 
            />
          </div>

          <button type="submit" class="btn btn-submit" :disabled="loading">
            {{ loading ? 'در حال ارسال...' : 'ارسال' }}
          </button>
        </form>

        <div v-if="message" class="success-message">
          {{ message }}
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue';

const email = ref('');
const loading = ref(false);
const message = ref('');

const handleSubmit = () => {
  loading.value = true;
  message.value = '';
  
  // شبیه‌سازی درخواست به سرور (چون هنوز اندپوینت واقعی نداریم)
  setTimeout(() => {
    loading.value = false;
    message.value = `ایمیلی حاوی لینک بازنشانی به ${email.value} ارسال شد (شبیه‌سازی).`;
    email.value = ''; // پاک کردن فرم
  }, 1500);
};
</script>

<style scoped>
.forgot-password-page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: var(--color-background-page);
}

/* --- Header Styles --- */
.duo-header {
  background-color: var(--color-secondary); /* Blue */
  padding: 1rem 2rem;
  display: flex;
  justify-content: center;
}
.header-content {
  width: 100%;
  max-width: 1000px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.logo-text {
  color: white;
  font-weight: 800;
  font-size: 1.8rem;
  text-decoration: none;
}
.header-actions {
  display: flex;
  gap: 1rem;
}
.btn-white {
  background-color: white;
  color: var(--color-secondary);
  border-bottom-color: rgba(0,0,0,0.1); /* Subtle shadow */
}
.btn-white:hover {
  filter: brightness(0.95);
}

/* --- Content Styles --- */
.forgot-content {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.form-container {
  width: 100%;
  max-width: 450px;
  text-align: center;
}

.title {
  font-size: 1.8rem;
  color: var(--color-text);
  margin-bottom: 1rem;
  font-weight: 800;
}

.description {
  font-size: 1.1rem;
  color: var(--color-text-light);
  margin-bottom: 2rem;
  line-height: 1.6;
}

.forgot-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.input-group {
  width: 100%;
}

.duo-input {
  width: 100%;
  padding: 1rem;
  font-size: 1.1rem;
  background-color: #f7f7f7;
  border: 2px solid var(--color-border);
  border-radius: 16px;
  box-sizing: border-box;
  text-align: right;
  color: var(--color-text);
}
.duo-input:focus {
  outline: none;
  border-color: var(--color-secondary);
  background-color: white;
}

.btn-submit {
  background-color: var(--color-secondary);
  color: white;
  border-bottom-color: var(--color-secondary-shadow);
  width: 100%;
  font-size: 1.1rem;
  padding: 1rem;
}

.success-message {
  margin-top: 1.5rem;
  padding: 1rem;
  background-color: #d7ffb8;
  color: var(--color-primary-dark);
  border-radius: 12px;
  border: 2px solid var(--color-primary);
}
</style>