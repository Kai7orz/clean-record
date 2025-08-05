<script setup lang="ts">
// Backend から image_url を取得してリスト化する
// リスト化した image_url を props として <ui-card-list> に渡す 
const {data:images,error} = await useFetch('/api/images/getImages')

</script>

<template>
    <ui-card-list :images="images"/>
</template>