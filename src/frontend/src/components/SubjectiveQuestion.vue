<template>
  <div class="subjective-question">
    <p class="text-content">
      {{order}}.{{subjectiveQuestion.text_content}}
    </p>
    <el-button type="primary" icon="el-icon-edit" circle></el-button>
  </div>
</template>

<script>
export default {
    name: 'SubjectiveQuestion',
    props: ['subjectiveQuestion', 'order']
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
</style>
