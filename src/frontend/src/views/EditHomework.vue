<template>
  <div>
    <Header v-bind:userName="userName"></Header>
    <el-header class="title">
      {{ homework.title }}
      <el-button type="primary" class="go-back" @click=goBack>返回</el-button>
    </el-header>
    <ChoiceQuestion v-for="(choiceQuestion, index) in choiceQuestions" :choicequestion="choiceQuestion"
                    :order='order + index' :key="choiceQuestionConst+choiceQuestion.id">
    </ChoiceQuestion>
    <el-button type="success" style="margin-top: 5px;" @click=newChoiceQuestion>新增选择题</el-button>
    <CompletionQuestion v-for="(completionQuestion, index) in this.completionQuestions"
                        :completionquestion="completionQuestion"
                        :order='order + choiceQuestions.length + index'
                        :key="completionQuestionConst+completionQuestion.id">

    </CompletionQuestion>
    <el-button type="success" style="margin-top: 5px;" @click=newCompletionQuestion>新增填空题</el-button>
    <SubjectiveQuestion v-for="(subjectiveQuestion, index) in this.subjectiveQuestions"
                        :subjectivequestion="subjectiveQuestion"
                        :order='order + choiceQuestions.length + completionQuestions.length + index'
                        :key="subjectiveQuestionConst+subjectiveQuestion.id">
    </SubjectiveQuestion>
    <el-button type="success" style="margin-top: 5px;" @click=newSubjectiveQuestion>新增主观题</el-button>
  </div>
</template>

<script>
import Header from '../components/Header';
import ChoiceQuestion from '@/components/ChoiceQuestion';
import CompletionQuestion from '@/components/CompletionQuestion';
import SubjectiveQuestion from '@/components/SubjectiveQuestion';
export default {
    name: 'EditHomework',
    data() {
        return {
            order: 1,
            userName: 'admin',
            homework: '',
            choiceQuestionConst: 'choiceQuestion',
            completionQuestionConst: 'completionQuestion',
            subjectiveQuestionConst: 'subjectiveQuestion',
            choiceQuestions: [],
            completionQuestions: [],
            subjectiveQuestions: []
        };
    },
    components: {
        Header,
        ChoiceQuestion,
        CompletionQuestion,
        SubjectiveQuestion
    },
    mounted: function() {
        this.homework = this.$route.query.homework;
        this.userName = this.$route.query.userName;
        this.$http.get('Homework/' + this.homework.id + '/get_choice_question/')
            .then(response => {
                this.choiceQuestions = response.data;
            });
        this.$http.get('Homework/' + this.homework.id + '/get_completion_question/')
            .then(response => {
                this.completionQuestions = response.data;
            });
        this.$http.get('Homework/' + this.homework.id + '/get_subjective_question/')
            .then(response => {
                this.subjectiveQuestions = response.data;
            });
    },
    beforeDestroy() {
        for (let i = 0; i < this.choiceQuestions.length; i++) {
            this.$http.put('ChoiceQuestion/' + this.choiceQuestions[i].id + '/', {
                text_content: this.choiceQuestions[i].text_content,
                homework: this.choiceQuestions[i].homework
            });
        }
        for (let i = 0; i < this.completionQuestions.length; i++) {
            this.$http.put('CompletionQuestion/' + this.completionQuestions[i].id + '/', {
                text_content: this.completionQuestions[i].text_content,
                homework: this.completionQuestions[i].homework
            });
        }
        for (let i = 0; i < this.subjectiveQuestions.length; i++) {
            this.$http.put('SubjectiveQuestion/' + this.subjectiveQuestions[i].id + '/', {
                text_content: this.subjectiveQuestions[i].text_content,
                homework: this.subjectiveQuestions[i].homework
            });
        }
    },
    methods: {
        goBack() {
            this.$router.push({ path: '/home/' + this.userName });
        },
        newChoiceQuestion() {
            this.$http.post('Homework/' + this.homework.id + '/new_choice_question/', {
                text_content: '请输入题目'
            }).then(response => {
                this.choiceQuestions.push(response.data);
            });
        },
        newCompletionQuestion() {
            this.$http.post('Homework/' + this.homework.id + '/new_completion_question/', {
                text_content: '请输入题目'
            }).then(response => {
                this.completionQuestions.push(response.data);
            });
        },
        newSubjectiveQuestion() {
        }
    }
};
</script>

<style scoped>
.title {
    padding-top: 10px;
    font-size: 30px;
    text-align: center;
    background-color: white;
}

.go-back {
    float: right;
}
</style>
