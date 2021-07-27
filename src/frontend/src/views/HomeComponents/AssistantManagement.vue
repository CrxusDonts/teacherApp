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
                prop="id"
                label="账号"
                width="180">
            </el-table-column>
            <el-table-column
                prop="name"
                label="姓名"
                width="180">
            </el-table-column>
            <el-table-column
                prop="status"
                label="身份">
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
            tableData: [{
                id: '12',
                name: '果果果',
                status: '老师',
            }, {
                id: '20',
                name: '王小虎',
                status: '助教',
            }],
            form: {
                id: ''
            },
            dialogFormVisible: false,
            formLabelWidth: '120px'
        };
    },
    methods: {
        // 移除助教
        handleRemove(index, row) {
            console.log(index, row);
        },
        // 邀请助教
        invite () {
            this.dialogFormVisible = false;
            // 向后端发送请求

            this.form.id='';
        },
        // 取消邀请
        cancel () {
            this.dialogFormVisible = false;
            this.form.id='';
        }
    }
};
</script>

<style scoped>

</style>
