import apiClient from './api';

export default {
  getQuizModules() {
    return apiClient.get('/quizzes/');
  },

  getQuizDetails(quizId) {
    return apiClient.get(`/quizzes/${quizId}`);
  },

  submitAnswer(quizId, questionId, answer, isLastQuestion, timeTaken) {
    return apiClient.post('/quizzes/submit', {
      quizId,
      questionId,
      answer,
      isLastQuestion,
      timeTaken
    });
  },
};