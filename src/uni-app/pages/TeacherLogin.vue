<template>
	<view>
		<view class="cu-bar bg-white">
			<view class="action">
				<text class="cuIcon-title text-blue"></text>请输入你的信息
			</view>
		</view>
		<view class="cu-form-group margin-top">
			<view class="title">后台账户名</view>
				<input placeholder="请输入你的后台用户名" name="input" @input="inputUsername"></input>
		</view>
		<view class="cu-form-group">
				<view class="title">后台账户密码</view>
				<input placeholder="请输入你的后台密码" name="input" password="true" @input="inputPasswork"></input>
		</view>
		<view class="padding flex justify-end">
			<button class="cu-btn bg-grey lg" @click="login()">确认提交</button>
		</view>
	</view>
</template>

<script>
export default {
	data() {
	    return {
			user: {
				user_name: '',
				password: ''
			}
	    };
	},
    methods: {
		inputUsername(e) {
			this.user.user_name = e.target.value;
		},
		inputPasswork(e) {
			this.user.password = e.target.value;
		},
		login() {
			uni.navigateTo({
				url: 'home/TeacherHome?user=' + JSON.stringify(this.user) 
			});
		}
	}
};
</script>

<style>
</style>
