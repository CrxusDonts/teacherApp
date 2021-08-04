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
        <span>你好,{{name}}</span>
        <span style="float: right;
                    margin-left: 10px;">
          <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png" :size=40></el-avatar>
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item :divided=true @click.native="passwordModify">修改密码</el-dropdown-item>
          <el-dropdown-item :divided=true @click.native="exit">退出登录</el-dropdown-item>
        </el-dropdown-menu>
        <em class="el-icon-arrow-down el-icon--right"></em>
      </div>
    </el-dropdown>
  </el-card>
</template>

<script>
export default {
    name: 'Header',
    data: function() {
        return {
            user_name: '',
            name: ''
        };
    },
    mounted() {
        this.user_name = this.$route.params.user_name;
        this.$http.post('People/get_name/', {
            user_name: this.user_name
        }).then(response => {
            if (response.data !== 'get_name failed.') {
                this.name = response.data;
            } else {
                this.name = '无名少侠';
            }
        });
    },
    methods: {
        passwordModify() {
            this.$router.push({ path: '/passwordModify' });
        },
        exit() {
            this.$http.post('BackendAccount/logout/');
            this.$router.push({ path: '/' });
        }
    }
};
</script>

<style scoped>
.common-header {
    height: 80px;
    line-height: 40px;
    background-color: white;
}

.el-dropdown-link {
    color: #409eff;
    cursor: pointer;
}

.el-icon-arrow-down {
    font-size: 12px;
}
</style>
