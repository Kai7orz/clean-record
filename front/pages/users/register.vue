<script setup lang="ts">
    const baseUrl = "/api/users/register"
    const postData = reactive({ userName:"", userEmail:"",ageString:""})
    const resetField = () => {
        postData.userName = ""
        postData.userEmail = "" 
        postData.ageString = ""
    }

    const onClick = () => {
        console.log("forms sent")
        $fetch(baseUrl,{
            method: 'POST',
            body: postData
        })

        resetField()
    }
</script>

<template>
    <v-container class="flex flex-col justify-center align-items-center text-center">
            <v-sheet>
            <v-text-field class="mx-auto m-3 w-25" label="ユーザー名" bg-color="grey" :rounded=10 v-model="postData.userName">
            </v-text-field>
            <v-text-field class="mx-auto m-3 w-25" label="Email" bg-color="grey" :rounded=10 v-model="postData.userEmail">
            </v-text-field>
            <v-text-field class="mx-auto  w-25" label="年齢" bg-color="grey" :rounded=10 v-model="postData.ageString">
            </v-text-field>
            <v-btn class="m-3 w-25" @click="onClick">send</v-btn>
        </v-sheet>
</v-container>
</template>