<script setup lang="ts">
    const baseUrl = "/api/categories"
    const categoryName = ref("");
    const postData = reactive({
        categoryName: "",
    })

    const onClick = () => {
        useFetch(baseUrl,{
            method:'POST',
            body: postData,
        })
    }
</script>

<template>
    <v-sheet>
        <v-text-field v-model="postData.categoryName">
            カテゴリー名：
        </v-text-field>
        <v-btn @click="onClick">
            send
        </v-btn>
    </v-sheet>    
</template>