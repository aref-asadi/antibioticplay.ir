<template>
  <div class="fill-blank-container">

    <div class="instruction-text">
      <span v-for="(part, index) in instructionParts" :key="index">
        <template v-if="!part.isBlank">
          {{ part.text }}
        </template>
        <div
          v-else
          class="blank-slot droppable"
          :class="{ 
            'filled': !!userAnswers[part.id],
            'correct': feedback[part.id] === 'correct',
            'incorrect': feedback[part.id] === 'incorrect',
            'disabled': disabled,
            'highlight-target': selectedOptionId && !disabled
          }"
          @dragover.prevent="onDragOver"
          @dragleave.prevent="onDragLeave"
          @drop.prevent="onDrop($event, part.id)"
          @click="onTargetClick(part.id)"
        >
          <div
            v-if="userAnswers[part.id]"
            class="item-card draggable"
            :class="{ 'selected-mode': selectedOptionId === userAnswers[part.id] }"
            :draggable="!disabled"
            @dragstart="onDragStart($event, getItemById(userAnswers[part.id]), part.id)"
            @click.stop="onItemClick(getItemById(userAnswers[part.id]), part.id)"
          >
            {{ getItemById(userAnswers[part.id]).text }}
          </div>
        </div>
      </span>
    </div>

    <div 
      class="item-bank droppable"
      :class="{ 
        'disabled': disabled,
        'highlight-target': selectedOptionId && !disabled
      }"
      @dragover.prevent="onDragOver"
      @dragleave.prevent="onDragLeave"
      @drop.prevent="onDrop($event, 'bank')"
      @click="onTargetClick('bank')"
    >
      <div 
        v-for="item in bankItems"
        :key="item.id"
        class="item-card draggable"
        :class="{ 'selected-mode': selectedOptionId === item.id }"
        :draggable="!disabled"
        @dragstart="onDragStart($event, item, 'bank')"
        @click.stop="onItemClick(item, 'bank')"
      >
        {{ item.text }}
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

// State
const userAnswers = ref({});
const itemsInBank = ref([]); // تمام آیتم‌ها در ابتدا اینجا هستند (منطق داخلی کمی فرق کرد)
// در این کامپوننت، bankItems به صورت computed از روی userAnswers و همه آپشن‌ها محاسبه می‌شود
// ما برای selectedOptionId فقط ID را نگه می‌داریم
const selectedOptionId = ref(null);
const selectedSourceId = ref(null); // 'bank' یا ID جای خالی

watch(() => props.question, (newQuestion) => {
  if (newQuestion) {
    userAnswers.value = {};
    selectedOptionId.value = null;
    emit('update:answer', null);
  }
}, { immediate: true });

// Helpers
const getItemById = (optionId) => {
  return props.question.options.find(opt => opt.id === optionId);
};

const instructionParts = computed(() => {
  const parts = [];
  let lastIndex = 0;
  const regex = /(_BLANK[0-9]+_)/g;
  let match;
  while ((match = regex.exec(props.question.instruction_template)) !== null) {
    if (match.index > lastIndex) {
      parts.push({ isBlank: false, text: props.question.instruction_template.substring(lastIndex, match.index) });
    }
    parts.push({ isBlank: true, id: match[1] });
    lastIndex = match.index + match[1].length;
  }
  if (lastIndex < props.question.instruction_template.length) {
    parts.push({ isBlank: false, text: props.question.instruction_template.substring(lastIndex) });
  }
  return parts;
});

const bankItems = computed(() => {
  const answeredOptionIds = Object.values(userAnswers.value).filter(Boolean);
  return props.question.options.filter(opt => !answeredOptionIds.includes(opt.id));
});

// --- Click Logic ---

