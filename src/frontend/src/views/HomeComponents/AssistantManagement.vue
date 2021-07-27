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
            <template slot-scope="scope">
                <el-button type="danger" plain icon="el-icon-delete" size="mini"
                           @click="handleRemove(scope.$index, scope.row)">移除</el-button>
            </template>
        </el-table-column>
    </el-table>
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
            }]
        };
    },
    methods :{
        // 移除助教
        handleRemove(index, row) {
            console.log(index, row);
        }
    }
};
</script>

<style scoped>

</style>
