<template>
	<view>
		<view class="cu-bar bg-white solid-bottom margin-top">
			<view class="action">
				<text class="cuIcon-title text-blue "></text> {{'欢迎你，' + user.user_name}}
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
			user: '',
			classes: [
				{
					id: 1304,
					class_name: '非人类研究中心'
				},
				{
					id: 1603,
					class_name: '嘉心糖俱乐部'
				}
			]
	    };
	},
	onLoad: function (option) {
		this.user = JSON.parse(option.user);
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
