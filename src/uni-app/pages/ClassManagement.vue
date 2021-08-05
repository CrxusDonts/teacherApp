<template>
	<view>
		<view class="cu-bar bg-white solid-bottom margin-top">
			<view class="action">
				<text class="cuIcon-title text-blue "></text> {{clazz.class_name}}
			</view>
		</view>
		<view class="cu-list menu-avatar">
			<view class="cu-item" :class="size?'solids-top':'solid-top'" v-for="homework in homeworks" @click="toHomeworkManagement(homework)">
				<view class="cu-avatar round lg cuIcon-copy"></view>
				<view class="content">
					<view class="text-grey">{{homework.title}}</view>
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
    onLoad: function(option) {
        this.clazz = JSON.parse(option.clazz);
        this.is_teacher = JSON.parse(option.is_teacher);
    },
    mounted() {
        uni.request({
            url: 'http://localhost:8002/teacherApp/Class/' + this.clazz.id + '/get_homeworks/',
            method: 'get',
            success: res => {
                if (res.data !== 'Class not found.') {
                    this.homeworks = res.data;
                } else {
                    uni.showToast({
                        title: '获取作业列表失败',
                        icon: 'none'
                    });
                }
            }
        });
    },
    methods: {
        toHomeworkManagement(homework) {
            if (this.is_teacher) {
                uni.navigateTo({
                    url: 'HomeworkManagement?homework=' + JSON.stringify(homework)
                });
            } else {
                uni.navigateTo({
                    url: 'DoHomework/DoHomework?homework=' + JSON.stringify(homework) + '&student=' + JSON.stringify(this.student)
                });
            }
        }
    }
};
</script>

<style>
</style>
