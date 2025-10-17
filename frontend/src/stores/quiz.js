// File: frontend/src/stores/quiz.js

import { defineStore } from 'pinia';
import quizService from '../services/quizService';

export const useQuizStore = defineStore('quiz', {
  state: () => ({
    modules: [], // آرایه‌ای برای نگهداری لیست ماژول‌های آزمون
    currentQuiz: null, // برای نگهداری سوالات آزمون فعلی
    loading: false,
    error: null,
  }),

  actions: {
    async fetchModules() {
      this.loading = true;
      this.error = null;
      try {
        const response = await quizService.getQuizModules();
        this.modules = response.data;
      } catch (err) {
        this.error = 'خطا در دریافت لیست آزمون‌ها.';
        console.error(err);
      } finally {
        this.loading = false;
      }
    },
    async fetchQuizDetails(quizId) {
      this.loading = true;
      this.error = null;
      this.currentQuiz = null;
      try {
        const response = await quizService.getQuizDetails(quizId);
        this.currentQuiz = response.data;
      } catch (err) {
        this.error = 'خطا در دریافت سوالات آزمون.';
        console.error(err);
      } finally {
        this.loading = false;
      }
    },
  },
});