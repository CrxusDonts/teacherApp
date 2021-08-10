<template>
    <div>
        <el-table
            :data="assistant"
            stripe
            style="width: 100%;
            margin-top: 10px;">
            <el-table-column align="center"
                             type="index"
                             :width="100">
            </el-table-column>
            <el-table-column
                prop="user_name"
                label="账号"
                width="180">
            </el-table-column>
            <el-table-column
                align="right"
                label="操作">
                <template slot="header">
                    <el-button type="success" plain icon="el-icon-plus" size="mini"
                               @click="dialog_form_visible = true">邀请</el-button>
                </template>
                <template slot-scope="scope">
                    <el-button type="danger" plain icon="el-icon-delete" size="mini"
                               @click="handleRemove(scope.$index, scope.row)">移除</el-button>
                </template>
            </el-table-column>
        </el-table>
        <!--邀请助教对话框-->
        <el-dialog title="邀请助教" :visible.sync="dialog_form_visible">
            <el-form :model="form">
                <el-form-item label="账号" :label-width="form_label_width">
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
            assistant: [],
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
        this.$http.post('Manager/get_teacher/', {
            class_id: this.class_id
        }).then(response => {
            if (response.data !== 'get_teacher failed.') {
                for (const value of response.data) {
                    this.assistant.push({ user_name: this.getUserName(value) });
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
                user_name: this.assistant[index].user_name,
                class_id: this.class_id
            }).then(response => {
                if (response.data !== 'delete_teacher failed.') {
                    alert('移除成功！');
                    this.assistant.splice(index, 1);
                } else {
                    alert('移除失败！不能移除该班的拥有者');
                }
            });
        },
        invite() {
            if (this.form.id === '') {
                alert('请输入账号');
                return;
            }
            this.dialog_form_visible = false;
            // 向后端发送请求
            if (!this.ifContain(this.assistant, this.form.id)) {
                this.$http.post('ManageInvitation/invite_assistant/', {
                    user_name: this.form.id,
                    class_id: this.class_id
                }).then(response => {
                    if (response.data !== 'invite failed.') {
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
            this.dialog_form_visible = false;
            this.form.id = '';
        },
        getUserName(string) {
            return string.split(',')[1].split(':')[1].split('"')[1];
        },
        ifContain(tableData, id) {
            for (const value of tableData) {
                if (value.user_name === id) {
                    return true;
                }
            }
            return false;
        }
    }
};
</script>
