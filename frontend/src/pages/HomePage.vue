<template>
  <div class="home-page">
    
    <header class="landing-header">
      <div class="header-content">
        <div class="logo-container">
          <font-awesome-icon icon="fas fa-microscope" class="logo-icon" />
          <h2 class="logo-text">AntibioticPlay</h2>
        </div>
        <div class="header-actions">
           <template v-if="!authStore.isAuthenticated">
             <router-link to="/login" class="btn-sm btn-outline">ورود</router-link>
             <router-link to="/register" class="btn-sm btn-primary">ثبت‌نام</router-link>
           </template>
           <router-link v-else to="/dashboard" class="btn-sm btn-primary">داشبورد</router-link>
        </div>
      </div>
    </header>

    <section class="hero-section">
      <div class="blob blob-1"></div>
      <div class="blob blob-2"></div>
      <div class="hero-container">
        <div class="hero-content">
          <div class="badge-pill">
            <span class="badge-icon">🛡️</span>
            <span>ایران؛ صدرنشین مصرف آنتی بیوتیک در جهان</span>
          </div>
          <h1 class="hero-title">
            افزایش آگاهی، سد اول دفاعی در <br />
            <span class="highlight-text">پیشگیری از مقاومت های میکروبی</span>
          </h1>
          <p class="hero-subtitle">
            ماژول‌های کوتاه و متمرکز که پیچیده‌ترین مباحث دارودرمانی آنتی‌بیوتیک‌ها را به لقمه‌های قابل‌هضم تبدیل می‌کنند. با سیستم امتیازدهی و لیدربورد، انگیزه خود را حفظ کنید و جایگاه دانشی خود را در میان همکلاسی‌ها و همکاران بسنجید.
          </p>
          <div class="hero-actions">
            <router-link v-if="authStore.isAuthenticated" to="/dashboard" class="btn btn-primary btn-lg">
              ورود به داشبورد <font-awesome-icon icon="fas fa-arrow-left" class="ms-2" />
            </router-link>
            <template v-else>
              <router-link to="/login" class="btn btn-primary btn-lg">
                شروع یادگیری <font-awesome-icon icon="fas fa-rocket" class="ms-2" />
              </router-link>
            </template>
          </div>
          <div class="hero-stats">
            <div class="stat-item"><strong>۳</strong><span>ماژول تخصصی</span></div>
            <div class="stat-separator"></div>
            <div class="stat-item"><strong>سطح‌بندی</strong><span>گیمیفیکیشن</span></div>
          </div>
        </div>
        <div class="hero-image-wrapper">
          <img src="/images/hero-awareness.png" alt="Antibiotic Awareness" class="hero-img" />
          <div class="floating-card card-1">
            <font-awesome-icon icon="fas fa-bacteria" class="icon-germ" /><span>MDR Organisms</span>
          </div>
          <div class="floating-card card-2">
            <font-awesome-icon icon="fas fa-prescription-bottle-alt" class="icon-drug" /><span>Stewardship</span>
          </div>
        </div>
      </div>
    </section>

    <section class="legends-section">
      <div class="section-header">
        <h2 class="section-title">میراث‌داران علم آنتی‌بیوتیک</h2>
        <p class="section-subtitle">
          تاریخ پزشکی بر شانه غول‌هایی ایستاده است که جهان میکروسکوپی را تسخیر کردند. 
          <br>شما می‌توانید در مسیر یادگیری خود، یکی از این پیشگامان را به عنوان نماد خود انتخاب کنید.
        </p>
      </div>
      
      <div class="legends-list">
        <div class="legend-item">
          <div class="legend-avatar">
            <img src="/avatars/avatar_fleming.png" alt="الکساندر فلمینگ" />
          </div>
          <div class="legend-content">
            <h3>الکساندر فلمینگ <span class="legend-year">(1945 Nobel)</span></h3>
            <span class="legend-badge">کاشف پنی‌سیلین</span>
            <p>
              آغازگر عصر طلایی آنتی‌بیوتیک‌ها. او با مشاهده ساده‌ای روی یک ظرف پتری فراموش‌شده، قدرتمندترین سلاح بشر علیه عفونت‌ها را کشف کرد و سرنوشت جنگ جهانی دوم و پزشکی مدرن را تغییر داد.
            </p>
          </div>
        </div>

        <div class="legend-item reverse">
          <div class="legend-avatar">
            <img src="/avatars/avatar_waksman.png" alt="سلمان واکسمن" />
          </div>
          <div class="legend-content">
            <h3>سلمان واکسمن <span class="legend-year">(1952 Nobel)</span></h3>
            <span class="legend-badge">پدر آنتی‌بیوتیک‌ها</span>
            <p>
              او کسی بود که واژه "آنتی‌بیوتیک" را ابداع کرد. با کاوش در خاک، استرپتومایسین را یافت و برای اولین بار، بیماری وحشتناک سل (The White Plague) را درمان‌پذیر کرد.
            </p>
          </div>
        </div>

        <div class="legend-item">
          <div class="legend-avatar">
            <img src="/avatars/avatar_domagk.png" alt="گرهارد دماک" />
          </div>
          <div class="legend-content">
            <h3>گرهارد دماک <span class="legend-year">(1939 Nobel)</span></h3>
            <span class="legend-badge">پیشگام سولفونامیدها</span>
            <p>
              او با کشف "پرونتوسیل"، اولین داروی آنتی‌باکتریال تجاری جهان، دختر خود را از مرگ نجات داد و ثابت کرد که رنگ‌های صنعتی می‌توانند ناجی جان انسان‌ها باشند.
            </p>
          </div>
        </div>

        <div class="legend-item reverse">
          <div class="legend-avatar">
            <img src="/avatars/avatar_florey.png" alt="هاوارد فلوری" />
          </div>
          <div class="legend-content">
            <h3>هاوارد فلوری <span class="legend-year">(1945 Nobel)</span></h3>
            <span class="legend-badge">معمار تولید انبوه</span>
            <p>
              کشف فلمینگ بدون نبوغ فلوری تنها یک کنجکاوی آزمایشگاهی باقی می‌ماند. او بود که پنی‌سیلین را از یک کپک آزمایشگاهی به دارویی برای نجات میلیون‌ها سرباز تبدیل کرد.
            </p>
          </div>
        </div>

        <div class="legend-item">
          <div class="legend-avatar">
            <img src="/avatars/avatar_hodgkin.png" alt="دوروتی هاجکین" />
          </div>
          <div class="legend-content">
            <h3>دوروتی هاجکین <span class="legend-year">(1964 Nobel)</span></h3>
            <span class="legend-badge">کاشف ساختارهای نامرئی</span>
            <p>
              با چشمان اشعه ایکس خود، راز ساختار مولکولی پنی‌سیلین را فاش کرد. شاهکار او به شیمیدانان اجازه داد تا آنتی‌بیوتیک‌های نیمه‌صناعی را خلق کنند.
            </p>
          </div>
        </div>

        <div class="legend-item reverse">
          <div class="legend-avatar">
            <img src="/avatars/avatar_bugie.png" alt="الیزابت بوگی" />
          </div>
          <div class="legend-content">
            <h3>الیزابت بوگی <span class="legend-year">(Researcher)</span></h3>
            <span class="legend-badge">همکار در کشف استرپتومایسین</span>
            <p>
              او یکی از اعضای کلیدی و تأثیرگذار آزمایشگاه واکسمن بود. اگرچه نام او در جایزه نوبل ذکر نشد، اما تحقیقات دقیق او نقش اساسی در اثبات اثربخشی استرپتومایسین داشت.
            </p>
          </div>
        </div>

        <div class="legend-item">
          <div class="legend-avatar">
            <img src="/avatars/avatar_youyou.png" alt="تو یویو" />
          </div>
          <div class="legend-content">
            <h3>تو یویو <span class="legend-year">(2015 Nobel)</span></h3>
            <span class="legend-badge">کاشف آرتمیسینین</span>
            <p>
              او با الهام از متون طب سنتی چین، دارویی حیاتی (آرتمیسینین) را برای درمان مالاریا کشف کرد که جان میلیون‌ها نفر را در سراسر جهان نجات داده است.
            </p>
          </div>
        </div>

      </div>
    </section>

    <section class="features-section">
      <h2 class="section-title">تجربه‌ای فراتر از مطالعه سنتی</h2>
      <div class="features-grid">
        <div class="feature-item">
          <div class="icon-box fire"><font-awesome-icon icon="fas fa-fire" /></div>
          <div class="feature-text">
            <h3>یادگیری خرد (Micro-Learning)</h3>
            <p>ماژول‌های کوتاه و متمرکز که پیچیده‌ترین مباحث فارماکولوژی را به لقمه‌های قابل‌هضم تبدیل می‌کنند.</p>
          </div>
        </div>
        <div class="feature-item">
          <div class="icon-box check"><font-awesome-icon icon="fas fa-check-circle" /></div>
          <div class="feature-text">
            <h3>بازخورد هوشمند آنی</h3>
            <p>تنها به گزینه درست بسنده نکنید. دلیل رد گزینه‌های غلط را یاد بگیرید تا استدلال بالینی خود را تقویت کنید.</p>
          </div>
        </div>
        <div class="feature-item">
          <div class="icon-box star"><font-awesome-icon icon="fas fa-star" /></div>
          <div class="feature-text">
            <h3>رقابت علمی سالم</h3>
            <p>با سیستم امتیازدهی و لیدربورد، انگیزه خود را حفظ کنید و جایگاه خود را در میان همکاران بسنجید.</p>
          </div>
        </div>
        <div class="feature-item">
          <div class="icon-box heart"><font-awesome-icon icon="fas fa-heart" /></div>
          <div class="feature-text">
            <h3>طراحی بالین‌محور</h3>
            <p>سناریوهایی که دقیقاً با چالش‌های واقعی شما در بیمارستان و داروخانه همخوانی دارد، نه صرفاً تئوری کتاب.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="bottom-cta-section">
      <h2 class="cta-title">آماده‌اید سطح دانش خود را ارتقا دهید؟</h2>
      <router-link to="/register" class="btn cta-btn">
        همین حالا رایگان شروع کنید
      </router-link>
    </section>

    <footer class="main-footer">
      <div class="footer-container">
        <div class="footer-column">
          <h4>درباره AntibioticPlay</h4>
          <ul>
            <li><router-link to="/about">درباره ما</router-link></li>
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
          <h4>با حمایت علمی</h4>
          <div class="uni-logo-box">
             <img src="/images/uni_logo.png" alt="University of Medical Sciences" class="uni-logo-img" />
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
import { faGlobeAmericas, faFire, faCheckCircle, faStar, faHeart, faUniversity, faArrowLeft, faRocket, faBacteria, faPrescriptionBottleAlt, faMicroscope } from '@fortawesome/free-solid-svg-icons';

