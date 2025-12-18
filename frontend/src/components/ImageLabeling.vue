<template>
  <div class="image-labeling-container">
    <p class="question-text">{{ question.text }}</p>

    <div class="workspace">
      <div class="image-wrapper" ref="imageRef">
        <div v-if="!imageLoaded" class="image-loading">
          <div class="spinner"></div>
          <p>در حال بارگذاری تصویر...</p>
        </div>

        <img 
          :src="question.image" 
          :alt="question.text" 
          class="question-image" 
          :class="{ 'hidden': !imageLoaded }"
          @load="onImageLoad" 
        />
        
        <template v-if="imageLoaded">
          <div 
            v-for="zone in question.zones" 
            :key="zone.id"
            class="drop-zone"
            :class="{ 
              'is-over': isDragOver === zone.id, 
              'has-items': userAnswers[zone.id] && userAnswers[zone.id].length > 0,
              'feedback-correct': feedback && feedback[zone.id] === 'correct',
              'feedback-incorrect': feedback && feedback[zone.id] === 'incorrect'
            }"
            :style="getZoneStyle(zone)"
            @dragover.prevent="onDragOver(zone.id)"
            @dragleave="onDragLeave"
            @drop="onDrop($event, zone.id)"
            @click="removeLastItem(zone.id)"
            :title="getZoneTooltip(zone.id)"
          >
            <div v-if="userAnswers[zone.id] && userAnswers[zone.id].length > 0" class="zone-badges">
              <span v-for="optId in userAnswers[zone.id]" :key="optId" class="mini-badge">
                {{ getOptionText(optId) }}
              </span>
            </div>
            
            <div v-else class="zone-placeholder">
              <span class="plus-icon">+</span>
            </div>

            <div v-if="feedback && feedback[zone.id]" class="feedback-icon">
              <span v-if="feedback[zone.id] === 'correct'">✅</span>
              <span v-else>❌</span>
            </div>
          </div>
        </template>
      </div>

      <div class="options-pool" v-if="availableOptions.length > 0">
        <p class="pool-title">گزینه‌ها را بکشید:</p>
        <div class="options-grid">
          <div 
            v-for="option in availableOptions" 
            :key="option.id"
            class="draggable-option"
            draggable="true"
            @dragstart="onDragStart($event, option)"
          >
            {{ option.text }}
          </div>
        </div>
      </div>
      <div v-else class="options-pool empty">
        <p>تمام گزینه‌ها جایگذاری شده‌اند.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue';

const props = defineProps(['question', 'feedback']);
const emit = defineEmits(['answer']);

const userAnswers = ref({}); // ساختار: { zoneId: [optionId1, optionId2] }
const isDragOver = ref(null);
const imageRef = ref(null);
const imageLoaded = ref(false);
const scale = ref(1);

// محاسبه گزینه‌هایی که هنوز استفاده نشده‌اند
const availableOptions = computed(() => {
  const usedOptionIds = new Set();
  Object.values(userAnswers.value).forEach(list => {
    if (Array.isArray(list)) {
      list.forEach(id => usedOptionIds.add(id));
    }
  });
  return props.question.options.filter(opt => !usedOptionIds.has(opt.id));
});

// وقتی سوال عوض می‌شود، همه چیز ریست شود
watch(() => props.question.id, () => {
  userAnswers.value = {};
  imageLoaded.value = false;
});

function onImageLoad() {
  imageLoaded.value = true;
  calculateScale();
}

function getOptionText(id) {
  const opt = props.question.options.find(o => o.id === id);
  return opt ? opt.text : id;
}

function getZoneTooltip(zoneId) {
  if (props.feedback && props.feedback[zoneId] === 'incorrect') {
    return 'پاسخ اشتباه است. کلیک کنید تا حذف شود.';
  }
  return 'برای حذف آخرین آیتم کلیک کنید';
}

// --- Drag & Drop Logic ---

function onDragStart(event, option) {
  // اگر فیدبک داده شده (یعنی سوال ثبت شده)، اجازه درگ نده
  if (props.feedback && Object.keys(props.feedback).length > 0) {
    event.preventDefault();
    return;
  }
  event.dataTransfer.dropEffect = 'move';
  event.dataTransfer.effectAllowed = 'move';
  event.dataTransfer.setData('optionId', option.id);
}

function onDragOver(zoneId) {
  if (props.feedback && Object.keys(props.feedback).length > 0) return;
  isDragOver.value = zoneId;
}

function onDragLeave() {
  isDragOver.value = null;
}

function onDrop(event, zoneId) {
  if (props.feedback && Object.keys(props.feedback).length > 0) return;
  
  const optionId = event.dataTransfer.getData('optionId');
  if (optionId) {
    if (!userAnswers.value[zoneId]) {
      userAnswers.value[zoneId] = [];
    }
    
    // جلوگیری از تکرار آیتم در یک زون (هرچند با منطق availableOptions نباید پیش بیاید)
    if (!userAnswers.value[zoneId].includes(optionId)) {
      userAnswers.value[zoneId].push(optionId);
      
      // کپی جدید برای واکنش‌گرایی Vue
      userAnswers.value = { ...userAnswers.value };
      emit('answer', userAnswers.value);
    }
  }
  isDragOver.value = null;
}

function removeLastItem(zoneId) {
  // اگر آزمون تمام شده، اجازه تغییر نده
  if (props.feedback && Object.keys(props.feedback).length > 0) return;

  if (userAnswers.value[zoneId] && userAnswers.value[zoneId].length > 0) {
    userAnswers.value[zoneId].pop(); // حذف آخرین آیتم
    
    if (userAnswers.value[zoneId].length === 0) {
      delete userAnswers.value[zoneId];
    }
    
    userAnswers.value = { ...userAnswers.value };
    emit('answer', userAnswers.value);
  }
}

