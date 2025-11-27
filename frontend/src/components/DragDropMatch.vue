<template>
  <div class="drag-drop-container">
    <p class="instruction">{{ question.instruction }}</p>
    
    <div class="main-area">
      <div class="categories">
        <div 
          v-for="category in question.categories" 
          :key="category.id"
          class="category-box droppable"
          :class="{ 
            'disabled': disabled,
            'highlight-target': selectedItemId && !disabled 
          }"
          @dragover.prevent="onDragOver"
          @dragleave.prevent="onDragLeave"
          @drop.prevent="onDrop($event, category.id)"
          @click="onTargetClick(category.id)"
        >
          <span class="category-title">{{ category.text }}</span>
          <div 
            v-for="item in itemsInCategories[category.id] || []"
            :key="item.id"
            class="item-card draggable"
            :class="[
              feedback[item.id], 
              { 'disabled': disabled, 'selected-mode': selectedItemId === item.id }
            ]"
            :draggable="!disabled"
            @dragstart="onDragStart($event, item)"
            @click.stop="onItemClick(item)"
          >
            {{ item.text }}
          </div>
        </div>
      </div>

      <div 
        class="item-bank droppable"
        :class="{ 
          'disabled': disabled,
          'highlight-target': selectedItemId && !disabled 
        }"
        @dragover.prevent="onDragOver"
        @dragleave.prevent="onDragLeave"
        @drop.prevent="onDrop($event, 'bank')"
        @click="onTargetClick('bank')"
      >
         <div 
            v-for="item in itemsInBank"
            :key="item.id"
            class="item-card draggable"
            :class="[
              feedback[item.id], 
              { 'disabled': disabled, 'selected-mode': selectedItemId === item.id }
            ]"
            :draggable="!disabled"
            @dragstart="onDragStart($event, item)"
            @click.stop="onItemClick(item)"
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

// State
const itemPositions = ref({});
const selectedItemId = ref(null); // آیتمی که برای جابجایی انتخاب شده

// Setup
watch(() => props.question, (newQuestion) => {
  if (newQuestion) {
    itemPositions.value = { bank: [...newQuestion.items] };
    selectedItemId.value = null;
    emit('update:answer', itemPositions.value);
  }
}, { immediate: true });

// Computed
const itemsInBank = computed(() => itemPositions.value.bank || []);
const itemsInCategories = computed(() => {
  const { bank, ...cats } = itemPositions.value;
  return cats;
});

// --- Logic for Click-to-Move (Mobile Friendly) ---

const onItemClick = (item) => {
  if (props.disabled) return;
  
  if (selectedItemId.value === item.id) {
    // اگر دوباره روی خودش کلیک کرد، از حالت انتخاب در بیاید
    selectedItemId.value = null;
  } else {
    // انتخاب آیتم
    selectedItemId.value = item.id;
  }
};

const onTargetClick = (targetCategoryId) => {
  if (props.disabled || !selectedItemId.value) return;

  // جابجایی آیتم انتخاب شده به مقصد کلیک شده
  moveItem(selectedItemId.value, targetCategoryId);
  selectedItemId.value = null; // پاک کردن انتخاب
};

// --- Logic for Drag & Drop ---

const onDragStart = (event, item) => {
  if (props.disabled) return;
  event.dataTransfer.dropEffect = 'move';
  event.dataTransfer.effectAllowed = 'move';
  event.dataTransfer.setData('itemId', item.id);
  selectedItemId.value = null; // درگ کردن انتخاب قبلی را کنسل می‌کند
};

const onDrop = (event, targetCategoryId) => {
  const itemId = event.dataTransfer.getData('itemId');
  if (props.disabled || !itemId) return;
  moveItem(itemId, targetCategoryId);
  event.target.closest('.droppable').classList.remove('drag-over');
};

// --- Shared Move Logic ---
const moveItem = (itemId, targetCategoryId) => {
  let itemToMove;
  
  // ۱. پیدا کردن و حذف از مکان فعلی
  for (const catId in itemPositions.value) {
    const index = itemPositions.value[catId].findIndex(i => i.id === itemId);
    if (index > -1) {
      itemToMove = itemPositions.value[catId].splice(index, 1)[0];
      break;
    }
  }

  // ۲. افزودن به مقصد
  if (itemToMove) {
    if (!itemPositions.value[targetCategoryId]) {
      itemPositions.value[targetCategoryId] = [];
    }
    itemPositions.value[targetCategoryId].push(itemToMove);
    emit('update:answer', itemPositions.value);
  }
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
/* استایل‌های قبلی ثابت می‌مانند، فقط کلاس‌های جدید از style.css اعمال می‌شوند */
.drag-drop-container { width: 100%; }
.instruction { font-size: 1.2rem; margin-bottom: 1.5rem; text-align: center; }
.main-area { display: flex; flex-direction: column; gap: 1rem; }
.categories { flex-grow: 1; display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
.category-box { background-color: #f7f7f7; border: 2px solid #e5e5e5; border-radius: 12px; padding: 1rem; min-height: 150px; transition: border-color 0.2s, background-color 0.2s; }
.category-title { font-weight: bold; color: #777; display: block; margin-bottom: 0.75rem; font-size: 1.1rem; }
.item-bank { background-color: #f7f7f7; border: 2px dashed #e5e5e5; border-radius: 12px; padding: 1rem; min-height: 100px; display: flex; flex-wrap: wrap; gap: 0.5rem; align-content: flex-start; transition: border-color 0.2s; }
.droppable.drag-over { border-color: #42b983; box-shadow: 0 0 10px rgba(66, 185, 131, 0.3); }
.item-card { background-color: white; border: 2px solid #e5e5e5; border-radius: 8px; padding: 0.75rem 1rem; cursor: grab; user-select: none; margin-bottom: 0.5rem; transition: all 0.2s; }
.item-card:hover { background-color: #f9f9f9; transform: translateY(-2px); }
.item-card.correct { border-color: #58a700; color: #58a700; background-color: #d7ffb8; }
.item-card.incorrect { border-color: #ff4b4b; color: #ff4b4b; background-color: #ffdfe0; }
.item-card.disabled { cursor: not-allowed; opacity: 0.8; }
</style>