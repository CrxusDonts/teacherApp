<template>
    <div>
        <el-table
            :data="gradeByHomework"
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
                               @click="handleDetail(scope.$index, scope.row)">查看详情
                    </el-button>
                </template>
            </el-table-column>
        </el-table>
        <!--表单提示框 -->
        <el-dialog title="新建作业" :visible.sync="new_homework_form_visible">
        </el-dialog>
    </div>
</template>

<script>
export default {
    name: 'GradeByHomework',
    data() {
        return {
            gradeByHomework: [],
            form: {
                title: '',
                time_value: '',
                repeatable: ''
            },
            new_homework_form_visible: false,
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
        handleDetail(index, row) {
            // TODO 与后端交互
        }
    }
};
</script>

