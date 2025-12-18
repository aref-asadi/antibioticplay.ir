<template>
  <div class="image-labeling-container">
    <p class="question-text">{{ question.text }}</p>

    <div class="workspace">
      <div class="image-wrapper" ref="imageRef">
        
        <div v-if="isLoading" class="image-loading">
          <div class="spinner"></div>
          <p>در حال بارگذاری تصویر...</p>
        </div>

        <div v-if="imageError" class="image-error-state">
          <p>متاسفانه تصویر بارگذاری نشد.</p>
          <button @click="retryImage" class="btn-retry">تلاش مجدد</button>
        </div>

        <img 
          ref="imgElement"
          :src="question.image" 
          :alt="question.text" 
          class="question-image" 
          :class="{ 'hidden': !imageLoaded || imageError }"
          @load="onImageLoad"
          @error="onImageError"
        />
        
        <template v-if="imageLoaded && !imageError">
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
            @click="handleZoneClick(zone.id)"
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
        <p class="pool-title">گزینه‌ها را بکشید یا کلیک کنید:</p>
        <div class="options-grid">
          <div 
            v-for="option in availableOptions" 
            :key="option.id"
            class="draggable-option"
            :class="{ 'selected': selectedOptionId === option.id }"
            draggable="true"
            @dragstart="onDragStart($event, option)"
            @click="toggleSelection(option)"
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
import { ref, computed, onMounted, onUnmounted, watch, nextTick } from 'vue';

const props = defineProps(['question', 'feedback']);
const emit = defineEmits(['answer']);

const userAnswers = ref({});
const isDragOver = ref(null);
const imageRef = ref(null);
const imgElement = ref(null);
const selectedOptionId = ref(null); // برای حالت کلیکی (موبایل)

const imageLoaded = ref(false);
const imageError = ref(false);

const isLoading = computed(() => !imageLoaded.value && !imageError.value);

// محاسبه گزینه‌های باقی‌مانده
const availableOptions = computed(() => {
  const usedOptionIds = new Set();
  Object.values(userAnswers.value).forEach(list => {
    if (Array.isArray(list)) {
      list.forEach(id => usedOptionIds.add(id));
    }
  });
  return props.question.options.filter(opt => !usedOptionIds.has(opt.id));
});

watch(() => props.question.id, () => {
  userAnswers.value = {};
  imageLoaded.value = false;
  imageError.value = false;
  selectedOptionId.value = null;
});

function onImageLoad() {
  imageLoaded.value = true;
  imageError.value = false;
}

function onImageError() {
  imageLoaded.value = false;
  imageError.value = true;
}

function retryImage() {
  imageError.value = false;
  imageLoaded.value = false;
  if (imgElement.value) {
    const src = props.question.image;
    imgElement.value.src = '';
    nextTick(() => {
        imgElement.value.src = src + '?t=' + new Date().getTime();
    });
  }
}

function getOptionText(id) {
  const opt = props.question.options.find(o => o.id === id);
  return opt ? opt.text : id;
}

function getZoneTooltip(zoneId) {
  if (props.feedback) return '';
  return selectedOptionId.value ? 'کلیک کنید تا گزینه اضافه شود' : 'کلیک کنید تا آخرین گزینه حذف شود';
}

// --- Interaction Logic (Drag & Click) ---

// 1. انتخاب گزینه با کلیک (برای موبایل)
function toggleSelection(option) {
  if (props.feedback && Object.keys(props.feedback).length > 0) return;
  
  if (selectedOptionId.value === option.id) {
    selectedOptionId.value = null; // لغو انتخاب
  } else {
    selectedOptionId.value = option.id; // انتخاب
  }
}

// 2. هندل کردن کلیک روی زون (هم برای افزودن و هم حذف)
function handleZoneClick(zoneId) {
  if (props.feedback && Object.keys(props.feedback).length > 0) return;

  if (selectedOptionId.value) {
    // اگر گزینه‌ای انتخاب شده، آن را به زون اضافه کن
    addItemToZone(zoneId, selectedOptionId.value);
    selectedOptionId.value = null; // پاک کردن انتخاب بعد از اضافه کردن
  } else {
    // اگر چیزی انتخاب نشده، آخرین آیتم زون را حذف کن
    removeLastItem(zoneId);
  }
}

function onDragStart(event, option) {
  if (props.feedback && Object.keys(props.feedback).length > 0) {
    event.preventDefault();
    return;
  }
  selectedOptionId.value = option.id; // برای هماهنگی با کلیک
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
    addItemToZone(zoneId, optionId);
  }
  isDragOver.value = null;
  selectedOptionId.value = null;
}

// تابع کمکی برای اضافه کردن آیتم
function addItemToZone(zoneId, optionId) {
  if (!userAnswers.value[zoneId]) {
    userAnswers.value[zoneId] = [];
  }
  
  if (!userAnswers.value[zoneId].includes(optionId)) {
    userAnswers.value[zoneId].push(optionId);
    
    // کپی جدید برای تریگر کردن reactivity
    const newAnswer = { ...userAnswers.value };
    userAnswers.value = newAnswer;
    emit('answer', newAnswer);
  }
}

function removeLastItem(zoneId) {
  if (userAnswers.value[zoneId] && userAnswers.value[zoneId].length > 0) {
    userAnswers.value[zoneId].pop();
    
    if (userAnswers.value[zoneId].length === 0) {
      delete userAnswers.value[zoneId];
    }
    
    const newAnswer = { ...userAnswers.value };
    userAnswers.value = newAnswer;
    emit('answer', newAnswer);
  }
}

