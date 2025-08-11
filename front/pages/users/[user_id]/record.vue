<script setup lang="ts">
    // 今はuserId を文字列で扱うが，int に変更する
    const baseUrl = "/api/records/record"
    const url = ref("")

    const postData = reactive({
        userId: "",
        categoryId: "",
        recordName: "",
    })

    watch(postData,()=>{
        url.value = baseUrl 
    })

    const onClick = () => {
        useFetch(url,{
            method: 'POST',
            body: postData,
        })
    }
</script>

<template>
    <v-text-field bg-color="grey" v-model="postData.userId">
        user id の指定
    </v-text-field>
    <v-text-field v-model="postData.categoryId">
        category Id の指定
    </v-text-field>
    <v-text-field v-model="postData.recordName">
        record name （自由）
    </v-text-field>
    <v-btn @click="onClick">
        情報送信
    </v-btn>
</template>