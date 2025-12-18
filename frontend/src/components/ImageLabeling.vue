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
import { ref, computed, onMounted, onUnmounted, watch, nextTick } from 'vue';

const props = defineProps(['question', 'feedback']);
const emit = defineEmits(['answer']);

const userAnswers = ref({}); 
const isDragOver = ref(null);
const imageRef = ref(null);
const imgElement = ref(null); // رفرنس مستقیم به تگ img

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

// ریست کردن وضعیت با تغییر سوال
watch(() => props.question.id, () => {
  userAnswers.value = {};
  imageLoaded.value = false;
  imageError.value = false;
});

function onImageLoad() {
  imageLoaded.value = true;
  imageError.value = false;
  calculateScale();
}

function onImageError() {
  console.error("خطا در بارگذاری تصویر:", props.question.image);
  imageLoaded.value = false;
  imageError.value = true;
}

function retryImage() {
  imageError.value = false;
  imageLoaded.value = false;
  if (imgElement.value) {
    // ترفند برای لود مجدد عکس با تغییر کوئری استرینگ
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
  if (props.feedback && props.feedback[zoneId] === 'incorrect') {
    return 'پاسخ اشتباه است. کلیک کنید تا حذف شود.';
  }
  return 'برای حذف آخرین آیتم کلیک کنید';
}

// --- Drag & Drop Logic ---

function onDragStart(event, option) {
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
    
    if (!userAnswers.value[zoneId].includes(optionId)) {
      userAnswers.value[zoneId].push(optionId);
      userAnswers.value = { ...userAnswers.value };
      emit('answer', userAnswers.value);
    }
  }
  isDragOver.value = null;
}

function removeLastItem(zoneId) {
  if (props.feedback && Object.keys(props.feedback).length > 0) return;

  if (userAnswers.value[zoneId] && userAnswers.value[zoneId].length > 0) {
    userAnswers.value[zoneId].pop();
    if (userAnswers.value[zoneId].length === 0) {
      delete userAnswers.value[zoneId];
    }
    userAnswers.value = { ...userAnswers.value };
    emit('answer', userAnswers.value);
  }
}

// --- Scaling Logic ---
const scale = ref(1);
const calculateScale = () => {
  // اگر نیاز به محاسبات خاصی روی سایز عکس بود اینجا قرار میگیرد
  // فعلا برای ریسپانسیو بودن CSS کافی است
  scale.value = 1; 
};

const getZoneStyle = (zone) => {
  return {
    left: `${zone.x}%`,
    top: `${zone.y}%`,
    width: `${zone.width}%`,
    height: `${zone.height}%`
  };
};

onMounted(() => {
  window.addEventListener('resize', calculateScale);
  
  // بررسی اینکه آیا عکس از کش لود شده است؟
  if (imgElement.value && imgElement.value.complete) {
    if (imgElement.value.naturalWidth > 0) {
        onImageLoad();
    } 
  }
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
  max-width: 800px;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  background-color: #f8f9fa;
  min-height: 300px;
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
  width: 0; 
  height: 0;
}

.image-loading, .image-error-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #7f8c8d;
  width: 100%;
  height: 100%;
  min-height: 300px;
  text-align: center;
}

.image-error-state p {
    color: #e74c3c;
    font-weight: bold;
    margin-bottom: 1rem;
}

.btn-retry {
    padding: 0.5rem 1rem;
    background: #e74c3c;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
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

/* --- Zone Badges --- */
.zone-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 3px;
  justify-content: center;
  align-items: center;
  width: 100%;
  max-height: 100%;
  overflow-y: auto;
}

.mini-badge {
  background: #34495e;
  color: white;
  font-size: 0.7rem;
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