const onItemClick = (item, sourceId) => {
  if (props.disabled) return;
  
  if (selectedOptionId.value === item.id) {
    selectedOptionId.value = null; // Deselect
    selectedSourceId.value = null;
  } else {
    selectedOptionId.value = item.id;
    selectedSourceId.value = sourceId; // 'bank' یا _BLANK1_
  }
};

const onTargetClick = (targetId) => {
  // targetId: 'bank' یا _BLANK1_
  if (props.disabled || !selectedOptionId.value) return;

  // جابجایی
  moveItem(selectedOptionId.value, selectedSourceId.value, targetId);
  
  selectedOptionId.value = null;
  selectedSourceId.value = null;
};

// --- Drag Logic ---

const onDragStart = (event, item, sourceBlankId) => {
  if (props.disabled) return;
  event.dataTransfer.dropEffect = 'move';
  event.dataTransfer.effectAllowed = 'move';
  event.dataTransfer.setData('optionId', item.id);
  event.dataTransfer.setData('sourceBlankId', sourceBlankId);
  selectedOptionId.value = null;
};

const onDrop = (event, targetBlankId) => {
  if (props.disabled) return;
  const optionId = event.dataTransfer.getData('optionId');
  const sourceBlankId = event.dataTransfer.getData('sourceBlankId');
  if (!optionId) return;

  moveItem(optionId, sourceBlankId, targetBlankId);
  event.target.closest('.droppable').classList.remove('drag-over');
};

const moveItem = (optionId, sourceId, targetId) => {
  // ۱. حذف از مبدا
  if (sourceId !== 'bank') {
    userAnswers.value[sourceId] = undefined;
  }

  // ۲. افزودن به مقصد
  if (targetId !== 'bank') {
    // اگر در مقصد آیتم دیگری بود، آن را به بانک برگردان (یا مبادله کن)
    // ساده‌ترین حالت: آیتم قبلی به بانک برمی‌گردد
    userAnswers.value[targetId] = optionId;
  }
  
  // اگر مقصد بانک بود، عملاً با حذف از مرحله ۱ کار تمام است (چون bankItems محاسباتی است)
  
  emit('update:answer', userAnswers.value);
};

const onDragOver = (event) => {
  if (props.disabled) return;
  event.target.closest('.droppable').classList.add('drag-over');
};
const onDragLeave = (event) => {
  event.target.closest('.droppable').classList.remove('drag-over');
};
</script>

<style scoped>
.instruction-text { font-size: 1.3rem; line-height: 2.5; color: #4b4b4b; text-align: right; margin-bottom: 2rem; }
.blank-slot { display: inline-block; vertical-align: middle; width: 150px; height: 50px; background-color: #f0f0f0; border: 2px dashed #d0d0d0; border-radius: 8px; margin: 0 0.5rem; padding: 4px; box-sizing: border-box; transition: all 0.2s; }
.blank-slot.filled { border-style: solid; background-color: #fff; }
.blank-slot.drag-over { border-color: #42b983; background-color: #e0f0e9; }
.item-bank { background-color: #f7f7f7; border: 2px dashed #e5e5e5; border-radius: 12px; padding: 1rem; min-height: 100px; display: flex; flex-wrap: wrap; gap: 0.75rem; align-content: flex-start; margin-top: 1rem; transition: border-color 0.2s; }
.item-bank.drag-over { border-color: #42b983; }
.item-card { background-color: white; border: 2px solid #e5e5e5; border-radius: 8px; padding: 0.5rem 1rem; cursor: grab; user-select: none; transition: background-color 0.2s; width: 100%; height: 100%; box-sizing: border-box; display: flex; align-items: center; justify-content: center; font-size: 0.9rem; }
.item-bank .item-card { width: auto; height: auto; padding: 0.75rem 1rem; font-size: 1rem; }
.item-card.disabled { cursor: not-allowed; }
.blank-slot.correct { border-color: #58a700; background-color: #d7ffb8; }
.blank-slot.incorrect { border-color: #ff4b4b; background-color: #ffdfe0; }
</style>