<template>
	<view>
		<view class="cu-bar bg-white solid-bottom margin-top">
						<view class="action">
							<text class="cuIcon-title text-orange "></text> 班级列表
						</view>
					</view>
					<view class="cu-list menu-avatar">
						<view class="cu-item">
							<view class="cu-avatar round lg" style="background-image:url(https://ossweb-img.qq.com/images/lol/web201310/skin/big10001.jpg);"></view>
							<view class="content">
								<view class="text-grey">凯尔</view>
								<view class="text-gray text-sm flex">
									<view class="text-cut">
										<text class="cuIcon-infofill text-red  margin-right-xs"></text>
										我已天理为凭，踏入这片荒芜，不再受凡人的枷锁遏制。我已天理为凭，踏入这片荒芜，不再受凡人的枷锁遏制。
									</view> </view>
							</view>
							<view class="action">
								<view class="text-grey text-xs">22:20</view>
								<view class="cu-tag round bg-grey sm">5</view>
							</view>
						</view>
						</view>
					</view>
	</view>
</template>

<script>
export default {
	props:['open_id'],
	data() {
	    return {
			clazz: [
				{
					id: 1304,
					class_name: 非人类研究中心
				},
				{
					id: 1603,
					class_name: 夹心糖俱乐部
				}
			]
	    };
	},
	onLoad: function (option) {
		this.open_id = option.open_id;
	}
};
</script>

<style>
</style>
