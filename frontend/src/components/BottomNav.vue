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
  right: 0;
  height: 70px;
  background-color: white;
  border-top: 2px solid #e5e5e5;
  display: flex;
  justify-content: space-around;
  align-items: center;
  z-index: 900; /* زیر پاپ‌آپ‌ها ولی روی محتوا */
  padding-bottom: env(safe-area-inset-bottom); /* برای آیفون‌های جدید */
}

.nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  color: #afafaf; /* رنگ غیرفعال */
  flex: 1;
  height: 100%;
  cursor: pointer;
  transition: color 0.2s;
}

.icon-container {
  font-size: 1.5rem;
  margin-bottom: 4px;
  transition: transform 0.1s;
}

.nav-label {
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
}

/* Active State */
.nav-item.active {
  color: var(--color-secondary); /* آبی دولینگو */
}
.nav-item.active .icon-container {
  transform: translateY(-2px);
}

/* Disabled State (For Profile placeholder) */
.nav-item.disabled {
  opacity: 0.5;
  cursor: default;
}

/* Desktop Hidden */
@media (min-width: 851px) {
  .bottom-nav {
    display: none;
  }
}
</style>