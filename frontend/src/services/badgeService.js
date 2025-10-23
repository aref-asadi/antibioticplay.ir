// File: frontend/src/services/badgeService.js

import apiClient from './api';

export default {
  /**
   * Gets the list of all possible badges.
   */
  getAllBadges() {
    return apiClient.get('/badges/all');
  },

  /**
   * Gets the list of badges earned by the current user.
   */
  getEarnedBadges() {
    return apiClient.get('/badges/earned');
  },
};