// --- Scaling Logic ---
const getZoneStyle = (zone) => {
  return {
    left: `${zone.x}%`,
    top: `${zone.y}%`,
    width: `${zone.width}%`,
    height: `${zone.height}%`
  };
};

onMounted(() => {
  if (imgElement.value && imgElement.value.complete) {
    if (imgElement.value.naturalWidth > 0) onImageLoad();
  }
});
</script>

<style scoped>
.image-labeling-container {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  width: 100%;
  max-width: 900px; /* حداکثر عرض کلی */
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
  /* نکته مهم: این تنظیمات باعث می‌شود رپر به اندازه عکس کوچک شود */
  display: inline-block; 
  width: auto;
  max-width: 100%;
  
  /* محدودیت ارتفاع برای جلوگیری از اسکرول زیاد */
  max-height: 60vh; 
  
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  background-color: #f8f9fa;
  min-height: 200px;
  overflow: hidden; /* جلوگیری از بیرون زدن */
}

.question-image {
  display: block;
  width: auto;
  height: auto;
  max-width: 100%;
  /* ارتفاع عکس محدود به ارتفاع رپر می‌شود */
  max-height: 60vh; 
  object-fit: contain; /* حفظ نسبت تصویر */
  transition: opacity 0.3s ease;
}

.question-image.hidden {
  opacity: 0;
  position: absolute;
}

.image-loading, .image-error-state {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #7f8c8d;
  background: #f8f9fa;
  min-height: 300px;
  text-align: center;
}

.image-error-state p { color: #e74c3c; font-weight: bold; margin-bottom: 1rem; }
.btn-retry { padding: 0.5rem 1rem; background: #e74c3c; color: white; border: none; border-radius: 6px; cursor: pointer; }
.spinner { width: 40px; height: 40px; border: 4px solid #f3f3f3; border-top: 4px solid var(--color-primary); border-radius: 50%; animation: spin 1s linear infinite; margin-bottom: 10px; }
@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

/* --- Drop Zones --- */
.drop-zone {
  position: absolute;
  border: 2px dashed rgba(52, 152, 219, 0.6);
  background-color: rgba(255, 255, 255, 0.4);
  border-radius: 8px;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 0.2s ease;
  cursor: pointer;
  overflow: hidden;
  padding: 2px;
}

.drop-zone:hover {
  background-color: rgba(255, 255, 255, 0.6);
  border-color: #3498db;
  z-index: 10;
}

.drop-zone.is-over {
  background-color: rgba(46, 204, 113, 0.3);
  border-color: #2ecc71;
  transform: scale(1.02);
}

.drop-zone.has-items {
  border-style: solid;
  border-color: #2c3e50;
  background-color: rgba(255, 255, 255, 0.85);
}

/* Feedback Styles */
.drop-zone.feedback-correct { border-color: #2ecc71; background-color: rgba(46, 204, 113, 0.2); }
.drop-zone.feedback-incorrect { border-color: #e74c3c; background-color: rgba(231, 76, 60, 0.2); }

.zone-placeholder { color: #555; font-weight: bold; opacity: 0.7; pointer-events: none; }
.plus-icon { font-size: 1.5rem; line-height: 1; }

/* --- Zone Badges --- */
.zone-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 2px;
  justify-content: center;
  align-items: center;
  width: 100%;
  max-height: 100%;
  overflow-y: auto;
}

.mini-badge {
  background: #34495e;
  color: white;
  font-size: 0.65rem;
  padding: 2px 4px;
  border-radius: 4px;
  white-space: nowrap;
  box-shadow: 0 1px 2px rgba(0,0,0,0.2);
  max-width: 98%;
  overflow: hidden;
  text-overflow: ellipsis;
}

.feedback-icon {
  position: absolute;
  top: -8px; right: -8px;
  background: white;
  border-radius: 50%;
  width: 20px; height: 20px;
  display: flex; justify-content: center; align-items: center;
  box-shadow: 0 2px 5px rgba(0,0,0,0.2);
  font-size: 0.8rem; z-index: 20;
}

/* --- Options Pool --- */
.options-pool {
  width: 100%;
  background-color: #f1f2f6;
  padding: 1.5rem;
  border-radius: 12px;
  border: 1px solid #dfe4ea;
}

.pool-title { font-size: 1rem; color: #57606f; margin-bottom: 1rem; font-weight: bold; }
.options-grid { display: flex; flex-wrap: wrap; gap: 0.8rem; justify-content: center; }

.draggable-option {
  background-color: white;
  padding: 0.6rem 1rem;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.05);
  cursor: pointer; /* تغییر به پوینتر برای نشان دادن قابلیت کلیک */
  font-weight: 500;
  color: #2f3542;
  border: 2px solid transparent; /* برای جلوگیری از پرش موقع بوردر دادن */
  border-color: #ced6e0;
  transition: all 0.2s;
  user-select: none;
  font-size: 0.9rem;
}

.draggable-option:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  border-color: var(--color-primary);
}

/* کلاس برای حالت انتخاب شده (کلیک شده) */
.draggable-option.selected {
  background-color: #e3f2fd; /* آبی کمرنگ */
  border-color: var(--color-primary);
  transform: scale(1.05);
  box-shadow: 0 0 0 3px rgba(66, 185, 131, 0.2); /* حلقه دور */
}

.draggable-option:active { cursor: grabbing; }
.options-pool.empty { text-align: center; color: #a4b0be; font-style: italic; padding: 2rem; }

@media (max-width: 600px) {
  .image-wrapper { max-height: 50vh; }
  .mini-badge { font-size: 0.55rem; padding: 1px 3px; }
  .draggable-option { font-size: 0.85rem; padding: 0.5rem 0.8rem; }
}
</style>