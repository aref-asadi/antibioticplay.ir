<template>
  <div class="true-false-container">
    <p class="instruction">{{ question.instruction }}</p>

    <div class="statements-list">
      <div 
        v-for="statement in question.statements" 
        :key="statement.id" 
        class="statement-row"
        :class="{ 
          'correct': feedback[statement.id] === 'correct', 
          'incorrect': feedback[statement.id] === 'incorrect' 
        }"
      >
        <p class="statement-text">{{ statement.text }}</p>

        <div class="button-group">
          <button
            class="tf-button true-button"
            :class="{ 'selected': userAnswers[statement.id] === true }"
            :disabled="disabled"
            @click="selectAnswer(statement.id, true)"
          >
            درست
          </button>
          <button
            class="tf-button false-button"
            :class="{ 'selected': userAnswers[statement.id] === false }"
            :disabled="disabled"
            @click="selectAnswer(statement.id, false)"
          >
            نادرست
          </button>
        </div>
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

// یک آبجکت برای نگهداری جواب‌های کاربر
// e.g., { 'tf-1-1': true, 'tf-1-2': false }
const userAnswers = ref({});

const selectAnswer = (statementId, answer) => {
  if (props.disabled) return;

  userAnswers.value[statementId] = answer;

  // ارسال آبجکت کامل جواب‌ها به کامپوننت والد
  emit('update:answer', userAnswers.value);
};

// با رفتن به سوال بعدی، جواب‌های قبلی را پاک کن
watch(() => props.question, (newQuestion) => {
  userAnswers.value = {};
  // مقدار اولیه را null می‌فرستیم تا دکمه "بررسی" غیرفعال شود
  emit('update:answer', null);
}, { immediate: true });

</script>

<style scoped>
.instruction {
  font-size: 1.2rem;
  margin-bottom: 2rem;
  text-align: center;
}

.statements-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.statement-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #fff;
  border: 2px solid #e5e5e5;
  border-radius: 12px;
  padding: 1rem 1.5rem;
  transition: border-color 0.3s, background-color 0.3s;
}

.statement-text {
  flex-grow: 1;
  margin: 0;
  text-align: right;
  line-height: 1.6;
  color: #4b4b4b;
}

.button-group {
  display: flex;
  gap: 0.5rem;
  margin-right: 1.5rem; /* فاصله بین متن و دکمه‌ها */
}

.tf-button {
  border: 2px solid #e5e5e5;
  border-bottom-width: 4px;
  background-color: #fff;
  padding: 0.75rem 1rem;
  min-width: 80px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: bold;
  font-size: 1rem;
  color: #777;
  transition: all 0.1s;
}
.tf-button:disabled {
  cursor: not-allowed;
  opacity: 0.6;
}
.tf-button:active:not(:disabled) {
  transform: translateY(2px);
  border-bottom-width: 2px;
}

/* --- حالت‌های دکمه‌ها --- */
.true-button.selected {
  background-color: #d7ffb8;
  border-color: #84e100;
  color: #58a700;
}
.false-button.selected {
  background-color: #ffdfe0;
  border-color: #ffc1c3;
  color: #ea2b2b;
}

/* --- حالت‌های بازخورد ردیف --- */
.statement-row.correct {
  background-color: #f0fff0;
  border-color: #84e100;
}
.statement-row.incorrect {
  background-color: #fff0f0;
  border-color: #ffc1c3;
}

/* وقتی جواب اشتباه بوده، دکمه درست را هم هایلایت کن */
.statement-row.incorrect .true-button.selected {
  opacity: 0.5;
}
.statement-row.incorrect .false-button.selected {
   opacity: 0.5;
}

</style>