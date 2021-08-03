<template>
    <div>
        <el-table
            :data="homeworks"
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
                width="200">
            </el-table-column>
            <el-table-column
                prop="due_time"
                label="结束时间">
            </el-table-column>
            <el-table-column align="right">
                <template slot="header">
                    <el-button type="success" plain icon="el-icon-plus" size="mini"
                               @click="new_homework_form_visible = true">新建
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
        <el-dialog title="新建作业" :visible.sync="new_homework_form_visible">
            <el-form :model="form">
                <el-form-item label="作业名称" :label-width="form_label_width">
                    <el-input v-model="form.title" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="时间" :label-width="form_label_width">
                    <div class="block">
                        <el-date-picker
                            v-model="form.time_value"
                            value-format="yyyy-MM-dd HH:mm"
                            :destroy-on-close="true"
                            type="datetimerange"
                            start-placeholder="开始日期"
                            end-placeholder="结束日期"
                            :default-time="['12:00:00']">
                        </el-date-picker>
                    </div>
                </el-form-item>
                <el-form-item label="是否可以重复提交" :label-width="form_label_width">
                    <el-radio v-model="form.repeatable" :label="true">可以重复提交</el-radio>
                    <el-radio v-model="form.repeatable" :label="false">不可重复提交</el-radio>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="form={};new_homework_form_visible = false;">取 消</el-button>
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
            homeworks: [],
            form: {
                title: '',
                time_value: '',
                repeatable: ''
            },
            new_homework_form_visible: false,
            form_label_width: '140px',
            class_id: '',
            user_name: ''
        };
    },
    mounted() {
        this.class_id = this.$route.query.class_id;
        this.user_name = this.$route.params.user_name;
        this.$http.get('Class/' + this.class_id + '/get_homeworks/').then(response => {
            if (response.data !== 'Class not found.') {
                this.homeworks = response.data;
            } else {
                alert('获取班级失败！');
            }
        });
    },
    methods: {
        newHomework() {
            if (this.form.name === '' || this.form.time_value === '' || this.form.repeatable === '') {
                alert('请填入所有信息!');
            } else {
                this.new_homework_form_visible = false;
                // 向后端发送请求
                this.$http.post('Class/' + this.class_id + '/new_homework/', {
                    title: this.form.title,
                    start_time: this.form.time_value[0],
                    due_time: this.form.time_value[1],
                    repeatable: this.form.repeatable
                }).then(response => {
                    if (response.data === 'New homework succeed.') {
                        alert('创建成功！');
                        this.$http.get('Class/' + this.class_id + '/get_homeworks/').then(response => {
                            if (response.data !== 'Class not found.') {
                                this.homeworks = response.data;
                            } else {
                                alert('获取班级失败！');
                            }
                        });
                    } else {
                        alert('创建失败！');
                    }
                    // 清空表单
                    this.form = {};
                });
            }
        },
        handleEdit(index) {
            this.$router.push({ path: '/edithomework/' + this.homeworks[index].id, query: {
                user_name: this.user_name,
                class_id: this.class_id
            }});
        },
        handleShare(index, row) {
            // TODO Share
        },
        handleCancel(index, row) {
            // TODO Cancel
        },
        handleDelete(index) {
            this.$http.delete('Homework/' + this.homeworks[index].id);
            this.homeworks.splice(index, index + 1);
        }
    }
};
</script>
