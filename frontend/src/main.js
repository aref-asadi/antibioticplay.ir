import { createApp } from 'vue';
import { createPinia } from 'pinia';
import router from './router';
import App from './App.vue';
import './style.css';

import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

import { polyfill } from "mobile-drag-drop";
import "mobile-drag-drop/default.css";

polyfill({
    forceApply: true,

    dragImageCenterOnTouch: false,

    dragImageTranslateOverride: (event, element, initialX, initialY, currentX, currentY) => {
        return {
            x: currentX - (element.offsetWidth / 2),
            y: currentY - element.offsetHeight - 50 // 50px بالاتر
        };
    }
});

window.addEventListener('touchmove', function(e) {
    if (e.target.closest('.draggable')) {
        e.preventDefault();
    }
}, { passive: false });

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