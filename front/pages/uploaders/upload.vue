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
    <div class="flex-row justify-center m-10">
            <v-file-input 
            @change="getPreview" class="max-w-xs" label="File input" ref="fileInput"></v-file-input>
            <v-btn @click="getIllustration" prepend-icon="$vuetify" append-icon="$vuetify" variant="outlined">
                イラスト生成
            </v-btn>
            <v-btn @click="createNewRecord">
                画像の保存
            </v-btn>
    </div>
    <v-sheet>
        <v-text-field bg-color="grey" v-model="postData.userId">
            user id の設定
        </v-text-field>
        <v-text-field bg-color="grey" v-model="postData.categoryId">
            category id の設定
        </v-text-field>
        <v-text-field bg-color="grey" v-model="postData.recordName">
            record name の設定
        </v-text-field>
        <v-text-field>
            image　の説明
        </v-text-field>
    </v-sheet>

    <v-sheet>
        <v-text-field v-model="postData.imageUrl">
            イラストの手動入力
        </v-text-field>
    </v-sheet>

    <!-- プレビュー画像 と レスポンスが像が欲しい -->
    <div class="flex justify-center">
        <!-- プレビュー画像-->
        <div v-if='previewUrl!=""' class=" w-1/3 flex flex-col flex-wrap md:flex-row md:justify-center m-10 ">
            <UiImageCard :image_url=previewUrl>
                <template #title>

                </template>
            </UiImageCard>
        </div>
    <!-- レスポンス -->
        <div v-if='responsedUrl!="" ' class="w-1/3 flex flex-col flex-wrap md:flex-row md:justify-center m-10 ">
            <UiImageCard :image_url=responsedUrl>
                <template #title>
                    <h1> カード名 </h1>
                </template>
            </UiImageCard>
        </div>
    </div>  
</template>
