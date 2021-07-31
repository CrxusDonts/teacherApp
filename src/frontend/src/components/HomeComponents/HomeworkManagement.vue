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
                prop="title"
                label="标题"
                width="250">
            </el-table-column>
            <el-table-column
                prop="start_time"
                label="开始时间"
                width="180">
            </el-table-column>
            <el-table-column
                prop="due_time"
                label="结束时间">
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
                            value-format="yyyy-MM-dd HH:mm"
                            :destroy-on-close="true"
                            type="datetimerange"
                            start-placeholder="开始日期"
                            end-placeholder="结束日期"
                            :default-time="['12:00:00']">
                        </el-date-picker>
                    </div>
                </el-form-item>
                <el-form-item label="是否可以重复提交" :label-width="formLabelWidth">
                    <el-radio v-model="form.repeatable" :label="true">可以重复提交</el-radio>
                    <el-radio v-model="form.repeatable" :label="false">不可重复提交</el-radio>
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
                id: 1,
                title: '三年级二班第二次作业',
                start_time: '2021-07-27 16:17',
                due_time: '2021-08-03 16:17',
                repeatable: 1
            }, {
                id: 2,
                title: '三年级二班第一次作业',
                start_time: '2021-07-27 16:17',
                due_time: '2021-08-03 16:17',
                repeatable: 1
            }, {
                id: 3,
                title: '三年级二班第三次作业',
                start_time: '2021-07-27 16:17',
                due_time: '2021-08-03 16:17',
                repeatable: 1
            }],
            form: {
                name: '',
                timeValue: '',
                repeatable: ''
            },
            newHomeworkFormVisible: false,
            formLabelWidth: '140px',
            classId: '',
            userName: ''
        };
    },
    mounted() {
        this.classId = this.$route.query.classId;
        this.userName = this.$route.query.userName;
    },
    methods: {
        newHomework() {
            if (this.form.name === '' || this.form.timeValue === '' || this.form.repeatable === '') {
                alert('请填入所有信息!');
            } else {
                this.newHomeworkFormVisible = false;
                // 向后端发送请求
                this.$http.post('Class/1/new_homework/', { // 暂时向id为1的班级添加作业 TODO 之后再改正
                    start_time: this.form.timeValue[0],
                    due_time: this.form.timeValue[1],
                    repeatable: this.form.repeatable
                }).then(response => {
                    if (response.data === 'New homework succeed.') {
                        alert('创建成功！');
                    } else {
                        alert('创建失败！');
                    }
                });
            }
            // 清空表单
            this.form = {};
        },
        handleEdit(index, row) {
            this.$router.push({ path: '/edithomework', query: { homeWork: row }});
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
