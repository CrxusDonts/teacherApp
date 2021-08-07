<template>
	<view class="cu-card case">
    <view class="cu-item shadow">
				<view class="cu-item">
					<view class="content flex-sub padding">
						<view class="text-lg margin-left">{{order + '.' + subjectiveQuestion.text_content}}</view>
					</view>
				</view>
				<view style="display: flex;">
					<view v-for="file in files">
						<image v-if="file.file_type === 0" class="margin-left margin-top image"
						:src="file.url" @click="previewImage(file.url)"></image>
						<video v-if="file.file_type === 1" class="margin-left margin-top video" :src="file.url"></video>
					</view>
				</view>
				<view class="flex margin-top margin-left">
					{{student_name}}的答案：
				</view>
		</view>
	</view>
</template>

<script>
export default {
    props: ['subjectiveQuestion', 'order', 'index', 'student_name'],
    name: 'SubjectiveQuestion',
    data() {
        return {
            files: []
        };
    },
    mounted() {
        uni.request({
            url: 'http://localhost:8002/teacherApp/SubjectiveQuestion/' + this.subjectiveQuestion.id + '/get_subjective_question_media/',
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
.image {
    width: 250upx;
    height: 250upx;
}

.video {
    width: 250upx;
    height: 250upx;
}
</style>
