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
            prop="date"
            label="日期"
            width="180">
        </el-table-column>
        <el-table-column
            prop="name"
            label="姓名"
            width="180">
        </el-table-column>
        <el-table-column
            prop="address"
            label="地址">
        </el-table-column>
        <el-table-column align="right">
            <template slot="header">
                <el-row :gutter="10" type="flex" justify="end">
                    <el-col :span="6">
                        <el-button type="success" plain icon="el-icon-plus" size="mini">新建</el-button>
                    </el-col>
                </el-row>
            </template>
            <template slot-scope="scope">
                <el-button type="primary" plain icon="el-icon-edit" size="mini"
                           @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
                <el-button type="success" plain icon="el-icon-share" size="mini"
                           @click="handleShare(scope.$index, scope.row)">分享</el-button>
                <el-button type="warning" plain icon="el-icon-edit" size="mini"
                           @click="handleCancel(scope.$index, scope.row)">取消发布</el-button>
                <el-button type="danger" plain icon="el-icon-delete" size="mini"
                           @click="handleDelete(scope.$index, scope.row)">删除</el-button>
            </template>
        </el-table-column>
    </el-table>
</template>

<script>
export default {
    name: 'HomeworkManagement',
    data() {
        return {
            tableData: [{
                date: '2016-05-03',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1518 弄'
            }, {
                date: '2016-05-02',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1518 弄'
            }, {
                date: '2016-05-04',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1518 弄'
            }]
        };
    },
    methods: {
        handleEdit(index, row) {
            // TODO Edit
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
