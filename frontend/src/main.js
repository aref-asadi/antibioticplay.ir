// File: frontend/src/main.js

import { createApp } from 'vue';
import { createPinia } from 'pinia';
import router from './router';
import App from './App.vue';
import './style.css';

// --- *** Font Awesome Imports *** ---
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
// Import specific icons you want to use globally
import { faPlay, faStar, faTrophy, faFire, faSitemap, faPills, faStethoscope } from '@fortawesome/free-solid-svg-icons';
// --- *** End Font Awesome Imports *** ---

const app = createApp(App);
const pinia = createPinia();

// --- *** Add Icons to Library & Register Component *** ---
library.add(faPlay, faStar, faTrophy, faFire, faSitemap, faPills, faStethoscope); // Add the imported icons
app.component('font-awesome-icon', FontAwesomeIcon); // Register the component globally
// --- *** End Configuration *** ---

app.use(pinia);
app.use(router);

app.mount('#app');