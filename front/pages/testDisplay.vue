<script setup lang="ts">
    import CardList from "@/containers/CardList.vue"
    const testuser_id = ref("1")
</script>

<template>
    <CardList :userId="testuser_id"/>
</template>

<style>
    .my-box{
        background-color:red;
        clip-path: polygon(0 0, 100% 100%, 50% 80%, 0 100%);
    }
</style>