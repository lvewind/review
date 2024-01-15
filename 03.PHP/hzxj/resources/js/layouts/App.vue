<template>
    <el-config-provider :locale="locale">
    <el-link>{{ form_obj }}</el-link>
        <router-view />
    </el-config-provider>
</template>

<script setup>
import {onMounted, ref} from "vue";
import axios from 'axios'
import zhCn from "element-plus/lib/locale/lang/zh-cn";


const locale = ref();
locale.value = zhCn;

const form_obj = ref();

onMounted(() => {
    const form_id = window.location.href.split('/').pop();
    axios.get('http://hzxj.test/api/v1/get-form/' + form_id.toString())
        .then(function (response) {
            form_obj.value = response.data
        });
});

</script>
