<script setup lang="ts">

    const fileInput = ref<HTMLInputElement | null >(null)
    const responsedUrl = ref<string>("")
    const previewUrl = ref<string>("")

    const getIllustration = async (event: Event) => {
        event.preventDefault();
        const file = fileInput.value?.files?.[0];
        if(!file) return 
        const responsedImageUrl = await useImageUploader(file)

        if(responsedImageUrl["image_url"]){
            responsedUrl.value = responsedImageUrl["image_url"]
        }
    }
    const getPreview = async (event: Event) => {
        event.preventDefault();
        const file = fileInput.value?.files?.[0];
        if(!file) return 
        previewUrl.value = URL.createObjectURL(file);
    }

</script>

<template>
    <div class="flex-row justify-center m-10">
            <v-file-input 
            @change="getPreview" class="max-w-xs" label="File input" ref="fileInput"></v-file-input>
            <v-btn @click="getIllustration" prepend-icon="$vuetify" append-icon="$vuetify" variant="outlined">
                Button
            </v-btn>
    </div>
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
