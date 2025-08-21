<script setup lang="ts">
    import { useUserStore } from '~/stores/userStore';

    const router = useRouter()
    const userStore = useUserStore()
    const userIdString = ref("")
    const userId = ref(0)
    const userName = ref("")

    const selectUser = () => {
        userStore.setUserInformation(userId.value,userName.value)
        router.push("/users/"+String(userId.value)+"/records")
    }
    
    watch(userIdString,()=>{
        userId.value = Number(userIdString.value)
        if(!userId.value || userId.value <= 0){
            console.log("Invalid Number or Not Number Error")
        }
    }
    )
</script>

<template>
    <v-container>
        <v-text-field v-model="userIdString" label="ユーザー選択 user id"/>    
        <v-text-field v-model="userName" label="ユーザー名"/>
        <v-btn @click="selectUser">Select</v-btn>
    </v-container>
</template>