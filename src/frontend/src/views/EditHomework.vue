<template>
    <el-container>
        <el-header class="head">
        <Header v-bind:user_name="user_name"></Header>
        <el-card class="title">
            {{ homework }}
            <el-button type="primary" class="go-back" @click=goBack>返回</el-button>
        </el-card>
        </el-header>
        <el-main class="body">
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
        </el-main>
    </el-container>
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
            homework_id: '',
            class_id: '',
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
        this.homework_id = this.$route.params.homework_id;
        this.user_name = this.$route.query.user_name;
        this.class_id = this.$route.query.class_id;
        // 根据id得到homework对象
        this.$http.get('Homework/' + this.homework_id + '/')
            .then(response => {
                this.homework = response.data.title;
            });
        this.$http.get('Homework/' + this.homework_id + '/get_choice_question/')
            .then(response => {
                this.choice_questions = response.data;
            });
        this.$http.get('Homework/' + this.homework_id + '/get_completion_question/')
            .then(response => {
                this.completion_questions = response.data;
            });
        this.$http.get('Homework/' + this.homework_id + '/get_subjective_question/')
            .then(response => {
                this.subjective_questions = response.data;
            });
    },
    methods: {
        goBack() {
            this.$router.push({
                path: '/home/' + this.user_name + '/homeworkManagement',
                query: { class_id: this.class_id }
            });
        },
        newChoiceQuestion() {
            this.$http.post('Homework/' + this.homework_id + '/new_choice_question/', {
                text_content: '请输入题目'
            }).then(response => {
                this.choice_questions.push(response.data);
            });
        },
        newCompletionQuestion() {
            this.$http.post('Homework/' + this.homework_id + '/new_completion_question/', {
                text_content: '请输入题目'
            }).then(response => {
                this.completion_questions.push(response.data);
            });
        },
        newSubjectiveQuestion() {
            this.$http.post('Homework/' + this.homework_id + '/new_subjective_question/', {
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
.head {
    position: fixed;
    z-index: 10;
    width: 100%;
    height: 120px;
    padding: 0;
    margin: 0;
}

.title {
    width: 100%;
    height: 60px;
    padding-top: 5px;
    margin-top: 0;
    font-size: 30px;
    text-align: center;
    background-color: #f9f0fb;
}

.go-back {
    float: right;
}

.body {
    align-self: center;
    width: 80%;
    margin-top: 125px;
}
</style>
