<template>
  <el-config-provider :locale="locale">
    <router-view />
  </el-config-provider>
</template>

<script setup lang="ts">
import zhCn from "element-plus/lib/locale/lang/zh-cn";
import { ref } from "vue";
const locale = ref();
locale.value = zhCn;
</script>

<style lang="scss">
#app {
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
