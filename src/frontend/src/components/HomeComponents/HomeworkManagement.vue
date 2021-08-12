<template>
    <div>
        <el-table
            :data="homeworks"
            stripe
            style="width: 100%;
            margin-top: 10px;">
            <el-table-column align="center"
                             type="index"
                             :width="100">
            </el-table-column>
            <el-table-column
                prop="title"
                label="标题"
                width="250">
            </el-table-column>
            <el-table-column
                prop="start_time"
                label="开始时间"
                width="200">
            </el-table-column>
            <el-table-column
                prop="due_time"
                label="结束时间">
            </el-table-column>
            <el-table-column align="right">
                <template slot="header">
                    <el-button type="success" plain icon="el-icon-plus" size="mini"
                               @click="new_homework_form_visible = true">新建
                    </el-button>
                </template>
                <template slot-scope="scope">
                    <el-button type="primary" plain icon="el-icon-edit" size="mini"
                               @click="handleEdit(scope.$index, scope.row)">编辑
                    </el-button>
                    <el-button type="success" plain icon="el-icon-share" size="mini"
                               @click="handleShare(scope.$index, scope.row)">分享
                    </el-button>
                    <el-button type="danger" plain icon="el-icon-delete" size="mini"
                               @click="handleDelete(scope.$index, scope.row)">删除
                    </el-button>
                </template>
            </el-table-column>
        </el-table>
        <!--表单提示框 -->
        <el-dialog title="新建作业" :visible.sync="new_homework_form_visible">
            <el-form :model="form">
                <el-form-item label="作业名称" :label-width="form_label_width">
                    <el-input class="title" v-model="form.title" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="时间" :label-width="form_label_width">
                        <el-date-picker
                            v-model="form.time_value"
                            value-format="yyyy-MM-dd HH:mm"
                            :destroy-on-close="true"
                            type="datetimerange"
                            start-placeholder="开始日期"
                            end-placeholder="结束日期"
                            :default-time="['12:00:00']">
                        </el-date-picker>
                </el-form-item>
                <el-form-item label="是否可以重复提交" :label-width="form_label_width">
                    <el-radio class="repeatable" v-model="form.repeatable" :label="true">可以重复提交</el-radio>
                    <el-radio class="repeatable" v-model="form.repeatable" :label="false">不可重复提交</el-radio>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="form={};new_homework_form_visible = false;">取 消</el-button>
                <el-button type="primary" @click="newHomework">确 定</el-button>
            </div>
        </el-dialog>
        <!--二维码-->
        <el-dialog title="分享" :visible.sync="qr_code_visible">
            <vue-qr :text="qr_code.url" :logoSrc="qr_code.image_url" :margin="10" colorDark="#333333" colorLight="#fff"
                    :size="200"></vue-qr>
        </el-dialog>
    </div>
</template>

<script>
import vueQr from 'vue-qr';
export default {
    name: 'HomeworkManagement',
    components: {
        vueQr
    },
    data() {
        return {
            homeworks: [],
            form: {
                title: '',
                time_value: '',
                repeatable: ''
            },
            new_homework_form_visible: false,
            form_label_width: '140px',
            class_id: '',
            user_name: '',
            qr_code_visible: false,
            qr_code: {
                url: 'https://se.jisuanke.com/CourseOrganizationPlatform/bugmakers/teacherapp/-/issues',
                // eslint-disable-next-line no-undef
                image_url: require('../../assets/icon3.jpg')
            }
        };
    },
    mounted() {
        this.class_id = this.$route.query.class_id;
        this.user_name = this.$route.params.user_name;
        this.$http.get('Class/' + this.class_id + '/get_homeworks/').then(response => {
            if (response.data !== 'Class not found.') {
                this.homeworks = response.data;
            } else {
                alert('获取班级失败！');
            }
            for (const homework of this.homeworks) {
                homework.start_time = this.handleTime(homework.start_time);
                homework.due_time = this.handleTime(homework.due_time);
            }
        });
    },
    methods: {
        newHomework() {
            if (this.form.title === '' || this.form.time_value === '' || this.form.repeatable === '') {
                alert('请填入所有信息!');
            } else {
                this.new_homework_form_visible = false;
                // 向后端发送请求
                this.$http.post('Class/' + this.class_id + '/new_homework/', {
                    title: this.form.title,
                    start_time: this.form.time_value[0],
                    due_time: this.form.time_value[1],
                    repeatable: this.form.repeatable
                }).then(response => {
                    if (response.data === 'New homework succeed.') {
                        alert('创建成功！');
                        this.$http.get('Class/' + this.class_id + '/get_homeworks/').then(get_homeworks_response => {
                            if (get_homeworks_response.data !== 'Class not found.') {
                                this.homeworks = get_homeworks_response.data;
                                for (const homework of this.homeworks) {
                                    homework.start_time = this.handleTime(homework.start_time);
                                    homework.due_time = this.handleTime(homework.due_time);
                                }
                            } else {
                                alert('获取班级失败！');
                            }
                        });
                    } else {
                        alert('创建失败！');
                    }
                    // 清空表单
                    this.form = {};
                });
            }
        },
        handleEdit(index) {
            this.$router.push({ path: '/edithomework/' + this.homeworks[index].id, query: {
                user_name: this.user_name,
                class_id: this.class_id
            }});
        },
        handleShare() {
            this.qr_code_visible = true;
        },
        handleDelete(index) {
            this.$http.delete('Homework/' + this.homeworks[index].id + '/');
            this.homeworks.splice(index, 1);
        },
        handleTime(time) {
            return time.substr(0, 19).replace('T', ' ');
        }
    }
};
</script>
<style scoped>

.title {
    width: 400px;
    text-align: left;
}

</style>
