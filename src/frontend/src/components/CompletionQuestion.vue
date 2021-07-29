<template>
  <div class="subjective-question">
    <p class="text-content">
      {{order}}.{{completionQuestion.text_content}}
    </p>
    <span>答案：</span><span class="answer" v-for="(answer, index) in answers">{{answer}}</span><br>
    <el-button type="primary" icon="el-icon-edit" circle></el-button>
  </div>
</template>

<script>
export default {
  name: "CompletionQuestion",
  props: ['completionQuestion', 'order'],
  data() {
    return {
      answers: ['疑似地上霜', '举头望明月', '低头思故乡', '好诗，好诗啊！']
    }
  },
}
</script>

<style scoped>
.subjective-question {
  padding-bottom: 10px;
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
