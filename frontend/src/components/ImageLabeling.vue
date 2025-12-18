<template>
  <div class="image-labeling-container">
    <p class="instruction">{{ question.instruction }}</p>

    <div class="image-wrapper">
      <img :src="question.question_image" class="base-image" alt="Structure" />
      
      <div 
        v-for="zone in question.drop_zones" 
        :key="zone.id"
        class="drop-zone"
        :style="{ top: zone.top, left: zone.left, width: zone.width, height: zone.height }"
        :class="{ 
          'filled': !!userAnswers[zone.id],
          'correct': feedback[zone.id] === 'correct',
          'incorrect': feedback[zone.id] === 'incorrect',
          'highlight-target': selectedOptionId
        }"
        @click="onZoneClick(zone.id)"
      >
        <div 
          v-if="userAnswers[zone.id]" 
          class="placed-item"
          @click.stop="onPlacedItemClick(zone.id)"
        >
          <img v-if="getItemById(userAnswers[zone.id]).image" :src="getItemById(userAnswers[zone.id]).image" class="option-img-mini" />
          <span v-else>{{ getItemById(userAnswers[zone.id]).text }}</span>
        </div>
      </div>
    </div>

    <div class="options-bank">
      <div 
        v-for="option in availableOptions" 
        :key="option.id"
        class="option-card"
        :class="{ 'selected': selectedOptionId === option.id }"
        @click="onOptionClick(option)"
      >
        <img v-if="option.image" :src="option.image" class="option-img" />
        <span v-else>{{ option.text }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue';

const props = defineProps({
  question: { type: Object, required: true },
  feedback: { type: Object, default: () => ({}) },
  disabled: { type: Boolean, default: false }
});

const emit = defineEmits(['update:answer']);

const userAnswers = ref({}); // { zone-1: opt-1, ... }
const selectedOptionId = ref(null);

watch(() => props.question, () => {
  userAnswers.value = {};
  selectedOptionId.value = null;
}, { immediate: true });

// گزینه‌هایی که هنوز استفاده نشده‌اند
const availableOptions = computed(() => {
  const usedIds = Object.values(userAnswers.value);
  return props.question.options.filter(opt => !usedIds.includes(opt.id));
});

const getItemById = (id) => props.question.options.find(o => o.id === id);

// --- منطق کلیک (Tap to Move) ---

// ۱. کلیک روی گزینه در بانک
const onOptionClick = (option) => {
  if (props.disabled) return;
  if (selectedOptionId.value === option.id) {
    selectedOptionId.value = null; // لغو انتخاب
  } else {
    selectedOptionId.value = option.id;
  }
};

// ۲. کلیک روی ناحیه دراپ (روی عکس)
const onZoneClick = (zoneId) => {
  if (props.disabled) return;
  
  // اگر گزینه‌ای انتخاب شده، آن را اینجا قرار بده
  if (selectedOptionId.value) {
    userAnswers.value[zoneId] = selectedOptionId.value;
    selectedOptionId.value = null;
    emit('update:answer', userAnswers.value);
  }
};

// ۳. کلیک روی آیتمی که قبلاً روی عکس گذاشته‌ایم (برای حذف)
const onPlacedItemClick = (zoneId) => {
  if (props.disabled) return;
  // حذف گزینه از زون و بازگشت به بانک
  delete userAnswers.value[zoneId];
  emit('update:answer', userAnswers.value);
};
</script>

<style scoped>
.image-labeling-container { display: flex; flex-direction: column; align-items: center; gap: 1.5rem; width: 100%; }
.instruction { font-size: 1.1rem; color: #555; margin: 0; }

.image-wrapper { position: relative; display: inline-block; max-width: 100%; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border: 2px solid #eee; }
.base-image { display: block; max-width: 100%; height: auto; user-select: none; }

/* ناحیه‌های دراپ */
.drop-zone {
  position: absolute;
  background-color: rgba(255, 255, 255, 0.4);
  border: 2px dashed #3c3c3c;
  border-radius: 8px;
  cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  transition: all 0.2s;
}
.drop-zone:hover { background-color: rgba(255, 255, 255, 0.6); }
.drop-zone.highlight-target { border-color: var(--color-primary); background-color: rgba(66, 185, 131, 0.2); animation: pulse 1.5s infinite; }
.drop-zone.filled { border-style: solid; background-color: white; box-shadow: 0 2px 5px rgba(0,0,0,0.2); border-color: #bbb; }

/* بازخورد صحیح/غلط */
.drop-zone.correct { border-color: #58cc02; background-color: #d7ffb8; color: #58cc02; }
.drop-zone.incorrect { border-color: #ff4b4b; background-color: #ffdfe0; color: #ff4b4b; }

.placed-item { width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.9rem; text-align: center; overflow: hidden; }
.option-img-mini { width: 100%; height: 100%; object-fit: contain; }

/* بانک گزینه‌ها */
.options-bank { display: flex; flex-wrap: wrap; gap: 0.8rem; justify-content: center; background: #f8f8f8; padding: 1rem; border-radius: 12px; width: 100%; }
.option-card { background: white; border: 2px solid #e0e0e0; padding: 0.5rem 1rem; border-radius: 8px; cursor: pointer; transition: all 0.2s; font-weight: bold; min-width: 80px; text-align: center; }
.option-card:hover { transform: translateY(-2px); border-color: #bbb; }
.option-card.selected { border-color: var(--color-primary); background-color: var(--color-primary-light); transform: scale(1.05); }

.option-img { max-height: 50px; display: block; margin: 0 auto; }

@keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.6; } 100% { opacity: 1; } }
</style>