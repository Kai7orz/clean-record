<script setup lang="ts">

import { useRoute } from 'vue-router';
import { useUserStore } from '~/stores/userStore'
    const route = useRoute()
    const { data } = useFetch("/api/users")
    const userStore = useUserStore()
    userStore.setUserInformation(1,"kaito")

</script>

<template>
    <div>
        <p> これはユーザー{{ userStore.userId }} レコード {{ userStore.userName }}のためのページです </p>
        user information : {{data}}
    </div>
</template>