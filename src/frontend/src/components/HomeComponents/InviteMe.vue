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
            if (response.data !== 'get_invitation failed.') {
                for (let i = 0; i < response.data.length; i++) {
                    this.inviteMe.push({
                        invitationId: this.getInviteId(response.data[i]),
                        invitorUserName: this.getInviter(response.data[i]),
                        inviteClassId: this.getInviterClassId(response.data[i]),
                        inviteClassName: this.getInviterClassName(response.data[i])
                    });
                }
            } else {
                alert('获取邀请列表，请重试！');
            }
        });
    },
    methods: {
        handleAccept(index) {
            this.$http.post('ManageInvitation/handle_invitation/', {
                if_accept: 1,
                invitation_id: this.inviteMe[index].invitationId
            }).then(() => {
                this.inviteMe.splice(index, index + 1);
            });
        },
        handleRefuse(index) {
            this.$http.post('ManageInvitation/handle_invitation/', {
                if_accept: 0,
                invitation_id: this.inviteMe[index].invitationId
            }).then(() => {
                this.inviteMe.splice(index, index + 1);
            });
        },
        // 由于后端返回的是字符串，所以要对字符串进行处理
        getInviteId(string) {
            return string.split(',')[0].split(':')[1];
        },
        getInviter(string) {
            return string.split(',')[1].split(':')[1].split('"')[1];
        },
        getInviterClassId(string) {
            return string.split(',')[2].split(':')[1];
        },
        getInviterClassName(string) {
            return string.split(',')[3].split(':')[1].split('"')[1];
        }
    }
};
</script>

<style scoped>

</style>
