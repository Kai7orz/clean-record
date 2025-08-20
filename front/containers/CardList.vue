<script setup lang="ts">
    // user に紐づいたイメージ一覧をすべて取得
    import { useCardsStore } from '~/stores/cardsStore';

    const props = defineProps<{
        userId: string
    }>();

    const router = useRouter() 
    // Card 押下時に詳細画面へ遷移する処理
    const handleSendRecordId = (record_id: number) => {
        router.push("/cards/" + record_id)
    }
    // Backend から image_url を取得してリスト化する
    // リスト化した image_url を props として <ui-card-list> に渡す 
    const {data:images,error} = await useFetch('/api/images/getImages',{
        method: 'POST',
        body: {userId: props.userId},
    })
    console.log("data: ",props.userId," をopst")
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
