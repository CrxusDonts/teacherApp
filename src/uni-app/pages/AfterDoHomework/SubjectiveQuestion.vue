<template>
	<view class="cu-card case">
		<view class="cu-item shadow">
			<view class="cu-item">
				<view class="content flex-sub padding">
					<view class="text-lg margin-left">{{order + '.' + subjectiveQuestion.text_content}}</view>
				</view>
			</view>
			<view class="grid">
				<view v-for="file in files">
					<image v-if="file.file_type === 0" class="margin-left margin-top image"
					:src="file.url" @click="previewImage(file.url)"></image>
					<video v-if="file.file_type === 1" class="margin-left margin-top video" :src="file.url"></video>
				</view>
			</view>
			<view class="margin-top margin-left">
				你的答案：
			</view>
			<view class="grid">
				<view v-for="student_answer in student_answers">
					<comment-image v-if="student_answer.file_type === 0" :studentanswer='student_answer' ref="commentImage"></comment-image>
					<comment-video v-if="student_answer.file_type === 1" :studentanswer='student_answer' ref="commentVideo"></comment-video>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
import CommentImage from './CommentImage.vue';
import CommentVideo from './CommentVideo.vue';
export default {
    props: ['subjectiveQuestion', 'order', 'index', 'student'],
    name: 'SubjectiveQuestion',
    data() {
        return {
            files: [],
            student_answers: []
        };
    },
    components: {
        CommentImage,
        CommentVideo
    },
    mounted() {
        uni.request({
            url: this.$BASICURL + 'SubjectiveQuestion/' + this.subjectiveQuestion.id + '/get_subjective_question_media/',
            method: 'GET',
            success: res => {
                this.files = res.data;
                for (let i = 0; i < this.files.length; i++) {
                    this.files[i].url = this.$FILEBASICURL + this.files[i].url.substring(6);
                }
            }
        });
        uni.request({
            url: this.$BASICURL + 'SubjectiveQuestionUserAnswer/get_user_answer/',
            data: {
                'question_id': this.subjectiveQuestion.id,
                'student_id': this.student.id
            },
            method: 'POST',
            success: res => {
                this.student_answers = res.data;
                for (let i = 0; i < this.student_answers.length; i++) {
                    this.student_answers[i].url = this.$FILEBASICURL + this.student_answers[i].url.substring(6);
                    this.student_answers[i].currentTime = 0;
                    this.student_answers[i].isPaused = true;
                }
            }
        });
    },
    methods: {
        // 提交评论
        comment() {
            for (const commentImage of this.$refs.commentImage) {
                commentImage.comment();
            }
            for (const commentVideo of this.$refs.commentVideo) {
                commentVideo.comment();
            }
        }
    }
};
</script>

<style>
.image {
    width: 250upx;
    height: 250upx;
}

.video {
    width: 250upx;
    height: 250upx;
}
</style>
