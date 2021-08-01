<template>
    <el-table
        :data="inviteMe"
        stripe
        style="width: 100%;
            margin-top: 10px;">
        <el-table-column align="center"
                         type="index"
                         :width="100">
        </el-table-column>
        <el-table-column
            prop="invitorUserName"
            label="邀请人账号"
            width="180">
        </el-table-column>
        <el-table-column
            prop="inviteClassId"
            label="邀请班级号"
            width="180">
        </el-table-column>
        <el-table-column
            prop="inviteClassName"
            label="邀请班级名">
        </el-table-column>
        <el-table-column
            align="right"
            label="操作">
            <template slot-scope="scope">
                <el-button type="success" plain icon="el-icon-check" size="mini"
                           @click="handleAccept(scope.$index, scope.row)">接受
                </el-button>
                <el-button type="danger" plain icon="el-icon-close" size="mini"
                           @click="handleRefuse(scope.$index, scope.row)">拒绝
                </el-button>
            </template>
        </el-table-column>
    </el-table>
</template>

<script>
export default {
    name: 'InviteMe',
    data() {
        return {
            inviteMe: [],
            form: {
                id: ''
            },
            dialogFormVisible: false,
            formLabelWidth: '120px',
            classId: '',
            userName: ''
        };
    },
    mounted() {
        this.classId = this.$route.query.classId;
        this.userName = this.$route.params.userName;
        this.$http.get('ManageInvitation/get_invitation/').then(response => {
            for (let i = 0;i < response.data.length;i++) {
                this.inviteMe.push({ invitationId: response.data[i].id, invitorUserName: response.data[i].inviter, inviteClassId: response.data[i].clazz, inviteClassName: '1465' });
            }
        });
    },
    methods: {
        handleAccept(index) {
            // TODO 与后端交互
            this.$http.post('ManageInvitation/handle_invitation/', {
                if_accept: 1,
                invitation_id: this.inviteMe[index].invitationId
            }).then(response => {
                console.log(response.data);
            });
        },
        handleRefuse(index) {
            // TODO 与后端交互
            this.$http.post('ManageInvitation/handle_invitation/', {
                if_accept: 0,
                invitation_id: this.inviteMe[index].invitationId
            }).then(response => {
                console.log(response.data);
            });
        }
    }
};
</script>

<style scoped>

</style>
