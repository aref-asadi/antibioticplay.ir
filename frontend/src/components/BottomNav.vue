<template>
  <nav class="bottom-nav">
    
    <router-link to="/dashboard" class="nav-item" active-class="active">
      <div class="icon-container">
        <font-awesome-icon icon="fas fa-house" />
      </div>
      <span class="nav-label">خانه</span>
    </router-link>

    <router-link to="/leaderboard" class="nav-item" active-class="active">
      <div class="icon-container">
        <font-awesome-icon icon="fas fa-trophy" />
      </div>
      <span class="nav-label">لیگ</span>
    </router-link>

    <div class="nav-item disabled">
      <div class="icon-container">
        <font-awesome-icon icon="fas fa-user" />
      </div>
      <span class="nav-label">پروفایل</span>
    </div>

  </nav>
</template>

<style scoped>
.bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%; /* استفاده از width 100% بجای right:0 برای اطمینان */
  height: 70px; /* ارتفاع ثابت */
  background-color: white;
  border-top: 2px solid #e5e5e5;
  display: flex;
  justify-content: space-around;
  align-items: center;
  z-index: 999; /* بالاترین لایه */
  padding-bottom: env(safe-area-inset-bottom);
  box-shadow: 0 -4px 10px rgba(0,0,0,0.05); /* سایه برای جدا شدن از محتوا */
  box-sizing: border-box; /* اطمینان از اینکه پدینگ عرض را زیاد نکند */
}

/* ... (بقیه استایل‌های داخلی مثل .nav-item بدون تغییر) ... */
.nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  color: #afafaf;
  flex: 1;
  height: 100%;
  cursor: pointer;
  transition: color 0.2s;
}

.icon-container { font-size: 1.5rem; margin-bottom: 4px; transition: transform 0.1s; }
.nav-label { font-size: 0.75rem; font-weight: 700; text-transform: uppercase; }
.nav-item.active { color: var(--color-secondary); }
.nav-item.active .icon-container { transform: translateY(-2px); }
.nav-item.disabled { opacity: 0.5; cursor: default; }

@media (min-width: 851px) {
  .bottom-nav { display: none; }
}
</style>