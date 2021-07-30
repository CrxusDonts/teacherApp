<template>
  <div class="subjective-question">
    <p class="text-content">
      {{order}}.{{subjectiveQuestion.text_content}}
    </p>
    <el-button type="primary" icon="el-icon-edit" circle
               @click="editSubjectQuestionFormVisible = true"></el-button>
    <!--编辑主观题页面 -->
    <el-dialog title="编辑题目" :visible.sync="editSubjectQuestionFormVisible">
      <el-form>
        <el-form-item label="题目" :label-width="formLabelWidth">
          <el-input :value=subjectiveQuestion.text_content autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" icon="el-icon-picture-outline">添加图片</el-button>
        <el-button type="primary" icon="el-icon-video-camera">添加视频</el-button>
        <el-button @click="editSubjectQuestionFormVisible = false;" type="primary">确定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
    name: 'SubjectiveQuestion',
    props: ['subjectiveQuestion', 'order'],
    data() {
        return {
            editSubjectQuestionFormVisible: false,
            formLabelWidth: '140px'
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
</style>
