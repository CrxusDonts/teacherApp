<template>
	<view>
		<view class="cu-bar bg-white">
			<view class="action">
				<text class="cuIcon-title text-blue"></text>请选择你的身份
			</view>
		</view>
		<view class="padding flex flex-direction">
			<button class="cu-btn bg-grey lg cuIcon-people" @click="toTeacherHome()">我是老师</button>
			<button class="cu-btn bg-grey margin-tb-sm lg cuIcon-people" @click="toStudentHome()">我是学生</button>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			open_id: '',
		}
	},
	mounted() {
		uni.login({
		  success: res => {
		    const appid = 'wx9d16d4512ab0e560';
		    const secret = '739d9212f30d5daf9bc419528967de60';
		    const url = 'https://api.weixin.qq.com/sns/jscode2session?appid=' + appid + '&secret=' + secret + '&js_code=' + res.code + '&grant_type=authorization_code';
		    uni.request({
		      url: url, 
		      method: 'GET', 
		      success: result => {
		        this.open_id = result.data.openid;
		      },
		      fail: err => {
				  console.log('获取openId失败')
			  } 
		    });
		  }
		});
	},
    methods: {
		toTeacherHome() {
			uni.navigateTo({
				url: './TeacherHome?open_id='+this.open_id
			});
		},
		toStudentHome() {
			uni.navigateTo({
				url: './StudentHome?open_id='+this.open_id
			})
		}
	}
};
</script>

<style>
</style>
