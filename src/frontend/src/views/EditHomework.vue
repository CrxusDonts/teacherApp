<template>
  <div>
    <Header v-bind:userName="user_name"></Header>
    <el-header class="title">
      {{ homework.title }}
      <el-button type="primary" class="go-back" @click=goBack>返回</el-button>
    </el-header>
    <ChoiceQuestion v-for="(choiceQuestion, index) in choice_questions" :choicequestion="choiceQuestion"
                    :order='order + index' :index="index" :key="choice_questionConst+choiceQuestion.id">
    </ChoiceQuestion>
    <el-button type="success" style="margin-top: 5px;" @click=newChoiceQuestion>新增选择题</el-button>
    <CompletionQuestion v-for="(completionQuestion, index) in this.completion_questions"
                        :completionquestion="completionQuestion"
                        :order='order + choice_questions.length + index' :index="index"
                        :key="completion_questionConst+completionQuestion.id">

    </CompletionQuestion>
    <el-button type="success" style="margin-top: 5px;" @click=newCompletionQuestion>新增填空题</el-button>
    <SubjectiveQuestion v-for="(subjectiveQuestion, index) in this.subjective_questions"
                        :subjectivequestion="subjectiveQuestion"
                        :order='order + choice_questions.length + completion_questions.length + index'
                        :index="index" :key="subjective_questionConst+subjectiveQuestion.id">
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
            user_name: 'admin',
            homework: '',
            choice_questionConst: 'choiceQuestion',
            completion_questionConst: 'completionQuestion',
            subjective_questionConst: 'subjectiveQuestion',
            choice_questions: [],
            completion_questions: [],
            subjective_questions: []
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
        this.user_name = this.$route.query.user_name;
        this.$http.get('Homework/' + this.homework.id + '/get_choice_question/')
            .then(response => {
                this.choice_questions = response.data;
            });
        this.$http.get('Homework/' + this.homework.id + '/get_completion_question/')
            .then(response => {
                this.completion_questions = response.data;
            });
        this.$http.get('Homework/' + this.homework.id + '/get_subjective_question/')
            .then(response => {
                this.subjective_questions = response.data;
            });
    },
    methods: {
        goBack() {
            this.$router.push({ path: '/home/' + this.user_name });
        },
        newChoiceQuestion() {
            this.$http.post('Homework/' + this.homework.id + '/new_choice_question/', {
                text_content: '请输入题目'
            }).then(response => {
                this.choice_questions.push(response.data);
            });
        },
        newCompletionQuestion() {
            this.$http.post('Homework/' + this.homework.id + '/new_completion_question/', {
                text_content: '请输入题目'
            }).then(response => {
                this.completion_questions.push(response.data);
            });
        },
        newSubjectiveQuestion() {
            this.$http.post('Homework/' + this.homework.id + '/new_subjective_question/', {
                text_content: '请输入题目'
            }).then(response => {
                this.subjective_questions.push(response.data);
            });
        },
        deleteChoiceQuestion(index) {
            this.choice_questions.splice(index, 1);
        },
        deleteCompletionQuestion(index) {
            this.completion_questions.splice(index, 1);
        },
        deleteSubjectiveQuestion(index) {
            this.subjective_questions.splice(index, 1);
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
