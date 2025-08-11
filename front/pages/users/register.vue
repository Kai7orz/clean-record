<script setup lang="ts">
    const baseUrl = "/api/users/register"
    const postData = reactive({ userName:"", userEmail:"",ageString:""})
    
    const onClick = () => {
        console.log("forms sent")
        useFetch(baseUrl,{
            method: 'POST',
            body: postData
        })
    }
</script>

<template>
    <v-text-field class="m-3 w-25" bg-color="grey" :rounded=10 v-model="postData.userName">
            ユーザー名:
    </v-text-field>
     <v-text-field class="m-3 w-25" bg-color="grey" :rounded=10 v-model="postData.userEmail">
            Email:
    </v-text-field>
    <v-text-field class="m-3 w-25" bg-color="grey" :rounded=10 v-model="postData.ageString">
            年齢:
    </v-text-field>

    <v-btn @click="onClick">send</v-btn>
</template>