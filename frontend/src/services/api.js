// File: frontend/src/services/api.js

import axios from 'axios';
import { useAuthStore } from '../stores/auth';

const apiClient = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

// --- 1. Request Interceptor (افزودن توکن به درخواست‌ها) ---
apiClient.interceptors.request.use(
  (config) => {
    const authStore = useAuthStore();
    const token = authStore.token;
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// --- 2. Response Interceptor (مدیریت خطای 401 و انقضای توکن) ---
apiClient.interceptors.response.use(
  (response) => {
    // اگر پاسخ موفقیت‌آمیز بود، آن را برگردان
    return response;
  },
  (error) => {
    const authStore = useAuthStore();
    
    // اگر خطا 401 (غیرمجاز) بود
    if (error.response && error.response.status === 401) {
      console.warn('Token expired or unauthorized. Logging out...');
      
      // فراخوانی اکشن خروج (که کاربر را به صفحه لاگین هدایت می‌کند)
      authStore.logout();
    }
    
    return Promise.reject(error);
  }
);

export default apiClient;