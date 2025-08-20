<script setup lang="ts">
    const props = defineProps<{
        record_id: number
        image_url: string 
        image_description?: string 
    }>()

    const emit = defineEmits<{
        clickCard: [number]
    }>()
    const clicked = (record_id:number) => {
        emit('clickCard',record_id)
    }

</script>

<template>
    <v-sheet @click="()=> clicked(props.record_id)" class="d-inline-flex flex-col align-center justify-center gap-1 border-black mt-4 min-w-[300px] rounded-lg bg-grey">
        <img class="w-[300px] rounded-lg mx-10 mt-10":src="props.image_url"/>
        <p>画像の詳細 : {{ props.image_description }}</p>
    </v-sheet>
</template>

<style>

</style>