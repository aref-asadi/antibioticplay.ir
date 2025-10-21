// File: frontend/src/services/quizService.js

import apiClient from './api';

export default {
  /**
   * لیست تمام ماژول‌های آزمون را دریافت می‌کند.
   */
  getQuizModules() {
    return apiClient.get('/quizzes/');
  },

  /**
   * جزئیات و سوالات یک ماژول خاص را بر اساس ID دریافت می‌کند.
   * @param {string} quizId - شناسه ماژول آزمون (e.g., 'classification-structure')
   */
  getQuizDetails(quizId) {
    return apiClient.get(`/quizzes/${quizId}`);
  },

  submitAnswer(quizId, questionId, answer) {
    return apiClient.post('/quizzes/submit', {
      quizId: quizId,
      questionId: questionId,
      answer: answer,
    });
  },
};