<template>
    <el-table
        :data="join_class_request"
        stripe
        style="width: 100%;
            margin-top: 10px;">
        <el-table-column align="center"
                         type="index"
                         :width="100">
        </el-table-column>
        <el-table-column
            prop="name"
            label="姓名">
        </el-table-column>
        <el-table-column
            align="right"
            label="操作">
            <template slot-scope="scope">
                <el-button plain icon="el-icon-edit" size="mini" @click="handleAccept(scope.$index, scope.row)">同意
                </el-button>
                <el-button type="danger" plain icon="el-icon-delete" size="mini"
                           @click="handleRefuse(scope.$index, scope.row)">拒绝
                </el-button>
            </template>
        </el-table-column>
    </el-table>
</template>

<script>
export default {
    name: 'StudentApply',
    data() {
        return {
            join_class_request: [],
            class_id: '',
            user_name: ''
        };
    },
    mounted() {
        this.class_id = this.$route.query.class_id;
        this.user_name = this.$route.params.user_name;
        this.$http.post('JoinClassRequest/get_join_class_request/', {
            class_id: this.class_id
        }).then(response => {
            for (const value of response.data.length) {
                this.join_class_request.push({
                    id: value.join_class_request_id,
                    name: value.name
                });
            }
        });
    },
    methods: {
        handleAccept(index) {
            this.$http.post('JoinClassRequest/handle_join_class_request/', {
                if_accept: 1,
                join_class_request_id: this.join_class_request[index].id
            }).then(response => {
                if (response.data === 'handle_join_class_request succeed.') {
                    this.join_class_request.splice(index, 1);
                    this.$emit('nums_of_join_class_request_changed');
                } else {
                    alert('失败，请重试！');
                }
            });
        },
        handleRefuse(index) {
            this.$http.post('JoinClassRequest/handle_join_class_request/', {
                if_accept: 0,
                join_class_request_id: this.join_class_request[index].id
            }).then(response => {
                if (response.data === 'handle_join_class_request succeed.') {
                    this.join_class_request.splice(index, 1);
                    this.$emit('nums_of_join_class_request_changed');
                } else {
                    alert('失败，请重试！');
                }
            });
        }
    }
};
</script>

