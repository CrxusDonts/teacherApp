<template>
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
            prop="invitor_id"
            label="邀请人账号"
            width="180">
        </el-table-column>
        <el-table-column
            prop="invitor_name"
            label="邀请人姓名"
            width="180">
        </el-table-column>
        <el-table-column
            prop="class_id"
            label="邀请班级号"
            width="180">
        </el-table-column>
        <el-table-column
            prop="class_name"
            label="邀请班级名">
        </el-table-column>
        <el-table-column
            align="right"
            label="操作">
            <template slot-scope="scope">
                <el-button type="success" plain icon="el-icon-check" size="mini"
                           @click="handleAccept(scope.$index, scope.row)">接受
                </el-button>
                <el-button type="danger" plain icon="el-icon-close" size="mini"
                           @click="handleRefuse(scope.$index, scope.row)">拒绝
                </el-button>
            </template>
        </el-table-column>
    </el-table>
</template>

<script>
export default {
    name: 'InviteMe',
    data() {
        return {
            tableData: [{
                invitor_id: '12',
                invitor_name: '果果果',
                class_id: '34',
                class_name: '1'
            }, {
                invitor_id: '12',
                invitor_name: '果果果',
                class_id: '34',
                class_name: '1'
            }],
            form: {
                id: ''
            },
            dialogFormVisible: false,
            formLabelWidth: '120px',
            classId: '',
            userName: ''
        };
    },
    mounted() {
        this.classId = this.$route.query.classId;
        this.userName = this.$route.params.userName;
    },
    methods: {
        handleAccept(index, row) {
            // TODO 与后端交互
        },
        handleRefuse(index, row) {
            // TODO 与后端交互
        }
    }
};
</script>

<style scoped>

</style>
