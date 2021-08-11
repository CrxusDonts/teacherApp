<template>
	<view>
		<movable-area class="video margin-left margin-top">
			<video id="myVideo" class="video" @timeupdate="watchTime" @play="videoPlay" :src="student_answer.url"></video>
			<movable-view v-for="(comment, comment_index) in teacher_comments" :v-if="comment.show" :x="comment.pos_x" :y="comment.pos_y"
			direction="all" class="comment round bg-red">
			<text style="margin-left: 8rpx;"></text>{{comment_index+1}}
			</movable-view>
		</movable-area>
		<view class="voice-content margin">老师的评价：
			<view v-for="(comment, comment_index) in teacher_comments" class="flex margin-top">
				<view>{{comment_index + 1 + '.'}}</view>
				<text></text>{{comment.text_content}}
				<button class="cu-btn sm cuIcon-notification bg-green" @click="voicePlay(comment)"></button>
			</view>
		</view>
	</view>
</template>

<script>
export default {
    props: ['studentanswer'],
    data() {
        return {
            file: '',
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
        uni.request({
            url: this.$BASICURL + 'TeacherComment/get_teacher_comment/',
            data: {
                'media_id': this.student_answer.id
            },
            method: 'post',
            success: res => {
                this.teacher_comments = res.data;
                for (const comment of this.teacher_comments) {
                    comment.url = this.$FILEBASICURL + comment.url.substring(6);
                    comment.show = false;
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
        // 播放视频
        videoPlay() {
            for (const comment of this.teacher_comments) {
                comment.show = false;
            }
        },
        // 播放音频
        voicePlay(comment) {
            const innerAudioContext = uni.createInnerAudioContext();
            innerAudioContext.autoplay = true;
            innerAudioContext.src = comment.url;
            innerAudioContext.onPlay();
        },
        // 更新时间
        watchTime(e) {
            for (const comment of this.teacher_comments) {
                if (Math.abs(comment.time_slot - e.detail.currentTime) < 0.12) {
                    this.videoContext.pause();
                    comment.show = true;
                }
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
</style>
