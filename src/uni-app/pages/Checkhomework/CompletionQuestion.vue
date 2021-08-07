<template>
	<view class="cu-card case">
		<view class="cu-item shadow">
				<view class="cu-item">
					<view class="content flex-sub padding">
						<view class="text-lg margin-left">{{order + '.' + completionQuestion.text_content}}</view>
						<view style="display: flex;">
							<view v-for="file in files">
								<image v-if="file.file_type === 0" class="margin-left margin-top image"
								:src="file.url" @click="previewImage(file.url)"></image>
								<video v-if="file.file_type === 1" class="margin-left margin-top video" :src="file.url"></video>
							</view>
						</view>
						<view class="flex margin-top margin-left">
							正确答案：
							<view v-for="answer in answers" class="answer">
							{{answer.answer}}
							</view>
						</view>
						<view class="flex margin-top margin-left">
							{{student_name}}的答案：
							<view v-for="student_answer in student_answers">
							{{student_answer.answer}}
							</view>
						</view>
					</view>
				</view>
		</view>
	</view>
</template>

<script>
export default {
    props: ['completionQuestion', 'order', 'index', 'student_name'],
    name: 'CompletionQuestion',
    data() {
        return {
            answers: [],
            files: [],
            student_answers: []
        };
    },
    mounted() {
        uni.request({
            url: 'http://localhost:8002/teacherApp/CompletionQuestion/' + this.completionQuestion.id + '/get_answers/',
            method: 'GET',
            success: res => {
                this.answers = res.data;
            }
        });
        uni.request({
            url: 'http://localhost:8002/teacherApp/CompletionQuestion/' + this.completionQuestion.id + '/get_completion_media/',
            method: 'GET',
            success: res => {
                this.files = res.data;
                for (let i = 0; i < this.files.length; i++) {
                    this.files[i].url = 'http://localhost:8002/' + this.files[i].url.substring(6);
                }
            }
        });
    },
    methods: {
        // 预览图片
        previewImage(url) {
            uni.previewImage({
                current: 0,
                urls: [url]
            });
        }
    }
};
</script>

<style>
.answer + .answer {
    margin-left: 50rpx;
}

.image {
    width: 250upx;
    height: 250upx;
}

.video {
    width: 250upx;
    height: 250upx;
}
</style>
