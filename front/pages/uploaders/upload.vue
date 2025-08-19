<script setup lang="ts">

    const url = "/api/records/record"
    const fileInput = ref<HTMLInputElement | null >(null)
    const responsedUrl = ref<string>("")
    const previewUrl = ref<string>("")

    const postData = reactive({
        userId: "",
        categoryId: "",
        recordName: "",
        imageUrl: "",
        imageDescription: "",
    })
    
    const getIllustration = async (event: Event) => {
        event.preventDefault();
        const file = fileInput.value?.files?.[0];
        if(!file) return 
        const responsedImageUrl = await useImageUploader(file)

        if(responsedImageUrl["image_url"]){
            responsedUrl.value = responsedImageUrl["image_url"]
            postData.imageUrl = responsedUrl.value
            console.log("イラストURL :",postData.imageUrl)
        }
    }

    const getPreview = async (event: Event) => {
        event.preventDefault();
        const file = fileInput.value?.files?.[0];
        if(!file) return 
        previewUrl.value = URL.createObjectURL(file);
    }

    const createNewRecord = () => {
        if(postData.imageUrl == ""){
            console.log("Image is Empty")
            return 
        }
        useFetch(url,{
            method: 'POST',
            body: postData,
        })
    }
</script>

<template>
    <v-sheet class="flex-row justify-center m-10 p-2">
            <v-file-input 
              class="max-w-xs m-5 p-3" 
              label="Select Image to Illustrate" 
              ref="fileInput"
              @change="getPreview" >
            </v-file-input>
            <v-text-field
              class="w-1/3 m-5"
              v-model="postData.imageUrl"
              label="イラストURL手動入力">
            </v-text-field>
            <v-btn  
              class="m-5"
              prepend-icon="$vuetify" 
              append-icon="$vuetify" 
              variant="outlined"
              @click="getIllustration" >
                イラスト生成
            </v-btn>
            <v-btn 
              class="m-5" 
              prepend-icon="$vuetify" 
              append-icon="$vuetify" 
              variant="outlined"
              @click="createNewRecord" >
                画像の保存
            </v-btn>
    </v-sheet>

    <v-sheet class="flex justify-center">
        <!-- プレビュー画像-->
        <div v-if='previewUrl!=""' class=" w-1/3 flex flex-col flex-wrap md:flex-row md:justify-center m-10">
            <UiImageCard :image_url=previewUrl>
                <template #title>
                </template>
            </UiImageCard>
        </div>
        <!-- レスポンス -->
        <div v-if='responsedUrl!="" ' class="w-1/3 flex flex-col flex-wrap md:flex-row md:justify-center m-10">
            <UiImageCard :image_url=responsedUrl>
                <template #title>
                    <h1> カード名 </h1>
                </template>
            </UiImageCard>
        </div>
    </v-sheet>

    <v-sheet class="flex-row justify-center m-10 p-2">
        <v-text-field 
          class="w-1/3" 
          v-model="postData.userId"
          label="user id の設定">
        </v-text-field>
        <v-text-field 
          class="w-1/3" 
          v-model="postData.categoryId"
          label="category id の設定">
        </v-text-field>
        <v-text-field 
          class="w-1/3" 
          v-model="postData.recordName"
          label="record name の設定">
        </v-text-field>
        <v-text-field 
          class="w-1/3"
          label="image の説明">
        </v-text-field>
    </v-sheet>

</template>
