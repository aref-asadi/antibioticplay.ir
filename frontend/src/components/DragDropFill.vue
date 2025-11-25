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
            'disabled': disabled
          }"
          @dragover.prevent="onDragOver"
          @dragleave.prevent="onDragLeave"
          @drop.prevent="onDrop($event, part.id)"
        >
          <div
            v-if="userAnswers[part.id]"
            class="item-card draggable"
            :draggable="!disabled"
            @dragstart="onDragStart($event, getItemById(userAnswers[part.id]), part.id)"
          >
            {{ getItemById(userAnswers[part.id]).text }}
          </div>
        </div>
      </span>
    </div>

    <div 
      class="item-bank droppable"
      :class="{ 'disabled': disabled }"
      @dragover.prevent="onDragOver"
      @dragleave.prevent="onDragLeave"
      @drop.prevent="onDrop($event, 'bank')"
    >
      <div 
        v-for="item in bankItems"
        :key="item.id"
        class="item-card draggable"
        :draggable="!disabled"
        @dragstart="onDragStart($event, item, 'bank')"
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

const userAnswers = ref({});
const itemsInBank = ref([]);

watch(() => props.question, (newQuestion) => {
  if (newQuestion) {
    itemsInBank.value = [...newQuestion.options];
    userAnswers.value = {};
    emit('update:answer', null);
  }
}, { immediate: true });

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
  const answeredOptionIds = Object.values(userAnswers.value);
  return props.question.options.filter(opt => !answeredOptionIds.includes(opt.id));
});

const onDragStart = (event, item, sourceBlankId) => {
  if (props.disabled) return;
  event.dataTransfer.dropEffect = 'move';
  event.dataTransfer.effectAllowed = 'move';
  event.dataTransfer.setData('optionId', item.id);
  event.dataTransfer.setData('sourceBlankId', sourceBlankId);
};

const onDrop = (event, targetBlankId) => {
  if (props.disabled) return;

  const optionId = event.dataTransfer.getData('optionId');
  const sourceBlankId = event.dataTransfer.getData('sourceBlankId');
  if (!optionId) return;

  if (sourceBlankId !== 'bank') {
    userAnswers.value[sourceBlankId] = undefined; 
  }

  if (targetBlankId !== 'bank') {
    userAnswers.value[targetBlankId] = optionId;
  }

  event.target.closest('.droppable').classList.remove('drag-over');
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
.instruction-text {
  font-size: 1.3rem;
  line-height: 2.5;
  color: #4b4b4b;
  text-align: right;
  margin-bottom: 2rem;
}

.blank-slot {
  display: inline-block;
  vertical-align: middle;
  width: 150px;
  height: 50px;
  background-color: #f0f0f0;
  border: 2px dashed #d0d0d0;
  border-radius: 8px;
  margin: 0 0.5rem;
  padding: 4px;
  box-sizing: border-box;
}

.blank-slot.filled {
  border-style: solid;
  background-color: #fff;
}

.blank-slot.drag-over {
  border-color: #42b983;
  background-color: #e0f0e9;
}

.item-bank {
  background-color: #f7f7f7;
  border: 2px dashed #e5e5e5;
  border-radius: 12px;
  padding: 1rem;
  min-height: 100px;
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  align-content: flex-start;
  margin-top: 1rem;
}
.item-bank.drag-over {
  border-color: #42b983;
}

.item-card {
  background-color: white;
  border: 2px solid #e5e5e5;
  border-radius: 8px;
  padding: 0.5rem 1rem;
  cursor: grab;
  user-select: none;
  transition: background-color 0.2s;
  width: 100%;
  height: 100%;
  box-sizing: border-box;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.9rem;
}

.item-bank .item-card {
  width: auto;
  height: auto;
  padding: 0.75rem 1rem;
  font-size: 1rem;
}

.item-card.disabled {
  cursor: not-allowed;
}

.blank-slot.correct {
  border-color: #58a700;
  background-color: #d7ffb8;
}
.blank-slot.incorrect {
  border-color: #ff4b4b;
  background-color: #ffdfe0;
}
</style>