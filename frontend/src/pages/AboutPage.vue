<template>
  <div class="page-container">
    
    <button @click="$router.go(-1)" class="back-button" title="بازگشت">
      <font-awesome-icon icon="fas fa-arrow-right" />
    </button>

    <div class="content-wrapper">
      <section class="intro-section">
        <h1 class="page-title">درباره <span class="highlight">AntibioticPlay</span></h1>
        <p class="intro-text">
          ما در حال ساختن آینده‌ای هستیم که در آن آموزش پزشکی دیگر یک فرآیند یک‌طرفه و خسته‌کننده نیست. 
          پلتفرم ما با تلفیق <strong>دقت علمی</strong> و <strong>جذابیت بازی‌سازی (Gamification)</strong>، مسیری نوین برای تسلط بر پیچیدگی‌های آنتی‌بیوتیک‌ها و فارماکولوژی بالینی ارائه می‌دهد.
        </p>
      </section>

      <section class="team-section">
        <h2 class="section-title">تیم توسعه و علمی</h2>
        <div class="team-grid">
          
          <div class="team-card">
            <div class="img-container">
              <img src="/images/team/sholeh.jpg" alt="دکتر شعله ابراهیم‌پور" class="team-img" />
            </div>
            <div class="team-info">
              <h3>دکتر شعله ابراهیم‌پور</h3>
              <span class="team-role">ناظر علمی و طراح آموزشی</span>
              <p class="team-desc">
                استادیار داروسازی بالینی با دیدگاهی نوآورانه در آموزش پزشکی. ایشان با نظارت دقیق بر محتوا، تضمین‌کننده اعتبار علمی تمام ماژول‌های این پلتفرم هستند.
              </p>
              <div class="badges">
                <span class="badge">Clinical Pharmacy</span>
                <span class="badge">Supervisor</span>
              </div>
            </div>
          </div>

          <div class="team-card">
            <div class="img-container">
              <img src="/images/team/mehdi.jpg" alt="دکتر مهدی محمدی" class="team-img" />
            </div>
            <div class="team-info">
              <h3>دکتر مهدی محمدی</h3>
              <span class="team-role">ناظر علمی و استراتژیست</span>
              <p class="team-desc">
                عضو هیئت علمی و متخصص فارماکوتراپی (iBCPS). تجربیات ارزشمند ایشان در بالین، راهنمای اصلی ما در پیاده‌سازی کیس‌های واقعی و کاربردی بوده است.
              </p>
              <div class="badges">
                <span class="badge">Pharm.D</span>
                <span class="badge">iBCPS</span>
              </div>
            </div>
          </div>

          <div class="team-card">
            <div class="img-container">
              <img src="/images/team/aref.jpg" alt="عارف اسدی" class="team-img" />
            </div>
            <div class="team-info">
              <h3>عارف اسدی</h3>
              <span class="team-role">توسعه‌دهنده Full-Stack</span>
              <p class="team-desc">
                دانشجوی داروسازی و برنامه‌نویس. خالق زیرساخت فنی و تجربه کاربری (UX) سایت که پل میان دنیای کدنویسی و علوم دارویی را بنا کرده است.
              </p>
              <div class="badges">
                <span class="badge">Developer</span>
                <span class="badge">Designer</span>
              </div>
            </div>
          </div>

        </div>
      </section>

      <div class="university-credit">
        <font-awesome-icon icon="fas fa-university" class="uni-icon" />
        <p>توسعه یافته در دانشکده داروسازی دانشگاه علوم پزشکی البرز</p>
      </div>

    </div>
  </div>
</template>

<script setup>
import { library } from '@fortawesome/fontawesome-svg-core';
import { faUniversity, faArrowRight } from '@fortawesome/free-solid-svg-icons';
library.add(faUniversity, faArrowRight);
</script>

<style scoped>
.page-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
  padding: 6rem 1.5rem 4rem;
  display: flex;
  justify-content: center;
  position: relative;
}

/* Back Button Circle Fix */
.back-button {
  position: fixed;
  top: 2rem;
  right: 2rem;
  width: 50px;
  height: 50px;
  min-width: 0; /* <--- این خط را اضافه کنید تا قانون کلی ۱۲۰ پیکسل را نادیده بگیرد */
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

.content-wrapper { max-width: 1000px; width: 100%; }
.intro-section { text-align: center; margin-bottom: 5rem; background: white; padding: 4rem 3rem; border-radius: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); position: relative; overflow: hidden; }
.intro-section::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 6px; background: linear-gradient(90deg, var(--color-primary), var(--color-secondary)); }
.page-title { font-size: 2.5rem; font-weight: 900; color: #1e293b; margin-bottom: 1.5rem; }
.highlight { color: var(--color-primary); }
.intro-text { font-size: 1.1rem; line-height: 1.9; color: #475569; max-width: 800px; margin: 0 auto; }
.team-section { margin-bottom: 4rem; }
.section-title { text-align: center; font-size: 2rem; font-weight: 800; color: #334155; margin-bottom: 3rem; }
.team-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2.5rem; }
.team-card { background: rgba(255, 255, 255, 0.7); backdrop-filter: blur(10px); border-radius: 20px; padding: 2rem; text-align: center; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); border: 1px solid rgba(255, 255, 255, 0.5); transition: transform 0.3s ease, box-shadow 0.3s ease; }
.team-card:hover { transform: translateY(-8px); box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1); background: white; }
.img-container { width: 130px; height: 130px; margin: 0 auto 1.5rem; position: relative; }
.team-img { width: 100%; height: 100%; border-radius: 50%; object-fit: cover; border: 4px solid white; box-shadow: 0 8px 15px rgba(0,0,0,0.1); }
.team-info h3 { margin: 0 0 0.5rem; color: #1e293b; font-size: 1.3rem; font-weight: 800; }
.team-role { display: block; font-size: 0.95rem; font-weight: bold; color: var(--color-primary); margin-bottom: 1rem; }
.team-desc { font-size: 0.9rem; color: #64748b; line-height: 1.6; margin-bottom: 1.5rem; min-height: 4.5em; }
.badges { display: flex; justify-content: center; gap: 0.5rem; flex-wrap: wrap; }
.badge { background: #f1f5f9; color: #475569; padding: 0.3rem 0.8rem; border-radius: 12px; font-size: 0.75rem; font-weight: 600; border: 1px solid #e2e8f0; }
.university-credit { text-align: center; margin-top: 5rem; color: #94a3b8; display: flex; flex-direction: column; align-items: center; gap: 1rem; opacity: 0.7; }
.uni-icon { font-size: 2.5rem; color: #cbd5e1; }

@media (max-width: 600px) {
  .back-button { top: 1rem; right: 1rem; width: 40px; height: 40px; font-size: 1rem; }
}
</style>