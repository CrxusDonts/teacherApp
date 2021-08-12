<template>
    <div>
        <Header></Header>
        <div id="poster">
            <el-form ref="loginForm" class="login-container" label-position="left"
                     label-width="0px">
                <h3 class="login-title">系统登录</h3>
                <el-form-item>
                    <el-input type="text" v-model="user_name" prefix-icon="el-icon-user" :autofocus="true"
                              auto-complete="off" placeholder="账号"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-input type="password" v-model="password" prefix-icon="el-icon-lock"
                              auto-complete="off" placeholder="密码" v-on:keyup.enter.native="login"></el-input>
                </el-form-item>

                <el-form-item>
                    <el-button class="method-Button" type="primary" @click="login">登录</el-button>
                    <el-button class="method-Button" type="primary" @click="register">注册</el-button>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>

<script>
import Header from '../components/Header';

export default {
    name: 'Login',
    components: { Header },
    data: function() {
        return {
            user_name: '',
            password: ''
        };
    },
    methods: {
        login() {
            if (!this.user_name) {
                this.$message.error('请输入账号！');
            } else if (!this.password) {
                this.$message.error('请输入密码！');
            } else {
                this.$http.post('BackendAccount/login/', {
                    user_name: this.user_name,
                    password: this.password
                }).then(response => {
                    if (response.data === 'Login succeed.') {
                        this.$router.push({ path: '/home/' + this.user_name });
                    } else {
                        alert('登录失败！');
                    }
                });
            }
        },
        register() {
            this.$router.push({ path: '/register' });
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
    margin: 120px auto 90px;
    border: 1px solid #eaeaea;
    border-radius: 15px;
    background-clip: padding-box;
    background-color: #fff;
    box-shadow: 0 0 20px;
}

.login-title {
    margin: 0 auto 40px;
    text-align: center;
    color: #505458;
}

.method-Button {
    width: 80px;
    height: 40px;
    border: none;
    background-color: #505458;
}

</style>
