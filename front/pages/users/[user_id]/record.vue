<script setup lang="ts">
    // レコード設定にimage オブジェクトを追加する
    // image_url + image_description の追加をすればよさそう
    const baseUrl = "/api/records/record"
    const url = ref("")

    const postData = reactive({
        userId: "",
        categoryId: "",
        recordName: "",
        imageUrl:"",
        imageDescription:"",
    })

    watch(postData,()=>{
        url.value = baseUrl 
    })

    const onClick = () => {
        $fetch(url.value,{
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
    <v-text-field v-model="postData.imageUrl">
        image_url: の指定
    </v-text-field>
    <v-text-field v-model="postData.imageDescription">
        image_description: の指定
    </v-text-field>
    <v-btn @click="onClick">
        情報送信
    </v-btn>
</template>