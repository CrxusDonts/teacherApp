<template>
    <div>
        <Header></Header>
        <el-menu class="el-Menu" default-active="homeworkManagement" mode="horizontal" @select="handleSelect"
                 :router="true">
            <el-menu-item index="homeworkManagement" :route=
                "{ path: 'homeworkManagement', query: { class_id: this.class_id} }">作业管理</el-menu-item>
            <el-submenu index="management">
                <template slot="title">班级管理</template>
                <el-menu-item index="studentManagement" :route=
                    "{ path: 'studentManagement', query: { class_id: this.class_id} }">学生管理</el-menu-item>
                <el-menu-item index="studentApply" :route=
                    "{ path: 'studentApply', query: { class_id: this.class_id} }">学生申请
                    <el-badge v-if="num_of_join_class_request > 0" v-bind:value="num_of_join_class_request" /></el-menu-item>
                <el-menu-item index="assistantManagement" :route=
                    "{ path: 'assistantManagement', query: { class_id: this.class_id} }">助教管理</el-menu-item>
                <el-menu-item index="inviteMe" :route=
                    "{ path: 'inviteMe', query: { class_id: this.class_id} }">邀请我的
                    <el-badge v-if="num_of_invite_me > 0" v-bind:value="num_of_invite_me" /></el-menu-item>
            </el-submenu>
            <el-submenu index="grade">
                <template slot="title">成绩统计</template>
                <el-menu-item index="gradeByHomework" :route=
                    "{ path: 'gradeByHomework', query: { class_id: this.class_id} }">按作业统计</el-menu-item>
                <el-menu-item index="gradeByStudent" :route=
                    "{ path: 'gradeByStudent', query: { class_id: this.class_id} }">按学生统计</el-menu-item>
            </el-submenu>
            <el-menu-item index="switchClass" :route=
                "{ path: 'switchClass', query: { class_id: this.class_id} }">班级切换</el-menu-item>
        </el-menu>
        <router-view class="router" @classIdChanged="classIdChanged"
                     @nums_of_invite_me_changed="nums_of_invite_me_changed"
                     @nums_of_join_class_request_changed="nums_of_join_class_request_changed"></router-view>
    </div>
</template>

<script>
import Header from '../components/Header';

export default {
    name: 'Home',
    data() {
        return {
            user_name: '',
            class_name: '',
            class_id: '',
            num_of_invite_me: '',
            num_of_join_class_request: ''
        };
    },
    components: {
        Header
    },
    mounted: function() {
        this.user_name = this.$route.params.user_name;
        // 获取班级
        this.$http.get('Class/get_my_class/').then(response => {
            if (response.data !== 'Get my own class failed.') {
                this.class_name = response.data.class_name;
                this.class_id = response.data.id;
                this.$router.push({ path: '/home/' + this.user_name + '/homeworkManagement', query: { class_id: this.class_id }});
                this.handleBadgeNum();
            } else {
                alert('获取班级失败！');
            }
        });
    },
    methods: {
        handleSelect(key) {
            this.$router.push({ path: key });
        },
        // 获取旗袍数量
        handleBadgeNum() {
            this.$http.get('ManageInvitation/get_invitation/').then(get_invitation_response => {
                if (get_invitation_response.data !== 'get_invitation failed.') {
                    this.num_of_invite_me = get_invitation_response.data.length;
                } else {
                    alert('获取邀请列表失败，请重试！');
                }
            });
            this.$http.post('JoinClassRequest/get_join_class_request/', {
                class_id: this.class_id
            }).then(get_join_class_request_response => {
                this.num_of_join_class_request = get_join_class_request_response.data.length;
            });
        },
        classIdChanged(val) {
            this.class_id = val;
            this.handleBadgeNum();
        },
        nums_of_invite_me_changed() {
            this.num_of_invite_me -= 1;
        },
        nums_of_join_class_request_changed() {
            this.num_of_join_class_request -= 1;
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

.router {
    margin-bottom: 10px;
}
</style>
