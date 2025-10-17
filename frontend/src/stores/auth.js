// File: frontend/src/stores/auth.js

import { defineStore } from 'pinia';
import authService from '../services/authService'; // <-- ایمپورت جدید
import router from '../router'; // <-- ایمپورت روتر برای هدایت کاربر

export const useAuthStore = defineStore('auth', {
  // state: user رو به null تغییر می‌دیم چون اطلاعات کامل بعداً میاد
  state: () => ({
    token: localStorage.getItem('token') || null,
    user: JSON.parse(localStorage.getItem('user')) || null,
    returnUrl: null,
  }),

  getters: {
    isAuthenticated: (state) => !!state.token,
  },

  actions: {
    async fetchUser() {
      try {
        const response = await authService.getProfile();
        this.user = response.data; // ذخیره آبجکت کامل کاربر
        localStorage.setItem('user', JSON.stringify(this.user));
      } catch (error) {
        console.error('Failed to fetch user profile:', error);
        // اگر توکن معتبر نباشه، کاربر رو خارج می‌کنیم
        this.logout();
      }
    },

    async login(username, password) {
      try {
        const response = await authService.login(username, password);
        this.token = response.data.access_token;
        localStorage.setItem('token', response.data.access_token);

        // بلافاصله بعد از لاگین، اطلاعات پروفایل رو دریافت می‌کنیم
        await this.fetchUser();

        router.push(this.returnUrl || '/dashboard');
      } catch (error) {
        console.error('Login failed:', error);
        throw error;
      }
    },

    async register(username, email, password) {
      try {
        // فراخوانی سرویس ثبت نام
        await authService.register(username, email, password);

        // پس از ثبت نام موفق، کاربر را به طور خودکار لاگین می‌کنیم
        await this.login(username, password);

      } catch (error) {
        console.error('Registration failed:', error);
        throw error; // خطا را پرتاب می‌کنیم تا کامپوننت آن را مدیریت کند
      }
    },

    logout() {
      this.token = null;
      this.user = null;
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      router.push('/login'); // هدایت کاربر به صفحه ورود
    },
  },
});