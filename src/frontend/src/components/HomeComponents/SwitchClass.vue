<template>
    <div>
        <el-table
            :data="classes"
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
            classes: [{
                id: '',
                class_name: ''
            }],
            class_id: '',
            user_name: ''
        };
    },
    mounted() {
        this.class_id = this.$route.query.class_id;
        this.user_name = this.$route.params.user_name;
        this.$http.get('Class/get_my_class/').then(response => {
            if (response.data !== 'Get my own class failed.') {
                this.classes[0].id = response.data.id;
                this.classes[0].class_name = response.data.class_name;
            } else {
                alert('失败！');
            }
            this.$http.get('Class/get_manage_class_list/').then(get_manage_class_list_response => {
                if (get_manage_class_list_response.data !== 'Get my manage class failed.') {
                    for (const value of get_manage_class_list_response.data) {
                        this.classes.push({ id: value.id, class_name: value.class_name });
                    }
                } else {
                    alert('失败！');
                }
            });
        });
    },
    methods: {
        handleSwitch(index) {
            if (this.class_id === this.classes[index].id.toString()) {
                alert('你当前位于此班级');
                return;
            }
            this.class_id = this.classes[index].id;
            this.$emit('classIdChanged', this.class_id);
            alert('切换成功');
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