library.add(faGlobeAmericas, faFire, faCheckCircle, faStar, faHeart, faUniversity, faArrowLeft, faRocket, faBacteria, faPrescriptionBottleAlt, faMicroscope);

const authStore = useAuthStore();
</script>

<style scoped>
/* Basic Layout */
.home-page { width: 100%; min-height: 100vh; display: flex; flex-direction: column; }

/* Header */
.landing-header { position: sticky; top: 0; padding: 0.8rem 2rem; z-index: 1000; background: rgba(255, 255, 255, 0.85); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(0, 0, 0, 0.05); }
.header-content { max-width: 1100px; display: flex; align-items: center; justify-content: space-between; margin: 0 auto; width: 100%; }
.logo-container { display: flex; align-items: center; gap: 0.5rem; }
.logo-icon { font-size: 1.5rem; color: var(--color-primary); }
.logo-text { background: linear-gradient(45deg, var(--color-primary), #2c3e50); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 800; font-size: 1.5rem; margin: 0; }
.header-actions { display: flex; gap: 0.8rem; align-items: center; } /* فاصله بین دکمه‌ها */
.btn-sm { padding: 0.4rem 1rem; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 0.9rem; }
.btn-outline { border: 2px solid var(--color-primary); color: var(--color-primary); }
.btn-outline:hover { background: var(--color-primary); color: white; }
.btn-primary { background: var(--color-primary); color: white; border: none; box-shadow: 0 4px 14px rgba(66, 185, 131, 0.4); }

/* Hero */
.hero-section { background: linear-gradient(180deg, #f0f9ff 0%, #ffffff 100%); display: flex; justify-content: center; padding: 6rem 1.5rem 4rem; position: relative; overflow: hidden; }
.blob { position: absolute; border-radius: 50%; filter: blur(80px); opacity: 0.5; z-index: 1; }
.blob-1 { width: 400px; height: 400px; background: #dcfce7; top: -100px; right: -150px; }
.blob-2 { width: 350px; height: 350px; background: #dbeafe; bottom: 0; left: -100px; }
.hero-container { max-width: 1200px; width: 100%; display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; z-index: 2; align-items: center; }
.hero-content { display: flex; flex-direction: column; align-items: flex-start; }
.badge-pill { background: white; color: #1976d2; padding: 0.5rem 1rem; border-radius: 50px; font-weight: bold; display: inline-flex; gap: 0.5rem; border: 1px solid #e3f2fd; margin-bottom: 1.5rem; }
.hero-title { font-size: 3rem; font-weight: 900; line-height: 1.2; color: #1e293b; margin-bottom: 1.5rem; }
.highlight-text { color: var(--color-primary); position: relative; display: inline-block; }
.highlight-text::after { content: ''; position: absolute; bottom: 5px; left: 0; width: 100%; height: 12px; background: rgba(66, 185, 131, 0.2); z-index: -1; border-radius: 4px; }
.hero-subtitle { font-size: 1.15rem; color: #475569; line-height: 1.8; margin-bottom: 2.5rem; }
.hero-actions { display: flex; gap: 1rem; margin-bottom: 3rem; }
.btn-lg { padding: 0.9rem 2.2rem; font-size: 1.1rem; border-radius: 12px; }
.hero-stats { display: flex; gap: 2rem; align-items: center; }
.stat-item { display: flex; flex-direction: column; }
.stat-item strong { font-size: 1.5rem; font-weight: 800; color: #1e293b; }
.stat-item span { color: #64748b; font-size: 0.9rem; }
.stat-separator { width: 1px; height: 40px; background: #cbd5e1; }
.hero-image-wrapper { position: relative; display: flex; justify-content: center; }
.hero-img { width: 100%; max-width: 550px; border-radius: 24px; filter: drop-shadow(0 20px 40px rgba(0,0,0,0.1)); background: white; }
.floating-card { position: absolute; background: rgba(255,255,255,0.95); padding: 0.8rem 1.2rem; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.08); display: flex; align-items: center; gap: 0.8rem; font-weight: bold; z-index: 2; animation: float 6s infinite; border: 1px solid rgba(255,255,255,0.5); }
.card-1 { top: 10%; left: -20px; } .card-2 { bottom: 15%; right: -10px; animation-delay: 3s; }
.icon-germ { color: #ef4444; } .icon-drug { color: #22c55e; }
@keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-15px); } }

/* Legends */
.legends-section { padding: 6rem 2rem; background-color: #f8fafc; }
.section-header { text-align: center; max-width: 800px; margin: 0 auto 4rem; }
.section-title { font-size: 2.2rem; font-weight: 900; color: #1e293b; margin-bottom: 1rem; }
.section-subtitle { color: #64748b; font-size: 1.1rem; line-height: 1.7; }
.legends-list { max-width: 1000px; margin: 0 auto; display: flex; flex-direction: column; gap: 3rem; }
.legend-item { display: flex; align-items: center; gap: 3rem; background: white; padding: 2.5rem; border-radius: 24px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); border: 1px solid #f1f5f9; transition: transform 0.3s ease, box-shadow 0.3s ease; }
.legend-item:hover { transform: translateY(-5px); box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1); border-color: var(--color-primary-light); }
.legend-item.reverse { flex-direction: row-reverse; text-align: left; }
.legend-item.reverse .legend-content { text-align: right; }

.legend-avatar { flex-shrink: 0; }
.legend-avatar img { width: 160px; height: 160px; border-radius: 50%; object-fit: cover; border: 5px solid #f0fdf4; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); }
.legend-content { flex: 1; }
.legend-content h3 { font-size: 1.5rem; color: #334155; margin: 0 0 0.5rem 0; font-weight: 800; display: flex; align-items: center; gap: 0.8rem; }
.legend-year { font-size: 0.9rem; color: #94a3b8; font-weight: 400; background: #f1f5f9; padding: 2px 8px; border-radius: 6px; }
.legend-badge { display: inline-block; background-color: #ecfdf5; color: var(--color-primary); font-weight: bold; font-size: 0.9rem; padding: 0.3rem 0.8rem; border-radius: 50px; margin-bottom: 1rem; }
.legend-content p { color: #475569; font-size: 1.05rem; line-height: 1.8; margin: 0; }

/* Features */
.features-section { padding: 6rem 2rem; background-color: white; text-align: center; }
.features-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 3rem; max-width: 1000px; margin: 3rem auto 0; text-align: right; }
.feature-item { display: flex; align-items: flex-start; gap: 1.5rem; padding: 1.5rem; border-radius: 16px; transition: background 0.2s; }
.feature-item:hover { background: #f8fafc; }
.icon-box { width: 60px; height: 60px; border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 1.8rem; flex-shrink: 0; }
.icon-box.fire { background: #fff7ed; color: #f97316; }
.icon-box.check { background: #f0fdf4; color: #22c55e; }
.icon-box.star { background: #fefce8; color: #eab308; }
.icon-box.heart { background: #fdf2f8; color: #ec4899; }
.feature-text h3 { margin: 0 0 0.5rem; font-size: 1.25rem; color: #1e293b; font-weight: 800; }
.feature-text p { margin: 0; color: #64748b; line-height: 1.6; }

/* CTA Section */
.bottom-cta-section {
  background: linear-gradient(135deg, var(--color-primary) 0%, #34d399 100%);
  padding: 5rem 2rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: white;
}
.cta-title {
  color: white;
  font-size: 2.2rem;
  margin-bottom: 2.5rem;
  font-weight: 900;
  text-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.cta-btn {
  background: white;
  color: var(--color-primary) !important;
  min-width: 250px;
  font-size: 1.2rem;
  padding: 1rem 2rem;
  font-weight: 800;
  box-shadow: 0 10px 25px rgba(0,0,0,0.1);
  text-decoration: none;
  border-radius: 12px;
  display: inline-block;
  transition: all 0.3s ease;
}
.cta-btn:hover {
  transform: translateY(-3px);
  background: #f0fdf4 !important; /* رنگ سبز خیلی روشن */
  color: #15803d !important; /* رنگ سبز تیره ثابت برای خوانایی */
}

/* Footer */
.main-footer { background: #0f172a; color: #94a3b8; padding: 4rem 2rem 2rem; border-top: 4px solid var(--color-primary); }
.footer-container { max-width: 1100px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 3rem; text-align: right; padding-bottom: 3rem; }
.footer-column h4 { color: white; margin-bottom: 1.5rem; font-weight: 700; }
.footer-column ul { list-style: none; padding: 0; }
.footer-column ul li { margin-bottom: 1rem; }
.footer-column ul li a { color: #cbd5e1; text-decoration: none; transition: 0.2s; }
.footer-column ul li a:hover { color: var(--color-primary); }
.uni-logo-box { background: rgba(255, 255, 255, 0.1); padding: 1.5rem; border-radius: 16px; display: inline-flex; justify-content: center; align-items: center; backdrop-filter: blur(5px); border: 1px solid rgba(255,255,255,0.15); }
.uni-logo-img { width: 180px; height: auto; object-fit: contain; filter: brightness(0) invert(1); opacity: 1; }

/* Copyright Centering */
.footer-bottom {
  text-align: center;
  width: 100%;
  display: flex;
  justify-content: center;
  padding-top: 2rem;
  border-top: 1px solid #1e293b;
  font-size: 0.9rem;
}

/* Responsive */
@media (max-width: 900px) {
  .hero-container { grid-template-columns: 1fr; text-align: center; }
  .hero-content { align-items: center; }
  .features-grid { grid-template-columns: 1fr; }
  .legends-list { gap: 2rem; }
  .legend-item, .legend-item.reverse { flex-direction: column; text-align: center; padding: 2rem 1.5rem; }
  .legend-item.reverse .legend-content { text-align: center; }
  .legend-content h3 { justify-content: center; }
  .footer-container { text-align: center; }
}
</style>