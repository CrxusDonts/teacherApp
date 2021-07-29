<template>
  <el-carousel :interval="4000" type="card" height="300px">
    <el-carousel-item v-for="item in 6" :key="item" @click="toClassId">
      <h3 class="medium">{{ item }}</h3>
    </el-carousel-item>
  </el-carousel>
</template>

<script>
export default {
    name: 'SwitchClass',
    data() {
        return {
            items: ''
        };
    },
    mounted: function() {
        this.$http.get('') // TODO 填写需要的地址
            .then((response) => {
                this.items = response.data;
            });
    },
    methods: {
        toClassId: function() {
            // TODO 实现页面跳转，跳转至对应班级界面
        }
    }
};
</script>

<style scoped>

.el-carousel__item h3 {
    margin: 0;
    font-size: 14px;
    line-height: 200px;
    color: #475669;
    opacity: .75;
}

</style>
