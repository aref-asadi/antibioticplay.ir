import { createApp } from 'vue';
import { createPinia } from 'pinia';
import router from './router';
import App from './App.vue';
import './style.css';

import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import "mobile-drag-drop/default.css";
import { polyfill } from "mobile-drag-drop";

polyfill({
    dragImageCenterOnTouch: true
});

window.addEventListener( 'touchmove', function() {}, {passive: false});

import { 
  faPlay, faStar, faTrophy, faFire, faSitemap, 
  faPills, faStethoscope, faHouse, faUser, faFlag,
  faQuestionCircle, faLightbulb, faCheck, faTimes,
  faMedal, faGem, faStopwatch, faArrowUp, faPlus
} from '@fortawesome/free-solid-svg-icons';

const app = createApp(App);
const pinia = createPinia();

library.add(
  faPlay, faStar, faTrophy, faFire, faSitemap, 
  faPills, faStethoscope, faHouse, faUser, faFlag,
  faQuestionCircle, faLightbulb, faCheck, faTimes,
  faMedal, faGem, faStopwatch, faArrowUp, faPlus
);

app.component('font-awesome-icon', FontAwesomeIcon);

app.use(pinia);
app.use(router);

app.mount('#app');