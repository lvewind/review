<template>
  <template v-if="iSuccess">
    <h3 class="success-title">上传成功！辛苦了！</h3>
  </template>
  <template v-else-if="true">
    <a-layout>
      <a-layout-header>
        <h3>{{ xj_form.name }}</h3>
      </a-layout-header>
      <a-layout-content>
        <a-form
          :ref="xjFormRef"
          :model="xj_form"
          :label-col="{ span: 4 }"
          :wrapper-col="{ span: 16 }"
          autocomplete="off"
          @finish="onSubmit"
        >
          <a-form-item
            label="部门"
            name="department"
            :rules="[{ required: true, message: '部门不能为空' }]"
          >
            <a-input
              class="department-name"
              v-model:value="xj_form.department"
              disabled
            ></a-input>
          </a-form-item>

          <a-form-item
            label="巡检人"
            name="inspector"
            :rules="[{ required: true, message: '巡检人不能为空' }]"
          >
            <a-select v-model:value="xj_form.inspector">
              <template
                v-for="(inspector, index) in xj_form.inspectorList"
                :key="index"
              >
                <a-select-option :value="inspector.name">
                  {{ inspector.name }}
                </a-select-option>
              </template>
            </a-select>
          </a-form-item>

          <a-form-item
            label="班次"
            name="scheduling"
            :rules="[{ required: true, message: '班次不能为空' }]"
          >
            <a-select v-model:value="xj_form.scheduling">
              <template
                v-for="(schedule, index) in xj_form.schedulingList"
                :key="index"
              >
                <a-select-option :value="schedule.id">
                  {{ schedule.name }}
                </a-select-option>
              </template>
            </a-select>
          </a-form-item>

          <template
            v-for="(project, index) in xj_form.projectList"
            :key="project.id"
          >
            <a-divider></a-divider>
            <h3 class="project-name">{{ project.name }}</h3>
            <a-form-item
              label="状态"
              :name="['projectList', index, 'project_status']"
              :rules="[{ required: true, message: '状态不能为空' }]"
            >
              <a-select
                v-model:value="project.project_status"
                @change="onProjectStatusChange"
              >
                <a-select-option :value="1">正常</a-select-option>
                <a-select-option :value="0">异常</a-select-option>
              </a-select>
            </a-form-item>

            <a-form-item
              v-if="project.photo"
              label="拍照"
              :name="['projectList', index, 'photo_url']"
              :rules="[
                { required: true, message: '照片不能为空', trigger: 'change' },
              ]"
            >
              <a-input
                v-model:value="project.photo_url"
                hidden="hidden"
              ></a-input>
              <a-form-item-rest>
                <a-upload
                  v-model:file-list="fileList"
                  list-type="picture-card"
                  class="avatar-uploader"
                  accept="image/*"
                  capture="camera"
                  :name="'photo_' + project.id"
                  :data="{ p_id: project.id, index: index }"
                  :maxCount="1"
                  :show-upload-list="false"
                  :action="apiBaseUrl + 'upload-image'"
                  :before-upload="beforeUploadImage"
                  @change="handleChangeImage"
                >
                  <img
                    class="upload_image_preview"
                    v-if="imageUrl[index]"
                    :src="imageUrl[index]"
                    alt="photo"
                  />
                  <div v-else>
                    <loading-outlined v-if="loading"></loading-outlined>
                    <plus-outlined v-else></plus-outlined>
                    <div class="ant-upload-text">拍照</div>
                  </div>
                </a-upload>
              </a-form-item-rest>
            </a-form-item>
            <a-form-item
              v-if="project.video"
              label="录像"
              :name="['projectList', index, 'video_url']"
              :rules="[
                { required: true, message: '录像不能为空', trigger: 'change' },
              ]"
            >
              <a-input v-model:value="project.video_url" hidden></a-input>
              <video
                class="upload_video_preview"
                v-if="videoUrl[index]"
                :src="videoUrl[index]"
                autoplay
                controls
                muted
              />
              <a-form-item-rest>
                <a-upload
                  v-model:file-list="fileList"
                  list-type="picture-card"
                  class="avatar-uploader"
                  accept="video/*"
                  capture="camcorder"
                  :name="'video_' + project.id"
                  :data="{ p_id: project.id, index: index }"
                  :maxCount="1"
                  :show-upload-list="false"
                  :action="apiBaseUrl + 'upload-video'"
                  :before-upload="beforeUploadVideo"
                  @change="handleChangeVideo"
                >
                  <div v-if="videoUrl[index]">
                    <loading-outlined v-if="loading"></loading-outlined>
                    <plus-outlined v-else></plus-outlined>
                    <div class="ant-upload-text">重新录像</div>
                  </div>
                  <div v-else>
                    <loading-outlined v-if="loading"></loading-outlined>
                    <plus-outlined v-else></plus-outlined>
                    <div class="ant-upload-text">录像</div>
                  </div>
                </a-upload>
              </a-form-item-rest>
            </a-form-item>
            <a-form-item label="备注" :name="['projectList', index, 'note']">
              <a-textarea v-model:value="project.note" />
            </a-form-item>
          </template>
          <a-divider></a-divider>
          <a-form-item>
            <a-button type="primary" html-type="submit">提交</a-button>
          </a-form-item>
        </a-form>
        <div hidden="hidden"></div>
      </a-layout-content>
      <a-layout-footer
        ><p class="copy-right">
          东莞会展国际大酒店版权所有@2022
        </p></a-layout-footer
      >
    </a-layout>
  </template>
  <template v-else>
    <a-empty description="不存在此表单，请联系管理员更新二维码！" />
  </template>
</template>

