<template>
  <div class="image-labeling-container">
    <p class="instruction">{{ question.instruction }}</p>

    <div class="image-wrapper">
      <img :src="question.question_image" class="base-image" alt="Question Image" />
      
      <div 
        v-for="zone in question.drop_zones" 
        :key="zone.id"
        class="drop-zone"
        :style="{ top: zone.top, left: zone.left, width: zone.width, height: zone.height }"
        :class="{ 
          'filled': !!userAnswers[zone.id],
          'correct': feedback && feedback[zone.id] === 'correct',   /* اضافه شده: کلاس سبز */
          'incorrect': feedback && feedback[zone.id] === 'incorrect', /* اضافه شده: کلاس قرمز */
          'highlight-target': selectedOptionId && !userAnswers[zone.id] && !feedback[zone.id]
        }"
        @click="onZoneClick(zone.id)"
      >
        <transition name="pop">
          <div 
            v-if="userAnswers[zone.id]" 
            class="placed-item"
            @click.stop="onPlacedItemClick(zone.id)"
          >
            <img v-if="getItemById(userAnswers[zone.id])?.image" :src="getItemById(userAnswers[zone.id]).image" class="option-img-mini" />
            <span v-else>{{ getItemById(userAnswers[zone.id])?.text }}</span>
          </div>
        </transition>

        <div v-if="feedback && feedback[zone.id]" class="feedback-icon">
             <font-awesome-icon :icon="feedback[zone.id] === 'correct' ? 'fas fa-check' : 'fas fa-times'" />
        </div>
      </div>
    </div>

    <div class="options-bank" :class="{ 'disabled': disabled }">
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
import { library } from '@fortawesome/fontawesome-svg-core';
import { faCheck, faTimes } from '@fortawesome/free-solid-svg-icons';

library.add(faCheck, faTimes);

const props = defineProps({
  question: { type: Object, required: true },
  feedback: { type: Object, default: () => ({}) },
  disabled: { type: Boolean, default: false }
});

const emit = defineEmits(['update:answer']);

const userAnswers = ref({}); // { zone-1: opt-1, ... }
const selectedOptionId = ref(null);

// ریست کردن وقتی سوال عوض میشه
watch(() => props.question, () => {
  userAnswers.value = {};
  selectedOptionId.value = null;
}, { immediate: true });

// گزینه‌هایی که هنوز استفاده نشده‌اند (برای نمایش در پایین)
const availableOptions = computed(() => {
  const usedIds = Object.values(userAnswers.value);
  return props.question.options.filter(opt => !usedIds.includes(opt.id));
});

const getItemById = (id) => props.question.options.find(o => o.id === id);

// --- منطق کلیک (Tap to Move) ---

const onOptionClick = (option) => {
  if (props.disabled) return;
  if (selectedOptionId.value === option.id) {
    selectedOptionId.value = null; // لغو انتخاب
  } else {
    selectedOptionId.value = option.id;
  }
};

const onZoneClick = (zoneId) => {
  if (props.disabled) return;
  
  // اگر گزینه‌ای انتخاب شده، آن را اینجا قرار بده
  if (selectedOptionId.value) {
    // اگر قبلاً چیزی اینجا بوده، برش گردون به بانک (با جایگزینی)
    userAnswers.value[zoneId] = selectedOptionId.value;
    selectedOptionId.value = null;
    emit('update:answer', userAnswers.value);
  }
};

const onPlacedItemClick = (zoneId) => {
  if (props.disabled) return;
  // حذف گزینه از زون و بازگشت به بانک
  delete userAnswers.value[zoneId];
  emit('update:answer', userAnswers.value);
};
</script>

<style scoped>
.image-labeling-container { display: flex; flex-direction: column; align-items: center; gap: 1.5rem; width: 100%; }
.instruction { font-size: 1.1rem; color: #555; margin: 0; text-align: center; }

.image-wrapper { position: relative; display: inline-block; max-width: 100%; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border: 2px solid #eee; background: white; }
.base-image { display: block; max-width: 100%; height: auto; user-select: none; pointer-events: none; }

/* --- Drop Zone Styles --- */
.drop-zone {
  position: absolute;
  background-color: rgba(255, 255, 255, 0.6);
  border: 2px dashed #3c3c3c;
  border-radius: 8px;
  cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  transition: all 0.2s;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.drop-zone:hover:not(.filled) { background-color: rgba(255, 255, 255, 0.8); }

.drop-zone.highlight-target { 
  border-color: var(--color-primary); 
  background-color: rgba(66, 185, 131, 0.3); 
  animation: pulse 1.5s infinite; 
}

.drop-zone.filled { 
  border-style: solid; 
  background-color: white; 
  border-color: #bbb; 
}

/* --- Feedback Styles (Red & Green) --- */
.drop-zone.correct { 
  border-color: #58cc02 !important; 
  background-color: #d7ffb8 !important; 
  color: #58cc02;
  border-style: solid;
}

.drop-zone.incorrect { 
  border-color: #ff4b4b !important; 
  background-color: #ffdfe0 !important; 
  color: #ff4b4b;
  border-style: solid;
}

.feedback-icon {
  position: absolute;
  top: -10px;
  right: -10px;
  width: 24px; height: 24px;
  border-radius: 50%;
  color: white;
  display: flex; align-items: center; justify-content: center;
  font-size: 0.8rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.2);
  z-index: 10;
}
.drop-zone.correct .feedback-icon { background-color: #58cc02; }
.drop-zone.incorrect .feedback-icon { background-color: #ff4b4b; }

/* --- Item Styles --- */
.placed-item { width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.85rem; text-align: center; overflow: hidden; padding: 2px; }
.option-img-mini { width: 100%; height: 100%; object-fit: contain; }

/* --- Bank Styles --- */
.options-bank { display: flex; flex-wrap: wrap; gap: 0.8rem; justify-content: center; background: #f8f8f8; padding: 1rem; border-radius: 12px; width: 100%; border: 2px solid #eee; min-height: 80px; }
.options-bank.disabled { opacity: 0.6; pointer-events: none; filter: grayscale(1); }

.option-card { 
  background: white; border: 2px solid #e0e0e0; padding: 0.5rem 1rem; 
  border-radius: 12px; cursor: pointer; transition: all 0.2s; 
  font-weight: bold; min-width: 80px; text-align: center; 
  box-shadow: 0 2px 0 #e0e0e0;
}
.option-card:hover { transform: translateY(-2px); }
.option-card:active { transform: translateY(0); box-shadow: none; }

.option-card.selected { 
  border-color: var(--color-primary); 
  background-color: var(--color-primary-light); 
  color: var(--color-primary-dark);
  transform: scale(1.05); 
}

.option-img { max-height: 40px; display: block; margin: 0 auto; }

/* Animations */
@keyframes pulse { 0% { opacity: 1; transform: scale(1); } 50% { opacity: 0.8; transform: scale(1.02); } 100% { opacity: 1; transform: scale(1); } }
.pop-enter-active { animation: popIn 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
@keyframes popIn { from { opacity: 0; transform: scale(0.5); } to { opacity: 1; transform: scale(1); } }
</style>