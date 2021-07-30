<template>
  <div class="subjective-question">
    <p class="text-content">
      {{order}}.{{completionQuestion.text_content}}
    </p>
    <span>答案：</span><span class="answer" v-for="answer in answers" :key="answer.id">{{answer.answer}}</span><br>
    <el-button type="primary" icon="el-icon-edit" circle></el-button>
  </div>
</template>

<script>
export default {
    name: 'CompletionQuestion',
    props: ['completionQuestion', 'order'],
    data() {
        return {
            answers: [
                {
                    id: 1,
                    answer: '疑似地上霜'
                }, {
                    id: 2,
                    answer: '明月几时有'
                }, {
                    id: 3,
                    answer: '把酒问情况'
                }]
        };
    }
};
</script>

<style scoped>
.subjective-question {
    padding-bottom: 10px;
    margin-top: -20px;
    background-color: white;
}

.text-content {
    padding-top: 20px;
    font-size: 25px;
}

p + p {
    margin-top: -5px;
}

span {
    font-size: 15px;
}

.answer {
    margin-right: 15px;
}
</style>
