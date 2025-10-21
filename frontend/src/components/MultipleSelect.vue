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
.instruction {
  font-size: 1.2rem;
  margin-bottom: 1.5rem;
  text-align: center;
}

.options-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

.option-card {
  background-color: #fff;
  border: 2px solid #e5e5e5;
  border-bottom-width: 4px; /* سبک دکمه‌ای دولینگو */
  border-radius: 12px;
  padding: 1.5rem 1rem;
  cursor: pointer;
  user-select: none;
  font-size: 1.1rem;
  font-weight: bold;
  color: #4b4b4b;
  transition: background-color 0.2s, border-color 0.2s, transform 0.1s;
}

.option-card:hover:not(.disabled) {
  background-color: #f7f7f7;
}

.option-card:active:not(.disabled) {
  transform: translateY(2px); /* حس فشرده شدن دکمه */
  border-bottom-width: 2px;
}

/* حالت انتخاب شده */
.option-card.selected {
  background-color: #d7ffb8;
  border-color: #84e100;
  color: #58a700;
}

/* حالت‌های بازخورد بعد از بررسی */
.option-card.correct {
  background-color: #d7ffb8;
  border-color: #84e100;
  color: #58a700;
}

.option-card.incorrect {
  background-color: #ffdfe0;
  border-color: #ffc1c3;
  color: #ea2b2b;
  opacity: 0.8;
}

.option-card.disabled {
  cursor: not-allowed;
  opacity: 0.7;
}

/* وقتی جوابی بررسی شده و این گزینه انتخاب نشده بود */
.option-card.disabled:not(.selected):not(.correct):not(.incorrect) {
   background-color: #f7f7f7;
   opacity: 0.5;
}
</style>