<template>
    <view class="cu-card case">
        <!--题目 -->
        <view class="cu-item shadow">
            <view class="cu-item">
                <view class="content flex-sub padding">
                    <view class="text-lg margin-left">{{ order + '.' + subjectiveQuestion.text_content }}</view>
                </view>
            </view>
            <view class="grid">
                <view v-for="file in files">
                    <image v-if="file.file_type === 0" class="margin-left margin-top image"
                           :src="file.url" @click="previewImage(file.url)"></image>
                    <video v-if="file.file_type === 1" class="margin-left margin-top video" :src="file.url"></video>
                </view>
            </view>
            <!-- 学生答案 -->
            <view class="flex margin-top margin-left">
                你的答案：
            </view>
            <view class="grid">
                <view class="margin-left margin-top" v-for="(image,index) in images">
                    <image class="image" :src="image" :data-src="image" @click="previewImage(image)"></image>
                    <button class="cuIcon-close bg-red close-button" @click="delect(index)">
                    </button>
                </view>
                <view class="margin-left margin-top" v-for="(video, index) in videos">
                    <video class="video" :src="video"></video>
                    <button class="cuIcon-close bg-red close-button" @click="delectVideo(index)">
                    </button>
                </view>
            </view>
            <button class="cu-btn block line-black lg margin" @click="chooseVideoImage()">
                <text class="cuIcon-upload"></text>
                上传答案
            </button>
        </view>
    </view>
</template>

<script>
const sourceType = [['camera'], ['album'], ['camera', 'album']];
export default {
    props: ['subjectiveQuestion', 'order', 'index'],
    name: 'SubjectiveQuestion',
    data() {
        return {
            files: [],
            videoOfImagesShow: true,
            images: [],
            videos: [],
            sourceType: ['拍摄', '相册', '拍摄或相册'],
            sourceTypeIndex: 2,
            cameraList: [{value: 'back', name: '后置摄像头', checked: 'true'}, {value: 'front', name: '前置摄像头'}],
            cameraIndex: 0
        };
    },
    onUnload() {
        (this.images = []), (this.sourceTypeIndex = 2), (this.sourceType = ['拍摄', '相册', '拍摄或相册']);
    },
    mounted() {
        uni.request({
            url: this.$BASICURL + 'SubjectiveQuestion/' + this.subjectiveQuestion.id + '/get_subjective_question_media/',
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
        // 点击上传图片或视频
        chooseVideoImage() {
            uni.showActionSheet({
                title: '选择上传类型',
                itemList: ['图片', '视频'],
                success: res => {
                    if (res.tapIndex == 0) {
                        this.chooseImages();
                    } else {
                        this.chooseVideo();
                    }
                }
            });
        },
        // 上传图片
        chooseImages() {
            uni.chooseImage({
                count: 4, // 默认是9张
                sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
                sourceType: ['album', 'camera'], // 从相册选择
                success: res => {
                    this.images = this.images.concat(res.tempFilePaths);
                    if (this.images.length == 4) {
                        this.videoOfImagesShow = false; // 图片上传数量和count一样时，让点击拍照按钮消失
                    }
                }
            });
        },
        // 上传视频
        chooseVideo(index) {
            uni.chooseVideo({
                maxDuration: 30, // 拍摄视频最长拍摄时间，单位秒。最长支持 60 秒
                count: 4,
                camera: this.cameraList[this.cameraIndex].value, // 'front'、'back'，默认'back'
                sourceType: sourceType[this.sourceTypeIndex],
                success: res => {
                    this.videos = this.videos.concat(res.tempFilePath);
                    if (this.videos.length == 4) {
                        this.videoOfImagesShow = false;
                    }
                }
            });
        },
        // 预览图片
        previewImage(url) {
            uni.previewImage({
                current: 0,
                urls: [url]
            });
        },
        // 删除图片
        delect(index) {
            uni.showModal({
                title: '提示',
                content: '是否要删除该图片',
                success: res => {
                    if (res.confirm) {
                        this.images.splice(index, 1);
                    }
                    if (this.images.length == 4) {
                        this.videoOfImagesShow = false;
                    } else {
                        this.videoOfImagesShow = true;
                    }
                }
            });
        },
        // 删除视频
        delectVideo(index) {
            uni.showModal({
                title: '提示',
                content: '是否要删除此视频',
                success: res => {
                    if (res.confirm) {
                        this.videos.splice(index, 1);
                    }
                    if (this.videos.length == 4) {
                        this.videoOfImagesShow = false;
                    } else {
                        this.videoOfImagesShow = true;
                    }
                }
            });
        },
        submitSubjectiveQuestion(student_id) {
            let answer_id;
            uni.request({
                url: this.$BASICURL + 'SubjectiveQuestionUserAnswer/delete_historical_answer/',
                method: 'POST',
                data: {
                    'question_id': this.subjectiveQuestion.id,
                    'student_id': student_id
                },
                success: res => {
                    answer_id = res.data;
                    for (let i = 0; i < this.images.length; i++) {
                        uni.uploadFile({
                            url: this.$BASICURL + 'SubjectiveQuestionUserAnswer/put_subjective_question_media/',
                            filePath: this.images[i],
                            name: 'media',
                            formData: {
                                'answer_id': answer_id,
                                'file_type': 'image'
                            }
                        });
                    }
                    for (const video of this.videos) {
                        uni.uploadFile({
                            url: this.$BASICURL + 'SubjectiveQuestionUserAnswer/put_subjective_question_media/',
                            filePath: video,
                            name: 'media',
                            formData: {
                                'answer_id': answer_id,
                                'file_type': 'video'
                            }
                        });
                    }
                },
                fail: err => {
                    console.log(err.data);
                }
            });
        },
        isEmpty() {
            if (this.images.length === 0 && this.videos.length === 0) {
                return true;
            }
            return false;
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

.close-button {
    position: absolute;
    margin-top: -259 upx;
    margin-left: 167 upx;
}
</style>
