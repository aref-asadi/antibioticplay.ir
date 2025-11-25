<template>
  <Transition name="fade-bounce">
    <div v-if="notificationStore.isVisible" class="notification-overlay" @click="close">
      <div class="notification-card">
        <h2>{{ notificationStore.title }}</h2>

        <img v-if="notificationStore.imageSrc" :src="notificationStore.imageSrc" class="notification-image" alt="Notification Image"/>
        <font-awesome-icon v-else-if="notificationStore.badgeIcon" :icon="badgeIconArray" class="badge-icon-large" />

        <p class="notification-message">{{ notificationStore.message }}</p>
        <button @click="close" class="close-button btn-primary">ادامه</button>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { computed } from 'vue';
import { useNotificationStore } from '../stores/notificationStore';

const notificationStore = useNotificationStore();

const badgeIconArray = computed(() => {
  const iconString = notificationStore.badgeIcon || 'fas fa-question';
  return iconString.split(' ');
});

const close = () => {
  notificationStore.hideNotification();
};
</script>

<style scoped>

.notification-overlay {
  position: fixed; inset: 0; background-color: rgba(0, 0, 0, 0.6);
  display: flex; align-items: center; justify-content: center;
  z-index: 1000; direction: rtl;
}
.notification-card {
  background-color: var(--color-background-light); padding: 2rem 3rem; border-radius: 16px;
  text-align: center; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2); max-width: 400px;
  width: 90%; border: 2px solid var(--color-border); border-bottom-width: 4px;
}
.notification-card h2 { color: var(--color-text); margin-bottom: 1rem; font-size: 1.8rem; } /* Adjusted color/size */
.notification-image { max-width: 150px; height: auto; margin-bottom: 1rem; } /* Style for character image */
.badge-icon-large { font-size: 5rem; color: var(--color-warning); margin-bottom: 1rem; } /* Keep badge icon style */
.notification-message { color: var(--color-text-light); margin-bottom: 2rem; font-size: 1.1rem; line-height: 1.7; }
.close-button { min-width: 120px; }

/* --- Transition Animations --- */
.fade-bounce-enter-active { animation: fadeBounceIn 0.4s ease-out; }
.fade-bounce-leave-active { animation: fadeBounceOut 0.3s ease-in; }
@keyframes fadeBounceIn { /* ... */ from { opacity: 0; transform: translateY(20px) scale(0.9); } to { opacity: 1; transform: translateY(0) scale(1); } }
@keyframes fadeBounceOut { /* ... */ from { opacity: 1; transform: scale(1); } to { opacity: 0; transform: scale(0.95); } }
</style>