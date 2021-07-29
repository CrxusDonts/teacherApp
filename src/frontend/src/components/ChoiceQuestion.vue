<template>
  <div class="subjective-question">
    <p class="text-content">
      {{order}}.{{choiceQuestion.text_content}}
    </p>
    <p class="option" v-for="(option, order) in options">{{option.order}}.{{option.answer}}</p>
    <el-button type="primary" icon="el-icon-edit" circle></el-button>
  </div>
</template>

<script>
export default {
  name: "ChoiceQuestion",
  props: ['choiceQuestion', 'order'],
  data() {
    return {
      options: [
          {
            order: 'A',
            answer: '兔子'
          }, {
          order: 'B',
          answer: '狗'
        },{
          order: 'C',
          answer: '萝卜'
        },
      ]
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
.option {
  font-size: 17px;
}
p + p {
  margin-top: -5px;
}
</style>
