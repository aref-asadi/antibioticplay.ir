<template>
  <div class="login-container">
    <h2>ورود به antibioticplay.ir</h2>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="username">نام کاربری</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div class="form-group">
        <label for="password">رمز عبور</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <div v-if="error" class="error-message">{{ error }}</div>
      <button type="submit" :disabled="loading">
        {{ loading ? 'در حال ورود...' : 'ورود' }}
      </button>
    </form>
     <p class="register-link">
        حساب کاربری ندارید؟ <router-link to="/register">ثبت نام کنید</router-link>
    </p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '../stores/auth';

// استفاده از store احراز هویت
const authStore = useAuthStore();

// متغیرهای محلی برای نگهداری مقادیر فرم
const username = ref('');
const password = ref('');
const loading = ref(false);
const error = ref(null);

const handleLogin = async () => {
  loading.value = true;
  error.value = null;
  try {
    // فراخوانی اکشن لاگین از store
    await authStore.login(username.value, password.value);
    // هدایت به صفحه بعد در خود store انجام می‌شود
  } catch (err) {
    // مدیریت خطاهای احتمالی از سمت سرور
    error.value = 'نام کاربری یا رمز عبور نامعتبر است.';
    console.error(err);
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 50px auto;
  padding: 2rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
.form-group {
  margin-bottom: 1rem;
  text-align: right;
}
label {
  display: block;
  margin-bottom: 0.5rem;
}
input {
  width: 100%;
  padding: 0.5rem;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 4px;
}
button {
  width: 100%;
  padding: 0.75rem;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
}
button:disabled {
  background-color: #a5d6c1;
}
.error-message {
    color: #e74c3c;
    margin-bottom: 1rem;
}
.register-link {
    margin-top: 1.5rem;
    font-size: 0.9rem;
}
</style>