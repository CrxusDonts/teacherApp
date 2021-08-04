import Vue from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';
import ElementUI from 'element-ui';
import VideoPlayer from 'vue-video-player';
import 'vue-video-player/src/custom-theme.css';
import 'video.js/dist/video-js.css';
import 'element-ui/lib/theme-chalk/index.css';

axios.defaults.withCredentials = true;
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
axios.defaults.xsrfCookieName = 'csrftoken';
Vue.config.productionTip = false;
Vue.prototype.$http = axios;
Vue.use(ElementUI);
Vue.use(VideoPlayer);

Vue.prototype.$http = axios.create({
    baseURL: 'http://localhost:8002/teacherApp/',
    timeout: 3000
});

Vue.use(axios);
new Vue({
    router,
    render: h => h(App)
}).$mount('#app');

