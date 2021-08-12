<template>
    <view>
        <view class="cu-bar bg-white solid-bottom margin-top">
            <view class="action">
                <text class="cuIcon-title text-blue "></text>
                {{ homework.title }}
            </view>
        </view>
        <view class="cu-list menu-avatar">
            <view class="cu-item" :class="size?'solids-top':'solid-top'" v-for="student in students"
                  @click="checkHomework(student)">
                <view class="cu-avatar round lg cuIcon-people"></view>
                <view class="content">
                    <view class="text-grey">{{ student.name }}</view>
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
            homework: '',
            students: []
        };
    },
    onLoad: function (option) {
        this.clazz = JSON.parse(option.clazz);
        this.homework = JSON.parse(option.homework);
    },
    mounted() {
        uni.request({
            url: this.$BASICURL + 'People/get_done_homework_students/',
            data: {
                'class_id': this.clazz.id,
                'homework_id': this.homework.id
            },
            method: 'POST',
            success: res => {
                this.students = res.data;
            }
        });
    },
    methods: {
        checkHomework(student) {
            uni.request({
                url: this.$BASICURL + 'Homework/is_corrected/',
                data: {
                    'homework_id': this.homework.id,
                    'student_id': student.id
                },
                method: 'POST',
                success: res => {
                    if (res.data === 'True') {
                        uni.navigateTo({
                            url: 'AfterCheckhomework/AfterCheckHomework?student=' + JSON.stringify(student) + '&homework=' + JSON.stringify(this.homework)
                        });
                    } else if (res.data === 'False') {
                        uni.navigateTo({
                            url: 'Checkhomework/CheckHomework?student=' + JSON.stringify(student) + '&homework=' + JSON.stringify(this.homework)
                        });
                    }
                }
            });
        }
    }
};
</script>
