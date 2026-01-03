// File: frontend/src/services/authService.js

import apiClient from './api';

export default {
  login(username, password) {
    return apiClient.post('/auth/login', {
      username: username,
      password: password,
    });
  },
  register(username, email, password, firstName, lastName) {
    return apiClient.post('/auth/register', {
      username,
      email,
      password,
      first_name: firstName,
      last_name: lastName
    });
  },
  getProfile() {
    return apiClient.get('/auth/profile');
  },
};