<template>
	<view>
		<view class="cu-bar bg-white">
			<view class="action">
				<text class="cuIcon-title text-blue"></text>{{ '目前的班级:' + clazz.class_name }}
			</view>
		</view>
		<view class="padding flex flex-direction">
			<button class="cu-btn bg-grey lg cuIcon-people">切换班级</button>
			<button class="cu-btn bg-grey margin-tb-sm lg cuIcon-people">批改作业</button>
		</view>
	</view>
</template>

<script>
export default {
	props:['open_id'],
	data() {
	    return {
			clazz: {
				id: 1304,
				class_name: '非人类研究中心',
			}
	    };
	},
	onLoad: function (option) {
		this.open_id = option.open_id;
	}
};
</script>

<style>
</style>
