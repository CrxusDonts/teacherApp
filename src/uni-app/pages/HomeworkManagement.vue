<template>
    <view>
        <view class="cu-bar bg-white solid-bottom margin-top">
            <view class="action">
                <text class="cuIcon-title text-blue" style="float: right;"></text>
                {{ clazz.class_name }}
            </view>
            <view v-if="!is_teacher" class="action">
                <text style="float: right;"></text>
                {{ student.name }}
            </view>
        </view>
        <view class="cu-list menu-avatar">
            <view class="cu-item" :class="size?'solids-top':'solid-top'" v-for="homework in homeworks"
                  @click="toHomeworkManagement(homework)">
                <view class="cu-avatar round lg cuIcon-copy"></view>
                <view class="content">
                    <view class="text-grey">{{ homework.title }}</view>
                </view>
                <view class="margin-top-lg">
                    <view class="margin-top-lg text-grey text-xs">{{ '截止时间:' + homework.due_time }}</view>
                </view>
            </view>
        </view>
    </view>
</template>

<script>
export default {
    data() {
        return {
            clazz: '',
            is_teacher: '',
            student: [],
            homeworks: []
        };
    },
    onLoad: function (option) {
        this.clazz = JSON.parse(option.clazz);
        this.is_teacher = JSON.parse(option.is_teacher);
    },
    mounted() {
        uni.request({
            url: this.$BASICURL + 'Class/' + this.clazz.id + '/get_homeworks/',
            method: 'get',
            success: res => {
                if (res.data !== 'Class not found.') {
                    this.homeworks = res.data;
                    for (const homework of this.homeworks) {
                        uni.request({
                            url: this.$BASICURL + 'Homework/' + homework.id + '/get_due_time/',
                            method: 'get',
                            success: res => {
                                homework.due_time = res.data;
                            }
                        });
                    }
                } else {
                    uni.showToast({
                        title: '获取作业列表失败',
                        icon: 'none'
                    });
                }
            }
        });
        uni.request({
            url: this.$BASICURL + 'People/get_student/',
            data: {
                'class_id': this.clazz.id
            },
            method: 'POST',
            success: res => {
                this.student = res.data;
            }
        });
    },
    methods: {
        toHomeworkManagement(homework) {
            if (this.is_teacher) {
                uni.navigateTo({
                    url: 'StudentHomeworkManagement?homework=' + JSON.stringify(homework) + '&clazz=' + JSON.stringify(this.clazz)
                });
            } else {
                uni.request({
                    url: this.$BASICURL + 'Homework/is_corrected/',
                    data: {
                        'homework_id': homework.id,
                        'student_id': this.student.id
                    },
                    method: 'POST',
                    success: isCorrectedRes => {
                        if (isCorrectedRes.data === 'True') {
                            uni.navigateTo({
                                url: 'AfterDoHomework/AfterDoHomework?homework=' + JSON.stringify(homework) + '&student=' + JSON.stringify(this.student)
                            });
                        } else if (isCorrectedRes.data === 'False') {
                            uni.request({
                                url: this.$BASICURL + 'Homework/' + homework.id + '/is_overdue/',
                                method: 'GET',
                                success: isOverdueRes => {
                                    if (isOverdueRes.data === 'False') {
                                        uni.navigateTo({
                                            url: 'DoHomework/DoHomework?homework=' + JSON.stringify(homework) + '&student=' + JSON.stringify(this.student)
                                        });
                                    } else if (isOverdueRes.data === 'True') {
                                        uni.showToast({
                                            title: '该作业已过期',
                                            icon: 'none'
                                        });
                                    }
                                }
                            });
                        }
                    }
                });
            }
        }
    }
};
</script>
