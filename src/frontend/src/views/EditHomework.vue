<template>
  <div>
    <Header v-bind:userName="userName"></Header>
    <el-header class="title">
      {{homeWork.title}}
      <el-button type="primary" class="go-back" @click=goBack>返回</el-button>
    </el-header>
    <ChoiceQuestion v-for="(choiceQuestion, index) in choiceQuestions" v-bind:choiceQuestion="choiceQuestion"
                    v-bind:order='order + index' :key="choiceQuestion.id">

    </ChoiceQuestion>
    <CompletionQuestion v-for="(completionQuestion, index) in this.completionQuestions"
                        v-bind:completionQuestion="completionQuestion"
                        v-bind:order='order + choiceQuestions.length + index' :key="completionQuestion.id">

    </CompletionQuestion>
    <SubjectiveQuestion v-for="(subjectiveQuestion, index) in this.subjectiveQuestions"
                        v-bind:subjectiveQuestion="subjectiveQuestion"
                        v-bind:order='order + choiceQuestions.length + completionQuestions.length + index'
                        :key="subjectiveQuestion.id">
    </SubjectiveQuestion>
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
            homeWork: {
                id: 1,
                title: '三年级二班第一次作业',
                start_time: '2021/07/27 16:17',
                due_time: '2021/08/03 16:17',
                repeatable: 1
            },
            choiceQuestions: [{
                id: 1,
                text_content: '请选出下列是动物的生物'
            },
            {
                id: 2,
                text_content: '请选出下列是植物的生物'
            }
            ],
            completionQuestions: [{
                id: 1,
                text_content: '床前明月光，__________'
            },
            {
                id: 2,
                text_content: '国破山河在，__________'
            }
            ],
            subjectiveQuestions: [{
                id: 1,
                text_content: '请如视频所示制作一个剪纸作品。'
            },
            {
                id: 2,
                text_content: '请画出图片中的主要内容。'
            }
            ]
        };
    },
    components: {
        Header,
        ChoiceQuestion,
        CompletionQuestion,
        SubjectiveQuestion
    },
    created: function() {
        this.homeWork = this.$route.query.homeWork;
    },
    methods: {
        goBack() {
            this.$router.push({ path: '/home' });
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
