<template>
  <div class="subjective-question">
    <p class="text-content">
      {{order}}.{{choiceQuestion.text_content}}
    </p>
    <p class="option" v-for="option in options" :key="option.id">{{option.order}}.{{option.answer}}</p>
    <el-button type="primary" icon="el-icon-edit" circle @click="newHomeworkFormVisible = true"></el-button>
    <!--表单提示框 -->
    <el-dialog title="编辑题目" :visible.sync="newHomeworkFormVisible">
      <el-form :model="form">
        <el-form-item label="题目" :label-width="formLabelWidth">
          <el-input :value=this.choiceQuestion.text_content autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item :model="form" v-for="(option, index) in options" :key="option.id">
          <el-form-item v-bind:label=optionConstant+(index+1) :label-width="formLabelWidth">
            <el-input v-model=option.answer autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="是否正确" :label-width="formLabelWidth">
            <el-radio-group>
              <el-radio label="是" :key="option.if_correct"></el-radio>
              <el-radio label="否"></el-radio>
            </el-radio-group>
          </el-form-item>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="form={};newHomeworkFormVisible = false;">取 消</el-button>
        <el-button type="primary">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
    name: 'ChoiceQuestion',
    props: ['choiceQuestion', 'order'],
    mounted: function() {
        this.form.name = this.choiceQuestion.text_content;
    },
    data() {
        return {
            options: [
                {
                    id: 1,
                    order: 'A',
                    answer: '兔子',
                    if_correct: true
                }, {
                    id: 2,
                    order: 'B',
                    answer: '狗',
                    if_correct: true
                }, {
                    id: 3,
                    order: 'C',
                    answer: '萝卜',
                    if_correct: false
                }
            ],
            newHomeworkFormVisible: false,
            formLabelWidth: '140px',
            optionConstant: '选项'
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

.option {
    font-size: 17px;
}

p + p {
    margin-top: -5px;
}
</style>
