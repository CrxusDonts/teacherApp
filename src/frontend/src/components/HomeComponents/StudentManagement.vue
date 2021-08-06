<template>
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
            align="right"
            label="操作">
            <template slot-scope="scope">
                <el-button plain icon="el-icon-edit" size="mini" @click="handleEdit(scope.$index, scope.row)">编辑学生</el-button>
                <el-button type="danger" plain icon="el-icon-delete" size="mini" @click="handleRemove(scope.$index, scope.row)">移除学生</el-button>
            </template>
        </el-table-column>
    </el-table>
</template>

<script>
export default {
    name: 'StudentManagement',
    data() {
        return {
            students: [],
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
                this.students = response.data;
            } else {
                alert('失败！');
            }
        });
    },
    methods: {
        handleEdit(index, row) {
            // TODO 与后端交互
        },
        handleRemove(index) {
            this.$http.delete('People/' + this.students[index].id + '/');
            this.students.splice(index, 1);
        }
    }
};
</script>
