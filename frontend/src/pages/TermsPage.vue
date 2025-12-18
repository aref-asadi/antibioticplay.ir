<template>
  <div class="page-container">
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
          <p>
            ما به حریم خصوصی شما احترام می‌گذاریم. اطلاعات ثبت‌نامی شما (مانند ایمیل و نام کاربری) صرفاً برای ذخیره پیشرفت تحصیلی، امتیازات و رتبه‌بندی در لیدربورد استفاده می‌شود و در اختیار شخص ثالث قرار نمی‌گیرد.
          </p>
        </div>

        <div class="term-section">
          <h2>۳. حقوق مالکیت فکری</h2>
          <p>
            تمامی محتوای علمی، سوالات، طراحی‌ها و کدهای این وب‌سایت متعلق به تیم توسعه‌دهنده AntibioticPlay و دانشگاه علوم پزشکی البرز است. هرگونه کپی‌برداری کلی یا جزئی بدون اجازه کتبی ممنوع است.
          </p>
        </div>

        <div class="term-section">
          <h2>۴. رفتار کاربران</h2>
          <p>
            هدف ما ایجاد محیطی سالم برای یادگیری است. هرگونه تلاش برای تقلب در آزمون‌ها، دستکاری در امتیازات یا ایجاد اختلال در عملکرد سایت منجر به مسدود شدن حساب کاربری خواهد شد.
          </p>
        </div>

        <div class="agreement-box">
          <font-awesome-icon icon="fas fa-check-circle" class="check-icon" />
          <p>استفاده شما از این وب‌سایت به منزله پذیرش تمامی قوانین فوق است.</p>
        </div>
      </div>

      <div class="actions">
        <router-link to="/" class="btn btn-primary">بازگشت به خانه</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { library } from '@fortawesome/fontawesome-svg-core';
import { faScroll, faCheckCircle } from '@fortawesome/free-solid-svg-icons';
library.add(faScroll, faCheckCircle);
</script>

<style scoped>
.page-container {
  min-height: 100vh;
  background-color: #f1f5f9;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding: 8rem 1.5rem 4rem;
}

.terms-card {
  background: white;
  max-width: 800px;
  width: 100%;
  border-radius: 20px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.06);
  overflow: hidden;
}

.terms-header {
  background: linear-gradient(135deg, var(--color-primary) 0%, #34d399 100%);
  color: white;
  padding: 3rem 2rem;
  text-align: center;
}

.header-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
  opacity: 0.9;
}

.terms-header h1 {
  margin: 0;
  font-size: 2rem;
  font-weight: 800;
}

.last-updated {
  opacity: 0.8;
  font-size: 0.9rem;
  margin-top: 0.5rem;
}

.terms-content {
  padding: 3rem;
}

.term-section {
  margin-bottom: 3rem;
}

.term-section h2 {
  color: #1e293b;
  font-size: 1.3rem;
  border-right: 4px solid var(--color-primary);
  padding-right: 1rem;
  margin-bottom: 1rem;
}

.term-section p {
  color: #475569;
  line-height: 1.8;
  text-align: justify;
}

.warning-list {
  background-color: #fff1f2;
  border-right: 4px solid #f43f5e;
  padding: 1.5rem 2rem 1.5rem 1rem;
  margin-top: 1rem;
  border-radius: 8px 0 0 8px;
  list-style-type: disc;
  color: #881337;
}

.warning-list li {
  margin-bottom: 0.5rem;
}

.agreement-box {
  background-color: #f0fdf4;
  border: 2px dashed #86efac;
  border-radius: 12px;
  padding: 1.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  margin-top: 2rem;
  color: #166534;
  font-weight: bold;
}

.check-icon {
  font-size: 1.5rem;
}

.actions {
  padding: 0 3rem 3rem;
  text-align: center;
}

.btn-primary {
  padding: 0.8rem 2.5rem;
  border-radius: 10px;
  font-size: 1rem;
}

@media (max-width: 600px) {
  .terms-content {
    padding: 2rem 1.5rem;
  }
}
</style>