import  { ref } from 'vue';
import { defineStore } from 'pinia';

export const useUserStore = defineStore('user',() => {
    const userId = ref(0)
    const userName = ref('')

    function setUserInformation(id:number,name:string){
        userId.value = id
        userName.value = name 
    }

    return { userId,userName,setUserInformation}
})