<template>
  <div class="subjective-question">
    <p class="text-content">
      {{order}}.{{choiceQuestion.text_content}}
    </p>
    <el-image class="image" v-for="file in fileList" :key="file.url" :src="file.url" :preview-src-list="fileList">
    </el-image><br>
    <p class="option" v-for="option in options" :key="option.id">
      <i v-if="option.if_correct" class="el-icon-check"></i>
      <i v-if="!option.if_correct" class="el-icon-close"></i>
      {{option.order}}.{{option.answer}}</p>
    <el-button type="primary" icon="el-icon-edit" circle @click="editChoiceQuestionFormVisible = true"></el-button>
    <!--编辑选择题页面 -->
    <el-dialog title="编辑题目" :visible.sync="editChoiceQuestionFormVisible">
      <el-form>
        <!--题目输入框-->
        <el-form-item label="题目" :label-width="formLabelWidth">
          <el-input v-model=choiceQuestion.text_content autocomplete="off"></el-input>
        </el-form-item>
        <!--选项输入框-->
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
      <!--图片上传框-->
      <el-upload action="#" list-type="picture-card" :file-list="fileList"
                 :class = "{disabled:isMax}" :limit = 3 :on-change = "change"
                 :on-remove = "remove" :before-upload = "beforeAvatarUpload">
        <i class="el-icon-picture-outline"></i>
        <div slot="tip" class="el-upload__tip">请上传多媒体</div>
      </el-upload>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click=newOption>新增选项</el-button>
        <el-button @click="editChoiceQuestionFormVisible = false;" type="primary">确定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
    name: 'ChoiceQuestion',
    props: ['choicequestion', 'order'],
    maxId: '',
    mounted() {
        this.choiceQuestion = this.choicequestion;
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
            fileList: [
                {
                    id: 2,
                    url: 'https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg'
                }
            ],
            editChoiceQuestionFormVisible: false,
            formLabelWidth: '140px',
            optionConstant: '选项',
            choiceQuestion: '',
            isMax: false
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
                id: this.options.length > 0 ? this.options[this.options.length - 1].id + 1 : 1,
                order: 'D',
                answer: '请输入选项',
                if_correct: true
            };
            this.options.push(option);
        },
        change(file, fileList) {
            console.log('change');
            if (fileList.length >= 3) {
                this.isMax = true;
            }
        },
        remove(file, fileList) {
            console.log('remove');
            if (fileList.length < 3) {
                this.isMax = false;
            }
        },
        beforeAvatarUpload(file) {
            const isJPG = file.type === 'image/jpg' || file.type === 'image/png';
            const isLt2M = file.size / 1024 / 1024 < 2;
            if (!isJPG) {
                this.$message.error('上传头像图片只能是 JPG 格式!');
            }
            if (!isLt2M) {
                this.$message.error('上传头像图片大小不能超过 2MB!');
            }
            const formData = new FormData();
            formData.append('url', file);
            formData.append('file_type', 1);
            this.$http.post('Media/', formData)
                .then(response => {
                    if (response.status === 201) {
                        console.log(response.data);
                        this.fileList.push(response.data);
                        console.log(this.fileList);
                    } else {
                        alert('上传失败');
                    }
                });
        }
    }
};

</script>

<style scoped>
.image {
    height: 200px;
}

.image + .image {
    margin-left: 50px;
}

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

.disabled {
    display: none;
}
</style>
