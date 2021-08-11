<template>
    <view>
        <movable-area class="video margin-left margin-top" @longpress="newComment">
            <video id="myVideo" class="video" @timeupdate="watchTime" @play="videoPlay" @pause="videoPause"
                   :src="student_answer.url"></video>
            <movable-view v-for="(comment, comment_index) in teacher_comments" v-if="comment.show" :x="comment.x"
                          :y="comment.y"
                          direction="all" class="comment round bg-red" @touchend="commentMove($event, comment_index)">
                <text class="text"></text>
                {{ comment_index + 1 }}
            </movable-view>
        </movable-area>
        <view class="voice-content margin">对答案进行评价：
            <view v-for="(comment, comment_index) in teacher_comments" class="flex margin-top">
                <view class="comment_class">{{ comment_index + 1 + '.' }}</view>
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
            voiceManager: '',
            videoContext: ''
        };
    },
    mounted() {
        this.student_answer = this.studentanswer;
        this.videoContext = uni.createVideoContext('myVideo', this);
    },
    methods: {
        // 新增评论
        newComment(e) {
            if (this.student_answer.isPaused) {
                if (this.teacher_comments.length < this.comment_limit) {
                    const comment = {
                        'currentTime': this.student_answer.currentTime,
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
        // 播放视频
        videoPlay() {
            this.student_answer.isPaused = false;
            for (const comment of this.teacher_comments) {
                comment.show = false;
            }
        },
        // 暂停视频
        videoPause() {
            this.student_answer.isPaused = true;
        },
        // 更新时间
        watchTime(e) {
            this.student_answer.currentTime = e.detail.currentTime;
            for (const comment of this.teacher_comments) {
                if (Math.abs(comment.currentTime - this.student_answer.currentTime) < 0.12) {
                    this.videoContext.pause();
                    comment.show = true;
                }
            }
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
                        'currentTime': comment.currentTime,
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
.video {
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

.comment_class {
    margin-top: 10rpx;
}
</style>
