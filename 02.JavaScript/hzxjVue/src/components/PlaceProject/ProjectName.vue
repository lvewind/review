<template>
  <p>{{ p_name }}</p>
</template>

<script setup lang="ts">
defineProps<{
  p_name: any;
}>();
</script>

<style scoped></style>
