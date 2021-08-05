<template>
	<view class="cu-card case">
		<view class="cu-item shadow">
				<view class="cu-item">
					<view class="content flex-sub padding">
						<view class="text-lg margin-left">{{order + '.' + choiceQuestion.text_content}}</view>
						<view class="flex margin-top margin-left" v-for="option in options">
							<view v-if="option.if_correct" class="cuIcon-check"></view>
							<view v-if="!option.if_correct" class="cuIcon-close"></view>
							{{String.fromCharCode("A".charCodeAt(0) - 1 + option.order)}}.{{option.text_content}}
						</view>
						<view class="flex margin-top margin-left">
							他的答案：
							<view v-for="student_answer in student_answers">
							{{String.fromCharCode("A".charCodeAt(0) - 1 + student_answer.order)}}
							</view>
						</view>
					</view>
				</view>
		</view>
	</view>
</template>

<script>
export default {
    props: ['choiceQuestion', 'order', 'index'],
    name: 'ChoiceQuestion',
    data() {
        return {
            options: [],
            student_answers: []
        };
    },
    mounted() {
        uni.request({
            url: 'ChoiceQuestion/' + this.choiceQuestion.id + '/get_options/',
            method: 'GET',
            success: res => {
                this.options = res.data;
            }
        });
    }
};
</script>

<style>
</style>
