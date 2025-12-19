<template>
  <div class="rules-page">
    <header class="rules-header">
      <router-link to="/dashboard" class="back-btn-circle">
        <font-awesome-icon icon="fas fa-times" />
      </router-link>
      <h1>قوانین و راهنما</h1>
    </header>

    <main class="rules-content">
      
      <section class="rule-card">
        <div class="icon-box warning"><font-awesome-icon icon="fas fa-star" /></div>
        <div class="text-box">
          <h3>سیستم امتیازدهی (XP)</h3>
          <p>هر سوال به طور پیش‌فرض <strong>۱۰ تا ۲۰ امتیاز</strong> دارد. امتیاز نهایی شما ترکیبی از درستی پاسخ، سرعت و دقت است.</p>
          <div class="highlight-box">
            <font-awesome-icon icon="fas fa-exclamation-circle" />
            <span>نکته مهم: امتیاز (XP) فقط زمانی به حساب شما اضافه می‌شود که <strong>رکورد قبلی خودتان را در آن آزمون بشکنید</strong>.</span>
          </div>
          <p class="sub-text">هر ۲۰۰ امتیاز = ۱ سطح (Level) بالاتر</p>
        </div>
      </section>

      <section class="rule-card">
        <div class="icon-box info"><font-awesome-icon icon="fas fa-lock-open" /></div>
        <div class="text-box">
          <h3>مراحل و قفل‌ها</h3>
          <p>بازی به صورت زنجیره‌ای طراحی شده است. ابتدا فقط مرحله اول باز است.</p>
          <p>برای باز کردن قفل مرحله بعد، باید مرحله فعلی را با موفقیت <strong>تکمیل کنید</strong> (پاسخ دادن به تمام سوالات).</p>
        </div>
      </section>

      <section class="rule-card">
        <div class="icon-box primary"><font-awesome-icon icon="fas fa-trophy" /></div>
        <div class="text-box">
          <h3>لیگ‌های رقابتی</h3>
          <p>جایگاه شما در جدول رده‌بندی بر اساس مجموع امتیازات (XP) تعیین می‌شود:</p>
          <ul class="league-list">
            <li style="border-left-color: #cd7f32"><strong>برنز:</strong> ۰ تا ۵۰۰</li>
            <li style="border-left-color: #a0a0a0"><strong>نقره:</strong> ۵۰۱ تا ۱۰۰۰</li>
            <li style="border-left-color: #e6c200"><strong>طلا:</strong> ۱۰۰۱ تا ۲۰۰۰</li>
            <li style="border-left-color: #ce82ff"><strong>الماس:</strong> +۲۰۰۰</li>
          </ul>
        </div>
      </section>

      <section class="rule-card">
        <div class="icon-box danger"><font-awesome-icon icon="fas fa-fire" /></div>
        <div class="text-box">
          <h3>پاسخ‌های متوالی (Streak)</h3>
          <p>اگر بدون اشتباه پیش بروید، "آتش" می‌گیرید! هر ۵ پاسخ صحیح پشت سر هم، <strong>۲۰ امتیاز پاداش</strong> دارد.</p>
        </div>
      </section>

      <section class="rule-card">
        <div class="icon-box secondary"><font-awesome-icon icon="fas fa-stopwatch" /></div>
        <div class="text-box">
          <h3>پاداش سرعت</h3>
          <p>پاسخ سریع‌تر = امتیاز بیشتر:</p>
          <ul class="simple-grid">
            <li>زیر ۵ ثانیه: <span>+۵ امتیاز</span></li>
            <li>زیر ۱۰ ثانیه: <span>+۴ امتیاز</span></li>
            <li>زیر ۱۵ ثانیه: <span>+۳ امتیاز</span></li>
            <li>زیر ۲۰ ثانیه: <span>+۲ امتیاز</span></li>
          </ul>
        </div>
      </section>

      <section class="rule-card">
        <div class="icon-box success"><font-awesome-icon icon="fas fa-medal" /></div>
        <div class="text-box">
          <h3>نشان‌ها (Badges)</h3>
          <p>با رسیدن به اهداف خاص (مثل لول ۵، حفظ استریک بالا یا تکمیل یک فصل کامل)، نشان‌های افتخار دریافت می‌کنید که در پروفایل نمایش داده می‌شوند.</p>
        </div>
      </section>

    </main>
  </div>
