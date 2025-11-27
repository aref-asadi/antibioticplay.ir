import { defineStore } from 'pinia';
import bookmarkService from '../services/bookmarkService';
import { useAuthStore } from './auth';

export const useBookmarkStore = defineStore('bookmark', {
  state: () => ({
    loading: false,
    reviewQuestions: [],
  }),

  actions: {
    async toggleBookmark(quizId, questionId) {
      const authStore = useAuthStore();
      try {
        const response = await bookmarkService.toggleBookmark(quizId, questionId);
        
        if (authStore.user) {
          authStore.user.bookmarks = response.data.bookmarks;
          localStorage.setItem('user', JSON.stringify(authStore.user));
        }
        
        return response.data.action;
      } catch (error) {
        console.error('Bookmark toggle failed:', error);
        throw error;
      }
    },

    async fetchReviewItems() {
      this.loading = true;
      try {
        const response = await bookmarkService.getBookmarkedQuestions();
        this.reviewQuestions = response.data;
      } catch (error) {
        console.error('Failed to fetch bookmarks:', error);
      } finally {
        this.loading = false;
      }
    },
    
    isBookmarked(quizId, questionId) {
      const authStore = useAuthStore();
      if (!authStore.user || !authStore.user.bookmarks) return false;
      
      return authStore.user.bookmarks.some(
        b => b.quiz_id === quizId && b.question_id === questionId
      );
    }
  },
});