<template>
  <div class="register-container">
    <h2>ثبت نام در antibioticplay.ir</h2>
    <form @submit.prevent="handleRegister">
      <div class="form-group">
        <label for="username">نام کاربری</label>
        <input type="text" id="username" v-model="username" required />
      </div>
       <div class="form-group">
        <label for="email">ایمیل</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div class="form-group">
        <label for="password">رمز عبور</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <div v-if="error" class="error-message">{{ error }}</div>
      <button type="submit" :disabled="loading">
        {{ loading ? 'در حال ثبت نام...' : 'ثبت نام' }}
      </button>
    </form>
    <p class="login-link">
        قبلاً ثبت نام کرده‌اید؟ <router-link to="/login">وارد شوید</router-link>
    </p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '../stores/auth';

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
    // هدایت به داشبورد بعد از لاگین خودکار انجام می‌شود
  } catch (err) {
    error.value = 'ثبت نام ناموفق بود. این نام کاربری یا ایمیل ممکن است قبلاً استفاده شده باشد.';
    console.error(err);
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
/* استایل‌ها مشابه صفحه ورود هستند و می‌توان آن‌ها را در یک فایل مشترک قرار داد */
.register-container {
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
.login-link {
    margin-top: 1.5rem;
    font-size: 0.9rem;
}
</style>