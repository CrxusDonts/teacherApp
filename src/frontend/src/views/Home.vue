<template>
    <div>
        <Header v-bind:userName="userName"></Header>
        <el-menu class="elMenu" default-active="homeworkManagement" mode="horizontal" @select="handleSelect"
                 :router="true">
            <el-menu-item index="homeworkManagement">作业管理</el-menu-item>
            <el-submenu index="management">
                <template slot="title">班级管理</template>
                <el-menu-item index="studentManagement">学生管理</el-menu-item>
                <el-menu-item index="assistantManagement">助教管理</el-menu-item>
            </el-submenu>
            <el-submenu index="grade">
                <template slot="title">成绩统计</template>
                <el-menu-item index="gradeByClass">按班级统计</el-menu-item>
                <el-menu-item index="gradeByStudent">按学生统计</el-menu-item>
            </el-submenu>
            <el-menu-item index="switchClass">班级切换</el-menu-item>
        </el-menu>
        <router-view/>
    </div>
</template>

<script>
import Header from '../components/Header.vue';

export default {
    name: 'Home',
    data() {
        return {
            activeIndex: 'homeworkManagement',
            userName: 'admin'
        };
    },
    components: {Header},
    mounted: function () {
        this.userName = this.$route.query.userName;
    },
    methods: {
        handleSelect(key) {
            this.$router.push({path: key});
            // console.log(key, keyPath);
        }
    }
};
</script>

<style scoped>

.elMenu {
    margin-top: 5px;
    margin-right: 5px;
    margin-left: 5px;
}

</style>
