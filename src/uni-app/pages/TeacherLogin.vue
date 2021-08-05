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
            open_id: '',
            user_name: '',
            password: ''
        };
    },
    onLoad: function(option) {
        this.open_id = option.open_id;
    },
    methods: {
        inputUsername(e) {
            this.user_name = e.target.value;
        },
        inputPasswork(e) {
            this.password = e.target.value;
        },
        login() {
            uni.request({
                url: 'http://localhost:8002/teacherApp/BackendAccount/miniapp_teacher_first_login/',
                data: {
                    'open_id': this.open_id,
                    'user_name': this.user_name,
                    'password': this.password
                },
                method: 'post',
                success: res => {
                    if (res.data === 'login succeeded.') {
                        uni.navigateTo({
                            url: 'home/TeacherHome?user_name=' + this.user_name
                        });
                    } else {
						uni.showToast({
						    title: '登陆失败',
							icon: "none"
						});
					}
                }
            });
        }
    }
};
</script>

<style>
</style>