</template>

<script setup>
import { library } from '@fortawesome/fontawesome-svg-core';
import { 
  faTimes, faStar, faTrophy, faFire, faStopwatch, faMedal, faLockOpen, faExclamationCircle 
} from '@fortawesome/free-solid-svg-icons';

library.add(faTimes, faStar, faTrophy, faFire, faStopwatch, faMedal, faLockOpen, faExclamationCircle);
</script>

<style scoped>
.rules-page { background-color: #f7f7f7; min-height: 100vh; display: flex; flex-direction: column; direction: rtl; }
.rules-header { background: white; padding: 1rem 2rem; display: flex; align-items: center; border-bottom: 2px solid #e5e5e5; position: sticky; top: 0; z-index: 10; gap: 1rem; }
.rules-header h1 { flex: 1; text-align: right; margin: 0; font-size: 1.1rem; color: #555; font-weight: 800; }
.back-btn-circle { width: 40px; height: 40px; border-radius: 50%; background: #f0f0f0; display: flex; justify-content: center; align-items: center; color: #777; text-decoration: none; transition: background 0.2s; flex-shrink: 0; }
.back-btn-circle:hover { background: #e5e5e5; }

.rules-content { padding: 1.5rem; max-width: 600px; margin: 0 auto; width: 100%; box-sizing: border-box; display: flex; flex-direction: column; gap: 1rem; }

.rule-card { background: white; border: 2px solid #e5e5e5; border-radius: 16px; padding: 1.2rem; display: flex; gap: 1rem; align-items: flex-start; transition: transform 0.2s; }
.rule-card:hover { transform: translateY(-2px); border-color: #ddd; box-shadow: 0 4px 10px rgba(0,0,0,0.03); }

.icon-box { width: 45px; height: 45px; flex-shrink: 0; display: flex; justify-content: center; align-items: center; font-size: 1.3rem; border-radius: 12px; }
.icon-box.warning { background: #fff5d1; color: var(--color-warning); }
.icon-box.primary { background: #d7ffb8; color: var(--color-primary); }
.icon-box.danger { background: #ffdfe0; color: var(--color-danger); }
.icon-box.secondary { background: #ddf4ff; color: var(--color-secondary); }
.icon-box.info { background: #e3f2fd; color: #2196f3; }
.icon-box.success { background: #e0f2f1; color: #009688; }

.text-box { flex: 1; }
.text-box h3 { margin: 0 0 0.4rem 0; color: var(--color-text); font-size: 1rem; font-weight: 800; }
.text-box p { margin: 0; color: var(--color-text-light); line-height: 1.7; font-size: 0.9rem; }

/* استایل باکس نکته */
.highlight-box {
  background-color: #fff8e1;
  border: 1px dashed #ffb300;
  border-radius: 8px;
  padding: 0.8rem;
  margin: 0.8rem 0;
  display: flex;
  gap: 0.5rem;
  align-items: flex-start;
  font-size: 0.85rem;
  color: #8d6e63;
}

.sub-text { display: block; margin-top: 0.5rem !important; font-size: 0.85rem !important; opacity: 0.8; border-top: 1px dashed #eee; padding-top: 0.5rem; font-weight: bold; color: var(--color-primary-dark) !important; }

/* لیست لیگ‌ها */
.league-list { list-style: none; padding: 0; margin: 0.8rem 0 0 0; display: flex; flex-direction: column; gap: 0.4rem; }
.league-list li { padding-right: 0.8rem; border-right: 4px solid #ccc; font-size: 0.85rem; color: #555; }

/* لیست شبکه‌ای برای سرعت */
.simple-grid { 
  list-style: none; padding: 0; margin: 0.5rem 0 0 0; 
  display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; 
}
.simple-grid li { 
  background: #f9f9f9; padding: 0.4rem 0.8rem; border-radius: 6px; 
  font-size: 0.85rem; display: flex; justify-content: space-between; 
}
.simple-grid li span { font-weight: bold; color: var(--color-primary); }
</style>