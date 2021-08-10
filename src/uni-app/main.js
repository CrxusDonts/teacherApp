import Vue from 'vue';
import App from './App';
import './node_modules/weapp-cookie/index';
import cuCustom from 'colorui/components/cu-custom.vue';

Vue.component('cu-custom', cuCustom);

Vue.config.productionTip = false;

Vue.prototype.$BASICURL = 'http://10.22.53.143:8002/teacherApp/';
Vue.prototype.$FILEBASICURL = 'http://10.22.53.143:8002/';

App.mpType = 'app';

const app = new Vue({
    ...App
});
app.$mount();
