<template>
  <el-carousel :interval="4000" type="card" height="300px">
    <el-carousel-item v-for="item in 6" :key="item" @click="to_classid">
      <h3 class="medium">{{ item }}</h3>
    </el-carousel-item>
  </el-carousel>
</template>

<script>
export default {
    name: 'SwitchClass',
    data(){
        return {
            items:'',
        };
    },
    mounted:function(){
        this.$http.get('')//填写需要的地址
            .then((response) => {
                this.items=response.data;
            });
    },
    methods:{
        to_classid:function(){//实现页面跳转，跳转到对应班级界面
      
        }
    }
};
</script>

<style scoped>
  .el-carousel--card{
    margin-top: 100px;
  }
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }
  
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>
