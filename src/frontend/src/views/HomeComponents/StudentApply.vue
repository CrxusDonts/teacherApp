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
            label="学号"
            width="180">
        </el-table-column>
        <el-table-column
            prop="name"
            label="姓名"
            width="180">
        </el-table-column>
        <el-table-column
            prop="gender"
            label="性别">
        </el-table-column>
        <el-table-column
            align="right"
            label="操作">
            <template>
                <el-button plain icon="el-icon-edit" size="mini" @click="permit">同意</el-button>
                <el-button type="danger" plain icon="el-icon-delete" size="mini" @click="refuse">拒绝</el-button>
            </template>
        </el-table-column>
    </el-table>
</template>

<script>
export default {
    name: 'StudentApply',
    data() {
        return {
            search: '',
            tableData: [{
                id: '12',
                name: '果果果',
                gender: '男',
            }, {
                id: '20',
                name: '王小虎',
                gender: '男',
            }]
        };
    },
    methods: {
        permit() {

        },
        refuse() {

        }
    }
};
</script>

<style scoped>

</style>
