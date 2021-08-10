<template>
	<view>
		<view class="cu-bar bg-white solid-bottom margin-top">
			<view class="action">
				<text class="cuIcon-title text-blue "></text> {{homework.title}}
			</view>
			<button class="cu-btn bg-grey margin-right" @click="submitHomework()">点击提交</button>
		</view>
		<choice-question v-for="(choiceQuestion, index) in choice_questions" :choiceQuestion="choiceQuestion"
                    :order='order + index' :index="index" ref="choiceQuestion">
		</choice-question>
		<completion-question v-for="(completionQuestion, index) in completion_questions" :completionQuestion="completionQuestion"
                        :order='choice_questions.length + order + index' :index="index" ref="completionQuestion">
		</completion-question>
		<subjective-question v-for="(subjectiveQuestion, index) in subjective_questions" :subjectiveQuestion="subjectiveQuestion"
                        :order='choice_questions.length + completion_questions.length + order + index' :index="index"
						ref="subjectiveQuestion">
		</subjective-question>
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
            clazz: '',
            choice_questions: [],
            completion_questions: [],
            subjective_questions: []
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
    mounted() {
        uni.request({
            url: this.$BASICURL + 'Homework/' + this.homework.id + '/get_choice_question/',
            method: 'GET',
            success: res => {
                this.choice_questions = res.data;
            }
        });
        uni.request({
            url: this.$BASICURL + 'Homework/' + this.homework.id + '/get_completion_question/',
            method: 'GET',
            success: res => {
                this.completion_questions = res.data;
            }
        });
        uni.request({
            url: this.$BASICURL + 'Homework/' + this.homework.id + '/get_subjective_question/',
            method: 'GET',
            success: res => {
                this.subjective_questions = res.data;
            }
        });
    },
    methods: {
        submitHomework() {
            const _this = this;
            uni.showModal({
                title: '是否提交?',
                success: res => {
                    if (res.confirm) {
                        let is_empty = false;
                        _this.$refs.choiceQuestion.forEach(choiceQuestion => {
                            if (choiceQuestion.isEmpty()) {
                                uni.showToast({
                                    title: '请完成所有题目',
                                    icon: 'none'
                                });
                                is_empty = true;
                            }
                        });
                        _this.$refs.completionQuestion.forEach(completionQuestion => {
                            if (completionQuestion.isEmpty()) {
                                uni.showToast({
                                    title: '请完成所有题目',
                                    icon: 'none'
                                });
                                is_empty = true;
                            }
                        });
                        _this.$refs.subjectiveQuestion.forEach(subjectiveQuestion => {
                            if (subjectiveQuestion.isEmpty()) {
                                uni.showToast({
                                    title: '请完成所有题目',
                                    icon: 'none'
                                });
                                is_empty = true;
                            }
                        });
                        if (!is_empty) {
                            _this.$refs.choiceQuestion.forEach(choiceQuestion => {
                                choiceQuestion.submitChoiceQuestion(_this.student.id);
                            });
                            _this.$refs.completionQuestion.forEach(completionQuestion => {
                                completionQuestion.submitCompletionQuestion(_this.student.id);
                            });
                            _this.$refs.subjectiveQuestion.forEach(subjectiveQuestion => {
                                subjectiveQuestion.submitSubjectiveQuestion(_this.student.id);
                            });
                            uni.showToast({
                                title: '提交成功',
                                icon: 'none'
                            });
                            setTimeout(() => {
                                uni.navigateBack();
                            }, 1000);
                        }
                    }
                }
            });
        }
    }
};
</script>

