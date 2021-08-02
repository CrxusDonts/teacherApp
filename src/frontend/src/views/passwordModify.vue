<template>
    <div id="poster">
        <el-form ref="loginForm" class="passwordModify-container" label-position="left"
                 label-width="0px">
            <h3 class="login-title">修改密码</h3>
            <el-form-item>
                <el-input type="password" v-model="old_password" prefix-icon="el-icon-lock" :autofocus="true"
                          auto-complete="off" placeholder="原密码"></el-input>
            </el-form-item>
            <el-form-item>
                <el-input type="password" v-model="new_password" prefix-icon="el-icon-lock"
                          auto-complete="off" placeholder="新密码"></el-input>
            </el-form-item>
            <el-form-item>
                <el-input type="password" v-model="new_password_again" prefix-icon="el-icon-lock"
                          auto-complete="off" placeholder="再次输入新密码" v-on:keyup.enter.native="modify"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button class="method-Button" type="primary" @click="modify">确定修改</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
export default {
    name: 'passwordModify',
    data: function() {
        return {
            old_password: '',
            new_password: '',
            new_password_again: ''
        };
    },
    methods: {
        modify() {
            if (!this.old_password) {
                this.$message.error('请输入原密码！');// message组件弹出框
            } else if (!this.new_password) {
                this.$message.error('请输入新密码！');
            } else if (!this.new_password_again) {
                this.$message.error('请再次输入新密码！');
            } else if (this.new_password !== this.new_password_again) {
                this.$message.error('请保证两次密码输入一致！');
            } else {
                this.$http.put('BackendAccount/change_password/', {
                    old_password: this.old_password,
                    new_password: this.new_password
                }).then(response => {
                    console.log(response.data);
                    if (response.data === 'Modify password succeed.') {
                        this.$message({
                            message: '密码修改成功',
                            type: 'success'
                        });
                        this.$router.push({ path: '/home' });
                    } else if (response.data === 'Old password is not correct.') {
                        this.$message.error('原密码错误');
                    } else {
                        this.$message.error('密码修改失败，请重新再试');
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

.login-title {
    margin: 0 auto 40px;
    text-align: center;
    color: #505458;
}

.method-Button {
    width: 100px;
    height: 40px;
    border: none;
    background-color: #505458;
}
</style>
