<script setup lang="ts">
    import { useCardsStore} from '@/stores/cardsStore';
    const props = defineProps<{
        record_id :number
    }>();
    const cardsStore = useCardsStore() 
    const cardInfo = cardsStore.getCardById(props.record_id)
    if(cardInfo===null){
        console.log("card info null")
    }


</script>

<template>
    <ui-card-detail :image=cardInfo />
</template>