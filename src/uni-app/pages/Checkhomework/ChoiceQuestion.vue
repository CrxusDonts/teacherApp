<template>
    <view class="cu-card case">
        <view class="cu-item shadow">
            <view class="cu-item">
                <view class="content flex-sub padding">
                    <view class="text-lg margin-left">{{ order + '.' + choiceQuestion.text_content }}</view>
                    <view class="grid">
                        <view v-for="(file, file_index) in files">
                            <image v-if="file.file_type === 0" class="margin-left margin-top image"
                                   :src="file.url" @click="previewImage(file.url)"></image>
                            <video v-if="file.file_type === 1" class="margin-left margin-top video"
                                   :src="file.url"></video>
                        </view>
                    </view>
                    <view class="flex margin-top margin-left" v-for="(option, index) in options">
                        <view v-if="option.if_correct" class="cuIcon-check"></view>
                        <view v-if="!option.if_correct" class="cuIcon-close"></view>
                        {{ String.fromCharCode("A".charCodeAt(0) - 1 + option.order) }}.{{ option.text_content }}
                    </view>
                    <view class="flex margin-top margin-left">
                        {{ student.name }}的答案：
                        <view v-for="(student_answer, index) in student_answers">
                            {{ String.fromCharCode("A".charCodeAt(0) - 1 + student_answer.answer_order) }}
                        </view>
                    </view>
                </view>
            </view>
        </view>
    </view>
</template>

<script>
export default {
    props: ['choiceQuestion', 'order', 'index', 'student'],
    name: 'ChoiceQuestion',
    data() {
        return {
            options: [],
            files: [],
            student_answers: []
        };
    },
    mounted() {
        uni.request({
            url: this.$BASICURL + 'ChoiceQuestion/' + this.choiceQuestion.id + '/get_options/',
            method: 'GET',
            success: res => {
                this.options = res.data;
            }
        });
        uni.request({
            url: this.$BASICURL + 'ChoiceQuestion/' + this.choiceQuestion.id + '/get_topic_media/',
            method: 'GET',
            success: res => {
                this.files = res.data;
                for (let i = 0; i < this.files.length; i++) {
                    this.files[i].url = this.$FILEBASICURL + this.files[i].url.substring(6);
                }
            }
        });
        uni.request({
            url: this.$BASICURL + 'ChoiceQuestionUserAnswer/get_user_answer/',
            data: {
                'question_id': this.choiceQuestion.id,
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
.image {
    width: 250 upx;
    height: 250 upx;
}

.video {
    width: 250 upx;
    height: 250 upx;
}
</style>
