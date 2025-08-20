import { ref } from 'vue';
import { defineStore } from 'pinia';

type Image = {
        record_id: number 
        image_id: number 
        image_url: string 
        image_description: string 
    }

export const useCardsStore = defineStore('cards', () => {
    // 状態の初期定義: card: image_url,image_description を保持したい
    // card & cards(list) の set 
    // return 
    // ※ cards だけ保持して，id でフィルターかければcard はとりだせるが，list が大きくなると検索時間O(n) かかるので注意
    
    const cardList = ref<Image[] | null>(null);

    function setCardList(imageObjects: Image[]){
        cardList.value = imageObjects
    }

    function getCardById(id:number): Image | null {
        const targetCard = cardList.value?.find((card:Image) => card.record_id === id) ?? null
        return targetCard
    }

    return { cardList,setCardList,getCardById}

})