<script setup lang="ts">

    import { useCardsStore } from '~/stores/cardsStore';
    import type { Image } from '@/containers/type.ts';

    const router = useRouter() 
    const handleSendRecordId = (record_id: number) => {
        router.push("/cards/" + record_id)
    }
    // Backend から image_url を取得してリスト化する
    // リスト化した image_url を props として <ui-card-list> に渡す 
    const {data:images,error} = await useFetch('/api/images/getImages')
    const cardsStore = useCardsStore() 
    // watch にはリアクティブなオブジェクトでいいが，console などには .value アクセスをわすれずに   
    watch(images,(newImages) => {
        if(newImages){
            cardsStore.setCardList(newImages)
        }
    },{immediate:true})

</script>

<template>
    <ui-card-list :images="images" @send-record-id="handleSendRecordId"/>
</template>
