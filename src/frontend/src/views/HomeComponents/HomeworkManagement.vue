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
                prop="date"
                label="日期"
                width="180">
            </el-table-column>
            <el-table-column
                prop="name"
                label="姓名"
                width="180">
            </el-table-column>
            <el-table-column
                prop="address"
                label="地址">
            </el-table-column>
            <el-table-column align="right">
                <template slot="header">
                    <el-button type="success" plain icon="el-icon-plus" size="mini"
                               @click="newHomeworkFormVisible = true">新建
                    </el-button>
                </template>
                <template slot-scope="scope">
                    <el-button type="primary" plain icon="el-icon-edit" size="mini"
                               @click="handleEdit(scope.$index, scope.row)">编辑
                    </el-button>
                    <el-button type="success" plain icon="el-icon-share" size="mini"
                               @click="handleShare(scope.$index, scope.row)">分享
                    </el-button>
                    <el-button type="warning" plain icon="el-icon-edit" size="mini"
                               @click="handleCancel(scope.$index, scope.row)">取消发布
                    </el-button>
                    <el-button type="danger" plain icon="el-icon-delete" size="mini"
                               @click="handleDelete(scope.$index, scope.row)">删除
                    </el-button>
                </template>
            </el-table-column>
        </el-table>
        <!--表单提示框 -->
        <el-dialog title="新建作业" :visible.sync="newHomeworkFormVisible">
            <el-form :model="form">
                <el-form-item label="作业名称" :label-width="formLabelWidth">
                    <el-input v-model="form.name" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="时间" :label-width="formLabelWidth">
                    <div class="block">
                        <el-date-picker
                            v-model="form.timeValue"
                            :destroy-on-close="true"
                            type="datetimerange"
                            start-placeholder="开始日期"
                            end-placeholder="结束日期"
                            :default-time="['12:00:00']">
                        </el-date-picker>
                    </div>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="form={};newHomeworkFormVisible = false;">取 消</el-button>
                <el-button type="primary" @click="newHomework">确 定</el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>
export default {
    name: 'HomeworkManagement',
    data() {
        return {
            tableData: [{
                date: '2016-05-03',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1518 弄'
            }, {
                date: '2016-05-02',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1518 弄'
            }, {
                date: '2016-05-04',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1518 弄'
            }],
            form: {
                name: '',
                timeValue: ''
            },
            newHomeworkFormVisible: false,
            formLabelWidth: '120px'
        };
    },
    methods: {
        newHomework() {
            this.newHomeworkFormVisible = false;
            // TODO 像后端发送请求
            // 清空表单
            this.form = {};
        },
        handleEdit(index, row) {
            // TODO Edit
        },
        handleShare(index, row) {
            // TODO Share
        },
        handleCancel(index, row) {
            // TODO Cancel
        },
        handleDelete(index, row) {
            // TODO Delete
        }
    }
};
</script>
