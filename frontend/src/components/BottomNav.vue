<template>
  <nav class="bottom-nav">

    <router-link to="/dashboard" class="nav-item" active-class="active">
      <div class="icon-container">
        <font-awesome-icon icon="fas fa-house" />
      </div>
      <span class="nav-label">خانه</span>
    </router-link>

    <div class="nav-item logo-item">
      <span class="nav-logo-text">AntibioticPlay</span>
    </div>

    <router-link to="/leaderboard" class="nav-item" active-class="active">
      <div class="icon-container">
        <font-awesome-icon icon="fas fa-trophy" />
      </div>
      <span class="nav-label">لیگ</span>
    </router-link>

  </nav>
</template>

<style scoped>
.bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 70px;
  background-color: white;
  border-top: 2px solid #e5e5e5;
  display: flex;
  justify-content: space-between; /* پخش کردن آیتم‌ها */
  align-items: center;
  z-index: 999;
  padding-bottom: env(safe-area-inset-bottom);
  box-shadow: 0 -4px 10px rgba(0,0,0,0.05);
  box-sizing: border-box;
  padding-left: 1rem;
  padding-right: 1rem;
}

.nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  color: #afafaf;
  flex: 1; /* هر کدام یک سوم فضا را بگیرند */
  height: 100%;
  cursor: pointer;
  transition: color 0.2s;
}

/* استایل مخصوص آیتم لوگو در وسط */
.logo-item {
  flex: 2; /* فضای بیشتری بگیرد */
  cursor: default;
}
.nav-logo-text {
  color: var(--color-primary);
  font-weight: 900;
  font-size: 1.1rem;
  letter-spacing: 0.5px;
}

.icon-container { font-size: 1.5rem; margin-bottom: 4px; transition: transform 0.1s; }
.nav-label { font-size: 0.75rem; font-weight: 700; text-transform: uppercase; }

.nav-item.active { color: var(--color-secondary); }
.nav-item.active .icon-container { transform: translateY(-2px); }

@media (min-width: 851px) {
  .bottom-nav { display: none; }
}
</style>