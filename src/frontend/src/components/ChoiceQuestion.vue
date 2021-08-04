<template>
  <div class="choice-question">
    <p class="text-content">
      {{ order }}.{{ choice_question.text_content }}
    </p>
    <el-image class="image" v-for="file in file_list" :key="file.url" :src="file.url" :preview-src-list="file_list">
    </el-image><br>
    <p class="option" v-for="option in options" :key="option.id">
      <em v-if="option.if_correct" class="el-icon-check"></em>
      <em v-if="!option.if_correct" class="el-icon-close"></em>
      {{String.fromCharCode("A".charCodeAt(0) - 1 + option.order)}}.{{option.text_content}}</p>
    <el-button type="primary" icon="el-icon-edit" circle @click="edit_choice_question_form_visible = true"></el-button>
    <el-button type="danger" icon="el-icon-delete" circle @click=deleteQuestion></el-button>
    <!--编辑选择题页面-->
    <el-dialog title="编辑题目" :visible.sync="edit_choice_question_form_visible">
      <el-form>
        <!--题目输入框-->
        <el-form-item label="题目" :label-width="form_label_width">
          <el-input v-model=choice_question.text_content autocomplete="off"></el-input>
        </el-form-item>
        <!--选项输入框-->
        <el-form-item v-for="(option, index) in options" :key="option.id">
          <el-form-item :label=option_constant+(index+1) :label-width="form_label_width">
            <el-input v-model=option.text_content autocomplete="off"></el-input>
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
      <el-upload action="#" list-type="picture-card" :file-list="file_list"
                 :on-change = "change" :on-remove = "remove" :before-upload = "beforeAvatarUpload">
        <em class="el-icon-upload"></em>
        <div slot="tip" class="el-upload__tip">请上传多媒体</div>
      </el-upload>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click=newOption>新增选项</el-button>
        <el-button @click="save" type="primary">确定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
    name: 'ChoiceQuestion',
    props: ['choicequestion', 'order', 'index'],
    maxId: '',
    data() {
        return {
            options: [],
            file_limit: 3,
            file_list: [],
            edit_choice_question_form_visible: false,
            form_label_width: '140px',
            option_constant: '选项',
            choice_question: '',
            is_max: false
        };
    },
    mounted() {
        this.choice_question = this.choicequestion;
        this.$http.get('ChoiceQuestion/' + this.choice_question.id + '/get_options/')
            .then(response => {
                this.options = response.data;
            });
    },
    methods: {
        deleteQuestion() {
            this.$http.delete('ChoiceQuestion/' + this.choice_question.id + '/');
            this.choice_question = '';
            this.options = [];
            this.$parent.$parent.$parent.deleteChoiceQuestion(this.index);
        },
        deleteOption(option) {
            this.$http.delete('Options/' + option.id + '/');
            this.options.contains = function(obj) {
                let i = this.length;
                while (i--) {
                    if (this[i] === obj) {
                        return i;
                    }
                }
                return false;
            };
            let optionIndex = this.options.contains(option);
            this.options.splice(optionIndex, 1);
            for (; optionIndex < this.options.length; optionIndex++) {
                this.options[optionIndex].order--;
            }
        },
        newOption() {
            this.$http.post('ChoiceQuestion/' + this.choice_question.id + '/add_option/', {
                text_content: '请输入选项内容',
                order: this.options.length > 0 ? this.options[this.options.length - 1].order + 1 : 1,
                if_correct: 1,
                question: this.choice_question
            }).then(response => {
                this.options.push(response.data);
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
                formData.append('choice_question', this.choice_question.id);
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
            this.edit_choice_question_form_visible = false;
            if (this.choice_question !== '') {
                this.$http.put('ChoiceQuestion/' + this.choice_question.id + '/', {
                    text_content: this.choice_question.text_content,
                    homework: this.choice_question.homework
                });
            }
            for (let i = 0; i < this.options.length; i++) {
                this.$http.put('Options/' + this.options[i].id + '/', {
                    text_content: this.options[i].text_content,
                    order: this.options[i].order,
                    if_correct: this.options[i].if_correct,
                    question: this.options[i].question
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

.choice-question {
    padding-bottom: 10px;
    margin-top: -20px;
    border-radius: 10px;
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
