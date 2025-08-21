<script setup lang="ts">
    // DB から画像関連取得処理
    // props で渡してもいい気がするが他で利用できなくなる？ null なら DB からたたく処理入れた方がスムーズかな
    // records から category 取得する必要がある
    // CardDetail　の利用想定は，一覧からpush した時だから基本的には props で渡せそうな気がする．
    // props 渡し方困るかも router に対してprops 渡さないといけない？？　store で管理させるか

    //　現状の カード詳細画面の実装としては　
        // image, category をそれぞれ毎回DB からたたいて表示する
        // image をcardlistから props or store で管理して，受け取って表示する
        // pinia で 一覧表示で取得したimage_url を管理しておく（props でrouter経由が手間に感じたから＋一覧表示画面は頻繁アクセスしそうだからキャッシュが効いていい） 
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