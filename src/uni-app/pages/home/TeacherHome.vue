<template>
	<view>
		<view class="cu-bar bg-white solid-bottom margin-top">
			<view class="action">
				<text class="cuIcon-title text-blue "></text> {{'欢迎你，' + user_name}}
			</view>
			<button class="cu-btn bg-grey margin-right">退出登陆</button>
		</view>
		<view class="cu-list menu-avatar">
			<view class="cu-item" :class="size?'solids-top':'solid-top'" v-for="clazz in classes" @click="toClassManagement(clazz)">
				<view class="cu-avatar round lg cuIcon-group"></view>
				<view class="content">
					<view class="text-grey">{{clazz.class_name}}</view>
				</view>
				<view class="action">
					<view class="cu-tag round bg-grey sm">5</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
export default {
	data() {
	    return {
			user_name: '',
			classes: []
	    };
	},
	onLoad: function (option) {
		this.user_name = option.user_name;
	},
	mounted() {
		uni.request({
		    url: 'http://localhost:8002/teacherApp/Class/get_my_class/',
		    method: 'get',
		    success: res => {
		        if (res.data !== 'Get my own class failed.') {
		            this.classes.push(res.data);
		        } else {
					uni.showToast({
					    title: '获取我的班级失败',
						icon: "none"
					});
				}
		    }
		});
		uni.request({
		    url: 'http://localhost:8002/teacherApp/Class/get_manage_class_list/',
		    method: 'get',
		    success: res => {
		        if (res.data !== 'Get my manage class failed.') {
		           for (let i = 0;i < res.data.length; i++) {
		               this.classes.push(res.data[i]);
		           }
		        } else {
					uni.showToast({
					    title: '获取我管理的班级失败',
						icon: "none"
					});
				}
		    }
		});
	},
	methods: {
		toClassManagement(clazz) {
			uni.navigateTo({
				url: '../ClassManagement?clazz=' + JSON.stringify(clazz) + '&is_teacher=1'
			});
		}
	}
};
</script>

<style>
</style>
