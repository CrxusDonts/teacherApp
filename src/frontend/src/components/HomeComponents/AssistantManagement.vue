<template>
    <div>
        <el-table
            :data="tableData"
            stripe
            style="width: 100%;
            margin-top: 10px;">
            <el-table-column align="center"
                             type="index"
                             :width="100">
            </el-table-column>
            <el-table-column
                prop="userName"
                label="账号"
                width="180">
            </el-table-column>
            <el-table-column
                align="right"
                label="操作">
                <template slot="header">
                    <el-button type="success" plain icon="el-icon-plus" size="mini"
                               @click="dialogFormVisible = true">邀请</el-button>
                </template>
                <template slot-scope="scope">
                    <el-button type="danger" plain icon="el-icon-delete" size="mini"
                               @click="handleRemove(scope.$index, scope.row)">移除</el-button>
                </template>
            </el-table-column>
        </el-table>
        <!--邀请助教对话框-->
        <el-dialog title="邀请助教" :visible.sync="dialogFormVisible">
            <el-form :model="form">
                <el-form-item label="账号" :label-width="formLabelWidth">
                    <!-- 暂未实现自动获得焦点-->
                    <el-input v-model="form.id" autocomplete="off" :autofocus="true"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="cancel">取 消</el-button>
                <el-button type="primary" @click="invite">邀 请</el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>
export default {
    name: 'AssistantManagement',
    data() {
        return {
            tableData: [],
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
        this.$http.post('Manager/get_teacher/', {
            class_id: this.classId
        }).then(response => {
            if (response.data !== 'get_teacher failed.') {
                for (let i = 0;i < response.data.length;i++) {
                    this.tableData.push({ userName: this.getUserName(response.data[i]) });
                }
            } else {
                alert('获取管理人员失败！');
            }
        });
    },
    methods: {
        // 移除助教
        handleRemove(index) {
            this.$http.post('Manager/delete_teacher/', {
                user_name: this.tableData[index].userName,
                class_id: this.classId
            }).then(response => {
                if (response.data !== 'delete_teacher failed.') {
                    alert('移除成功！');
                    this.tableData.splice(index, index + 1);
                } else {
                    alert('移除失败！不能移除该班的拥有者');
                }
            });
        },
        invite() {
            this.dialogFormVisible = false;
            // 向后端发送请求
            if (!this.ifContain(this.tableData, this.form.id)) {
                this.$http.post('ManageInvitation/invite_assistant/', {
                    user_name: this.form.id,
                    class_id: this.classId
                }).then(response => {
                    if (response.data === 'invite succeed.') {
                        alert('邀请成功！');
                    } else if (response.data === 'invite failed.') {
                        alert('邀请失败！请检查用户名');
                    }
                });
            } else {
                alert('该用户已在班级中。');
            }
            this.form.id = '';
        },
        cancel() {
            this.dialogFormVisible = false;
            this.form.id = '';
        },
        getUserName(string) {
            return string.split(',')[1].split(':')[1].split('"')[1];
        },
        ifContain(tableData, id) {
            for (let i = 0;i < tableData.length;i++) {
                if (tableData[i].userName === id) {
                    return true;
                }
            }
            return false;
        }
    }
};
</script>

<style scoped>

</style>
