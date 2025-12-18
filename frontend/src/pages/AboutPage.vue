<template>
  <div class="page-container">
    
    <div class="content-wrapper">
      <section class="intro-section">
        <h1 class="page-title">درباره <span class="highlight">AntibioticPlay</span></h1>
        <p class="intro-text">
          این پلتفرم با هدف آموزش جذاب و گیمیفاید اصول آنتی‌بیوتیک‌ها و مبارزه با مقاومت میکروبی طراحی شده است. 
          ما معتقدیم که یادگیری داروسازی نباید خشک و خسته‌کننده باشد؛ بلکه می‌تواند مسیری پویا، تعاملی و سرگرم‌کننده برای کادر درمان و دانشجویان باشد.
        </p>
      </section>

      <section class="team-section">
        <h2 class="section-title">تیم ما</h2>
        <div class="team-grid">
          
          <div class="team-card">
            <div class="img-container">
              <img src="/images/team/sholeh.jpg" alt="دکتر شعله ابراهیم‌پور" class="team-img" />
            </div>
            <div class="team-info">
              <h3>دکتر شعله ابراهیم‌پور</h3>
              <span class="team-role">ناظر علمی پروژه</span>
              <p class="team-desc">
                استادیار گروه داروسازی بالینی دانشگاه علوم پزشکی البرز. <br>
                دارای بورد تخصصی فارماکوتراپی از دانشگاه علوم پزشکی تهران.
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
              <span class="team-role">ناظر علمی پروژه</span>
              <p class="team-desc">
                عضو هیئت علمی گروه داروسازی بالینی دانشگاه علوم پزشکی البرز. <br>
                دارای بورد تخصصی فارماکوتراپی (iBCPS).
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
              <span class="team-role">توسعه‌دهنده و طراح</span>
              <p class="team-desc">
                دانشجوی داروسازی ورودی ۹۹ دانشگاه علوم پزشکی البرز. <br>
                طراح و برنامه‌نویس پلتفرم AntibioticPlay.
              </p>
              <div class="badges">
                <span class="badge">Full-Stack Dev</span>
                <span class="badge">Student</span>
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
import { faUniversity } from '@fortawesome/free-solid-svg-icons';
library.add(faUniversity);
</script>

<style scoped>
.page-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
  padding: 8rem 1.5rem 4rem; /* Padding top زیاد برای هدر چسبان */
  display: flex;
  justify-content: center;
}

.content-wrapper {
  max-width: 1000px;
  width: 100%;
}

/* Intro Section */
.intro-section {
  text-align: center;
  margin-bottom: 5rem;
  background: white;
  padding: 3rem;
  border-radius: 24px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.05);
}

.page-title {
  font-size: 2.5rem;
  font-weight: 900;
  color: #1e293b;
  margin-bottom: 1.5rem;
}

.highlight {
  color: var(--color-primary);
}

.intro-text {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #475569;
  max-width: 800px;
  margin: 0 auto;
}

/* Team Section */
.team-section {
  margin-bottom: 4rem;
}

.section-title {
  text-align: center;
  font-size: 2rem;
  font-weight: 800;
  color: #334155;
  margin-bottom: 3rem;
}

.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2.5rem;
}

.team-card {
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 2rem;
  text-align: center;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.5);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.team-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
  background: white;
}

.img-container {
  width: 120px;
  height: 120px;
  margin: 0 auto 1.5rem;
  position: relative;
}

.team-img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  border: 4px solid white;
  box-shadow: 0 8px 15px rgba(0,0,0,0.1);
}

.team-info h3 {
  margin: 0 0 0.5rem;
  color: #1e293b;
  font-size: 1.25rem;
}

.team-role {
  display: block;
  font-size: 0.9rem;
  font-weight: bold;
  color: var(--color-primary);
  margin-bottom: 1rem;
}

.team-desc {
  font-size: 0.9rem;
  color: #64748b;
  line-height: 1.6;
  margin-bottom: 1.5rem;
  min-height: 3em; /* برای هم‌تراز شدن ارتفاع کارت‌ها */
}

.badges {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.badge {
  background: #f1f5f9;
  color: #475569;
  padding: 0.3rem 0.8rem;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
}

/* University Credit */
.university-credit {
  text-align: center;
  margin-top: 4rem;
  color: #94a3b8;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}

.uni-icon {
  font-size: 2rem;
  color: #cbd5e1;
}
</style>