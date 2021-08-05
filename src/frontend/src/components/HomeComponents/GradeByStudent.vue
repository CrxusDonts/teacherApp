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
                prop="name"
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
                    <el-button plain icon="el-icon-edit" size="mini" @click="handleDetail(scope.$index, scope.row)">查看详情
                    </el-button>
                </template>
            </el-table-column>
        </el-table>
        <el-dialog title="作业详情" :visible.sync="dialog_visible">
            <el-table :data="this_student_grade">
                <el-table-column property="title" label="作业标题" width="200"></el-table-column>
                <el-table-column property="if_finish" label="是否完成" width="200"></el-table-column>
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
            grades_by_student: [],
            this_student_grade: [],
            dialog_visible: false,
            class_id: '',
            user_name: ''
        };
    },
    mounted() {
        this.class_id = this.$route.query.class_id;
        this.user_name = this.$route.params.user_name;
        this.$http.post('People/get_class_student/', {
            class_id: this.class_id
        }).then(response => {
            if (response.data !== 'get_class_student failed.') {
                for (let i = 0; i < response.data.length; i++) {
                    this.students.push({
                        id: response.data[i].id,
                        name: response.data[i].name,
                        have_finished: 0,
                        have_not_finished: 0
                    });
                }
                for (let i = 0; i < this.students.length; i++) {
                    this.$http.post('People/get_student_homework/', {
                        class_id: this.class_id,
                        people_id: this.students[i].id
                    }).then(response => {
                        for (let j = 0; j < response.data.length; j++) {
                            this.grades_by_student.push({
                                id: this.students[i].id, name: this.students[i].name,
                                homework_title: response.data[j].homework_title, if_finish: response.data[j].if_finish
                            });
                            if (this.grades_by_student[j].if_finish) {
                                this.students[i].have_finished += 1;
                            }
                            if (!this.grades_by_student[j].if_finish) {
                                this.students[i].have_not_finished += 1;
                            }
                        }
                    });
                }
            } else {
                alert('获取学生失败！');
            }
        });
    },
    methods: {
        handleDetail(index) {
            for (let i = 0; i < this.grades_by_student.length; i++) {
                if (this.grades_by_student[i].id === this.students[index].id) {
                    this.this_student_grade.push({
                        title: this.grades_by_student[i].homework_title,
                        if_finish: this.grades_by_student[i].if_finish ? '完成' : '未完成'
                    });
                }
            }
            this.dialog_visible = true;
        }
    }
};
</script>

<style scoped>

</style>
