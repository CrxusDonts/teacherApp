<template>
    <el-table
        :data="invite_me"
        stripe
        style="width: 100%;
            margin-top: 10px;">
        <el-table-column align="center"
                         type="index"
                         :width="100">
        </el-table-column>
        <el-table-column
            prop="invitor_user_name"
            label="邀请人账号"
            width="180">
        </el-table-column>
        <el-table-column
            prop="invite_class_id"
            label="邀请班级号"
            width="180">
        </el-table-column>
        <el-table-column
            prop="invite_class_name"
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
            invite_me: [],
            form: {
                id: ''
            },
            dialog_form_visible: false,
            form_label_width: '120px',
            class_id: '',
            user_name: ''
        };
    },
    mounted() {
        this.class_id = this.$route.query.class_id;
        this.user_name = this.$route.params.user_name;
        this.$http.get('ManageInvitation/get_invitation/').then(response => {
            if (response.data !== 'get_invitation failed.') {
                for (let i = 0; i < response.data.length; i++) {
                    this.invite_me.push({
                        invitation_id: this.getInviteId(response.data[i]),
                        invitor_user_name: this.getInviter(response.data[i]),
                        invite_class_id: this.getInviterClassId(response.data[i]),
                        invite_class_name: this.getInviterClassName(response.data[i])
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
                invitation_id: this.invite_me[index].invitation_id
            }).then(() => {
                this.invite_me.splice(index, 1);
                this.$emit('nums_of_invite_me_changed');
            });
        },
        handleRefuse(index) {
            this.$http.post('ManageInvitation/handle_invitation/', {
                if_accept: 0,
                invitation_id: this.invite_me[index].invitation_id
            }).then(() => {
                this.invite_me.splice(index, 1);
                this.$emit('nums_of_invite_me_changed');
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
