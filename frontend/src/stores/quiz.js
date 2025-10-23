import { defineStore } from 'pinia';
import quizService from '../services/quizService';
import { useNotificationStore } from './notificationStore';

export const useQuizStore = defineStore('quiz', {
  state: () => ({
    modules: [],
    currentQuiz: null,
    loading: false,
    error: null,
    currentSessionScore: 0,
    lastSubmissionResult: null,
    newlyEarnedBadges: [],
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
        this.currentSessionScore = 0;
        this.lastSubmissionResult = null;
        this.newlyEarnedBadges = [];
        const response = await quizService.getQuizDetails(quizId);
        this.currentQuiz = response.data;
      } catch (err) {
        this.error = 'خطا در دریافت سوالات آزمون.';
        console.error(err);
      } finally {
        this.loading = false;
      }
    },

    async submitAnswer(quizId, questionId, answer, isLastQuestion) {
      if (!this.currentQuiz) throw new Error("No active quiz.");
      try {
        const response = await quizService.submitAnswer(quizId, questionId, answer, isLastQuestion);
        this.lastSubmissionResult = response.data;
        return response;
      } catch (error) {
        console.error("Error submitting answer:", error);
        this.lastSubmissionResult = null;
        throw error;
      }
    },

    setNewlyEarnedBadges(badges) {
      const notificationStore = useNotificationStore();
      let firstNewBadge = null;
      badges.forEach(newBadge => {
        if (!this.newlyEarnedBadges.some(existing => existing.id === newBadge.id)) {
          this.newlyEarnedBadges.push(newBadge);
          if (!firstNewBadge) {
            firstNewBadge = newBadge;
          }
        }
      });
      if (firstNewBadge) {
        // Use timeout to show badge notification slightly after feedback notification closes
        setTimeout(() => {
            notificationStore.showNewBadge(firstNewBadge);
        }, 400); // Delay slightly longer than feedback animation
      }
    },

    addSessionScore(score) {
      if(typeof score === 'number' && !isNaN(score)){
         this.currentSessionScore += score;
      } else {
         console.warn("Attempted to add non-numeric score:", score);
      }
    }
  },
});