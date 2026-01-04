<template>
  <div class="multiple-select-container">
    <p class="instruction">{{ question.instruction }}</p>

    <div class="options-grid">
      <div 
        v-for="option in question.options" 
        :key="option.id"
        class="option-card"
        :class="{ 
          'selected': selectedOptions.includes(option.id),
          'correct': feedback[option.id] === 'correct',
          'incorrect': feedback[option.id] === 'incorrect',
          'disabled': disabled
        }"
        @click="toggleOption(option.id)"
      >
        <div class="checkbox-indicator">
          <font-awesome-icon v-if="selectedOptions.includes(option.id)" icon="fas fa-check" />
        </div>
        <span class="option-text">{{ option.text }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';

const props = defineProps({
  question: { type: Object, required: true },
  feedback: { type: Object, default: () => ({}) },
  disabled: { type: Boolean, default: false }
});

const emit = defineEmits(['update:answer']);
const selectedOptions = ref([]);

// اگر سوال تغییر کرد، انتخاب‌ها را ریست کن
watch(() => props.question, () => {
  selectedOptions.value = [];
  emit('update:answer', []);
});

const toggleOption = (optionId) => {
  if (props.disabled) return;

  if (selectedOptions.value.includes(optionId)) {
    // حذف از انتخاب‌ها
    selectedOptions.value = selectedOptions.value.filter(id => id !== optionId);
  } else {
    // افزودن به انتخاب‌ها
    selectedOptions.value.push(optionId);
  }
  emit('update:answer', selectedOptions.value);
};
</script>

<style scoped>
.multiple-select-container {
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
}

.instruction {
  font-size: 1.2rem;
  color: #555;
  margin-bottom: 1.5rem;
  text-align: right;
  line-height: 1.8;
}

.options-grid {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.option-card {
  display: flex;
  align-items: center;
  background-color: white;
  border: 2px solid #e5e5e5;
  border-radius: 12px;
  padding: 1rem 1.5rem;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.25, 0.8, 0.25, 1);
  user-select: none;
  position: relative;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0,0,0,0.02);
}

.option-card:hover:not(.disabled) {
  transform: translateY(-2px);
  border-color: #b0bec5;
  box-shadow: 0 6px 12px rgba(0,0,0,0.05);
}

.option-card:active:not(.disabled) {
  transform: scale(0.98);
}

/* حالت انتخاب شده */
.option-card.selected {
  border-color: #0c54c4; /* رنگ اصلی */
  background-color: #e3f2fd;
}

.checkbox-indicator {
  width: 24px;
  height: 24px;
  border: 2px solid #bdbdbd;
  border-radius: 6px;
  margin-left: 1rem;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: white;
  color: white;
  transition: all 0.2s;
  flex-shrink: 0;
}

.option-card.selected .checkbox-indicator {
  background-color: #0c54c4;
  border-color: #0c54c4;
}

.option-text {
  font-size: 1.1rem;
  font-weight: 500;
  color: #333;
}

/* --- Feedback Styles --- */
.option-card.correct {
  border-color: #58cc02;
  background-color: #d7ffb8;
  color: #58a700;
}
.option-card.correct .checkbox-indicator {
  background-color: #58cc02;
  border-color: #58cc02;
}

.option-card.incorrect {
  border-color: #ff4b4b;
  background-color: #ffdfe0;
  color: #d32f2f;
}
.option-card.incorrect .checkbox-indicator {
  background-color: #ff4b4b;
  border-color: #ff4b4b;
}

.option-card.disabled {
  opacity: 0.8;
  cursor: default;
}
</style>