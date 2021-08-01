<template>
  <div class="subjective-question">
    <p class="text-content">
      {{order}}.{{subjectiveQuestion.text_content}}
    </p>
    <el-image class="image" v-for="file in fileList" :key="file.url" :src="file.url" :preview-src-list="fileList">
    </el-image><br>
    <el-button type="primary" icon="el-icon-edit" circle
               @click="editSubjectQuestionFormVisible = true"></el-button>
    <el-button type="danger" icon="el-icon-delete" circle @click=deleteQuestion></el-button>
    <!--编辑主观题页面 -->
    <el-dialog title="编辑题目" :visible.sync="editSubjectQuestionFormVisible">
      <el-form>
        <el-form-item label="题目" :label-width="formLabelWidth">
          <el-input v-model=subjectiveQuestion.text_content autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <!--图片上传框-->
      <el-upload action="#" list-type="picture-card" :file-list="fileList"
                 :class = "{disabled:isMax}" :limit = 3 :on-change = "change"
                 :on-remove = "remove" :before-upload = "beforeAvatarUpload">
        <i class="el-icon-upload"></i>
        <div slot="tip" class="el-upload__tip">请上传多媒体</div>
      </el-upload>
      <div slot="footer" class="dialog-footer">
        <el-button @click="editSubjectQuestionFormVisible = false;" type="primary">确定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
    name: 'SubjectiveQuestion',
    props: ['subjectivequestion', 'order', 'index'],
    mounted() {
        this.subjectiveQuestion = this.subjectivequestion;
    },
    beforeDestroy() {
        this.$http.put('SubjectiveQuestion/' + this.subjectiveQuestion.id + '/', {
            text_content: this.subjectiveQuestion.text_content,
            homework: this.subjectiveQuestion.homework
        });
    },
    data() {
        return {
            fileList: [
                {
                    id: 2,
                    url: 'https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg'
                }
            ],
            editSubjectQuestionFormVisible: false,
            formLabelWidth: '140px',
            subjectiveQuestion: '',
            isMax: false
        };
    },
    methods: {
        deleteQuestion() {
            this.$http.delete('SubjectiveQuestion/' + this.subjectiveQuestion.id + '/');
            this.subjectiveQuestion = '';
            this.$parent.deleteSubjectiveQuestion(this.index);
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

p + p {
    margin-top: -5px;
}

.disabled {
    display: none;
}
</style>
