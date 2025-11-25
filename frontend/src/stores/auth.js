import { defineStore } from 'pinia';
import authService from '../services/authService';
import router from '../router';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('token') || null,
    user: JSON.parse(localStorage.getItem('user')) || null,
    returnUrl: null,
    triggerScoreAnimation: false,
    correct_streak: 0,
    quizzes_completed: 0,
  }),

  getters: {
    isAuthenticated: (state) => !!state.token,
    username: (state) => state.user?.username,
    score: (state) => state.user?.score || 0,
    level: (state) => state.user?.level || 1,
    streak: (state) => state.correct_streak,
    completedQuizzes: (state) => state.quizzes_completed,
  },

  actions: {
    async fetchUser() {
      try {
        const response = await authService.getProfile();
        this.user = response.data;
        localStorage.setItem('user', JSON.stringify(this.user));
        
        this.correct_streak = response.data.correct_streak || 0;
        this.quizzes_completed = response.data.quizzes_completed || 0;
        
      } catch (error) {
        console.error('Failed to fetch user profile:', error);
        this.logout();
      }
    },

    async login(username, password) {
      try {
        const response = await authService.login(username, password);
        this.token = response.data.access_token;
        localStorage.setItem('token', response.data.access_token);
        await this.fetchUser();
        router.push(this.returnUrl || '/dashboard');
      } catch (error) {
        console.error('Login failed:', error);
        throw error;
      }
    },

    async register(username, email, password) {
      try {
        await authService.register(username, email, password);
        await this.login(username, password);
      } catch (error) {
        console.error('Registration failed:', error);
        throw error;
      }
    },

    logout() {
      this.token = null;
      this.user = null;
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      // Reset streak and completed quizzes on logout
      this.correct_streak = 0;
      this.quizzes_completed = 0;
      router.push('/login');
    },

    updateUserScore(newScore) {
      if (this.user) {
        const oldScore = this.user.score;
        this.user.score = newScore;
        localStorage.setItem('user', JSON.stringify(this.user));
        if (newScore > oldScore) {
          this.triggerScoreAnimation = true;
        }
      }
    },

    updateUserLevel(newLevel) {
       if (this.user) {
         this.user.level = newLevel;
         localStorage.setItem('user', JSON.stringify(this.user));
       }
    },

    updateUserStreak(newStreak) {
      this.correct_streak = newStreak;
    },
    
    updateUserQuizzesCompleted(newCompleted) {
      this.quizzes_completed = newCompleted;
    },

    resetScoreAnimationTrigger() {
      this.triggerScoreAnimation = false;
    }
  },
});