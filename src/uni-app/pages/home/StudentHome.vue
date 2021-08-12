<template>
    <view>
        <view class="cu-bar bg-white solid-bottom margin-top">
            <view class="action">
                <text class="cuIcon-title text-blue "></text>
                班级列表
            </view>
            <button class="cu-btn bg-grey margin-right" @click="toJoinClass()">加入班级</button>
        </view>
        <view class="cu-list menu-avatar">
            <view class="cu-item" :class="size?'solids-top':'solid-top'" v-for="clazz in classes"
                  @click="toClassManagement(clazz)">
                <view class="cu-avatar round lg cuIcon-group"></view>
                <view class="content">
                    <view class="text-grey">{{ clazz.class_name }}</view>
                </view>
            </view>
        </view>
    </view>
</template>

<script>
export default {
    data() {
        return {
            open_id: '',
            classes: []
        };
    },
    onLoad: function (option) {
        this.open_id = option.open_id;
    },
    mounted() {
        uni.request({
            url: this.$BASICURL + 'Class/get_class_of_student/',
            method: 'get',
            success: res => {
                if (res.data !== 'Get my manage class failed.') {
                    this.classes = res.data;
                } else {
                    uni.showToast({
                        title: '获取班级列表失败',
                        icon: 'none'
                    });
                }
            }
        });
    },
    methods: {
        toClassManagement(clazz) {
            uni.navigateTo({
                url: '../HomeworkManagement?clazz=' + JSON.stringify(clazz) + '&is_teacher=0'
            });
        },
        toJoinClass() {
            uni.navigateTo({
                url: '../JoinClass?open_id=' + this.open_id
            });
        }
    }
};
</script>
