<template>
    <div>
        <el-table
            :data="students"
            stripe
            style="width: 100%;
            margin-top: 10px;">
            <el-table-column align="center"
                             type="index"
                             :width="100">
            </el-table-column>
            <el-table-column
                prop="student_name"
                label="姓名"
                width="180">
            </el-table-column>
            <el-table-column
                prop="have_finished"
                label="已提交作业"
                width="180">
            </el-table-column>
            <el-table-column
                prop="have_not_finished"
                label="未提交作业"
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
        <el-dialog title="作业详情" :visible.sync="dialog_visible" width="650px">
            <el-table :data="this_student_grade">
                <el-table-column property="homework_title" label="作业标题" width="300"></el-table-column>
                <el-table-column property="if_finish" label="是否完成" width="300"></el-table-column>
            </el-table>
        </el-dialog>
    </div>
</template>

<script>
export default {
    name: 'GradeByStudent',
    data() {
        return {
            students: [],
            details: [],
            this_student_grade: [],
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
            this.details = response.data;
            this.$http.post('People/get_class_student/', {
                class_id: this.class_id
            }).then(homework_response => {
                for (let i = 0;i < homework_response.data.length;i++) {
                    this.students.push({ student_id: homework_response.data[i].id, student_name: homework_response.data[i].name, have_finished: 0, have_not_finished: 0 });
                    for (const value of this.details) {
                        if (value.student_id === this.students[i].student_id && value.if_finish) {
                            this.students[i].have_finished += 1;
                        }
                        if (value.student_id === this.students[i].student_id && !value.if_finish) {
                            this.students[i].have_not_finished += 1;
                        }
                    }
                }
            });
        });
    },
    methods: {
        handleDetail(index) {
            this.this_student_grade = [];
            for (const value of this.details) {
                if (this.students[index].student_id === value.student_id) {
                    this.this_student_grade.push({ homework_title: value.homework_title, if_finish: value.if_finish ? '已完成' : '未完成' });
                }
            }
            this.dialog_visible = true;
        }
    }
};
</script>
