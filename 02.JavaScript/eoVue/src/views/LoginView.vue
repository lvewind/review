<template>
  <div class="mian">
      <el-main>
        <div class="jvzhong">
          <div class="rongqi">
            <div class="form">
              <div style="font-size: 25px;padding-top: 50px">会展国际大酒店EO单</div>
              <div style="font-size: 31px;padding: 50px 0 30px 0;font-weight:bold">登录</div>
              <div>Login</div>
              <el-form
                  :model="ruleForm"
                  ref="ruleFormsss"
                  :label-position="labelPosition"
                  :rules="rules"
              >
                <el-form-item label="工号" prop="username">
                  <el-input v-model="ruleForm.username"/>
                </el-form-item>
                <el-form-item label="密码" prop="password">
                  <el-input type="password" v-model="ruleForm.password"/>
                </el-form-item>
                <el-form-item>
                  <el-button type="primary" @click="submitForm">登录</el-button>
                </el-form-item>
              </el-form>
            </div>

          </div>
          <div>
            <img src="../assets/images/small-team-discussing-ideas-2194220-0.png" alt="">
          </div>
          </div>
      </el-main>
  </div>
</template>

<script lang="ts" setup>
import { reactive, ref ,unref} from 'vue'
import { genFileId, ElMessage, ElMessageBox } from "element-plus";
import { useRouter } from "vue-router";

import "@/assets/login.css"
import axios from "axios";

const router = useRouter();
const labelPosition = ref('top')

const ruleFormsss = ref(null)
// 定义变量
const ruleForm = reactive({
  username: '',
  password: ''
})

const rules = {
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' },
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
  ],
}

const submitForm  = () => {
  axios({
      baseURL: "https://eo.eihotel.com.cn",
      url: "/index/login",
      method: "post",
      withCredentials: false,
      timeout: 5000,
      data: {
        username: ruleForm.username,
        password:ruleForm.password,
      },
    })
        .then(function (response) {
          if(response.data.code == 400){
            ElMessage.error(response.data.msg);
            router.push('/login')
          }
          if(response.data.code == 200){
            sessionStorage.setItem('token',response.data.token)
            sessionStorage.setItem('username',response.data.username)
            ElMessage({
              message: response.data.msg,
              type: 'success',
            })
            router.push('/')
            }
        })
        .catch(function (error) {
          ElMessage.error("请求超时，请稍后重试或者重新刷新页面");
        });
  // console.log(ruleForm.username)
}


</script>
<style scoped>
</style>