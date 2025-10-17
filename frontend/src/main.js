// File: frontend/src/main.js

import { createApp } from 'vue';
import { createPinia } from 'pinia'; // <-- ایمپورت Pinia
import router from './router';       // <-- ایمپورت Router
import App from './App.vue';
import './style.css';

const app = createApp(App);
const pinia = createPinia(); // <-- ساخت یک نمونه از Pinia

app.use(pinia);  // <-- اتصال Pinia به اپلیکیشن
app.use(router); // <-- اتصال Router به اپلیکیشن

app.mount('#app');