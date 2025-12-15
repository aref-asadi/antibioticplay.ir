<template>
  <div class="page-container">
    <header class="page-header">
      <router-link to="/" class="back-btn"><font-awesome-icon icon="fas fa-arrow-right" /></router-link>
      <h1>درباره ما</h1>
    </header>
    
    <div class="content-card card mb-4">
      <h3>درباره پلتفرم</h3>
      <p>AntibioticPlay یک پلتفرم گیمیفیکیشن آموزشی است که با هدف تسهیل یادگیری مباحث پیچیده آنتی‌بیوتیک‌ها برای دانشجویان داروسازی طراحی شده است.</p>
    </div>

    <h2 class="text-center mb-2">تیم ما</h2>
    <div class="team-grid">
      <div class="team-card card">
        <div class="avatar-placeholder bg-blue">A</div>
        <h3>عارف اسدی</h3>
        <p class="role">توسعه‌دهنده</p>
        <p class="bio">علاقمند به برنامه‌نویسی و آموزش پزشکی.</p>
      </div>
      <div class="team-card card">
        <div class="avatar-placeholder bg-teal">M</div>
        <h3>عضو دوم</h3>
        <p class="role">محتوا</p>
        <p class="bio">دانشجوی داروسازی و طراح سوالات.</p>
      </div>
      <div class="team-card card">
        <div class="avatar-placeholder bg-red">S</div>
        <h3>عضو سوم</h3>
        <p class="role">گرافیک</p>
        <p class="bio">طراح رابط کاربری و تجربه کاربری.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { library } from '@fortawesome/fontawesome-svg-core';
import { faArrowRight } from '@fortawesome/free-solid-svg-icons';
library.add(faArrowRight);
</script>

<style scoped>
.page-container { padding: 2rem; max-width: 900px; margin: 0 auto; }
.page-header { display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem; }
.back-btn { color: var(--color-text-light); font-size: 1.2rem; }
.mb-4 { margin-bottom: 2rem; }
.mb-2 { margin-bottom: 1rem; }
.team-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; }
.team-card { text-align: center; display: flex; flex-direction: column; align-items: center; }
.avatar-placeholder { width: 80px; height: 80px; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-size: 2rem; color: white; font-weight: bold; margin-bottom: 1rem; }
.bg-blue { background-color: var(--color-secondary); }
.bg-teal { background-color: var(--color-primary); }
.bg-red { background-color: var(--color-danger); }
.role { color: var(--color-secondary); font-weight: bold; font-size: 0.9rem; margin-bottom: 0.5rem; }
.bio { font-size: 0.9rem; color: var(--color-text-light); }
</style>