<script setup lang="ts">
import axios from "axios";
import { onMounted, ref } from "vue";
import { PlusOutlined, LoadingOutlined } from "@ant-design/icons-vue";
import { message } from "ant-design-vue";

import type {
  UploadChangeParam,
  UploadProps,
  FormInstance,
} from "ant-design-vue";
import "ant-design-vue/es/message/style/css";
import "./FormAnt.css";

interface XjForm {
  name: string;
  place_id: number;
  inspection_status: number;
  department: string;
  department_id: number;
  inspector: string;
  inspectorList: [];
  scheduling: string;
  schedulingList: [];
  projectList: [
    {
      id: number;
      name: string;
      project_status: number;
      photo_path: string;
      photo_url: string;
      video_path: string;
      video_url: string;
      video: number;
      photo: number;
      note: string;
    }
  ];
}

const iSuccess = ref(false);
const placeExist = ref(false);
const server = "http://192.168.13.24";
const apiBaseUrl = server + "/api/v1/";
const xjFormRef = ref<FormInstance>();
const imageUrl: { [index: string]: any } = ref({});
const videoUrl: { [index: string]: any } = ref({});
const xj_form = ref<XjForm>({
  name: "东莞会展国际大酒店",
  place_id: 0,
  inspection_status: 1,
  department: "",
  department_id: 0,
  inspector: "",
  inspectorList: [],
  scheduling: "",
  schedulingList: [],
  projectList: [
    {
      id: 0,
      name: "",
      project_status: 0,
      photo_path: "",
      photo_url: "",
      video_path: "",
      video_url: "",
      photo: 0,
      video: 0,
      note: "",
    },
  ],
});

const onSubmit = () => {
  axios
    .post(apiBaseUrl + "save-inspection", xj_form.value)
    .then(function (response) {
      if (response.data == "success") {
        iSuccess.value = true;
        console.log("inspection success");
      }
    });
};
const onProjectStatusChange = (value: any) => {
  if (value != 1) {
    xj_form.value.inspection_status = -1;
  }
  console.log(value);
  console.log(xj_form.value);
};
const loading = ref<boolean>(false);
const fileList = ref([]);
const handleChangeImage = (info: UploadChangeParam) => {
  if (info.file.status === "uploading") {
    loading.value = true;
    return;
  }
  if (info.file.status === "done" && info.file.originFileObj) {
    getBase64(info.file.originFileObj, (base64Url: string) => {
      const upload_result: { [index: string]: any } = info.file.response;
      imageUrl.value[upload_result.index] = base64Url;
      xj_form.value.projectList[upload_result.index].photo_path =
        upload_result.photo_path;
      xj_form.value.projectList[upload_result.index].photo_url =
        upload_result.photo_url;
      loading.value = false;
      console.log("xj_form: handleChangeImage: ", xj_form);
    });
  }
  if (info.file.status === "error") {
    loading.value = false;
    message.error("upload error");
  }
};
const handleChangeVideo = (info: UploadChangeParam) => {
  if (info.file.status === "uploading") {
    loading.value = true;
    return;
  }
  if (info.file.status === "done" && info.file.originFileObj) {
    const upload_result: { [index: string]: any } = info.file.response;
    videoUrl.value[upload_result.index] =
      server + "/" + upload_result.video_url;
    loading.value = false;
    xj_form.value.projectList[upload_result.index].video_path =
      upload_result.video_path;
    xj_form.value.projectList[upload_result.index].video_url =
      upload_result.video_url;

    console.log(xj_form);
  }
  if (info.file.status === "error") {
    loading.value = false;
    message.error("upload error");
  }
};
const beforeUploadImage = (file: UploadProps["fileList"][number]) => {
  const isLt20M = file.size / 1024 / 1024 < 200;
  if (!isLt20M) {
    message.error("图片必须小于 20MB!");
  }
  return isLt20M;
};
const beforeUploadVideo = (file: UploadProps["fileList"][number]) => {
  const isLt100M = file.size / 1024 / 1024 < 100;
  if (!isLt100M) {
    message.error("视频必须小于 100MB!");
  }
  return isLt100M;
};

onMounted(() => {
  getFormData();
  // console.log("placeData", placeData.value);
});

function getBase64(img: Blob, callback: (base64Url: string) => void) {
  const reader = new FileReader();
  reader.addEventListener("load", () => callback(reader.result as string));
  reader.readAsDataURL(img);
}
function getFormData() {
  const place_id = window.location.href.split("/").pop();
  if (place_id) {
    placeExist.value = true;
    axios
      .get(apiBaseUrl + "get-form/" + place_id.toString())
      .then(function (response) {
        console.log("response: getFormData: ", response.data);
        xj_form.value.name = response.data.place.name;
        xj_form.value.place_id = response.data.place.id;
        xj_form.value.department = response.data.department.name;
        xj_form.value.department_id = response.data.department.id;
        xj_form.value.schedulingList = response.data.scheduling;
        for (const project of response.data.project) {
          Object.assign(project, {
            photo_path: "",
            photo_url: "",
            video_path: "",
            video_url: "",
            note: "",
          });
          xj_form.value.projectList.pop();
          xj_form.value.projectList.push(project);
        }
        xj_form.value.projectList = Object.assign(
          xj_form.value.projectList,
          response.data.project
        );
        getInspector(response.data.department.id);
        console.log("xj_form: afterGetFormData: ", xj_form);
      })
      .catch(function (error) {
        message.error(error.toString());
      });
  } else {
    message.error("参数错误");
    placeExist.value = false;
  }
}
function getInspector(department_id: number) {
  axios
    .get(apiBaseUrl + "get-inspector/" + department_id.toString())
    .then(function (response) {
      xj_form.value.inspectorList = response.data;
    })
    .catch(function (error) {
      message.error(error.toString());
    });
}
</script>
