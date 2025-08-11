<script setup lang="ts">
    import CardList from "@/containers/CardList.vue";

    const router = useRouter()
    const onClick = ()=>{
        router.push("/uploaders/upload")
    }
</script>

<template>
    <v-sheet>
        <v-btn @click="onClick">
            アップロード画面へ遷移する
        </v-btn>
        <CardList />
    </v-sheet>
</template>