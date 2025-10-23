<template>
  <div class="multiple-select-container">
    <p class="instruction">{{ question.instruction }}</p>

    <div class="options-grid">
      <div
        v-for="option in question.options"
        :key="option"
        class="option-card"
        :class="{ 
          'selected': isSelected(option), 
          'correct': feedback[option] === 'correct', 
          'incorrect': feedback[option] === 'incorrect',
          'disabled': disabled 
        }"
        @click="toggleSelection(option)"
      >
        {{ option }}
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

// یک آرایه برای نگهداری گزینه‌های انتخاب شده توسط کاربر
const selectedOptions = ref([]);

// چک می‌کند که آیا یک گزینه در آرایه انتخاب‌ها وجود دارد یا نه
const isSelected = (option) => {
  return selectedOptions.value.includes(option);
};

// تابع اصلی برای انتخاب یا عدم انتخاب یک گزینه
const toggleSelection = (option) => {
  if (props.disabled) return; // اگر آزمون قفل شده، کاری نکن

  const index = selectedOptions.value.indexOf(option);
  if (index > -1) {
    // اگر از قبل انتخاب شده بود، آن را حذف کن
    selectedOptions.value.splice(index, 1);
  } else {
    // اگر انتخاب نشده بود، آن را اضافه کن
    selectedOptions.value.push(option);
  }

  // جواب جدید (آرایه انتخاب‌ها) را به کامپوننت والد (QuizPage) بفرست
  emit('update:answer', selectedOptions.value);
};

// با رفتن به سوال بعدی، انتخاب‌های قبلی را پاک کن
watch(() => props.question, () => {
  selectedOptions.value = [];
  emit('update:answer', []);
});
</script>

<style scoped>
  .instruction { font-size: 1.2rem; margin-bottom: 1.5rem; text-align: center; color: var(--color-text); }
  .options-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; }
  .option-card { /* Base styles from .card in style.css */
    padding: 1rem !important; /* Slightly override card padding */
    cursor: pointer;
    user-select: none;
    font-size: 1rem; /* Slightly smaller text */
    font-weight: bold;
    color: var(--color-text-light); /* Default gray text */
    border-color: var(--color-border); /* Default border color */
    background-color: var(--color-background-light); /* Default white */
    text-align: center; /* Center text */
  }
  .option-card:active:not(.disabled) { transform: translateY(1px); border-bottom-width: 3px; } /* Adjust press effect */
  .option-card.selected { background-color: #e8f8d7; border-color: var(--color-primary); color: var(--color-primary-dark); }
  .option-card.correct { background-color: #d7ffb8 !important; border-color: var(--color-primary-dark) !important; color: var(--color-primary-dark) !important; }
  .option-card.incorrect { background-color: #ffdfe0 !important; border-color: var(--color-danger-dark) !important; color: var(--color-danger-dark) !important; opacity: 0.8; }
  .option-card.disabled { cursor: not-allowed; opacity: 0.7; }
  .option-card.disabled:not(.selected):not(.correct):not(.incorrect) { background-color: var(--color-background-page); opacity: 0.6; }
</style>