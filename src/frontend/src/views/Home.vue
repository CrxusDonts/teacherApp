<template>
    <div>
        <Header v-bind:userName="userName"></Header>
        <el-menu class="el-Menu" default-active="homeworkManagement" mode="horizontal" @select="handleSelect"
                 :router="true">
            <el-menu-item index="homeworkManagement" :route=
                "{ path: 'homeworkManagement', query: { classId: this.classId} }">作业管理</el-menu-item>
            <el-submenu index="management">
                <template slot="title">班级管理</template>
                <el-menu-item index="studentManagement" :route=
                    "{ path: 'studentManagement', query: { classId: this.classId} }">学生管理</el-menu-item>
                <el-menu-item index="studentApply" :route=
                    "{ path: 'studentApply', query: { classId: this.classId} }">学生申请 <el-badge :value="12" /></el-menu-item>
                <el-menu-item index="assistantManagement" :route=
                    "{ path: 'assistantManagement', query: { classId: this.classId} }">助教管理</el-menu-item>
                <el-menu-item index="inviteMe" :route=
                    "{ path: 'inviteMe', query: { classId: this.classId} }">邀请我的 <el-badge :value="12" /></el-menu-item>
            </el-submenu>
            <el-submenu index="grade">
                <template slot="title">成绩统计</template>
                <el-menu-item index="gradeByClass" :route=
                    "{ path: 'gradeByClass', query: { classId: this.classId} }">按班级统计</el-menu-item>
                <el-menu-item index="gradeByStudent" :route=
                    "{ path: 'gradeByStudent', query: { classId: this.classId} }">按学生统计</el-menu-item>
            </el-submenu>
            <el-menu-item index="switchClass" :route=
                "{ path: 'switchClass', query: { classId: this.classId} }">班级切换</el-menu-item>
        </el-menu>
        <router-view @classIdChanged="classIdChanged"></router-view>
    </div>
</template>

<script>
import Header from '../components/Header';

export default {
    name: 'Home',
    data() {
        return {
            activeIndex: 'homeworkManagement',
            userName: '',
            className: '',
            classId: ''
        };
    },
    components: { Header },
    mounted: function() {
        this.userName = this.$route.params.userName;
        this.$http.get('Class/get_my_class/').then(response => {
            if (response.data !== 'Get my own class failed.') {
                this.className = response.data.class_name;
                this.classId = response.data.id;
                this.$router.push({ path: '/home/' + this.userName + '/homeworkManagement', query: { classId: this.classId }});
            } else {
                alert('获取班级失败！');
            }
        });
    },
    methods: {
        handleSelect(key) {
            this.$router.push({ path: key });
        },
        classIdChanged(val) {
            this.classId = val;
        }
    }
};
</script>

<style scoped>

.el-Menu {
    margin-top: 5px;
    margin-right: 5px;
    margin-left: 5px;
}

</style>
