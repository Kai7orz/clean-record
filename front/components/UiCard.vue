<script setup lang="ts">
    const props = defineProps<{
        image_url: string 
        image_description?: string 
    }>()

    console.log("props.image_url ->",props.image_url)
</script>

<template>
    <v-sheet class="d-inline-flex flex-col align-center justify-center gap-1 border-black mt-4 min-w-[300px] rounded-lg bg-grey">
        <img class="w-[300px] rounded-lg mx-10 mt-10":src="props.image_url"/>
        <p>画像の詳細 : {{ props.image_description }}</p>
    </v-sheet>
</template>

<style>

</style>