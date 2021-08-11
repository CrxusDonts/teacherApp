<template>
    <view>
        <movable-area class="image margin-left margin-top" @longpress="newComment">
            <image class="image" :src="student_answer.url" @click="previewImage(student_answer.url)"></image>
            <movable-view v-for="(comment, comment_index) in teacher_comments" :x="comment.x" :y="comment.y"
                          direction="all" class="comment round bg-red" @touchend="commentMove($event, comment_index)">
                <text style="margin-left: 8rpx;"></text>
                {{ comment_index + 1 }}
            </movable-view>
        </movable-area>
        <view class="voice-content margin">对答案进行评价：
            <view v-for="(comment, comment_index) in teacher_comments" class="flex margin-top">
                <view style="margin-top: 10rpx;">{{ comment_index + 1 + '.' }}</view>
                <input class="solid" @input="getInput($event, comment_index)" :value="comment.comment"/>
                <button class="cu-btn cuIcon-voice margin-left bg-green" @touchstart="record(comment_index)"
                        @touchend="recordEnd()"></button>
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
    },
    methods: {
        // 新增评论
        newComment(e) {
            if (this.teacher_comments.length < this.comment_limit) {
                const comment = {
                    'comment': '',
                    'x': e.detail.x - e.currentTarget.offsetLeft - 6,
                    'y': e.detail.y - e.currentTarget.offsetTop - 6,
                    'component_x': e.currentTarget.offsetLeft,
                    'component_y': e.currentTarget.offsetTop,
                    'voice': '',
                    'show': true
                };
                this.teacher_comments.push(comment);
            } else {
                uni.showToast({
                    title: '评论已达上限',
                    icon: 'none'
                });
            }
        },
        // 移动气泡评论
        commentMove(e, comment_index) {
            this.teacher_comments[comment_index].x = e.changedTouches[0].pageX - this.teacher_comments[comment_index].component_x - 6;
            this.teacher_comments[comment_index].y = e.changedTouches[0].pageY - this.teacher_comments[comment_index].component_y - 6;
        },
        // 初始化语音输入助手
        voiceManagerInit(comment_index) {
            var plugin = requirePlugin('WechatSI');
            this.voiceManager = plugin.getRecordRecognitionManager();
            this.voiceManager.onRecognize = res => {
                this.teacher_comments[comment_index].comment = res.result;
            };
            this.voiceManager.onStop = res => {
                this.teacher_comments[comment_index].comment = res.result;
                this.teacher_comments[comment_index].voice = res.tempFilePath;
            };
            this.voiceManager.onError = res => {
                console.error('error msg', res.msg);
            };
        },
        // 开始录音
        record(comment_index) {
            this.voiceManagerInit(comment_index);
            this.voiceManager.start({
                lang: 'zh_CN'
            });
            uni.vibrateShort();
        },
        // 结束录音
        recordEnd() {
            this.voiceManager.stop();
            uni.vibrateShort();
        },
        // 预览图片
        previewImage(url) {
            uni.previewImage({
                current: 0,
                urls: [url]
            });
        },
        // 实时获得评论
        getInput(e, comment_index) {
            const _this = this;
            _this.teacher_comments[comment_index].comment = e.target.value;
        },
        // 提交评论
        comment() {
            for (const comment of this.teacher_comments) {
                uni.request({
                    url: this.$BASICURL + 'TeacherComment/add_teacher_comment/',
                    data: {
                        'pos_x': comment.x,
                        'pos_y': comment.y,
                        'content': comment.comment,
                        'currentTime': 0,
                        'media_id': this.student_answer.id
                    },
                    method: 'POST',
                    success: res => {
                        uni.uploadFile({
                            url: this.$BASICURL + 'TeacherComment/add_comment_voice/',
                            filePath: comment.voice,
                            formData: {
                                'comment_id': res.data.id
                            },
                            name: 'voice'
                        });
                    }
                });
            }
        }
    }
};
</script>

<style>
.image {
    width: 650 upx;
    height: 500 upx;
}

.comment {
    width: 30 rpx;
    height: 30 rpx;
}
</style>