// --- Scaling Logic (Responsive) ---

const calculateScale = () => {
  if (imageRef.value) {
    const img = imageRef.value.querySelector('.question-image');
    if (img && img.naturalWidth) {
      // محاسبه نسبت عرض فعلی به عرض اصلی عکس
      // 800 عرض فرضی است که مختصات zones بر اساس آن تنظیم شده‌اند (درصدگیری بهتر است)
      // اما اینجا فرض می‌کنیم مختصات درصدی (0 تا 100) از بک‌اند می‌آیند.
      // اگر مختصات بک‌اند درصدی باشند (x: 10 به معنی 10%) نیازی به scale نیست.
      // کد زیر برای حالتی است که x, y درصد هستند:
      scale.value = 1; 
    }
  }
};

const getZoneStyle = (zone) => {
  // فرض می‌کنیم x, y, width, height در دیتابیس به صورت درصد (0 تا 100) ذخیره شده‌اند
  return {
    left: `${zone.x}%`,
    top: `${zone.y}%`,
    width: `${zone.width}%`,
    height: `${zone.height}%`
  };
};

// گوش دادن به تغییر سایز پنجره
onMounted(() => {
  window.addEventListener('resize', calculateScale);
});

onUnmounted(() => {
  window.removeEventListener('resize', calculateScale);
});
</script>

<style scoped>
.image-labeling-container {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  width: 100%;
  max-width: 900px;
  margin: 0 auto;
}

.question-text {
  font-size: 1.2rem;
  font-weight: bold;
  color: #2c3e50;
  text-align: right;
  margin-bottom: 1rem;
}

.workspace {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  align-items: center;
}

/* --- Image Wrapper --- */
.image-wrapper {
  position: relative;
  width: 100%;
  max-width: 800px; /* حداکثر عرض عکس */
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  background-color: #f8f9fa;
  min-height: 300px; /* حداقل ارتفاع برای لودینگ */
  display: flex;
  justify-content: center;
  align-items: center;
}

.question-image {
  width: 100%;
  height: auto;
  display: block;
  transition: opacity 0.3s ease;
}

.question-image.hidden {
  opacity: 0;
  position: absolute;
}

.image-loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  color: #7f8c8d;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid var(--color-primary);
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 10px;
}

@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

/* --- Drop Zones --- */
.drop-zone {
  position: absolute;
  border: 2px dashed rgba(52, 152, 219, 0.6); /* آبی کمرنگ */
  background-color: rgba(255, 255, 255, 0.4);
  border-radius: 8px;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 0.2s ease;
  cursor: pointer;
  overflow: hidden; /* جلوگیری از بیرون زدن آیتم‌ها */
  padding: 2px;
}

.drop-zone:hover {
  background-color: rgba(255, 255, 255, 0.6);
  border-color: #3498db;
  z-index: 10; /* آمدن روی بقیه */
}

.drop-zone.is-over {
  background-color: rgba(46, 204, 113, 0.3); /* سبز هنگام درگ */
  border-color: #2ecc71;
  transform: scale(1.02);
}

.drop-zone.has-items {
  border-style: solid;
  border-color: #2c3e50;
  background-color: rgba(255, 255, 255, 0.85);
}

/* Feedback Styles */
.drop-zone.feedback-correct {
  border-color: #2ecc71;
  background-color: rgba(46, 204, 113, 0.2);
}

.drop-zone.feedback-incorrect {
  border-color: #e74c3c;
  background-color: rgba(231, 76, 60, 0.2);
}

.zone-placeholder {
  color: #555;
  font-weight: bold;
  opacity: 0.7;
  pointer-events: none;
}

.plus-icon {
  font-size: 1.5rem;
  line-height: 1;
}

/* --- Zone Badges (Items inside zone) --- */
.zone-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 3px;
  justify-content: center;
  align-items: center;
  width: 100%;
  max-height: 100%;
  overflow-y: auto; /* اگر زیاد شد اسکرول بخورد */
}

.mini-badge {
  background: #34495e;
  color: white;
  font-size: 0.7rem; /* فونت ریز برای جا شدن */
  padding: 2px 6px;
  border-radius: 4px;
  white-space: nowrap;
  box-shadow: 0 1px 3px rgba(0,0,0,0.2);
  max-width: 95%;
  overflow: hidden;
  text-overflow: ellipsis;
}

.feedback-icon {
  position: absolute;
  top: -10px;
  right: -10px;
  background: white;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0 2px 5px rgba(0,0,0,0.2);
  font-size: 0.8rem;
  z-index: 20;
}

/* --- Options Pool --- */
.options-pool {
  width: 100%;
  background-color: #f1f2f6;
  padding: 1.5rem;
  border-radius: 12px;
  border: 1px solid #dfe4ea;
}

.pool-title {
  font-size: 1rem;
  color: #57606f;
  margin-bottom: 1rem;
  font-weight: bold;
}

.options-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 0.8rem;
  justify-content: center;
}

.draggable-option {
  background-color: white;
  padding: 0.6rem 1.2rem;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.05);
  cursor: grab;
  font-weight: 500;
  color: #2f3542;
  border: 1px solid #ced6e0;
  transition: all 0.2s;
  user-select: none;
}

.draggable-option:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  border-color: var(--color-primary);
}

.draggable-option:active {
  cursor: grabbing;
}

.options-pool.empty {
  text-align: center;
  color: #a4b0be;
  font-style: italic;
  padding: 2rem;
}

/* Mobile Adjustments */
@media (max-width: 600px) {
  .mini-badge {
    font-size: 0.6rem;
    padding: 1px 3px;
  }
  .draggable-option {
    font-size: 0.9rem;
    padding: 0.5rem 0.8rem;
  }
}
</style>