<script setup lang="ts">
    import type { Image } from '@/containers/type.ts'

    const props = defineProps<{
        image:Image | null        
    }>();
</script>

<template>
    <div>
        <p>ストアテストの画像</p>
        <img v-if="props.image?.image_url!=undefined" :src=props.image?.image_url > 
        <div v-else>cannot read image...</div>
    </div>
</template>