<template>
  <div>
    <Header v-bind:userName="userName"></Header>
    <el-header class="title">
      {{ homework.title }}
      <el-button type="primary" class="go-back" @click=goBack>返回</el-button>
    </el-header>
    <ChoiceQuestion v-for="(choiceQuestion, index) in choiceQuestions" :choicequestion="choiceQuestion"
                    :order='order + index' :index="index" :key="choiceQuestionConst+choiceQuestion.id">
    </ChoiceQuestion>
    <el-button type="success" style="margin-top: 5px;" @click=newChoiceQuestion>新增选择题</el-button>
    <CompletionQuestion v-for="(completionQuestion, index) in this.completionQuestions"
                        :completionquestion="completionQuestion"
                        :order='order + choiceQuestions.length + index' :index="index"
                        :key="completionQuestionConst+completionQuestion.id">

    </CompletionQuestion>
    <el-button type="success" style="margin-top: 5px;" @click=newCompletionQuestion>新增填空题</el-button>
    <SubjectiveQuestion v-for="(subjectiveQuestion, index) in this.subjectiveQuestions"
                        :subjectivequestion="subjectiveQuestion"
                        :order='order + choiceQuestions.length + completionQuestions.length + index'
                        :index="index" :key="subjectiveQuestionConst+subjectiveQuestion.id">
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
            this.$http.post('Homework/' + this.homework.id + '/new_subjective_question/', {
                text_content: '请输入题目'
            }).then(response => {
                this.subjectiveQuestions.push(response.data);
            });
        },
        deleteChoiceQuestion(index) {
            this.choiceQuestions.splice(index, 1);
        },
        deleteCompletionQuestion(index) {
            this.completionQuestions.splice(index, 1);
        },
        deleteSubjectiveQuestion(index) {
            this.subjectiveQuestions.splice(index, 1);
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
