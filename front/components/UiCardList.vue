<script setup lang="ts"> 
    import UiCard from '@/components/UiCard.vue';
    import { register } from 'swiper/element/bundle';
    import type { Image } from '@/containers/type.ts'
    register();

    // emits でクリックされたときに イベントを発火させる，その際にどのrecord_id かの情報を親の CardList component に対して渡す
    // 親から images という配列を props として受け取る
    
    defineProps<{ images: Image[] | null}>()
    
    const emit = defineEmits<{
        sendRecordId: [number]    
    }>();

    const handleSendRecordId = (record_id: number) => {
        console.log("record_id->",record_id)
        emit('sendRecordId',record_id)
    }

</script>

<template>
    <v-main class="test-design">
        <swiper-container class="flex">
            <swiper-slide v-for="image in images" :key="image.image_id" class="flex justify-center">
                <ui-card 
                    class="m-5"
                    :record_id = image.record_id
                    :image_url = image.image_url
                    :image_description = image.image_description
                    @click-card="handleSendRecordId"
                />
            </swiper-slide>
        </swiper-container>
    </v-main>
</template>

<style>
    .test-design{
        background-color:rgb(0, 0, 0);
        margin: 100px;
    }
</style>