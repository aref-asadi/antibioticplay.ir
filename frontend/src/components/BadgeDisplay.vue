<template>
  <div class="badge-item" :title="badge.description">
    <font-awesome-icon :icon="['fas', badge.icon.split(' ')[1]]" class="badge-icon" />
    <span class="badge-name">{{ badge.name }}</span>
  </div>
</template>

<script setup>
defineProps({
  badge: {
    type: Object,
    required: true
  }
});
</script>

<style scoped>
.badge-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1rem;
  border: 1px solid #eee;
  border-radius: 8px;
  background-color: #fff;
  min-width: 100px;
  text-align: center;
  transition: transform 0.2s, box-shadow 0.2s;
}
.badge-item:hover {
  transform: translateY(-3px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.05);
}
.badge-icon {
  font-size: 2.5rem;
  color: #f59e0b; /* Amber/Gold color */
  margin-bottom: 0.5rem;
}
.badge-name {
  font-size: 0.9rem;
  color: #555;
  font-weight: 500;
}
</style>