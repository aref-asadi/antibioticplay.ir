// File: frontend/src/services/leaderboardService.js

import apiClient from './api';

export default {
  getLeaderboard() {
    // apiClient به طور خودکار توکن JWT را اضافه می‌کند
    return apiClient.get('/leaderboard/');
  },
};