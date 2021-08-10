<template>
	<view class="cu-card case">
		<view class="cu-item shadow">
			<view class="cu-item">
				<view class="content flex-sub padding">
					<view class="text-lg margin-left">{{order + '.' + completionQuestion.text_content}}</view>
				</view>
				<view class="grid">
					<view v-for="file in files">
						<image v-if="file.file_type === 0" class="margin-left margin-top image"
						:src="file.url" @click="previewImage(file.url)"></image>
						<video v-if="file.file_type === 1" class="margin-left margin-top video" :src="file.url"></video>
					</view>
				</view>
			</view>
			<view v-for="(student_answer, index) in student_answers" class="cu-form-group margin-left">
				<view class="title">{{student_answer.order}}.</view>
				<input class="solid" placeholder="请输入答案" name="input"
				:value="student_answer.answer" @input="inputAnswer($event,index)"></input>
			</view>
		</view>
	</view>
</template>

<script>
export default {
    props: ['completionQuestion', 'order', 'index'],
    name: 'CompletionQuestion',
    data() {
        return {
            student_answers: [],
            files: []
        };
    },
    mounted() {
        uni.request({
            url: this.$BASICURL + 'CompletionQuestion/' + this.completionQuestion.id + '/get_answers/',
            method: 'GET',
            success: res => {
                this.student_answers = res.data;
                for (let i = 0; i < res.data.length; i++) {
                    this.student_answers[i].order = i + 1;
                    this.student_answers[i].answer = '';
                }
            }
        });
        uni.request({
            url: this.$BASICURL + 'CompletionQuestion/' + this.completionQuestion.id + '/get_completion_media/',
            method: 'GET',
            success: res => {
                this.files = res.data;
                for (const file of this.files) {
                    file.url = this.$FILEBASICURL + file.url.substring(6);
                }
            }
        });
    },
    methods: {
        inputAnswer(e, index) {
            this.student_answers[index].answer = e.target.value;
        },
        // 预览图片
        previewImage(url) {
            uni.previewImage({
                current: 0,
                urls: [url]
            });
        },
        submitCompletionQuestion(student_id) {
            let answer = '';
            for (const student_answer of this.student_answers) {
                answer += student_answer.answer;
                answer += ' ';
            }
            uni.request({
                url: this.$BASICURL + 'CompletionQuestionUserAnswer/add_user_answer/',
                data: {
                    'answers': answer,
                    'question_id': this.completionQuestion.id,
                    'student_id': student_id
                },
                method: 'POST'
            });
        },
        isEmpty() {
            for (const student_answer of this.student_answers) {
                if (student_answer.answer == '') {
                    return true;
                }
            }
            return false;
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
