<template>
  <div class="review-page">
    <header class="review-header">
      <router-link to="/dashboard" class="back-btn">
        <font-awesome-icon icon="fas fa-arrow-right" />
      </router-link>
      <h1>مرور سوالات نشان‌دار</h1>
    </header>

    <div v-if="loading" class="loading-state">در حال بارگذاری...</div>
    <div v-else-if="questions.length === 0" class="empty-state">
      <div class="empty-icon">🔖</div>
      <p>هیچ سوالی را نشان نکرده‌اید.</p>
      <router-link to="/dashboard" class="btn btn-primary">برو به آزمون‌ها</router-link>
    </div>

    <div v-else class="review-list">
      <div v-for="(q, index) in questions" :key="index" class="review-card card">
        <div class="card-header">
          <span class="quiz-tag">{{ q.quiz_title }}</span>
          <button class="delete-btn" @click="removeBookmark(q)">
            <font-awesome-icon icon="fas fa-trash" />
          </button>
        </div>
        
        <h3 class="question-text">{{ q.title }}</h3>
        <p class="instruction">{{ q.instruction }}</p>

        <div class="answer-reveal">
          <button class="btn btn-outline show-ans-btn" @click="toggleAnswer(index)">
            {{ q.showAnswer ? 'مخفی کردن پاسخ' : 'نمایش پاسخ صحیح' }}
          </button>
          
          <div v-if="q.showAnswer" class="answer-content slide-down">
            <p v-if="q.explanation" class="explanation">
              <strong>توضیحات:</strong> {{ q.explanation }}
            </p>
            </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useBookmarkStore } from '../stores/bookmarkStore';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faArrowRight, faTrash } from '@fortawesome/free-solid-svg-icons';

library.add(faArrowRight, faTrash);

const bookmarkStore = useBookmarkStore();
const questions = ref([]);
const loading = ref(true);

onMounted(async () => {
  await bookmarkStore.fetchReviewItems();
  // اضافه کردن فیلد لوکال برای نمایش/مخفی کردن جواب
  questions.value = bookmarkStore.reviewQuestions.map(q => ({ ...q, showAnswer: false }));
  loading.value = false;
});

const toggleAnswer = (index) => {
  questions.value[index].showAnswer = !questions.value[index].showAnswer;
};

const removeBookmark = async (question) => {
  if (confirm('این سوال از لیست مرور حذف شود؟')) {
    await bookmarkStore.toggleBookmark(question.quiz_id, question.id);
    questions.value = questions.value.filter(q => q.id !== question.id);
  }
};
</script>

<style scoped>
.review-page { min-height: 100vh; background-color: #f7f7f7; padding-bottom: 80px; }
.review-header { background: white; padding: 1rem 2rem; display: flex; align-items: center; gap: 1rem; border-bottom: 2px solid #e5e5e5; position: sticky; top: 0; z-index: 10; }
.review-header h1 { margin: 0; font-size: 1.2rem; color: var(--color-text); }
.back-btn { font-size: 1.5rem; color: var(--color-text-light); }

.review-list { max-width: 600px; margin: 2rem auto; padding: 0 1rem; display: flex; flex-direction: column; gap: 1.5rem; }
.review-card { position: relative; }
.card-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; }
.quiz-tag { background: var(--color-secondary-light); color: var(--color-secondary); padding: 0.3rem 0.8rem; border-radius: 12px; font-size: 0.8rem; font-weight: bold; }
.delete-btn { background: none; border: none; color: #ffbcbc; padding: 0.5rem; min-width: auto; border-bottom: none; }
.delete-btn:hover { color: var(--color-danger); }

.question-text { font-size: 1.1rem; margin-bottom: 0.5rem; }
.instruction { color: var(--color-text-light); font-size: 0.9rem; margin-bottom: 1.5rem; }

.show-ans-btn { width: 100%; color: var(--color-secondary); border-color: var(--color-secondary); font-size: 0.9rem; padding: 0.6rem; }
.answer-content { margin-top: 1rem; padding: 1rem; background: #f0faff; border-radius: 12px; border: 1px solid var(--color-secondary-light); }
.explanation { font-size: 0.95rem; color: var(--color-text); line-height: 1.6; }

.empty-state { text-align: center; margin-top: 4rem; }
.empty-icon { font-size: 4rem; margin-bottom: 1rem; }
</style>