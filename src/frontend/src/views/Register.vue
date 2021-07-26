<template>
    <div id="poster">
        <el-form ref="loginForm" class="Register-container" label-position="left" label-width="0px">
            <h3 class="login_title">注册</h3>
            <el-form-item>
                <el-input type="text" v-model="userName" prefix-icon="el-icon-user"
                          auto-complete="off" placeholder="账号"></el-input>
            </el-form-item>
            <el-form-item>
                <el-input type="password" v-model="password" prefix-icon="el-icon-lock"
                          auto-complete="off" placeholder="密码"></el-input>
            </el-form-item>
            <el-form-item>
                <el-input type="text" v-model="classId" prefix-icon="el-icon-menu"
                          auto-complete="off" placeholder="班级" v-on:keyup.enter.native="doRegister"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button class="methodButton" type="primary" @click="doRegister">注册</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
export default {
    name: 'Register',
    data: function () {
        return {
            userName: '',
            password: '',
            classId: ''
        };
    },
    methods: {
        doRegister() {
            if (!this.userName) {
                this.$message.error('请输入账号！');//message组件弹出框
                return;
            } else if (!this.password) {
                this.$message.error('请输入密码！');
                return;
            } else if (!this.classid) {
                this.$message.error('请输入班级！');
                return;
            } else {
                /* this.$router.push({ path: "/" }); */ //无需向后台提交数据，方便前台调试,与后端交互时可以删除
                console.log(this.userName);
                this.$http.post('BackendAccount/register/', {
                    user_name: this.userName,
                    password: this.password
                }).then(response => {
                    if (response.data !== 'The user exist') {//200是判断http请求是否成功
                        this.$router.push({path: '/home', query: {userName: this.userName}});
                    } else {
                        alert('登录失败！');
                    }
                });
                this.$router.push({path: '/register'});
            }
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

.Register-container {
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
    width: 100px;
    height: 40px;
    border: none;
    background: #505458;
}

</style>
