<template>
  <div class="home-page">
    
    <header class="landing-header">
      <div class="header-content">
        <h2 class="logo-text">AntibioticPlay</h2>
        </div>
    </header>

    <section class="hero-section">
      <div class="hero-container">
        
        <div class="hero-content">
          <div class="badge-pill">
            <span class="badge-icon">🛡️</span>
            <span>مبارزه با مقاومت میکروبی</span>
          </div>
          
          <h1 class="hero-title">
            آگاهی، خط اول دفاع در <br />
            <span class="highlight-text">دنیای آنتی‌بیوتیک‌ها</span>
          </h1>
          
          <p class="hero-subtitle">
            ما در AntibioticPlay به کادر درمان کمک می‌کنیم تا با تسلط بر اصول تجویز و فارماکولوژی، سدی محکم در برابر مقاومت میکروبی بسازند. دانش شما، نجات‌بخش آینده است.
          </p>
          
          <div class="hero-actions">
            <router-link v-if="authStore.isAuthenticated" to="/dashboard" class="btn btn-primary btn-lg">
              ورود به داشبورد
              <font-awesome-icon icon="fas fa-arrow-left" class="ms-2" />
            </router-link>
            <router-link v-else to="/login" class="btn btn-primary btn-lg">
              شروع یادگیری
              <font-awesome-icon icon="fas fa-rocket" class="ms-2" />
            </router-link>
            
            <router-link to="/about" class="btn btn-outline btn-lg">
              درباره ما
            </router-link>
          </div>

          <div class="hero-stats">
            <div class="stat-item">
              <strong>+۵</strong>
              <span>ماژول تخصصی</span>
            </div>
            <div class="stat-separator"></div>
            <div class="stat-item">
              <strong>سطح‌بندی</strong>
              <span>گیمیفیکیشن</span>
            </div>
          </div>
        </div>

        <div class="hero-image-wrapper">
          <img src="/images/hero-awareness.png" alt="Antibiotic Awareness" class="hero-img" />
          
          <div class="floating-card card-1">
            <font-awesome-icon icon="fas fa-bacteria" class="icon-germ" />
            <span>MDR Organisms</span>
          </div>
          <div class="floating-card card-2">
            <font-awesome-icon icon="fas fa-prescription-bottle-alt" class="icon-drug" />
            <span>Stewardship</span>
          </div>
        </div>

      </div>
    </section>

    <section class="legends-section">
      <h2 class="section-title">با قهرمانان آنتی‌بیوتیک آشنا شوید</h2>
      <p class="section-subtitle">شما می‌توانید یکی از این دانشمندان بزرگ را به عنوان آواتار خود انتخاب کنید!</p>
      
      <div class="legends-grid">
        <div class="legend-card">
          <img src="/avatars/avatar_fleming.png" alt="الکساندر فلمینگ" class="legend-img" />
          <div class="legend-info">
            <h3>الکساندر فلمینگ</h3>
            <span class="legend-role">کاشف پنی‌سیلین</span>
            <p>در سال ۱۹۲۸، او به طور اتفاقی متوجه شد که کپک پنی‌سیلیوم باکتری‌ها را نابود می‌کند. این کشف سرآغاز عصر آنتی‌بیوتیک‌ها بود.</p>
          </div>
        </div>

        <div class="legend-card">
          <img src="/avatars/avatar_waksman.png" alt="سلمان واکسمن" class="legend-img" />
          <div class="legend-info">
            <h3>سلمان واکسمن</h3>
            <span class="legend-role">کاشف استرپتومایسین</span>
            <p>او کاشف اولین داروی موثر علیه سل بود و برای اولین بار واژه «آنتی‌بیوتیک» را به معنای امروزی آن تعریف کرد.</p>
          </div>
        </div>

        <div class="legend-card">
          <img src="/avatars/avatar_domagk.png" alt="گرهارد دماک" class="legend-img" />
          <div class="legend-info">
            <h3>گرهارد دماک</h3>
            <span class="legend-role">کاشف سولفونامید</span>
            <p>او اولین داروی ضدباکتریایی تجاری (پرونتوسیل) را کشف کرد که توانست عفونت‌های کشنده را درمان کند و جایزه نوبل گرفت.</p>
          </div>
        </div>

        <div class="legend-card">
          <img src="/avatars/avatar_florey.png" alt="هاوارد فلوری" class="legend-img" />
          <div class="legend-info">
            <h3>هاوارد فلوری</h3>
            <span class="legend-role">توسعه تولید پنی‌سیلین</span>
            <p>او با تشکیل تیمی قدرتمند در آکسفورد، توانست پنی‌سیلین را خالص‌سازی کرده و به تولید انبوه برساند تا جان سربازان را نجات دهد.</p>
          </div>
        </div>

        <div class="legend-card">
          <img src="/avatars/avatar_hodgkin.png" alt="دوروتی هاجکین" class="legend-img" />
          <div class="legend-info">
            <h3>دوروتی هاجکین</h3>
            <span class="legend-role">تعیین ساختار پنی‌سیلین</span>
            <p>او با استفاده از کریستالوگرافی اشعه ایکس، ساختار سه بعدی پنی‌سیلین را کشف کرد که راه را برای ساخت مصنوعی آن هموار کرد.</p>
          </div>
        </div>

        <div class="legend-card">
          <img src="/avatars/avatar_bugie.png" alt="الیزابت بوگی" class="legend-img" />
          <div class="legend-info">
            <h3>الیزابت بوگی</h3>
            <span class="legend-role">همکار در کشف استرپتومایسین</span>
            <p>او یکی از اعضای کلیدی آزمایشگاه واکسمن بود و نقش اساسی در کشف استرپتومایسین ایفا کرد، اگرچه اغلب نامش کمتر شنیده شده است.</p>
          </div>
        </div>

        <div class="legend-card">
          <img src="/avatars/avatar_youyou.png" alt="تو یویو" class="legend-img" />
          <div class="legend-info">
            <h3>تو یویو</h3>
            <span class="legend-role">کاشف آرتمیسینین</span>
            <p>او با الهام از متون طب سنتی چین، دارویی حیاتی برای درمان مالاریا کشف کرد که جان میلیون‌ها نفر را در سراسر جهان نجات داده است.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="features-section">
      <h2 class="section-title">چرا یادگیری با AntibioticPlay را دوست خواهید داشت؟</h2>
      
      <div class="features-grid">
        <div class="feature-item">
          <div class="icon-wrapper">
            <font-awesome-icon icon="fas fa-fire" class="feature-icon icon-fire" />
          </div>
          <div class="feature-text">
            <h3>مؤثر و کارآمد</h3>
            <p>دوره‌های ما به شما کمک می‌کنند تا دسته‌بندی‌ها و دوزها را سریع و عمیق یاد بگیرید.</p>
          </div>
        </div>

        <div class="feature-item">
          <div class="icon-wrapper">
            <font-awesome-icon icon="fas fa-check-circle" class="feature-icon icon-check" />
          </div>
          <div class="feature-text">
            <h3>یادگیری شخصی‌سازی شده</h3>
            <p>با تست‌های هوشمند، نقاط ضعف خود را بشناسید و روی آن‌ها تمرکز کنید.</p>
          </div>
        </div>

        <div class="feature-item">
          <div class="icon-wrapper">
            <font-awesome-icon icon="fas fa-star" class="feature-icon icon-star" />
          </div>
          <div class="feature-text">
            <h3>انگیزه بگیرید</h3>
            <p>با کسب امتیاز، مدال و رقابت در لیدربورد، مطالعه را به یک عادت روزانه تبدیل کنید.</p>
          </div>
        </div>

        <div class="feature-item">
          <div class="icon-wrapper">
            <font-awesome-icon icon="fas fa-heart" class="feature-icon icon-heart" />
          </div>
          <div class="feature-text">
            <h3>سرگرم‌کننده است!</h3>
            <p>یادگیری خشک و خسته‌کننده را فراموش کنید. اینجا بازی کنید و یاد بگیرید.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="bottom-cta-section">
      <h2 class="cta-title">یادگیری داروسازی با AntibioticPlay</h2>
      <router-link to="/register" class="btn btn-primary cta-btn">
        همین حالا شروع کنید
      </router-link>
    </section>

    <footer class="main-footer">
      <div class="footer-container">
        
        <div class="footer-column">
          <h4>درباره AntibioticPlay</h4>
          <ul>
            <li><router-link to="/about">درباره ما & تیم</router-link></li>
            <li><router-link to="/terms">قوانین و مقررات</router-link></li>
            <li><router-link to="/contact">تماس با پشتیبانی</router-link></li>
          </ul>
        </div>

        <div class="footer-column">
          <h4>آموزش</h4>
          <ul>
            <li><router-link to="/register">آزمون‌ها</router-link></li>
            <li><router-link to="/flashcards">فلش‌کارت‌ها</router-link></li>
          </ul>
        </div>

        <div class="footer-column uni-logo-section">
          <h4>با حمایت</h4>
          <div class="uni-logo-box">
             <img src="/images/uni_logo.png" alt="University Logo" class="uni-logo-img" />
          </div>
        </div>

      </div>
      <div class="footer-bottom">
        <p>© 2025 AntibioticPlay. تمامی حقوق محفوظ است.</p>
      </div>
    </footer>

  </div>
