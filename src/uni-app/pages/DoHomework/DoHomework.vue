<template>
	<view>
		<view class="cu-bar bg-white solid-bottom margin-top">
			<view class="action">
				<text class="cuIcon-title text-blue "></text> {{homework.title}}
			</view>
			<button class="cu-btn bg-grey margin-right">点击提交</button>
		</view>
		<ChoiceQuestion v-for="(choiceQuestion, index) in choice_questions" :choiceQuestion="choiceQuestion"
                    :order='order + index' :index="index">
		</ChoiceQuestion>
		<CompletionQuestion v-for="(completionQuestion, index) in completion_questions" :completionQuestion="completionQuestion"
                        :order='choice_questions.length + order + index' :index="index">
		</CompletionQuestion>
		<SubjectiveQuestion v-for="(subjectiveQuestion, index) in subjective_questions" :subjectiveQuestion="subjectiveQuestion"
                        :order='choice_questions.length + completion_questions.length + order + index' :index="index">
		</SubjectiveQuestion>
	</view>
</template>

<script>
import ChoiceQuestion from './ChoiceQuestion.vue';
import CompletionQuestion from './CompletionQuestion.vue';
import SubjectiveQuestion from './SubjectiveQuestion.vue';
export default {
    data() {
        return {
            order: 1,
            student: '',
            homework: '',
            choice_questions: [
                {
                    text_content: '请问你是嘉心糖吗？'
                }
            ],
            completion_questions: [
                {
                    text_content: '欲渡黄河冰塞川，____________。'
                }
            ],
            subjective_questions: [
                {
                    text_content: '请问你是嘉心糖吗？'
                }
            ]
        };
    },
    components: {
        ChoiceQuestion,
        CompletionQuestion,
        SubjectiveQuestion
    },
    onLoad: function(option) {
        this.student = JSON.parse(option.student);
        this.homework = JSON.parse(option.homework);
    },
    methods: {
    }
};
</script>

<style>
</style>
