// File: frontend/src/router/index.js

import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '../stores/auth';

// ما کامپوننت‌های صفحات را بعداً می‌سازیم، فعلاً فقط آنها را import می‌کنیم.
import HomePage from '../pages/HomePage.vue';
import LoginPage from '../pages/LoginPage.vue';
import RegisterPage from '../pages/RegisterPage.vue';
import ForgotPasswordPage from '../pages/ForgotPasswordPage.vue';
import DashboardPage from '../pages/DashboardPage.vue';
import QuizPage from '../pages/QuizPage.vue';
import LeaderboardPage from '../pages/LeaderboardPage.vue';
import QuizResultPage from '../pages/QuizResultPage.vue';
import RulesPage from '../pages/RulesPage.vue';
import ReviewPage from '../pages/ReviewPage.vue';
import TermsPage from '../pages/TermsPage.vue';
import AboutPage from '../pages/AboutPage.vue';
import ContactPage from '../pages/ContactPage.vue';
import FlashcardsPage from '../pages/FlashcardsPage.vue';
import ProfilePage from '../pages/ProfilePage.vue';

const routes = [
  { path: '/', name: 'Home', component: HomePage },
  { path: '/login', name: 'Login', component: LoginPage },
  { path: '/register', name: 'Register', component: RegisterPage },
  { path: '/forgot-password', name: 'ForgotPassword', component: ForgotPasswordPage },
  { path: '/dashboard', name: 'Dashboard', component: DashboardPage, meta: { requiresAuth: true } },
  { path: '/quiz/:id', name: 'Quiz', component: QuizPage, meta: { requiresAuth: true } },
  { path: '/leaderboard', name: 'Leaderboard', component: LeaderboardPage, meta: { requiresAuth: true } },
  { path: '/quiz/result', name: 'QuizResult', component: QuizResultPage, meta: { requiresAuth: true } },
  { path: '/rules', name: 'Rules', component: RulesPage, meta: { requiresAuth: true } },
  { path: '/review', name: 'Review', component: ReviewPage, meta: { requiresAuth: true } },
  { path: '/terms', name: 'Terms', component: TermsPage },
  { path: '/about', name: 'About', component: AboutPage },
  { path: '/contact', name: 'Contact', component: ContactPage },
  { path: '/flashcards', name: 'Flashcards', component: FlashcardsPage },
  { path: '/profile', name: 'Profile', component: ProfilePage, meta: { requiresAuth: true } },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } 
    return { top: 0 };
  }
});

// --- Navigation Guard ---
router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore();
  const isAuthenticated = authStore.isAuthenticated;
  const requiresAuth = to.meta.requiresAuth;

  if (requiresAuth && !isAuthenticated) {
    // اگر صفحه نیاز به لاگین داشت ولی کاربر لاگین نبود،
    // او را به صفحه ورود هدایت کن.
    authStore.returnUrl = to.fullPath;
    next('/login');
  } else if ((to.name === 'Login' || to.name === 'Register') && isAuthenticated) {
    // اگر کاربر لاگین بود و می‌خواست به صفحه ورود یا ثبت‌نام برود،
    // او را به داشبورد هدایت کن.
    next('/dashboard');
  } else {
    // در غیر این صورت، اجازه عبور بده.
    next();
  }
});
// --- End Navigation Guard ---

export default router;