<template>
    <div id="poster">
        <el-form ref="loginForm" class="login-container" label-position="left"
                 label-width="0px">
            <h3 class="login_title">系统登录</h3>
            <el-form-item>
                <el-input type="text" v-model="userName" prefix-icon="el-icon-user"
                          auto-complete="off" placeholder="账号"></el-input>
            </el-form-item>
            <el-form-item>
                <el-input type="password" v-model="password" prefix-icon="el-icon-lock"
                          auto-complete="off" placeholder="密码" v-on:keyup.enter.native="login"></el-input>
            </el-form-item>

            <el-form-item>
                <el-button class="methodButton" type="primary" @click="login">登录</el-button>
                <el-button class="methodButton" type="primary" @click="register">注册</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
export default {
    name: 'Login',
    data: function () {
        return {
            userName: '',
            password: ''
        };
    },
    methods: {
        login() {

        },
        register() {

        }
    }
};
</script>

<style scoped>

#poster {
    position: fixed;
    width: 100%;
    height: 100%;
    background-size: cover;
}

.login-container {
    width: 350px;
    padding: 35px 35px 15px;
    margin: 180px auto 90px;
    border: 1px solid #eaeaea;
    border-radius: 15px;
    background-clip: padding-box;
    background-color: #fff;
    box-shadow: 0 0 20px;
}

.login_title {
    margin: 0 auto 40px;
    text-align: center;
    color: #505458;
}

.methodButton {
    width: 80px;
    height: 40px;
    border: none;
    background-color: #505458;
}

</style>
