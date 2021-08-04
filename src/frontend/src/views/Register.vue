<template>
    <div id="poster">
        <el-form ref="loginForm" class="Register-container" label-position="left" label-width="0px">
            <h3 class="login-title">注册</h3>
            <el-form-item>
                <el-input type="text" v-model="user_name" prefix-icon="el-icon-user" :autofocus="true"
                          auto-complete="off" placeholder="账号"></el-input>
            </el-form-item>
            <el-form-item>
                <el-input type="password" v-model="password" prefix-icon="el-icon-lock"
                          auto-complete="off" placeholder="密码"></el-input>
            </el-form-item>
            <el-form-item>
                <el-input type="text" v-model="class_name" prefix-icon="el-icon-menu"
                          auto-complete="off" placeholder="班级"></el-input>
            </el-form-item>
            <el-form-item>
                <el-input type="text" v-model="name" prefix-icon="el-icon-s-custom"
                          auto-complete="off" placeholder="姓名"></el-input>
            </el-form-item>
            <el-form-item>
                <el-radio v-model="is_male" :label="true">男</el-radio>
                <el-radio v-model="is_male" :label="false">女</el-radio>
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
            user_name: '',
            password: '',
            class_name: '',
            name: '',
            is_male: ''
        };
    },
    methods: {
        doRegister() {
            if (!this.user_name) {
                this.$message.error('请输入账号！');
            } else if (!this.password) {
                this.$message.error('请输入密码！');
            } else if (!this.class_name) {
                this.$message.error('请输入班级！');
            } else if (!this.name) {
                this.$message.error('请输入姓名！');
            } else if (!this.is_male) {
                this.$message.error('请选择性别！');
            } else {
                console.log(this.user_name);
                console.log(this.password);
                console.log(this.class_name);
                console.log(this.name);
                console.log(this.is_male);
                this.$http.post('BackendAccount/register_teacher/', {
                    user_name: this.user_name,
                    password: this.password,
                    class_name: this.class_name,
                    name: this.name,
                    is_male: this.is_male
                }).then(response => {
                    if (response.data === 'Register succeed.') {
                        this.$router.push({ path: '/' });
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
    width: 100px;
    height: 40px;
    border: none;
    background: #505458;
}

</style>
