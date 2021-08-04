<template>
	<view class="cu-card case">
		<view class="cu-item shadow">
			<view class="cu-item">
				<view class="content flex-sub padding">
					<view class="text-lg margin-left">{{order + '.' + completionQuestion.text_content}}</view>
				</view>
			</view>
			<view v-for="student_answer in student_answers" class="cu-form-group margin-left">
				<view class="title">{{student_answer.order}}.</view>
				<input class="solid" placeholder="请输入答案" name="input" :value="student_answer.answer"></input>
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
			number: 3,
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
			student_answers: []
	    };
	},
	mounted() {
		for (var i = 1; i <= this.number; i++){
			var student_answer = {
				order: i,
				answer: '',
			};
			this.student_answers.push(student_answer);
		};
	}
};
</script>

<style>
</style>
