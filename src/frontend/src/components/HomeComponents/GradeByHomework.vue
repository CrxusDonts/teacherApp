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
                prop="homework_title"
                label="标题"
                width="180">
            </el-table-column>
            <el-table-column
                prop="have_finished"
                label="已提交人数"
                width="180">
            </el-table-column>
            <el-table-column
                prop="have_not_finished"
                label="未提交人数"
                width="180">
            </el-table-column>
            <el-table-column
                align="right"
                label="操作">
                <template slot-scope="scope">
                    <el-button plain icon="el-icon-search" size="mini" @click="handleDetail(scope.$index, scope.row)">查看详情
                    </el-button>
                </template>
            </el-table-column>
        </el-table>
        <el-dialog title="作业详情" :visible.sync="dialog_visible">
            <el-table :data="this_homework_grade">
                <el-table-column property="student_name" label="学生姓名" width="200"></el-table-column>
                <el-table-column property="if_finish" label="是否完成" width="200"></el-table-column>
            </el-table>
        </el-dialog>
    </div>
</template>

<script>
export default {
    name: 'GradeByHomework',
    data() {
        return {
            homeworks: [],
            details: [],
            this_homework_grade: [],
            dialog_visible: false,
            class_id: '',
            user_name: ''
        };
    },
    mounted() {
        this.class_id = this.$route.query.class_id;
        this.user_name = this.$route.params.user_name;
        this.$http.post('People/get_student_homework/', {
            class_id: this.class_id
        }).then(response => {
            // 获得作业完成详情
            this.details = response.data;
            this.$http.get('Class/' + this.class_id + '/get_homeworks/').then(homework_response => {
                for (let i = 0;i < homework_response.data.length;i++) {
                    this.homeworks.push({ homework_id: homework_response.data[i].id, homework_title: homework_response.data[i].title, have_finished: 0, have_not_finished: 0 });
                    for (const value of this.details) {
                        if (value.homework_id === this.homeworks[i].homework_id && value.if_finish) {
                            this.homeworks[i].have_finished += 1;
                        }
                        if (value.homework_id === this.homeworks[i].homework_id && !value.if_finish) {
                            this.homeworks[i].have_not_finished += 1;
                        }
                    }
                }
            });
        });
    },
    methods: {
        handleDetail(index) {
            this.this_homework_grade = [];
            for (const value of this.details) {
                if (this.homeworks[index].homework_id === value.homework_id) {
                    this.this_homework_grade.push({ student_name: value.student_name, if_finish: value.if_finish ? '已完成' : '未完成' });
                }
            }
            this.dialog_visible = true;
        }
    }
};
</script>

