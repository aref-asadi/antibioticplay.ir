<template>
  <div class="page-container center-content">
    <div class="card contact-card">
      <router-link to="/" class="close-icon"><font-awesome-icon icon="fas fa-times" /></router-link>
      <h1>تماس با ما</h1>
      <p>برای هرگونه سوال، پیشنهاد یا گزارش مشکل می‌توانید با ایمیل زیر در ارتباط باشید:</p>
      <div class="email-box">
        <font-awesome-icon icon="fas fa-envelope" />
        <a href="mailto:support@antibioticplay.ir">support@antibioticplay.ir</a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { library } from '@fortawesome/fontawesome-svg-core';
import { faEnvelope, faTimes } from '@fortawesome/free-solid-svg-icons';
library.add(faEnvelope, faTimes);
</script>

<style scoped>
.page-container { min-height: 80vh; display: flex; align-items: center; justify-content: center; padding: 1rem; }
.contact-card { text-align: center; max-width: 500px; width: 100%; position: relative; padding-top: 2.5rem; }
.close-icon { position: absolute; top: 1rem; right: 1rem; color: var(--color-text-light); font-size: 1.2rem; }
.email-box { background: var(--color-secondary-light); padding: 1rem; border-radius: 12px; display: flex; align-items: center; justify-content: center; gap: 0.5rem; margin-top: 1.5rem; color: var(--color-secondary); font-weight: bold; }
.email-box a { color: var(--color-secondary); direction: ltr; }
</style>