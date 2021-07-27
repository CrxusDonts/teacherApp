<template>
    <div id="poster">
        <el-form ref="loginForm" class="passwordModify-container" label-position="left"
                 label-width="0px">
            <h3 class="login_title">修改密码</h3>
            <el-form-item>
                <el-input type="password" v-model="oldPassword" prefix-icon="el-icon-lock"
                          auto-complete="off" placeholder="原密码"></el-input>
            </el-form-item>
            <el-form-item>
                <el-input type="password" v-model="newPassword" prefix-icon="el-icon-lock"
                          auto-complete="off" placeholder="新密码"></el-input>
            </el-form-item>
            <el-form-item>
                <el-input type="password" v-model="newPasswordAgain" prefix-icon="el-icon-lock"
                          auto-complete="off" placeholder="再次输入新密码" v-on:keyup.enter.native="modify"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button class="methodButton" type="primary" @click="modify">确定修改</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
export default {
    name: 'passwordModify',
    data: function () {
        return {
            oldPassword: '',
            newPassword: '',
            newPasswordAgain: ''
        };
    },
    methods: {
        modify() {
            if (!this.oldPassword) {
                this.$message.error('请输入原密码！');//message组件弹出框
            } else if (!this.newPassword) {
                this.$message.error('请输入新密码！');
            } else if (!this.newPasswordAgain) {
                this.$message.error('请再次输入新密码！');
            } else if (this.newPassword!=this.newPasswordAgain) {
                this.$message.error('请保证两次密码输入一致！');
            } else {
                this.$http.post('BackendAccount/change_password/', {//其中的路由需要修改
                    old_password: this.oldPassword,
                    new_password:this.newPassword
                }).then(response => {//在其中写后端交互方法
                    if (response.status === 200) {//200是判断http请求是否成功
                        this.$message.error('密码修改成功，请重新登录');
                    } else {
                        this.$message.error('密码修改失败，请重新修改');
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

.passwordModify-container {
    width: 350px;
    padding: 35px 15px;
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
    background-color: #505458;
}
</style>
