<template>
  <Transition name="fade-bounce">
    <div v-if="badge" class="notification-overlay" @click="closeNotification">
      <div class="notification-card">
        <h2>🏆 نشان جدید کسب شد! 🏆</h2>
        <font-awesome-icon :icon="['fas', badgeIconName]" class="badge-icon-large" />
        <h3>{{ badge.name }}</h3>
        <p>{{ badge.description }}</p>
        <button @click="closeNotification" class="close-button btn-primary">بستن</button> </div>
    </div>
  </Transition>
  </template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  badge: { type: Object, default: null }
});
const emit = defineEmits(['close']);

const badgeIconName = computed(() => {
  if (props.badge?.icon) {
    const parts = props.badge.icon.split(' ');
    return parts.length > 1 ? parts[1] : parts[0];
  }
  return 'question';
});

const closeNotification = () => {
  emit('close');
};
</script>

<style scoped>
.notification-overlay {
  position: fixed;
  inset: 0; /* Simpler top/left/right/bottom: 0 */
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  direction: rtl;
}

.notification-card {
  background-color: var(--color-background-light);
  padding: 2rem 3rem;
  border-radius: 16px;
  text-align: center;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  max-width: 400px;
  width: 90%; /* Ensure it fits smaller screens */
  border: 2px solid var(--color-border);
  border-bottom-width: 4px;
}

.notification-card h2 {
  color: var(--color-warning-dark); /* Use theme color */
  margin-bottom: 1.5rem;
}

.badge-icon-large {
  font-size: 5rem;
  color: var(--color-warning); /* Use theme color */
  margin-bottom: 1rem;
}

.notification-card h3 {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
  color: var(--color-text);
}

.notification-card p {
  color: var(--color-text-light);
  margin-bottom: 2rem;
}

/* Close button inherits from global button styles via .btn-primary */
.close-button {
  min-width: 120px; /* Ensure decent width */
}

/* --- Transition Animations --- */
/* These define how the element enters and leaves */
.fade-bounce-enter-active {
  animation: fadeBounceIn 0.4s ease-out;
}
.fade-bounce-leave-active {
  animation: fadeBounceOut 0.3s ease-in;
}

/* Keyframes define the actual animation steps */
/* (Ensure these are NOT duplicated in style.css) */
@keyframes fadeBounceIn {
  from {
    opacity: 0;
    transform: translateY(20px) scale(0.9);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}
@keyframes fadeBounceOut {
  from {
    opacity: 1;
    transform: scale(1);
  }
  to {
    opacity: 0;
    transform: scale(0.95);
  }
}
</style>