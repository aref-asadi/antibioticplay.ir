<template>
  <div ref="confettiContainer" class="confetti-overlay"></div>
</template>

<script setup>
import { onMounted, ref, onUnmounted } from 'vue';

const confettiContainer = ref(null);
let intervalId = null;

const confettiColors = ['#EF2964', '#00C09D', '#2D87B0', '#48485E', '#EFFF1D'];
const confettiAnimations = ['slow', 'medium', 'fast'];

const renderConfetti = () => {
  const container = confettiContainer.value;
  if (!container) return;

  intervalId = setInterval(() => {
    const confettiEl = document.createElement('div');
    const confettiSize = (Math.floor(Math.random() * 3) + 7) + 'px';
    const confettiBackground = confettiColors[Math.floor(Math.random() * confettiColors.length)];
    const confettiLeft = (Math.floor(Math.random() * container.offsetWidth)) + 'px';
    const confettiAnimation = confettiAnimations[Math.floor(Math.random() * confettiAnimations.length)];

    confettiEl.classList.add('confetti', 'confetti--animation-' + confettiAnimation);
    confettiEl.style.left = confettiLeft;
    confettiEl.style.width = confettiSize;
    confettiEl.style.height = confettiSize;
    confettiEl.style.backgroundColor = confettiBackground;

    // حذف المنت بعد از ۳ ثانیه برای جلوگیری از پر شدن حافظه
    setTimeout(() => {
      if (confettiEl.parentNode) {
        confettiEl.parentNode.removeChild(confettiEl);
      }
    }, 3000);

    container.appendChild(confettiEl);
  }, 25); // هر ۲۵ میلی‌ثانیه یک کاغذ جدید (فرکانس مناسب)
};

onMounted(() => {
  renderConfetti();
});

onUnmounted(() => {
  if (intervalId) clearInterval(intervalId);
  // پاکسازی DOM در صورت نیاز
  if (confettiContainer.value) {
    confettiContainer.value.innerHTML = '';
  }
});
</script>

<style>
/* استایل‌های گلوبال برای ذرات کانفتی */
.confetti-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none; /* کلیک‌ها ازش رد بشن */
  z-index: 50; /* بالاتر از همه چیز اما زیر مودال‌های خیلی مهم */
  overflow: hidden;
}

.confetti {
  position: absolute;
  z-index: 1;
  top: -10px;
  border-radius: 0%;
}

.confetti--animation-slow {
  animation: confetti-slow 2.25s linear 1 forwards;
}

.confetti--animation-medium {
  animation: confetti-medium 1.75s linear 1 forwards;
}

.confetti--animation-fast {
  animation: confetti-fast 1.25s linear 1 forwards;
}

@keyframes confetti-slow {
  0% { transform: translate3d(0, 0, 0) rotateX(0) rotateY(0); }
  100% { transform: translate3d(25px, 105vh, 0) rotateX(360deg) rotateY(180deg); }
}

@keyframes confetti-medium {
  0% { transform: translate3d(0, 0, 0) rotateX(0) rotateY(0); }
  100% { transform: translate3d(100px, 105vh, 0) rotateX(100deg) rotateY(360deg); }
}

@keyframes confetti-fast {
  0% { transform: translate3d(0, 0, 0) rotateX(0) rotateY(0); }
  100% { transform: translate3d(-50px, 105vh, 0) rotateX(10deg) rotateY(250deg); }
}
</style>