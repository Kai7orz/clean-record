<script setup lang="ts"> 
    import UiCard from '@/components/UiCard.vue';
    import { register } from 'swiper/element/bundle';
    register();
    // 親から images という配列を props として受け取る
    type Image = {
        record_id:number, 
        image_id:number,
        image_url:string,
        image_description:string
    }
    const props = defineProps<{ images: Image[] | null}>()

</script>

<template>
    <v-main class="test-design">
        <swiper-container class="flex">
            <swiper-slide class="flex justify-center" v-for="image in images">
                <ui-card 
                    class="m-5"
                    :image_url = image.image_url
                    :image_description = image.image_description
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