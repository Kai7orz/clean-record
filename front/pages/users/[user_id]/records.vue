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
        <v-btn class="m-10 gap-5" @click="onClick">
            アップロード画面へ
        </v-btn>
        <CardList :user-id="userId[0]"/>
</template>