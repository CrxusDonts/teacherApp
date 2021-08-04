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
			student: {
				name: 'asdsa',
			},
			homeworks: [
				{
					'title': '第一次作业'
				},
				{
					'title': '第二次作业'
				}
			]
	    };
	},
	onLoad: function (option) {
		this.clazz = JSON.parse(option.clazz);
		this.is_teacher = JSON.parse(option.is_teacher);
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
