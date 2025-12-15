<template>
  <div class="rules-page">
    <header class="rules-header">
      <router-link to="/dashboard" class="back-btn-circle">
        <font-awesome-icon icon="fas fa-times" />
      </router-link>
      <h1>راهنمای AntibioticPlay</h1>
    </header>

    <main class="rules-content">
      
      <section class="rule-card">
        <div class="icon-box warning"><font-awesome-icon icon="fas fa-star" /></div>
        <div class="text-box">
          <h3>امتیازدهی (XP)</h3>
          <p>شما فقط زمانی امتیاز می‌گیرید که <strong>رکورد خودتان را بشکنید</strong>. تکرار یک آزمون بدون پیشرفت، امتیازی ندارد. پس سعی کنید هر بار بهتر شوید!</p>
        </div>
      </section>

      <section class="rule-card">
        <div class="icon-box primary"><font-awesome-icon icon="fas fa-trophy" /></div>
        <div class="text-box">
          <h3>لیگ‌ها</h3>
          <p>بر اساس امتیاز کل، در یکی از ۴ لیگ قرار می‌گیرید:</p>
          <ul>
            <li style="color: #cd7f32">برنز: ۰ تا ۵۰۰</li>
            <li style="color: #a0a0a0">نقره: ۵۰۱ تا ۱۰۰۰</li>
            <li style="color: #e6c200">طلا: ۱۰۰۱ تا ۲۰۰۰</li>
            <li style="color: #ce82ff">الماس: +۲۰۰۰</li>
          </ul>
        </div>
      </section>

      <section class="rule-card">
        <div class="icon-box danger"><font-awesome-icon icon="fas fa-fire" /></div>
        <div class="text-box">
          <h3>پاسخ صحیح متوالی</h3>
          <p>این عدد نشان می‌دهد چند سوال را <strong>پشت سر هم و بدون غلط</strong> جواب داده‌اید. هر ۵ جواب صحیح متوالی، ۲۰ امتیاز پاداش دارد!</p>
        </div>
      </section>

      <section class="rule-card">
        <div class="icon-box secondary"><font-awesome-icon icon="fas fa-stopwatch" /></div>
        <div class="text-box">
          <h3>پاداش سرعت</h3>
          <p>اگر زیر ۵ ثانیه به سوالی درست جواب دهید، ۵ امتیاز اضافه می‌گیرید. سرعت عمل مهم است!</p>
        </div>
      </section>

    </main>
  </div>
</template>

<script setup>
import { library } from '@fortawesome/fontawesome-svg-core';
import { faTimes, faStar, faTrophy, faFire, faStopwatch } from '@fortawesome/free-solid-svg-icons';
library.add(faTimes, faStar, faTrophy, faFire, faStopwatch);
</script>

<style scoped>
.rules-page { background-color: #f7f7f7; min-height: 100vh; display: flex; flex-direction: column; }
.rules-header { background: white; padding: 1rem 2rem; display: flex; align-items: center; border-bottom: 2px solid #e5e5e5; position: sticky; top: 0; z-index: 10; }
.rules-header h1 { flex: 1; text-align: center; margin: 0; font-size: 1.2rem; color: #aaa; text-transform: uppercase; letter-spacing: 1px; }
.back-btn-circle { width: 40px; height: 40px; border-radius: 50%; background: #f0f0f0; display: flex; justify-content: center; align-items: center; color: #777; text-decoration: none; transition: background 0.2s; }
.back-btn-circle:hover { background: #e5e5e5; }

.rules-content { padding: 2rem; max-width: 600px; margin: 0 auto; width: 100%; box-sizing: border-box; }

.rule-card { background: white; border: 2px solid #e5e5e5; border-radius: 16px; padding: 1.5rem; margin-bottom: 1.5rem; display: flex; gap: 1.5rem; align-items: flex-start; }
.icon-box { width: 50px; height: 50px; flex-shrink: 0; display: flex; justify-content: center; align-items: center; font-size: 1.5rem; border-radius: 12px; }
.icon-box.warning { background: #fff5d1; color: var(--color-warning); }
.icon-box.primary { background: #d7ffb8; color: var(--color-primary); }
.icon-box.danger { background: #ffdfe0; color: var(--color-danger); }
.icon-box.secondary { background: #ddf4ff; color: var(--color-secondary); }

.text-box h3 { margin: 0 0 0.5rem 0; color: var(--color-text); }
.text-box p { margin: 0; color: var(--color-text-light); line-height: 1.6; }
.text-box ul { padding-right: 1.2rem; margin: 0.5rem 0 0 0; color: var(--color-text-light); }
</style>