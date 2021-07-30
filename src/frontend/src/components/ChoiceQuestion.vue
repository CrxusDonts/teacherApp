<template>
  <div class="subjective-question">
    <p class="text-content">
      {{order}}.{{choiceQuestion.text_content}}
    </p>
    <p class="option" v-for="option in options" :key="option.id">
      <i v-if="option.if_correct" class="el-icon-check"></i>
      <i v-if="!option.if_correct" class="el-icon-close"></i>
      {{option.order}}.{{option.answer}}</p>
    <el-button type="primary" icon="el-icon-edit" circle @click="editChoiceQuestionFormVisible = true"></el-button>
    <!--编辑选择题页面 -->
    <el-dialog title="编辑题目" :visible.sync="editChoiceQuestionFormVisible">
      <el-form>
        <el-form-item label="题目" :label-width="formLabelWidth">
          <el-input :value=this.choiceQuestion.text_content autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item v-for="(option, index) in options" :key="option.id">
          <el-form-item :label=optionConstant+(index+1) :label-width="formLabelWidth">
            <el-input v-model=option.answer autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item>
            <el-radio-group class="radio-group" v-model="option.if_correct">
              <el-radio :label="true">正确</el-radio>
              <el-radio :label="false">错误</el-radio>
            </el-radio-group>
            <el-button class="delete-button" type="danger" icon="el-icon-delete" circle
                       @click="deleteOption(option)"></el-button>
          </el-form-item>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click=newOption>新增选项</el-button>
        <el-button type="primary" icon="el-icon-picture-outline">添加图片</el-button>
        <el-button type="primary" icon="el-icon-video-camera">添加视频</el-button>
        <el-button @click="editChoiceQuestionFormVisible = false;" type="primary">确定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
    name: 'ChoiceQuestion',
    props: ['choiceQuestion', 'order'],
    maxId: '',
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
            editChoiceQuestionFormVisible: false,
            formLabelWidth: '140px',
            optionConstant: '选项'
        };
    },
    methods: {
        deleteOption(option) {
            this.options.contains = function(obj) {
                let i = this.length;
                while (i--) {
                    if (this[i] === obj) {
                        return i;
                    }
                }
                return false;
            };
            this.options.splice(this.options.contains(option), 1);
        },
        newOption() {
            const option = {
                id: this.options[this.options.length - 1].id + 1,
                order: 'D',
                answer: '',
                if_correct: true
            };
            this.options.push(option);
        }
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

.radio-group {
    float: left;
    margin-top: 15px;
    margin-left: 145px;
}

.delete-button {
    float: right;
    margin-top: 5px;
}
</style>
