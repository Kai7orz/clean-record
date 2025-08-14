<script setup lang="ts">
    import CardList from "@/containers/CardList.vue";

    const route = useRoute()
    const router = useRouter()
    const onClick = ()=>{
        router.push("/uploaders/upload")
    }
    const userId = route.params.user_id
</script>

<template>
    <v-sheet>
        <v-btn @click="onClick">
            アップロード画面へ遷移する
        </v-btn>
        <CardList :user-id="userId[0]"/>
    </v-sheet>
</template>