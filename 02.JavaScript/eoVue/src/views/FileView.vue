<template>
  <div class="all">
    <h2>营销EO单&nbsp; {{ routeMsg }}</h2>
        <el-upload
            v-if="can_upload"
            ref="upload"
            class="upload-demo"
            action="http://eo.eihotel.com.cn/api/upload"
            method="post"
            name="file"
            :data="{ day: routeMsg }"
            :limit="1"
            :on-exceed="handleExceed"
            :on-success="onSuccess"
            :auto-upload="false"
        >
          <template #trigger>
            <el-space :size="30" spacer="|">
              <el-button type="primary">选择文件</el-button>
            </el-space>
          </template>
          <el-button class="ml-3" type="success" @click="submitUpload">
            上载到服务器
          </el-button>
          <template #tip>
            <div class="el-upload__tip text-red">限制一次性上传为1个文件</div>
          </template>
        </el-upload>

        <el-table
            :data="tableData"
            v-loading="loading"
            :header-cell-style="{ 'text-align': 'center' }"
            :cell-style="{ 'text-align': 'center' }"
            style="width: 100%"
        >
          <el-table-column
              prop="id"
              type="index"
              label="序号"
              width="50"
          ></el-table-column>
          <el-table-column label="文件名" link>
            <template v-slot="scope">
              <a
                  :href="'http://pdfjs.eihotel.com.cn/web/viewer.html?file=' + scope.row.pathname.toString().substring(1)"
                  target="_blank"
                  class="buttonText preview"
              >{{ scope.row.name }}</a
              >
            </template>
          </el-table-column>
          <!--    <el-table-column prop="size" label="附件大小"/>-->
          <el-table-column fixed="right" label="操作">
            <template v-slot="scope">
              <el-button
                  link
                  type="primary"
                  size="small"
                  @click="open(scope.row)"
              >预览
              </el-button>
              <el-button
                  link
                  type="primary"
                  size="small"
                  @click="handleClick(scope.row)"
              >下载
              </el-button>
              <el-button
                  v-if="can_upload"
                  link
                  type="primary"
                  @click="test(scope.row)"
                  size="small"
              >删除</el-button
              >
            </template>
          </el-table-column>
        </el-table>
  </div>
</template>
<script setup lang="ts">
import { useRoute } from "vue-router";
import { genFileId, ElMessage, ElMessageBox } from "element-plus";
import { ref } from "vue";
import type { UploadInstance, UploadProps, UploadRawFile } from "element-plus";
import axios from "axios";
import type { TabsPaneContext } from 'element-plus'

const route = useRoute();
// 接收路由传入的参数
const routeMsg = ref(route.query.day);
const tableData = ref([]);
const loading = ref(null);
const can_upload = ref();
can_upload.value = route.path.toString().search("upload") >= 0;

const upload = ref<UploadInstance>();

getFilList();

const handleExceed: UploadProps["onExceed"] = (files) => {
  upload.value!.clearFiles();
  const file = files[0] as UploadRawFile;
  file.uid = genFileId();
  upload.value!.handleStart(file);
  // console.log(file);
};

const onSuccess: UploadProps["onExceed"] = () => {
  ElMessage({
    type: "success",
    message: "上传成功",
  });
  upload.value!.clearFiles();
  getFilList();
};

const test = (row: { id: any }) => {
  ElMessageBox.confirm("是否删除此文件", "警告", {
    confirmButtonText: "确认",
    cancelButtonText: "取消",
    type: "warning",
  })
    .then(() => {
      axios({
        baseURL: "http://eo.eihotel.com.cn",
        url: "api/delete",
        method: "get",
        params: {
          id: row.id,
        },
      }).then(function () {
        ElMessage({
          type: "success",
          message: "删除成功",
        });
        getFilList();
      });
    })
    .catch(() => {
      ElMessage({
        type: "info",
        message: "已取消当前操作",
      });
    });
  // console.log(row)
};

/**
 * 下载
 * @param 选中的当前行数据
 */
const handleClick = (row: { name: string }) => {
  axios({
    baseURL: "http://eo.eihotel.com.cn",
    url: "api/download",
    method: "get",
    headers: { "X-Requested-With": "XMLHttpRequest" },
    responseType: "blob",
    // `params` 是与请求一起发送的 URL 参数
    // 必须是一个简单对象或 URLSearchParams 对象
    params: {
      name: row.name,
      day:route.query.day,
    },
  }).then(function (response) {
    const blob = new Blob([response.data]);
    const url = window.URL.createObjectURL(blob); // 创建 url 并指向 blob
    const a = document.createElement("a");
    a.href = url;
    a.download = row.name;
    a.click();
    window.URL.revokeObjectURL(url);
  });
};

const submitUpload = () => {
  upload.value!.submit();
};

//预览功能
const open = (row: { name: string }) => {
  // let docUrl = 'http://eo.eihotel.com.cn/uploads/'+ route.query.day + '/' + row.name
  let docUrl = '/uploads/'+ route.query.day + '/' + row.name
  console.log(docUrl);
  let url = encodeURIComponent(docUrl)
  let officeUrl = 'http://pdfjs.eihotel.com.cn/web/viewer.html?file='+url
  window.open(officeUrl)
}
//tab选项卡
const activeName = ref('first')

const Lists = (tab: TabsPaneContext) => {
  function getFilList() {
    axios({
      baseURL: "http://eo.eihotel.com.cn",
      url: "/api/getList",
      method: "post",
      withCredentials: false,
      timeout: 5000,
      data: {
        day: routeMsg.value,
        name:tab.props.name,
      },
    })
        .then(function (response) {
          tableData.value = response.data.tableData;
          return tableData.value
        })
        .catch(function (error) {
          ElMessage.error("请求超时，请稍后重试或者重新刷新页面");
          // console.log(error);
        });
  }
}

//获取列表
function getFilList() {
  axios({
    baseURL: "http://eo.eihotel.com.cn",
    url: "/api/getList",
    method: "post",
    withCredentials: false,
    timeout: 5000,
    data: {
      day: routeMsg.value,
    },
  })
    .then(function (response) {
      tableData.value = response.data.tableData;
    })
    .catch(function (error) {
      ElMessage.error("请求超时，请稍后重试或者重新刷新页面");
      // console.log(error);
    });
}




</script>
<style>
.el-descriptions {
  margin-top: 20px;
}

.all {
  width: auto;
  height: auto;
  margin: 0 auto;
}
.preview {
  text-underline: none !important;
  color: inherit;
}
.demo-tabs > .el-tabs__content {
  padding: 32px;
  color: #6b778c;
  font-size: 32px;
  font-weight: 600;
}
.demo-tabs .custom-tabs-label .el-icon {
  vertical-align: middle;
}
.demo-tabs .custom-tabs-label span {
  vertical-align: middle;
  margin-left: 4px;
}
</style>
