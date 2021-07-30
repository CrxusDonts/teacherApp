<template>
  <div class="subjective-question">
    <p class="text-content">
      {{order}}.{{completionQuestion.text_content}}
    </p>
    <span>答案：</span><span class="answer" v-for="answer in answers" :key="answer.id">{{answer.answer}}</span><br>
    <el-button type="primary" icon="el-icon-edit" circle
               @click="editCompletionQuestionFormVisible = true" style="margin-top: 8px;"></el-button>
    <!--编辑填空题页面 -->
    <el-dialog title="编辑题目" :visible.sync="editCompletionQuestionFormVisible">
      <el-form>
        <el-form-item label="题目" :label-width="formLabelWidth">
          <el-input :value=this.completionQuestion.text_content autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item v-for="(answer, index) in answers" :key="answer.id">
          <el-form-item :label=answerConstant+(index+1) :label-width="formLabelWidth">
            <el-input v-model=answer.answer autocomplete="off"></el-input>
          </el-form-item>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" icon="el-icon-picture-outline">添加图片</el-button>
        <el-button type="primary" icon="el-icon-video-camera">添加视频</el-button>
        <el-button @click="editCompletionQuestionFormVisible = false;" type="primary">确定</el-button>
      </div>
    </el-dialog>
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
                    answer: '把酒问青天'
                }],
            editCompletionQuestionFormVisible: false,
            formLabelWidth: '140px',
            answerConstant: '答案'
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
