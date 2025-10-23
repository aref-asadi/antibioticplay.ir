// File: frontend/src/stores/notificationStore.js
import { defineStore } from 'pinia';

// Import images (Vite handles paths correctly)
import correctImg from '../assets/feedback_correct.jpg';
import incorrectImg from '../assets/feedback_wrong.avif';
import resultGoodImg from '../assets/result_good.jpg';
import resultBadImg from '../assets/result_bad.jpg';
import badgeDefaultIcon from '../assets/badge_default.gif'; // Optional: Add a default badge icon

export const useNotificationStore = defineStore('notification', {
  state: () => ({
    isVisible: false,
    title: '',
    message: '',
    imageSrc: null,
    badgeIcon: null, // For badge notifications specifically
  }),
  actions: {
    showNotification({ title, message, imageSrc = null, badgeIcon = null }) {
      this.title = title;
      this.message = message;
      this.imageSrc = imageSrc;
      this.badgeIcon = badgeIcon;
      this.isVisible = true;
    },
    showCorrectFeedback(customMessage = "آفرین!") {
      this.showNotification({
        title: "✅ درسته!",
        message: customMessage,
        imageSrc: correctImg,
      });
    },
    showIncorrectFeedback(customMessage = "جواب درست نبود.") {
       this.showNotification({
        title: "❌ اوه!",
        message: customMessage,
        imageSrc: incorrectImg,
      });
    },
    showGoodResult(sessionScore, totalScore) {
       this.showNotification({
        title: "🎉 عالی بود!",
        message: `شما ${sessionScore} امتیاز در این آزمون کسب کردید! امتیاز کل: ${totalScore}`,
        imageSrc: resultGoodImg,
      });
    },
    showBadResult(sessionScore, totalScore) {
       this.showNotification({
        title: "🤔 بد نبود!",
        message: `شما ${sessionScore} امتیاز کسب کردید. ادامه بده! امتیاز کل: ${totalScore}`,
        imageSrc: resultBadImg,
      });
    },
    showNewBadge(badge) {
        this.showNotification({
            title: "🏆 نشان جدید!",
            message: badge.description,
            badgeIcon: badge.icon || 'fas fa-question', // Pass FontAwesome class string
            imageSrc: null // Don't use character image for badges
        });
    },
    hideNotification() {
      this.isVisible = false;
      // Optional: Reset fields after fade out animation?
      // setTimeout(() => {
      //   this.title = ''; this.message = ''; this.imageSrc = null; this.badgeIcon = null;
      // }, 300); // Match animation duration
    },
  },
});