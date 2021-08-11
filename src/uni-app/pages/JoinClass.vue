<template>
	<view>
		<view class="cu-bar bg-white">
			<view class="action">
				<text class="cuIcon-title text-blue"></text>请输入班级信息和你的信息
			</view>
		</view>
		<view class="cu-form-group margin-top">
			<view class="title">班级id</view>
				<input placeholder="请输入要申请加入的班级id" name="input" @input="inputClassId"></input>
		</view>
		<view class="cu-form-group">
				<view class="title">姓名</view>
				<input placeholder="请输入你的姓名" name="input" @input="inputName"></input>
		</view>
		<view class="padding flex justify-end">
			<button class="cu-btn bg-grey lg" @click="joinClass()">确认提交</button>
		</view>
	</view>
</template>

<script>
export default {
    data() {
        return {
            open_id: '',
            class_id: '',
            name: ''
        };
    },
    onLoad: function(option) {
        this.open_id = option.open_id;
    },
    methods: {
        inputClassId(e) {
            this.class_id = e.target.value;
        },
        inputName(e) {
            this.name = e.target.value;
        },
        joinClass() {
            uni.request({
                url: this.$BASICURL + 'JoinClassRequest/create_join_class_request/',
                data: {
                    'open_id': this.open_id,
                    'class_id': this.class_id,
                    'name': this.name
                },
                method: 'post',
                success: res => {
                    if (res.data === 'create_join_class_request succeed') {
                        uni.showToast({
                            title: '申请成功',
                            icon: 'none'
                        });
                        setTimeout(() => {
                            uni.navigateBack();
                        }, 1000);
                    } else if (res.data === 'Class matching query does not exist.') {
                        uni.showToast({
                            title: '申请失败,班级不存在',
                            icon: 'none'
                        });
                    } else {
                        uni.showToast({
                            title: '申请失败',
                            icon: 'none'
                        });
                    }
                }
            });
        }
    }
};
</script>
