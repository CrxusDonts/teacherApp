<template>
  <div class="subjective-question">
    <p class="text-content">
      {{order}}.{{completionQuestion.text_content}}
    </p>
    <el-image class="image" v-for="file in fileList" :key="file.url" :src="file.url" :preview-src-list="fileList">
    </el-image><br>
    <span>答案：</span><span class="answer" v-for="answer in answers" :key="answer.id">{{answer.answer}}</span><br>
    <el-button type="primary" icon="el-icon-edit" circle
               @click="editCompletionQuestionFormVisible = true" style="margin-top: 8px;"></el-button>
    <!--编辑填空题页面 -->
    <el-dialog title="编辑题目" :visible.sync="editCompletionQuestionFormVisible">
      <el-form>
        <el-form-item label="题目" :label-width="formLabelWidth">
          <el-input v-model=completionQuestion.text_content autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item v-for="(answer, index) in answers" :key="answer.id">
          <el-form-item :label=answerConstant+(index+1) :label-width="formLabelWidth">
            <el-input v-model=answer.answer autocomplete="off"></el-input>
            <el-button class="delete-button" type="danger" icon="el-icon-delete" circle
                       @click="deleteAnswer(answer)"></el-button>
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
        <el-button type="primary" @click=newAnswer>新增答案</el-button>
        <el-button @click="editCompletionQuestionFormVisible = false;" type="primary">确定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
    name: 'CompletionQuestion',
    props: ['completionquestion', 'order'],
    data() {
        return {
            answers: [],
            fileList: [
                {
                    id: 2,
                    url: 'https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg'
                }
            ],
            editCompletionQuestionFormVisible: false,
            formLabelWidth: '140px',
            answerConstant: '答案',
            completionQuestion: '',
            isMax: false
        };
    },
    mounted() {
        this.completionQuestion = this.completionquestion;
        this.$http.get('CompletionQuestion/' + this.completionQuestion.id + '/get_answers/')
            .then(response => {
                this.answers = response.data;
            });
    },
    beforeDestroy() {
        for (let i = 0; i < this.answers.length; i++) {
            this.$http.put('CompletionQuestionAnswer/' + this.answers[i].id + '/', {
                answer: this.answers[i].answer,
                question: this.answers[i].question
            });
        }
    },
    methods: {
        deleteAnswer(answer) {
            this.$http.delete('CompletionQuestionAnswer/' + answer.id + '/');
            this.answers.contains = function(obj) {
                let i = this.length;
                while (i--) {
                    if (this[i] === obj) {
                        return i;
                    }
                }
                return false;
            };
            this.answers.splice(this.answers.contains(answer), 1);
        },
        newAnswer() {
            this.$http.post('CompletionQuestion/' + this.completionQuestion.id + '/add_answer/', {
                answer: '请输入答案内容',
                order: this.answers.length > 0 ? this.answers[this.answers.length - 1].answer_order + 1 : 1
            }).then(response => {
                this.answers.push(response.data);
            });
        },
        change(file, fileList) {
            if (fileList.length >= 3) {
                this.isMax = true;
            }
        },
        remove(file, fileList) {
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

p + p {
    margin-top: -5px;
}

span {
    font-size: 15px;
}

.answer {
    margin-right: 15px;
}

.delete-button {
    float: right;
    margin-top: 5px;
}

.disabled {
    display: none;
}
</style>
