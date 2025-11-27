import apiClient from './api';

export default {
  toggleBookmark(quizId, questionId) {
    return apiClient.post('/bookmarks/', {
      quizId,
      questionId
    });
  },

  getBookmarkedQuestions() {
    return apiClient.get('/bookmarks/list');
  }
};