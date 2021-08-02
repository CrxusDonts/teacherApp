import Vue from 'vue';
import VueRouter from 'vue-router';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';
import Passwordmodify from '../views/passwordModify.vue';
import Home from '../views/Home.vue';
import HomeworkManagement from '../components/HomeComponents/HomeworkManagement';
import StudentManagement from '../components/HomeComponents/StudentManagement';
import StudentApply from '../components/HomeComponents/StudentApply';
import AssistantManagement from '../components/HomeComponents/AssistantManagement';
import InviteMe from '../components/HomeComponents/InviteMe';
import GradeByClass from '../components/HomeComponents/GradeByClass';
import GradeByStudent from '../components/HomeComponents/GradeByStudent';
import SwitchClass from '../components/HomeComponents/SwitchClass';
import EditHomework from '../views/EditHomework';

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
    name: 'PasswordModify',
    component: Passwordmodify
},
{
    path: '/edithomework',
    name: 'EditHomework',
    component: EditHomework
},
// 主页及其子页面
{
    path: '/home/:user_name',
    name: 'Home',
    component: Home,
    children: [
        {
            path: 'homeworkManagement',
            name: 'HomeworkManagement',
            component: HomeworkManagement
        },
        {
            path: 'studentManagement',
            name: 'StudentManagement',
            component: StudentManagement
        },
        {
            path: 'studentApply',
            name: 'StudentApply',
            component: StudentApply
        },
        {
            path: 'assistantManagement',
            name: 'AssistantManagement',
            component: AssistantManagement
        },
        {
            path: 'inviteMe',
            name: 'InviteMe',
            component: InviteMe
        },
        {
            path: 'gradeByClass',
            name: 'GradeByClass',
            component: GradeByClass
        },
        {
            path: 'gradeByStudent',
            name: 'GradeByStudent',
            component: GradeByStudent
        },
        {
            path: 'switchClass',
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
