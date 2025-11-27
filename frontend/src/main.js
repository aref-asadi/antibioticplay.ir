// File: frontend/src/main.js

import { createApp } from 'vue';
import { createPinia } from 'pinia';
import router from './router';
import App from './App.vue';
import './style.css';

import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faPlay, faStar, faTrophy, faFire, faSitemap, faPills, faStethoscope, faQuestion, faHouse, faUser, faMedal, faFlag } from '@fortawesome/free-solid-svg-icons';

const app = createApp(App);
const pinia = createPinia();

// --- *** Add Icons to Library & Register Component *** ---
library.add(faPlay, faStar, faTrophy, faFire, faSitemap, faPills, faStethoscope, faQuestion, faHouse, faUser, faMedal, faFlag);
app.component('font-awesome-icon', FontAwesomeIcon); // Register the component globally

app.use(pinia);
app.use(router);

app.mount('#app');