<template>
	<view class="cu-card case">
		<view class="cu-item shadow">
				<view class="cu-item">
					<view class="content flex-sub padding">
						<view class="text-lg margin-left">{{order + '.' + completionQuestion.text_content}}</view>
						<view class="flex margin-top margin-left">
							正确答案：
							<view v-for="answer in answers" class="answer">
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
            answers: [],
            student_answers: []
        };
    },
    mounted() {
        uni.request({
            url: 'http://localhost:8002/teacherApp/CompletionQuestion/' + this.completionQuestion.id + '/get_answers/',
            method: 'GET',
            success: res => {
                this.answers = res.data;
            }
        });
    }
};
</script>

<style>
.answer + .answer {
    margin-left: 50rpx;
}
</style>
