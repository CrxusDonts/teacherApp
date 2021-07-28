<template>
    <div id="poster">
        <el-form ref="loginForm" class="Register-container" label-position="left" label-width="0px">
            <h3 class="login-title">注册</h3>
            <el-form-item>
                <el-input type="text" v-model="userName" prefix-icon="el-icon-user"
                          auto-complete="off" placeholder="账号"></el-input>
            </el-form-item>
            <el-form-item>
                <el-input type="password" v-model="password" prefix-icon="el-icon-lock"
                          auto-complete="off" placeholder="密码"></el-input>
            </el-form-item>
            <el-form-item>
                <el-input type="text" v-model="classname" prefix-icon="el-icon-menu"
                          auto-complete="off" placeholder="班级" v-on:keyup.enter.native="doRegister"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button class="method-Button" type="primary" @click="doRegister">注册</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
export default {
    name: 'Register',
    data: function() {
        return {
            userName: '',
            password: '',
            classname: ''
        };
    },
    methods: {
        doRegister() {
            if (!this.userName) {
                this.$message.error('请输入账号！');
            } else if (!this.password) {
                this.$message.error('请输入密码！');
            } else if (!this.classname) {
                this.$message.error('请输入班级！');
            } else {
                this.$http.post('BackendAccount/register_teacher/', {
                    user_name: this.userName,
                    password: this.password,
                    class_name: this.classname
                }).then(response => {
                    if (response.data === 'Register succeed.') {
                        this.$router.push({ path: '/home', query: { user_name: this.userName }});
                    } else if (response.data === 'User already existed.') {
                        this.$message.error('您注册的账号已存在，请重新注册！');
                    } else {
                        this.$message.error('注册失败！');
                    }
                });
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

.login-title {
    margin: 0 auto 40px;
    text-align: center;
    color: #505458;
}

.method-Button {
    width: 100px;
    height: 40px;
    border: none;
    background: #505458;
}

</style>
