<script setup lang="ts">
import { useUserStore } from "~/stores/userStore";

const userStore = useUserStore()
// router を用意して遷移画面ごとの url を用意する
// button で遷移ボタン用意, @click 時に遷移動作を記述
const drawer = ref(false)
const borderColor = "sm"
const router = useRouter()

const clickMenu = () => {
    router.push("/users/"+userStore.userId+"/records")
}

const clickRegisterUser = () => {
    router.push("/users/register")
}

const clickSelectUser = () => {
    router.push("/users/select")
}

const clickUpload = () => {
    router.push("/uploaders/upload")
}



</script>

<template>
    <v-app-bar app color="light-blue-darken-1" dark>
        <v-app-bar-nav-icon @click="drawer = !drawer" />
        <v-toolbar-title>CLEAN UP</v-toolbar-title>
        <v-btn icon>
            <v-icon>mdi-account</v-icon>
        </v-btn>
    </v-app-bar>
    <v-navigation-drawer 
      v-model="drawer">
      <v-list>
        <v-list-item @click="clickMenu" :border="borderColor">
          <v-list-item-title>Menu</v-list-item-title>
        </v-list-item>
        <v-list-item @click="clickRegisterUser" :border="borderColor">
          <v-list-item-title>Register User</v-list-item-title>
        </v-list-item>
        <v-list-item @click="clickSelectUser" :border="borderColor">
            <v-list-item-title>Select User</v-list-item-title>
        </v-list-item>
        <v-list-item @click="clickUpload" :border="borderColor">
          <v-list-item-title>Upload</v-list-item-title>
        </v-list-item>
      </v-list>      
      </v-navigation-drawer>
</template>