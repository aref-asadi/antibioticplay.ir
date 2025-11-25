<template>
  <div class="drag-drop-container">
    <p class="instruction">{{ question.instruction }}</p>
    
    <div class="main-area">
      <div class="categories">
        <div 
          v-for="category in question.categories" 
          :key="category.id"
          class="category-box droppable"
          :class="{ 'disabled': disabled }"
          @dragover.prevent="onDragOver"
          @dragleave.prevent="onDragLeave"
          @drop.prevent="onDrop($event, category.id)"
        >
          <span class="category-title">{{ category.text }}</span>
          <div 
            v-for="item in itemsInCategories[category.id] || []"
            :key="item.id"
            class="item-card draggable"
            :class="[feedback[item.id], { 'disabled': disabled }]"
            :draggable="!disabled"
            @dragstart="onDragStart($event, item)"
          >
            {{ item.text }}
          </div>
        </div>
      </div>

      <div 
        class="item-bank droppable"
        :class="{ 'disabled': disabled }"
        @dragover.prevent="onDragOver"
        @dragleave.prevent="onDragLeave"
        @drop.prevent="onDrop($event, 'bank')"
      >
         <div 
            v-for="item in itemsInBank"
            :key="item.id"
            class="item-card draggable"
            :class="[feedback[item.id], { 'disabled': disabled }]"
            :draggable="!disabled"
            @dragstart="onDragStart($event, item)"
          >
            {{ item.text }}
          </div>
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

const itemPositions = ref({});

watch(() => props.question, (newQuestion) => {
  if (newQuestion) {
    itemPositions.value = {
      bank: [...newQuestion.items]
    };
    emit('update:answer', itemPositions.value);
  }
}, { immediate: true });

const itemsInBank = computed(() => itemPositions.value.bank || []);
const itemsInCategories = computed(() => {
  const { bank, ...cats } = itemPositions.value;
  return cats;
});

const onDragStart = (event, item) => {
  if (props.disabled) return;
  event.dataTransfer.dropEffect = 'move';
  event.dataTransfer.effectAllowed = 'move';
  event.dataTransfer.setData('itemId', item.id);
};

const onDrop = (event, targetCategoryId) => {
  const itemId = event.dataTransfer.getData('itemId');
  if (props.disabled || !itemId) return;

  let itemToMove;
  
  for (const categoryId in itemPositions.value) {
    const index = itemPositions.value[categoryId].findIndex(item => item.id === itemId);
    if (index > -1) {
      itemToMove = itemPositions.value[categoryId].splice(index, 1)[0];
      break;
    }
  }

  if (itemToMove) {
    if (!itemPositions.value[targetCategoryId]) {
      itemPositions.value[targetCategoryId] = [];
    }
    itemPositions.value[targetCategoryId].push(itemToMove);
  }
  
  event.target.closest('.droppable').classList.remove('drag-over');
  emit('update:answer', itemPositions.value);
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
.drag-drop-container {
  width: 100%;
}
.instruction {
  font-size: 1.2rem;
  margin-bottom: 1.5rem;
  text-align: center;
}
.main-area {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.categories {
  flex-grow: 1;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.category-box {
  background-color: #f7f7f7;
  border: 2px solid #e5e5e5;
  border-radius: 12px;
  padding: 1rem;
  min-height: 150px;
}

.category-title {
  font-weight: bold;
  color: #777;
  display: block;
  margin-bottom: 0.75rem;
  font-size: 1.1rem;
}

.item-bank {
  background-color: #f7f7f7;
  border: 2px dashed #e5e5e5;
  border-radius: 12px;
  padding: 1rem;
  min-height: 100px;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  align-content: flex-start;
}

.droppable.drag-over {
  border-color: #42b983;
  box-shadow: 0 0 10px rgba(66, 185, 131, 0.3);
}

.item-card {
  background-color: white;
  border: 2px solid #e5e5e5;
  border-radius: 8px;
  padding: 0.75rem 1rem;
  cursor: grab;
  user-select: none;
  margin-bottom: 0.5rem;
  transition: background-color 0.2s;
}
.item-card:hover {
  background-color: #f9f9f9;
}

.item-card.correct {
  border-color: #58a700;
  color: #58a700;
  background-color: #d7ffb8;
}
.item-card.incorrect {
  border-color: #ff4b4b;
  color: #ff4b4b;
  background-color: #ffdfe0;
}
.item-card.disabled {
    cursor: not-allowed;
    opacity: 0.8;
}
.category-box.disabled, .item-bank.disabled {
    background-color: #f0f0f0;
}
</style>