<template>
  <el-calendar class="ri_li" ref="eeeeee">
    <template #date-cell="{ data }">
      <router-link
        v-if="upload"
        :to="{ name: 'upload_files', query: { day: data.day } }"
        class="r_link"
      >
        <p :class="data.isSelected ? 'is-selected' : ''">
          {{ data.day.split("-").slice(2).join("-") }}
        </p>
        <div style="width: 100%" v-for="(item,index) in scheduleData" :key="index">
          <el-tag class="tag" type="danger" v-if="item.date === data.day && item.views != 0">
            {{ item.views }}
            份文件
          </el-tag>
        </div>
      </router-link>

      <router-link
        v-else
        :to="{ name: 'read', query: { day: data.day } }"
        class="r_link"
      >
        <p :class="data.isSelected ? 'is-selected' : ''">
          {{ data.day.split("-").slice(2).join("-") }}
        </p>
        <div style="width: 100%" v-for="(item,index) in scheduleData" :key="index">
          <el-tag class="tag" type="danger" v-if="item.date === data.day && item.views != 0">
            {{ item.views }}
            份文件
          </el-tag>
        </div>
      </router-link>
    </template>
  </el-calendar>
</template>

<script setup lang="ts">
// import { useRouter } from "vue-router";
// const router = useRouter();
import {onMounted, ref} from "vue";
import axios from "axios";
const eeeeee = ref();

const scheduleData = ref([
  {
    views: 0,
    date:'0',
  }

]);
onMounted(() => console.log(eeeeee.value))
const url = window.location.href;
let upload = false;
if (url.search("upload") >= 0) {
  upload = true;
}
axios({
  baseURL: "http://eo.eihotel.com.cn",
  url: "api/getsList",
  method: "get",
}).then(function (response) {
  scheduleData.value = response.data.scheduleData;
});
</script>

<style>
.is-selected {
  color: #1989fa;
}

.r_link {
  text-decoration: inherit;
  color: inherit;
  display: inline-block;
  width: 100%;
}

.ri_li {
}
.tag {
  width: 100%;
  font-size: 13px;
  font-weight: bold;
}
</style>
