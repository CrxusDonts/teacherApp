<template>
	<view>
		<view class="cu-bar bg-white">
			<view class="action">
				<text class="cuIcon-title text-blue"></text>请输入班级信息和你的信息
			</view>
		</view>
		<view class="cu-form-group margin-top">
			<view class="title">班级id</view>
				<input placeholder="请输入要申请加入的班级id" name="input"></input>
		</view>
		<view class="cu-form-group">
				<view class="title">姓名</view>
				<input placeholder="请输入你的姓名" name="input"></input>
		</view>
		<view class="cu-form-group">
				<view class="title">性别</view>
				<input placeholder="请输入你的性别" name="input"></input>
		</view>
		<view class="padding flex justify-end">
			<button class="cu-btn bg-grey lg">确认提交</button>
		</view>
	</view>
</template>

<script>
export default {
	data() {
	    return {
			user: {
				user_name: 'stupid之人',
			}
	    };
	},
    methods: {
	}
};
</script>

<style>
</style>
