<template>
	<view class="cu-card case">
		<view class="cu-item shadow">
				<view class="cu-item">
					<view class="content flex-sub padding">
						<view class="text-lg margin-left">{{order + '.' + completionQuestion.text_content}}</view>
						<view class="flex margin-top margin-left">
							正确答案：
							<view v-for="answer in answers">
							{{answer.answer}}
							</view>
						</view>
						<view class="flex margin-top margin-left">
							他的答案：
							<view v-for="student_answer in student_answers">
							{{student_answer.answer}}
							</view>
						</view>
					</view>
				</view>
		</view>
	</view>
</template>

<script>
export default {
	props: ['completionQuestion', 'order', 'index'],
	name: 'CompletionQuestion',
	data() {
	    return {
			options: [
				{
					order: 1,
					text_content: '是',
					if_correct: true
				},
				{
					order: 2,
					text_content: '不是',
					if_correct: false
				}
			],
			answers: [
				{
					answer: '将登太行雪满山',
				}
			],
			student_answers: [
				{
					answer: '将登太行雪满山',
				}
			]
	    };
	},
};
</script>

<style>
</style>
