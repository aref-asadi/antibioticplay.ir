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
    currentQuizPossibleScore: 0,
    lastSubmissionResult: null,
    newlyEarnedBadges: [],
    pendingBadgeToShow: null,
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
        // مقداردهی امتیاز کل ممکن آزمون
        this.currentQuizPossibleScore = response.data.total_possible_score || 0; 
      } catch (err) {
        this.error = 'خطا در دریافت سوالات آزمون.';
        console.error(err);
      } finally {
        this.loading = false;
      }
    },

    async submitAnswer(quizId, questionId, answer, isLastQuestion, timeTaken) { 
      if (!this.currentQuiz) throw new Error("No active quiz.");
      try {
        const response = await quizService.submitAnswer(quizId, questionId, answer, isLastQuestion, timeTaken);
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
        this.pendingBadgeToShow = firstNewBadge;
      }
    },

    clearPendingBadge() {
        this.pendingBadgeToShow = null;
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