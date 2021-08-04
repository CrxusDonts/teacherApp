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
            user: {
                id: 3,
                user_name: '',
                password: ''
            }
        };
    },
    onLoad: function(option) {
        this.open_id = option.open_id;
    },
    methods: {
        inputUsername(e) {
            this.user.user_name = e.target.value;
        },
        inputPasswork(e) {
            this.user.password = e.target.value;
        },
        login() {
            uni.request({
                url: 'http://localhost:8002/teacherApp/BackendAccount/miniapp_teacher_first_login/',
                data: {
                    'open_id': this.open_id,
                    'user_name': this.user.user_name,
                    'password': this.user.password
                },
                method: 'post',
                success: res => {
                    if (res.data === 'login succeeded.') {
                        uni.navigateTo({
                            url: 'home/TeacherHome?user=' + JSON.stringify(this.user)
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
