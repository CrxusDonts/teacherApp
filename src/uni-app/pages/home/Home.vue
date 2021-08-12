<template>
    <view class="bg-gradual-blue light page">
        <view class="cu-bar bg-white">
            <view class="action">
                <text class="cuIcon-title text-blue"></text>
                请选择你的身份
            </view>
        </view>
        <view class="padding flex flex-direction">
            <button class="button bg-white" @click="toTeacherHome()">
                <image class="image" :src="teacher_image_url"></image>
			</button>
            <button class="button bg-white margin-tb-sm" @click="toStudentHome()">
                <image class="image" :src="student_image_url"></image>
			</button>
        </view>
    </view>
</template>

<script>
export default {
    data() {
        return {
            open_id: '',
			teacher_image_url: '/static/teacher.jpg',
            student_image_url: '/static/student.png'
        };
    },
    mounted() {
        // 获取open_id
        uni.login({
            success: res => {
                const appid = 'wx9d16d4512ab0e560';
                const secret = '739d9212f30d5daf9bc419528967de60';
                const url = 'https://api.weixin.qq.com/sns/jscode2session?appid=' + appid + '&secret=' + secret + '&js_code=' + res.code + '&grant_type=authorization_code';
                uni.request({
                    url: url,
                    method: 'GET',
                    success: res => {
                        this.open_id = res.data.openid;
                    }
                });
            }
        });
    },
    methods: {
        toTeacherHome() {
            if (this.open_id !== '') {
                uni.request({
                    url: this.$BASICURL + 'BackendAccount/determine_first_login/',
                    data: {
                        'open_id': this.open_id,
                        'is_teacher': true
                    },
                    method: 'post',
                    success: res => {
                        if (res.data === 'teacher first login') {
                            uni.navigateTo({
                                url: '../TeacherLogin?open_id=' + this.open_id
                            });
                        } else {
                            uni.navigateTo({
                                url: 'TeacherHome?user_name=' + res.data
                            });
                        }
                    },
                    fail: res => {
                        console.log(res);
                    }
                });
            }
        },
        toStudentHome() {
            if (this.open_id !== '') {
                uni.request({
                    url: this.$BASICURL + 'BackendAccount/determine_first_login/',
                    data: {
                        'open_id': this.open_id,
                        'is_teacher': false
                    },
                    method: 'post',
                    success: res => {
                        if (res.data !== 'login failed.') {
                            uni.navigateTo({
                                url: './StudentHome?open_id=' + this.open_id
                            });
                        } else {
                            uni.showToast({
                                title: '登陆失败',
                                icon: 'none'
                            });
                        }
                    }
                });
            }
        }
    }
};
</script>

<style>
.button {
    width: 450upx;
    height: 450upx;
    background-color: rgb(246, 246, 246);
}

.image {
    width: 200upx;
    height: 200upx;
	margin-top: 120upx;
}
</style>
