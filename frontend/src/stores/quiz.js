// File: frontend/src/stores/quiz.js

import { defineStore } from 'pinia';
import quizService from '../services/quizService';

export const useQuizStore = defineStore('quiz', {
  // 1. State
  state: () => ({
    modules: [], // لیست ماژول‌های آزمون
    currentQuiz: null, // آبجکت کامل آزمون فعلی (شامل سوالات)
    loading: false,
    error: null,
    currentSessionScore: 0,
    lastSubmissionResult: null,
  }),

  // 2. Actions
  actions: {
    /**
     * دریافت لیست تمام ماژول‌های آزمون از سرور.
     */
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

    /**
     * دریافت جزئیات و سوالات یک ماژول آزمون خاص.
     */
    async fetchQuizDetails(quizId) {
      this.loading = true;
      this.error = null;
      this.currentQuiz = null;
      try {
        this.currentSessionScore = 0;
        this.lastSubmissionResult = null;
        const response = await quizService.getQuizDetails(quizId);
        this.currentQuiz = response.data;
      } catch (err) {
        this.error = 'خطا در دریافت سوالات آزمون.';
        console.error(err);
      } finally {
        this.loading = false;
      }
    },

    /**
     * ارسال پاسخ کاربر به سرور و برگرداندن نتیجه (بازخورد و امتیاز).
     */
    async submitAnswer(quizId, questionId, answer) {
      if (!this.currentQuiz) throw new Error("No active quiz.");
      try {
        const response = await quizService.submitAnswer(quizId, questionId, answer);
        // --- *** بخش آپدیت شده *** ---
        // نتیجه کامل رو در store ذخیره می‌کنیم
        this.lastSubmissionResult = response.data;
        return response; 
      } catch (error) {
        console.error("Error submitting answer:", error);
        this.lastSubmissionResult = null;
        throw error;
      }
    },
  },
});