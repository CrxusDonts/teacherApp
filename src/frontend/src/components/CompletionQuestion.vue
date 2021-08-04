<template>
  <div class="completion-question">
    <p class="text-content">
        {{ order }}.{{ completion_question.text_content }}
    </p>
    <el-image class="image" v-for="file in file_list" :key="file.url" :src="file.url" :preview-src-list="file_list">
    </el-image><br>
    <span>答案：</span><span class="answer" v-for="answer in answers" :key="answer.id">{{answer.answer}}</span><br>
    <el-button type="primary" icon="el-icon-edit" circle
               @click="edit_completion_question_form_visible = true" style="margin-top: 8px;"></el-button>
    <el-button type="danger" icon="el-icon-delete" circle @click=deleteQuestion></el-button>
    <!--编辑填空题页面 -->
    <el-dialog title="编辑题目" :visible.sync="edit_completion_question_form_visible">
      <el-form>
        <el-form-item label="题目" :label-width="form_label_width">
          <el-input v-model=completion_question.text_content autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item v-for="(answer, index) in answers" :key="answer.id">
          <el-form-item :label=answer_constant+(index+1) :label-width="form_label_width">
            <el-input v-model=answer.answer autocomplete="off"></el-input>
            <el-button class="delete-button" type="danger" icon="el-icon-delete" circle
                       @click="deleteAnswer(answer)"></el-button>
          </el-form-item>
        </el-form-item>
      </el-form>
      <!--图片上传框-->
      <el-upload action="#" list-type="picture-card" :file-list="file_list"
                 :on-change = "change" :on-remove = "remove" :before-upload = "beforeAvatarUpload">
        <em class="el-icon-upload"></em>
        <div slot="tip" class="el-upload__tip">请上传多媒体</div>
      </el-upload>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click=newAnswer>新增答案</el-button>
        <el-button @click="save" type="primary">确定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
    name: 'CompletionQuestion',
    props: ['completionquestion', 'order', 'index'],
    data() {
        return {
            answers: [],
            file_limit: 3,
            file_list: [],
            edit_completion_question_form_visible: false,
            form_label_width: '140px',
            answer_constant: '答案',
            completion_question: '',
            is_max: false
        };
    },
    mounted() {
        this.completion_question = this.completionquestion;
        this.$http.get('CompletionQuestion/' + this.completion_question.id + '/get_answers/')
            .then(response => {
                this.answers = response.data;
            });
    },
    methods: {
        deleteQuestion() {
            this.$http.delete('CompletionQuestion/' + this.completion_question.id + '/');
            this.completion_question = '';
            this.answers = [];
            this.$parent.$parent.$parent.deleteCompletionQuestion(this.index);
        },
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
            this.$http.post('CompletionQuestion/' + this.completion_question.id + '/add_answer/', {
                answer: '请输入答案内容',
                order: this.answers.length > 0 ? this.answers[this.answers.length - 1].answer_order + 1 : 1
            }).then(response => {
                this.answers.push(response.data);
            });
        },
        change(file, fileList) {
            if (fileList.length > this.file_limit) {
                this.is_max = true;
            }
        },
        remove(file, fileList) {
            this.$http.delete('Media/' + file.id + '/');
            this.file_list = fileList;
            if (fileList.length < this.file_limit) {
                this.is_max = false;
            }
        },
        beforeAvatarUpload(file) {
            if (this.is_max) {
                this.$message.error('最多上传3个文件');
            } else {
                const isImage = file.type === 'image/jpeg' || file.type === 'image/png';
                const isVideo = file.type === 'video/mp4';
                if (!isImage && !isVideo) {
                    this.$message.error('只能上传图片或视频');
                    return;
                }
                const formData = new FormData();
                formData.append('url', file);
                if (isImage) {
                    formData.append('file_type', 0);
                } else if (isVideo) {
                    formData.append('file_type', 1);
                }
                formData.append('completion_question', this.completion_question.id);
                this.$http.post('Media/', formData)
                    .then(response => {
                        if (response.status === 201) {
                            this.file_list.push(response.data);
                        } else {
                            alert('上传失败');
                        }
                    });
            }
        },
        save() {
            this.edit_completion_question_form_visible = false;
            this.$http.put('CompletionQuestion/' + this.completion_question.id + '/', {
                text_content: this.completion_question.text_content,
                homework: this.completion_question.homework
            });
            for (let i = 0; i < this.answers.length; i++) {
                this.$http.put('CompletionQuestionAnswer/' + this.answers[i].id + '/', {
                    answer: this.answers[i].answer,
                    question: this.answers[i].question
                });
            }
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

.completion-question {
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
</style>