</template>

<script setup>
import { useAuthStore } from '../stores/auth';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faGlobeAmericas, faFire, faCheckCircle, faStar, faHeart, faUniversity, faArrowLeft, faRocket, faBacteria, faPrescriptionBottleAlt } from '@fortawesome/free-solid-svg-icons';

library.add(faGlobeAmericas, faFire, faCheckCircle, faStar, faHeart, faUniversity, faArrowLeft, faRocket, faBacteria, faPrescriptionBottleAlt);

const authStore = useAuthStore();
</script>

<style scoped>
.home-page {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* --- Header --- */
.landing-header {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  padding: 1.5rem 2rem;
  z-index: 10;
  display: flex;
  justify-content: center; /* Center logo on desktop usually, or space-between */
}
.header-content {
  width: 100%;
  max-width: 1100px;
  display: flex;
  align-items: center;
}
.logo-text {
  color: white;
  font-weight: 800;
  font-size: 1.8rem;
  margin: 0;
  letter-spacing: 1px;
}

/* --- Hero Section --- */
.hero-section {
  background-color: var(--color-hero-bg);
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  overflow: hidden;
  padding: 4rem 1.5rem;
  min-height: 90vh; /* تمام صفحه در دسکتاپ */
}
.bg-pattern {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background-image: radial-gradient(rgba(255, 255, 255, 0.2) 2px, transparent 2px);
  background-size: 50px 50px;
  opacity: 0.5;
  pointer-events: none;
}

.hero-container {
  max-width: 1200px;
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
}

/* --- Left Side: Content --- */
.hero-content {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  z-index: 2;
}

.badge-pill {
  background-color: #e3f2fd;
  color: #1976d2;
  padding: 0.5rem 1rem;
  border-radius: 50px;
  font-size: 0.9rem;
  font-weight: bold;
  margin-bottom: 1.5rem;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}

.hero-title {
  font-size: 3rem;
  font-weight: 900;
  line-height: 1.2;
  color: #2c3e50;
  margin-bottom: 1.5rem;
}

.highlight-text {
  color: var(--color-primary); /* رنگ اصلی سایت شما */
  position: relative;
  display: inline-block;
}

.highlight-text::after {
  content: '';
  position: absolute;
  bottom: 5px;
  left: 0;
  width: 100%;
  height: 12px;
  background-color: rgba(66, 185, 131, 0.2); /* رنگ سبز کمرنگ */
  z-index: -1;
  border-radius: 4px;
}

.hero-subtitle {
  font-size: 1.15rem;
  color: #555;
  line-height: 1.8;
  margin-bottom: 2.5rem;
  max-width: 90%;
}

.hero-actions {
  display: flex;
  gap: 1rem;
  margin-bottom: 3rem;
}

.btn-lg {
  padding: 0.8rem 2rem;
  font-size: 1.1rem;
  border-radius: 12px;
}

.hero-stats {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.stat-item {
  display: flex;
  flex-direction: column;
}

.stat-item strong {
  font-size: 1.5rem;
  font-weight: 800;
  color: #2c3e50;
}

.stat-item span {
  font-size: 0.9rem;
  color: #777;
}

.stat-separator {
  width: 1px;
  height: 40px;
  background-color: #ddd;
}

/* --- Right Side: Image --- */
.hero-image-wrapper {
  position: relative;
  display: flex;
  justify-content: center;
}

.hero-img {
  width: 100%;
  max-width: 550px;
  height: auto;
  border-radius: 24px;
  /* سایه نرم برای جدا شدن از پس‌زمینه */
  filter: drop-shadow(0 20px 40px rgba(0,0,0,0.1));
  z-index: 1;
}

/* کارت‌های شناور */
.floating-card {
  position: absolute;
  background: white;
  padding: 0.8rem 1.2rem;
  border-radius: 16px;
  box-shadow: 0 10px 25px rgba(0,0,0,0.08);
  display: flex;
  align-items: center;
  gap: 0.8rem;
  font-weight: bold;
  font-size: 0.9rem;
  z-index: 2;
  animation: float 6s ease-in-out infinite;
}

.card-1 {
  top: 10%;
  left: -20px;
  animation-delay: 0s;
}

.card-2 {
  bottom: 15%;
  right: -10px;
  animation-delay: 3s;
}

.icon-germ { color: #ff4b4b; font-size: 1.2rem; }
.icon-drug { color: #58cc02; font-size: 1.2rem; }

@keyframes float {
  0% { transform: translateY(0); }
  50% { transform: translateY(-15px); }
  100% { transform: translateY(0); }
}

/* --- Responsive --- */
@media (max-width: 992px) {
  .hero-container {
    grid-template-columns: 1fr;
    text-align: center;
    gap: 3rem;
  }

  .hero-content {
    align-items: center;
  }
  
  .hero-subtitle {
    max-width: 100%;
  }

  .hero-title {
    font-size: 2.2rem;
  }
  
  .card-1 { left: 0; }
  .card-2 { right: 0; }
}

/* --- Legends Section --- */
.legends-section {
  padding: 5rem 2rem;
  background-color: #f9fbfd; /* رنگ زمینه متفاوت برای تمایز */
  text-align: center;
}
.section-subtitle {
  color: var(--color-text-light);
  margin-bottom: 3rem;
  font-size: 1.1rem;
}
.legends-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  max-width: 1100px;
  margin: 0 auto;
}
.legend-card {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 4px 15px rgba(0,0,0,0.05);
  transition: transform 0.3s ease;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}
.legend-card:hover {
  transform: translateY(-5px);
}
.legend-img {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 1rem;
  border: 3px solid var(--color-primary-light);
}
.legend-info h3 {
  color: var(--color-primary);
  margin: 0.5rem 0;
  font-size: 1.3rem;
}
.legend-role {
  display: block;
  font-size: 0.9rem;
  color: var(--color-secondary);
  font-weight: bold;
  margin-bottom: 1rem;
}
.legend-info p {
  color: var(--color-text-light);
  font-size: 0.95rem;
  line-height: 1.6;
}

/* --- Features Section --- */
.features-section { padding: 5rem 2rem; background-color: white; text-align: center; display: flex; flex-direction: column; align-items: center; }
.section-title { font-size: 2rem; color: var(--color-text); margin-bottom: 4rem; font-weight: 800; }
.features-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 3rem 4rem; max-width: 1000px; width: 100%; text-align: right; }
.feature-item { display: flex; align-items: flex-start; gap: 1.5rem; }
.icon-wrapper { flex-shrink: 0; width: 60px; display: flex; justify-content: center; }
.feature-icon { font-size: 2.5rem; }
.icon-fire { color: var(--color-danger); }
.icon-check { color: var(--color-primary); }
.icon-star { color: var(--color-warning); }
.icon-heart { color: var(--color-secondary); }
.feature-text h3 { margin: 0 0 0.5rem 0; font-size: 1.4rem; color: var(--color-text); }
.feature-text p { margin: 0; color: var(--color-text-light); line-height: 1.6; font-size: 1.1rem; }

/* --- Bottom CTA Section --- */
.bottom-cta-section {
  background-color: var(--color-hero-bg); /* Same as hero */
  padding: 4rem 2rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.cta-title {
  color: white;
  font-size: 2rem;
  margin-bottom: 2rem;
  font-weight: 800;
}
.cta-btn {
  min-width: 250px;
  font-size: 1.2rem;
  padding: 1rem 2rem;
}

/* --- Footer --- */
.main-footer {
  background-color: #1a202c; /* رنگ تیره (سرمه‌ای/مشکی) برای کنتراست بهتر */
  color: rgba(255, 255, 255, 0.8);
  padding: 4rem 2rem 2rem;
  border-top: 1px solid rgba(255,255,255,0.1);
}
.footer-container {
  max-width: 1100px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); /* Responsive columns */
  gap: 2rem;
  text-align: right;
  padding-bottom: 3rem;
}
.footer-column h4 {
  color: white;
  margin-bottom: 1.5rem;
  font-size: 1.1rem;
}
.footer-column ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
.footer-column ul li {
  margin-bottom: 0.8rem;
}
.footer-column ul li a {
  color: rgba(255, 255, 255, 0.6);
  text-decoration: none;
  font-weight: 500;
  transition: color 0.2s;
}
.footer-column ul li a:hover {
  color: white;
}
.footer-bottom {
  text-align: center;
  padding-top: 2rem;
  border-top: 2px solid rgba(255,255,255,0.1);
  font-size: 0.9rem;
}

.uni-logo-box {
  background: rgba(255, 255, 255, 0.1); /* پس‌زمینه شیشه‌ای */
  padding: 1rem;
  border-radius: 12px;
  display: flex; /* برای وسط‌چین کردن عالی */
  justify-content: center;
  align-items: center;
  min-width: 140px;
  min-height: 80px;
  backdrop-filter: blur(5px); /* افکت محو شدن پشت (اختیاری) */
}

/* استایل خود تصویر لوگو */
.uni-logo-img {
  max-width: 120px; /* حداکثر عرض */
  max-height: 70px; /* حداکثر ارتفاع */
  width: auto;
  height: auto;
  object-fit: contain;
  /* اگر لوگوی شما مشکی است و فوتر تیره، خط زیر را فعال کنید تا لوگو سفید شود: */
  /* filter: brightness(0) invert(1); */
  transition: transform 0.3s ease;
}

.uni-logo-box:hover .uni-logo-img {
  transform: scale(1.05); /* افکت زوم هنگام هاور */
}

/* --- Responsive --- */
@media (max-width: 850px) {
  .hero-content { flex-direction: column; gap: 3rem; }
  .hero-title { font-size: 2rem; }
  .globe-icon { font-size: 10rem; }
  .hero-section { padding-top: 6rem; min-height: auto; }
  .features-grid { grid-template-columns: 1fr; gap: 2rem; text-align: center; }
  .feature-item { flex-direction: column; align-items: center; }
  .feature-text h3, .feature-text p { text-align: center; }
  .footer-container { text-align: center; }
}
</style>