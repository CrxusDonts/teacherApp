<template>
    <view>
        <movable-area class="image margin-left margin-top">
            <image class="image" :src="student_answer.url" @click="previewImage(student_answer.url)"></image>
            <movable-view v-for="(comment, comment_index) in teacher_comments" :x="comment.pos_x" :y="comment.pos_y"
                          direction="all" class="comment round bg-red">
                <text class="text"></text>
                {{ comment_index + 1 }}
            </movable-view>
        </movable-area>
        <view class="voice-content margin">你的评价：
            <view v-for="(comment, comment_index) in teacher_comments" class="flex margin-top">
                <view>{{ comment_index + 1 + '.' }}</view>
                <text></text>
                {{ comment.text_content }}
                <button v-if="comment.url" class="cu-btn sm cuIcon-notification bg-green"
                        @click="voicePlay(comment)"></button>
            </view>
        </view>
    </view>
</template>

<script>
export default {
    props: ['studentanswer'],
    data() {
        return {
            student_answer: '',
            teacher_comments: [],
            comment_limit: 9,
            voiceManager: ''
        };
    },
    mounted() {
        this.student_answer = this.studentanswer;
        uni.request({
            url: this.$BASICURL + 'TeacherComment/get_teacher_comment/',
            data: {
                'media_id': this.student_answer.id
            },
            method: 'post',
            success: res => {
                this.teacher_comments = res.data;
                for (const comment of this.teacher_comments) {
                    if (comment.url) {
                        comment.url = this.$FILEBASICURL + comment.url.substring(6);
                    }
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
        },
        // 播放音频
        voicePlay(comment) {
            const innerAudioContext = uni.createInnerAudioContext();
            innerAudioContext.autoplay = true;
            innerAudioContext.src = comment.url;
            innerAudioContext.onPlay();
        }
    }
};
</script>

<style>
.image {
    width: 650upx;
    height: 500upx;
}

.comment {
    width: 30rpx;
    height: 30rpx;
}

.text {
    margin-left: 8rpx;
}
</style>
