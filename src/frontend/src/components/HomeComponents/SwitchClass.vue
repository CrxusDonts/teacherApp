<template>
    <div>
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
                label="班级序号"
                width="180">
            </el-table-column>
            <el-table-column
                prop="class_name"
                label="班级名称"
                width="180">
            </el-table-column>
            <el-table-column
                align="right"
                label="操作">
                <template slot-scope="scope">
                    <el-button plain icon="el-icon-edit" size="mini" @click="handleSwitch(scope.$index)">切换</el-button>
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
export default {
    name: 'SwitchClass',
    data() {
        return {
            tableData: [{
                id: '',
                class_name: ''
            }],
            classId: '',
            userName: ''
        };
    },
    mounted() {
        this.classId = this.$route.query.classId;
        this.userName = this.$route.params.userName;
        this.$http.get('Class/get_my_class/').then(response => {
            if (response.data !== 'Get my own class failed.') {
                this.data = response.data;
                this.tableData[0].id = response.data.id;
                this.tableData[0].class_name = response.data.class_name;
            } else {
                alert('失败！');
            }
            this.$http.get('Class/get_manage_class_list/').then(response => {
                if (response.data !== 'Get my manage class failed.') {
                    if (response.data.length !== 0) {
                        this.tableData.push({ id: response.data.id, class_name: response.data.class_name });
                    }
                } else {
                    alert('失败！');
                }
            });
        });
    },
    methods: {
        handleSwitch(index) {
            this.classId = this.tableData[index].id;
            this.$emit('classIdChanged', this.classId);
        }
    }
};
</script>

<style scoped>

.el-carousel__item h3 {
    margin: 0;
    font-size: 14px;
    line-height: 200px;
    color: #475669;
    opacity: .75;
}

</style>
