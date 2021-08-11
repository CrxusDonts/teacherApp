<template>
    <view>
        <view class="cu-bar bg-white solid-bottom margin-top">
            <view class="action">
                <text class="cuIcon-title text-blue "></text>
                {{ student.name + '的' + homework.title }}
            </view>
            <button class="cu-btn bg-grey margin-right" @click="comment()">批改完毕</button>
        </view>
        <choice-question v-for="(choiceQuestion, index) in choice_questions" :choiceQuestion="choiceQuestion"
                         :order='order + index' :index="index" :student="student">
        </choice-question>
        <completion-question v-for="(completionQuestion, index) in completion_questions"
                             :completionQuestion="completionQuestion"
                             :order='choice_questions.length + order + index' :index="index" :student="student">
        </completion-question>
        <subjective-question v-for="(subjectiveQuestion, index) in subjective_questions"
                             :subjectiveQuestion="subjectiveQuestion"
                             :order='choice_questions.length + completion_questions.length + order + index'
                             :index="index" :student="student" ref="subjectiveQuestion">
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
    onLoad: function (option) {
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
        comment() {
            const _this = this;
            uni.showModal({
                title: '完成批改?',
                success: res => {
                    if (res.confirm) {
                        _this.$refs.subjectiveQuestion.forEach(subjectiveQuestion => {
                            subjectiveQuestion.comment();
                        });
                        uni.showToast({
                            title: '批改成功',
                            icon: 'none'
                        });
                        setTimeout(() => {
                            uni.navigateBack();
                        }, 1000);
                    }
                }
            });
        }
    }
};
</script>

