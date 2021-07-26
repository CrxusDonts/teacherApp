<template>
  <el-card class="common-header">
    <a>
      <img src="../assets/icon3.jpg" alt="" width="55px" style="float: left;
                margin-top: -5px;">
    </a>
    <span style="position: absolute;
    left: 100px;
    font-weight: bold;
    font-size: 32px;">布置作业系统</span>
    <el-dropdown :show-timeout=10 :hide-timeout=50 style="float: right;
    padding-right: 10px;">
      <div class="el-dropdown-link">
        <span>你好,{{userName}}</span>
        <span style="float: right;
                    margin-left: 10px;">
          <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png" :size=40></el-avatar>
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item :divided=true @click.native="passwordModify">修改密码</el-dropdown-item>
          <el-dropdown-item :divided=true @click.native="exit">退出登录</el-dropdown-item>
        </el-dropdown-menu>
        <i class="el-icon-arrow-down el-icon--right"></i>
      </div>
    </el-dropdown>
  </el-card>
</template>

<script>
export default {
    name: 'Header',
    props: ['userName'],
    data: function () {
        return {};
    },
    methods: {
        passwordModify() {
            this.$router.push({path: '/passwordModify', query: {userName: this.userName}});
        },
        exit() {
            this.$router.push({path: '/'});
        }
    }
};
</script>

<style scoped>
.common-header {
    height: 80px;
    line-height: 40px;
    opacity: .85;
}

.el-dropdown-link {
    color: #409eff;
    cursor: pointer;
}

.el-icon-arrow-down {
    font-size: 12px;
}
</style>
