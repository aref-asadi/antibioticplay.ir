// File: frontend/src/stores/auth.js

import { defineStore } from 'pinia';
import authService from '../services/authService';
import router from '../router';

export const useAuthStore = defineStore('auth', {
  // 1. State: داده‌های مرکزی
  state: () => ({
    // توکن و کاربر را از حافظه محلی می‌خوانیم تا لاگین ماندگار باشد
    token: localStorage.getItem('token') || null,
    user: JSON.parse(localStorage.getItem('user')) || null,
    returnUrl: null, // برای هدایت کاربر بعد از لاگین
  }),

  // 2. Getters: مقادیر مشتق‌شده
  getters: {
    isAuthenticated: (state) => !!state.token,
    username: (state) => state.user?.username,
    score: (state) => state.user?.score || 0,
    level: (state) => state.user?.level || 1,
  },

  // 3. Actions: توابعی که state را تغییر می‌دهند
  actions: {
    /**
     * دریافت اطلاعات کامل کاربر از سرور و ذخیره آن.
     */
    async fetchUser() {
      try {
        const response = await authService.getProfile();
        this.user = response.data; // ذخیره آبجکت کامل کاربر
        localStorage.setItem('user', JSON.stringify(this.user));
      } catch (error) {
        console.error('Failed to fetch user profile:', error);
        // اگر توکن معتبر نباشد (مثلا منقضی شده)، کاربر را خارج می‌کنیم
        this.logout();
      }
    },

    /**
     * لاگین کردن کاربر، دریافت توکن و سپس دریافت اطلاعات پروفایل.
     */
    async login(username, password) {
      try {
        const response = await authService.login(username, password);
        
        this.token = response.data.access_token;
        localStorage.setItem('token', response.data.access_token);
        
        // بلافاصله بعد از لاگین، اطلاعات کامل پروفایل را دریافت می‌کنیم
        await this.fetchUser();

        // هدایت کاربر به صفحه داشبورد
        router.push(this.returnUrl || '/dashboard');
        
      } catch (error) {
        console.error('Login failed:', error);
        throw error; // خطا را پرتاب می‌کنیم تا کامپوننت بتواند آن را نمایش دهد
      }
    },

    /**
     * ثبت نام کاربر جدید و سپس لاگین خودکار.
     */
    async register(username, email, password) {
      try {
        await authService.register(username, email, password);
        // پس از ثبت نام موفق، کاربر را به طور خودکار لاگین می‌کنیم
        await this.login(username, password);
      } catch (error) {
        console.error('Registration failed:', error);
        throw error;
      }
    },

    /**
     * خروج کاربر از سیستم.
     */
    logout() {
      this.token = null;
      this.user = null;
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      router.push('/login');
    },

    /**
     * آپدیت آنی امتیاز کاربر در state و حافظه محلی.
     */
    updateUserScore(newScore) {
      if (this.user) {
        this.user.score = newScore;
        localStorage.setItem('user', JSON.stringify(this.user));
      }
    },

    updateUserLevel(newLevel) {
      if (this.user) {
        this.user.level = newLevel;
        // user رو دوباره در localStorage ذخیره می‌کنیم تا سطح جدید هم ثبت بشه
        localStorage.setItem('user', JSON.stringify(this.user));
      }
    },
  },
});