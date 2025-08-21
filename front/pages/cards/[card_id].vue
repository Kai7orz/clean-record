<script setup lang="ts">
    definePageMeta({
        layout: 'navigator'
    })
    // レコード詳細表示画面の土台
    import CardDetail from '@/containers/CardDetail.vue';
    const route = useRoute()
    const card_id_string = route.params.card_id
    const card_id = Number(card_id_string)
    console.log("card id は",card_id)
    if(isNaN(card_id) || card_id <= 0){
        console.error("Invalid record_id ",card_id_string)
    }
</script>

<template>
    <CardDetail :record_id="card_id"/>
</template>