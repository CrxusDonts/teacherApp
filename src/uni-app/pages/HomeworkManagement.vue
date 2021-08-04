<template>
	<view>
		<view class="cu-bar bg-white solid-bottom margin-top">
			<view class="action">
				<text class="cuIcon-title text-blue "></text> {{homework.title}}
			</view>
		</view>
		<view class="cu-list menu-avatar">
			<view class="cu-item" :class="size?'solids-top':'solid-top'" v-for="student in students" @click="checkHome(student)">
				<view class="cu-avatar round lg cuIcon-people"></view>
				<view class="content">
					<view class="text-grey">{{student.name}}</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
export default {
	data() {
	    return {
			homework: '',
			students: [
				{
					'name': '嘉然'
				},
				{
					'name': '乃琳'
				}
			]
	    };
	},
	onLoad: function (option) {
		this.homework = JSON.parse(option.homework);
	},
	methods: {
		checkHome(student) {
			uni.navigateTo({
				url: 'Checkhomework/CheckHomework?student=' + JSON.stringify(student) + '&homework=' + JSON.stringify(this.homework)
			});
		}
	}
};
</script>

<style>
</style>
