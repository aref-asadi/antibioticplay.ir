<template>
  <div class="home-page">
    
    <header class="landing-header">
      <div class="header-content">
        <h2 class="logo-text">AntibioticPlay</h2>
        </div>
    </header>

    <section class="hero-section">
      <div class="hero-content">
        
        <div class="hero-image-container">
          <div class="globe-placeholder">
            <font-awesome-icon icon="fas fa-globe-americas" class="globe-icon" />
            <div class="orbit-item item-1">💊</div>
            <div class="orbit-item item-2">🦠</div>
            <div class="orbit-item item-3">🧪</div>
          </div>
        </div>

        <div class="hero-text-container">
          <h1 class="hero-title">
            راهی رایگان، جذاب و موثر برای یادگیری داروسازی!
          </h1>
          
          <div class="hero-actions">
            <template v-if="!authStore.isAuthenticated">
              <router-link to="/register" class="btn btn-primary hero-btn">
                شروع کنید
              </router-link>
              <router-link to="/login" class="btn btn-outline hero-btn">
                اکانت دارم
              </router-link>
            </template>
            
            <template v-else>
              <router-link to="/dashboard" class="btn btn-primary hero-btn">
                رفتن به داشبورد
              </router-link>
            </template>
          </div>
        </div>

      </div>
      <div class="bg-pattern"></div>
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
          <h4>درباره ما</h4>
          <ul>
            <li><a href="#">درباره سایت</a></li>
            <li><a href="#">تیم توسعه</a></li>
            <li><a href="#">فرصت‌های شغلی</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h4>محصولات</h4>
          <ul>
            <li><a href="#">آزمون‌ها</a></li>
            <li><a href="#">فلش‌کارت‌ها</a></li>
            <li><a href="#">AntibioticPlay برای دانشگاه‌ها</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h4>پشتیبانی</h4>
          <ul>
            <li><a href="#">سوالات متداول</a></li>
            <li><a href="#">تماس با ما</a></li>
            <li><a href="#">قوانین و مقررات</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h4>شبکه‌های اجتماعی</h4>
          <ul>
            <li><a href="#">اینستاگرام</a></li>
            <li><a href="#">توییتر</a></li>
            <li><a href="#">لینکدین</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2023 AntibioticPlay. تمامی حقوق محفوظ است.</p>
      </div>
    </footer>

  </div>
</template>

<script setup>
import { useAuthStore } from '../stores/auth';
import { library } from '@fortawesome/fontawesome-svg-core';
import { 
  faGlobeAmericas, 
  faFire, 
  faCheckCircle, 
  faStar, 
  faHeart 
} from '@fortawesome/free-solid-svg-icons';

library.add(faGlobeAmericas, faFire, faCheckCircle, faStar, faHeart);

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
  padding: 6rem 2rem 4rem; /* Added top padding for header space */
  position: relative;
  overflow: hidden;
  min-height: 85vh;
}
.bg-pattern {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background-image: radial-gradient(rgba(255, 255, 255, 0.2) 2px, transparent 2px);
  background-size: 50px 50px;
  opacity: 0.5;
  pointer-events: none;
}
.hero-content {
  display: flex;
  flex-direction: row-reverse;
  align-items: center;
  justify-content: center;
  max-width: 1100px;
  width: 100%;
  gap: 4rem;
  z-index: 1;
}
.hero-text-container { flex: 1; text-align: center; max-width: 500px; }
.hero-title { color: white; font-size: 2.5rem; line-height: 1.4; margin-bottom: 2rem; font-weight: 900; }
.hero-actions { display: flex; flex-direction: column; gap: 1rem; max-width: 350px; margin: 0 auto; }
.hero-btn { width: 100%; padding: 1rem; font-size: 1.1rem; }
.hero-image-container { flex: 1; display: flex; justify-content: center; align-items: center; }
.globe-placeholder { position: relative; width: 300px; height: 300px; display: flex; justify-content: center; align-items: center; }
.globe-icon { font-size: 14rem; color: #4cb6ea; filter: drop-shadow(0 10px 0 rgba(0,0,0,0.2)); }
.orbit-item { position: absolute; font-size: 3rem; animation: float 4s ease-in-out infinite; }
.item-1 { top: 0; right: 20px; animation-delay: 0s; }
.item-2 { bottom: 20px; left: 20px; animation-delay: 1s; }
.item-3 { bottom: 40px; right: 0; animation-delay: 2s; font-size: 2.5rem; }
@keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-20px); } }

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
  background-color: var(--color-hero-bg); /* Or slightly darker if desired */
  color: rgba(255, 255, 255, 0.7);
  padding: 4rem 2rem 2rem;
  border-top: 2px solid rgba(255,255,255,0.1); /* Separator line */
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