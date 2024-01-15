<template>
  <p>{{ d_name }}</p>
</template>

<script setup lang="ts">
defineProps<{
  d_name: string;
}>();
</script>

<style scoped></style>
