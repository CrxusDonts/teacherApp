<template>
  <div class="subjective-question">
    <p class="text-content">
        {{ order }}.{{ subjective_question.text_content }}
    </p>
    <div v-for="file in files" :key="file.url">
      <el-image v-if="file.file_type === 0" class="image" :src="file.url" :preview-src-list="[file.url]">
      </el-image>
      <video-player v-if="file.file_type === 1" class="video-player vjs-custom-skin video"
                    ref="videoPlayer" :playsinline="true" :options="playerOptions">
      </video-player>
    </div><br>
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
      <el-upload action="#" list-type="picture-card" :file-list="files"
                 :on-change = "change" :on-remove = "remove" :before-upload = "beforeMediaUpload">
        <em class="el-icon-upload"></em>
        <div slot="tip" class="el-upload__tip">请上传多媒体</div>
      </el-upload>
      <div slot="footer" class="dialog-footer">
        <el-button @click="save" type="primary">确定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
    name: 'SubjectiveQuestion',
    props: ['subjectivequestion', 'order', 'index'],
    data() {
        return {
            playerOptions: {
                autoplay: false,
                muted: false,
                loop: false,
                preload: 'auto',
                language: 'zh-CN',
                aspectRatio: '16:9',
                fluid: true,
                sources: [],
                notSupportedMessage: '此视频暂无法播放，请稍后再试',
                controlBar: {
                    timeDivider: true,
                    durationDisplay: true,
                    remainingTimeDisplay: false,
                    fullscreenToggle: true
                }
            },
            file_limit: 3,
            files: [],
            edit_subject_question_form_visible: false,
            form_label_width: '140px',
            subjective_question: '',
            is_max: false
        };
    },
    mounted() {
        this.subjective_question = this.subjectivequestion;
        this.$http.get('SubjectiveQuestion/' + this.subjective_question.id + '/get_subjective_question_media/')
            .then(response => {
                this.files = response.data;
            }).then(() => {
                for (const file of this.files) {
                    file.url = 'http://localhost:8002/' + file.url.substring(6);
                    if (file.file_type === 1) {
                        this.playerOptions.sources.push(file.url);
                    }
                }
            });
    },
    methods: {
        deleteQuestion() {
            this.$http.delete('SubjectiveQuestion/' + this.subjective_question.id + '/');
            this.subjective_question = '';
            this.$parent.$parent.$parent.deleteSubjectiveQuestion(this.index);
        },
        change(file, fileList) {
            if (fileList.length > this.file_limit) {
                this.is_max = true;
            }
        },
        remove(file, fileList) {
            this.$http.delete('Media/' + file.id + '/');
            this.files = fileList;
            if (fileList.length < this.file_limit) {
                this.is_max = false;
            }
        },
        beforeMediaUpload(file) {
            if (this.is_max) {
                this.$message.error('最多上传3个文件');
            } else {
                const isImage = file.type === 'image/jpeg' || file.type === 'image/png';
                const isVideo = file.type === 'video/mp4';
                if (!isImage && !isVideo) {
                    this.$message.error('只能上传图片或视频');
                    return;
                }
                if (isVideo && this.playerOptions.sources.length === 1) {
                    this.$message.error('只能上传一个视频');
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
                            this.files.push(response.data);
                            this.files[this.files.length - 1].url = 'http://localhost:8002/' +
                              this.files[this.files.length - 1].url.substring(46);
                            if (this.files[this.files.length - 1].file_type === 1) {
                                this.playerOptions.sources.push(this.files[this.files.length - 1].url);
                            }
                        } else {
                            alert('上传失败');
                        }
                    });
            }
        },
        save() {
            this.edit_subject_question_form_visible = false;
            this.$http.put('SubjectiveQuestion/' + this.subjective_question.id + '/', {
                text_content: this.subjective_question.text_content,
                homework: this.subjective_question.homework
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

.video {
    position: relative;
    display: inline-block;
    width: 600px;
    height: 338px;
    margin-right: 4px;
    border: 1px solid transparent;
    border-radius: 4px;
    overflow: hidden;
    line-height: 100px;
    text-align: center;
    background: #fff;
    box-shadow: 0 1px 1px rgba(0, 0, 0, .2);
}
</style>
