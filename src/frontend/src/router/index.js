import Vue from 'vue';
import VueRouter from 'vue-router';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';


Vue.use(VueRouter);

const originalPush = VueRouter.prototype.push;

VueRouter.prototype.push = function push(location) {
    return originalPush.call(this, location).catch(err => err);
};

const routes = [{
    // 登录界面
    path: '/',
    name: 'Login',
    component: Login
},
// 注册界面
{
    path: '/register',
    name: 'Register',
    component: Register
},
];

const router = new VueRouter({
    mode: 'history',
    routes
});


export default router;