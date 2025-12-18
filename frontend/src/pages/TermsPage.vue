<template>
  <div class="page-container">
    
    <button @click="$router.go(-1)" class="back-button" title="بازگشت">
      <font-awesome-icon icon="fas fa-arrow-right" />
    </button>

    <div class="terms-card">
      <header class="terms-header">
        <font-awesome-icon icon="fas fa-scroll" class="header-icon" />
        <h1>قوانین و مقررات</h1>
        <p class="last-updated">آخرین بروزرسانی: ۱۴۰۳</p>
      </header>
      
      <div class="terms-content">
        <div class="term-section">
          <h2>۱. سلب مسئولیت پزشکی (بسیار مهم)</h2>
          <p>
            محتوای ارائه شده در AntibioticPlay صرفاً جنبه <strong>آموزشی و کمک‌درسی</strong> دارد. 
            این اطلاعات نباید به عنوان جایگزین مشاوره حرفه‌ای پزشکی، تشخیص یا درمان در نظر گرفته شود.
          </p>
          <ul class="warning-list">
            <li>دوزهای دارویی ممکن است بر اساس رفرنس‌های مختلف متفاوت باشد.</li>
            <li>برای درمان بیماران واقعی، همواره به آخرین دستورالعمل‌های بالینی (Guidelines) و منابع معتبر رسمی مراجعه کنید.</li>
            <li>ما هیچ مسئولیتی در قبال تصمیمات بالینی اتخاذ شده بر اساس محتوای این نرم‌افزار نداریم.</li>
          </ul>
        </div>
        
        <div class="term-section">
          <h2>۲. حریم خصوصی کاربران</h2>
          <p>ما به حریم خصوصی شما احترام می‌گذاریم. اطلاعات ثبت‌نامی شما صرفاً برای ذخیره پیشرفت تحصیلی استفاده می‌شود.</p>
        </div>

        <div class="term-section">
          <h2>۳. حقوق مالکیت فکری</h2>
          <p>تمامی محتوای علمی و کدهای این وب‌سایت متعلق به تیم توسعه‌دهنده AntibioticPlay و دانشگاه علوم پزشکی البرز است.</p>
        </div>

        <div class="agreement-box">
          <font-awesome-icon icon="fas fa-check-circle" class="check-icon" />
          <p>استفاده شما از این وب‌سایت به منزله پذیرش تمامی قوانین فوق است.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { library } from '@fortawesome/fontawesome-svg-core';
import { faScroll, faCheckCircle, faArrowRight } from '@fortawesome/free-solid-svg-icons';
library.add(faScroll, faCheckCircle, faArrowRight);
</script>

<style scoped>
.page-container {
  min-height: 100vh;
  background-color: #f1f5f9;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding: 6rem 1.5rem 4rem;
  position: relative;
}

/* Back Button Circle Fix */
.back-button {
  position: fixed;
  top: 2rem;
  right: 2rem;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: white;
  border: none;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  color: var(--color-primary);
  font-size: 1.2rem;
  cursor: pointer;
  z-index: 1000;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
  aspect-ratio: 1;
}

.back-button:hover {
  transform: translateX(5px);
  background: var(--color-primary);
  color: white;
  box-shadow: 0 6px 20px rgba(66, 185, 131, 0.3);
}

.terms-card { background: white; max-width: 800px; width: 100%; border-radius: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.06); overflow: hidden; }
.terms-header { background: linear-gradient(135deg, var(--color-primary) 0%, #34d399 100%); color: white; padding: 3rem 2rem; text-align: center; }
.header-icon { font-size: 3rem; margin-bottom: 1rem; opacity: 0.9; }
.terms-header h1 { margin: 0; font-size: 2rem; font-weight: 800; }
.last-updated { opacity: 0.8; font-size: 0.9rem; margin-top: 0.5rem; }
.terms-content { padding: 3rem; }
.term-section { margin-bottom: 3rem; }
.term-section h2 { color: #1e293b; font-size: 1.3rem; border-right: 4px solid var(--color-primary); padding-right: 1rem; margin-bottom: 1rem; }
.term-section p { color: #475569; line-height: 1.8; text-align: justify; }
.warning-list { background-color: #fff1f2; border-right: 4px solid #f43f5e; padding: 1.5rem 2rem 1.5rem 1rem; margin-top: 1rem; border-radius: 8px 0 0 8px; list-style-type: disc; color: #881337; }
.agreement-box { background-color: #f0fdf4; border: 2px dashed #86efac; border-radius: 12px; padding: 1.5rem; display: flex; align-items: center; justify-content: center; gap: 1rem; margin-top: 2rem; color: #166534; font-weight: bold; }

@media (max-width: 600px) {
  .terms-content { padding: 2rem 1.5rem; }
  .back-button { top: 1rem; right: 1rem; width: 40px; height: 40px; font-size: 1rem; }
}
</style>