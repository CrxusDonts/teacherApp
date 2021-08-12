<template>
    <view class="cu-card case">
        <view class="cu-item shadow">
            <view class="cu-item">
                <view class="content flex-sub padding">
                    <view class="text-lg margin-left">{{ order + '.' + completionQuestion.text_content }}</view>
                    <view class="grid">
                        <view v-for="file in files">
                            <image v-if="file.file_type === 0" class="margin-left margin-top image"
                                   :src="file.url" @click="previewImage(file.url)"></image>
                            <video v-if="file.file_type === 1" class="margin-left margin-top video"
                                   :src="file.url"></video>
                        </view>
                    </view>
                    <view class="grid margin-top margin-left">
                        正确答案：
                        <view v-for="answer in answers" class="answer">
                            {{ answer.answer }}
                        </view>
                    </view>
                    <view class="grid margin-top margin-left">
                        {{ student.name }}的答案：
                        <view class="answer" v-for="student_answer in student_answers">
                            {{ student_answer.answer }}
                        </view>
                    </view>
                </view>
            </view>
        </view>
    </view>
</template>

<script>
export default {
    props: ['completionQuestion', 'order', 'index', 'student'],
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
            url: this.$BASICURL + 'CompletionQuestion/' + this.completionQuestion.id + '/get_answers/',
            method: 'GET',
            success: res => {
                this.answers = res.data;
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
        uni.request({
            url: this.$BASICURL + 'CompletionQuestionUserAnswer/get_user_answer/',
            data: {
                'question_id': this.completionQuestion.id,
                'student_id': this.student.id
            },
            method: 'POST',
            success: res => {
                this.student_answers = res.data;
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
