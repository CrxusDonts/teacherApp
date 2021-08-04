<template>
  <div class="subjective-question">
    <p class="text-content">
        {{ order }}.{{ subjective_question.text_content }}
    </p>
    <el-image class="image" v-for="file in file_list" :key="file.url" :src="file.url" :preview-src-list="file_list">
    </el-image><br>
    <el-button type="primary" icon="el-icon-edit" circle
               @click="edit_subject_question_form_visible = true"></el-button>
    <el-button type="danger" icon="el-icon-delete" circle @click=deleteQuestion></el-button>
    <!--编辑主观题页面 -->
    <el-dialog title="编辑题目" :visible.sync="edit_subject_question_form_visible">
      <el-form>
        <el-form-item label="题目" :label-width="form_label_width">
          <el-input v-model=subjective_question.text_content autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <!--图片上传框-->
      <el-upload action="#" list-type="picture-card" :file-list="file_list"
                 :on-change = "change" :on-remove = "remove" :before-upload = "beforeAvatarUpload">
        <em class="el-icon-upload"></em>
        <div slot="tip" class="el-upload__tip">请上传多媒体</div>
      </el-upload>
      <div slot="footer" class="dialog-footer">
        <el-button @click="edit_subject_question_form_visible = false;" type="primary">确定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
    name: 'SubjectiveQuestion',
    props: ['subjectivequestion', 'order', 'index'],
    mounted() {
        this.subjective_question = this.subjectivequestion;
    },
    beforeDestroy() {
        this.$http.put('SubjectiveQuestion/' + this.subjective_question.id + '/', {
            text_content: this.subjective_question.text_content,
            homework: this.subjective_question.homework
        });
    },
    data() {
        return {
            file_limit: 3,
            file_list: [],
            edit_subject_question_form_visible: false,
            form_label_width: '140px',
            subjective_question: '',
            is_max: false
        };
    },
    methods: {
        deleteQuestion() {
            this.$http.delete('SubjectiveQuestion/' + this.subjective_question.id + '/');
            this.subjective_question = '';
            this.$parent.deleteSubjectiveQuestion(this.index);
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
                formData.append('subjective_question', this.subjective_question.id);
                this.$http.post('Media/', formData)
                    .then(response => {
                        if (response.status === 201) {
                            this.file_list.push(response.data);
                        } else {
                            alert('上传失败');
                        }
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
