<template>
	<view class="cu-card case">
		<view class="cu-item shadow">
			<view class="cu-item">
				<view class="content flex-sub padding">
					<view class="text-lg margin-left">{{order + '.' + choiceQuestion.text_content}}</view>
					<view style="display: flex;">
						<view v-for="file in files">
							<image v-if="file.file_type === 0" class="margin-left margin-top image"
							:src="file.url" @click="previewImage(file.url)"></image>
							<video v-if="file.file_type === 1" class="margin-left margin-top video" :src="file.url"></video>
						</view>
					</view>
					<checkbox-group class="block" @change="CheckboxChange">
						<view v-for="option in options" class="margin-top margin-left">
							<checkbox :class="option.checked?'checked':''"
							:checked="option.checked?true:false" :value="option.order">
							</checkbox>
							{{String.fromCharCode("A".charCodeAt(0) - 1 + option.order)}}.{{option.text_content}}
						</view>
					</checkbox-group>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
export default {
    props: ['choiceQuestion', 'order', 'index'],
    name: 'ChoiceQuestion',
    data() {
        return {
            options: [],
            files: []
        };
    },
    mounted() {
        uni.request({
            url: 'http://localhost:8002/teacherApp/ChoiceQuestion/' + this.choiceQuestion.id + '/get_options/',
            method: 'GET',
            success: res => {
                this.options = res.data;
                for (const option of this.options) {
                    option.checked = false;
                }
            }
        });
        uni.request({
            url: 'http://localhost:8002/teacherApp/ChoiceQuestion/' + this.choiceQuestion.id + '/get_topic_media/',
            method: 'GET',
            success: res => {
                this.files = res.data;
                for (const file of this.files) {
                    file.url = 'http://localhost:8002/' + file.url.substring(6);
                }
            }
        });
    },
    methods: {
        CheckboxChange(e) {
            for (const option of this.options) {
                option.checked = false;
            }
            for (const value of e.detail.value) {
                this.options[value - 1].checked = true;
            }
        },
        // 预览图片
        previewImage(url) {
            uni.previewImage({
                current: 0,
                urls: [url]
            });
        },
        submitChoiceQuestion(student_id) {
            let answer = '';
            for (const option of this.options) {
                if (option.checked) {
                    answer += option.order;
                    answer += ' ';
                }
            }
            uni.request({
                url: 'http://localhost:8002/teacherApp/ChoiceQuestionUserAnswer/add_user_answer/',
                data: {
                    'answer_order': answer,
                    'question_id': this.choiceQuestion.id,
                    'student_id': student_id
                },
                method: 'POST'
            });
        },
        isEmpty() {
            for (const option of this.options) {
                if (option.checked) {
                    return false;
                }
            }
            return true;
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
