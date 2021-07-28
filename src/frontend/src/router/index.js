import Vue from 'vue';
import VueRouter from 'vue-router';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';
import Passwordmodify from '../views/passwordModify.vue';
import Home from '../views/Home.vue';
import HomeworkManagement from '../views/HomeComponents/HomeworkManagement';
import StudentManagement from '../views/HomeComponents/StudentManagement';
import StudentApply from '../views/HomeComponents/StudentApply';
import AssistantManagement from '../views/HomeComponents/AssistantManagement';
import InviteMe from '../views/HomeComponents/InviteMe';
import GradeByClass from '../views/HomeComponents/GradeByClass';
import GradeByStudent from '../views/HomeComponents/GradeByStudent';
import SwitchClass from '../views/HomeComponents/SwitchClass';

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
// 修改密码界面
{
    path: '/passwordmodify',
    name: 'Passwordmodify',
    component: Passwordmodify
},
// 主页及其子页面
{
    path: '/home',
    name: 'Home',
    component: Home,
    redirect: '/homeworkManagement',
    children: [
        {
            path: '/homeworkManagement',
            name: 'HomeworkManagement',
            component: HomeworkManagement
        },
        {
            path: '/studentManagement',
            name: 'StudentManagement',
            component: StudentManagement
        },
        {
            path: '/studentApply',
            name: 'StudentApply',
            component: StudentApply
        },
        {
            path: '/assistantManagement',
            name: 'AssistantManagement',
            component: AssistantManagement
        },
        {
            path: '/inviteMe',
            name: 'InviteMe',
            component: InviteMe
        },
        {
            path: '/gradeByClass',
            name: 'GradeByClass',
            component: GradeByClass
        },
        {
            path: '/gradeByStudent',
            name: 'GradeByStudent',
            component: GradeByStudent
        },
        {
            path: '/switchClass',
            name: 'SwitchClass',
            component: SwitchClass
        }
    ]
}
];

const router = new VueRouter({
    mode: 'history',
    routes
});

export default router;
