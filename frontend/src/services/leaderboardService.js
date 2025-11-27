import apiClient from './api';

export default {
  /**
   * دریافت جدول امتیازات بر اساس لیگ
   * @param {string} league - 'bronze', 'silver', 'gold', 'diamond'
   */
  getLeaderboard(league = 'diamond') {
    return apiClient.get(`/leaderboard/?league=${league}`);
  },
};