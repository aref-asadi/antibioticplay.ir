// File: frontend/src/services/authService.js

import apiClient from './api';

export default {
  login(username, password) {
    return apiClient.post('/auth/login', {
      username: username,
      password: password,
    });
  },
  register(username, email, password) {
    return apiClient.post('/auth/register', {
      username,
      email,
      password,
    });
  },
  getProfile() {
    return apiClient.get('/auth/profile');
  },
  // در آینده تابع گرفتن پروفایل را هم اضافه می‌کنیم
};