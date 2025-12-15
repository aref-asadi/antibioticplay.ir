<template>
  <div class="page-container">
    <header class="page-header">
      <router-link to="/" class="back-btn">
        <font-awesome-icon icon="fas fa-arrow-right" /> بازگشت
      </router-link>
      <h1>قوانین و مقررات</h1>
    </header>
    <div class="content-card card">
      <h3>قوانین استفاده از AntibioticPlay</h3>
      <p>۱. این پلتفرم صرفاً جهت آموزش دانشجویان داروسازی طراحی شده است.</p>
      <p>۲. محتوای علمی بر اساس منابع معتبر تهیه شده اما جایگزین رفرنس‌های اصلی دانشگاهی نیست.</p>
      <p>۳. استفاده از این پلتفرم برای مقاصد غیرآموزشی ممنوع است.</p>
      <p>۴. حفظ احترام در نظرات و پروفایل الزامی است.</p>
    </div>
  </div>
</template>

<script setup>
import { library } from '@fortawesome/fontawesome-svg-core';
import { faArrowRight } from '@fortawesome/free-solid-svg-icons';
library.add(faArrowRight);
</script>

<style scoped>
.page-container { padding: 2rem; max-width: 800px; margin: 0 auto; }
.page-header { display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem; }
.back-btn { color: var(--color-text-light); font-size: 1.2rem; }
.content-card p { margin-bottom: 1rem; line-height: 1.8; color: var(--color-text); }
</style>