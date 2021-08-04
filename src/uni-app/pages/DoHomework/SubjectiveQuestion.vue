<template>
	<view class="cu-card case">
		<view class="cu-item shadow">
			<view class="cu-item">
				<view class="content flex-sub padding">
					<view class="text-lg margin-left">{{order + '.' + subjectiveQuestion.text_content}}</view>
				</view>
			</view>
			<image class="margin" src="https://ossweb-img.qq.com/images/lol/web201310/skin/big10006.jpg"></image>
			<button class="cu-btn block line-black lg margin">
				<text class="cuIcon-upload"></text> 上传答案
			</button>
		</view>
	</view>
</template>

<script>
export default {
	props: ['subjectiveQuestion', 'order', 'index'],
	name: 'SubjectiveQuestion'
};
</script>

<style>
</style>
