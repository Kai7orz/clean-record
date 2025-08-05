<script setup lang="ts">
import {ref} from 'vue';
import { onMounted } from 'vue';
import Card from '@/components/Card.vue';


const alert = (msg: string) => {
  window.alert(msg);
};

const blobObjectUrls = ref<string[]>([]);

// 画像を取得し配列に保存する処理
onMounted(async () => {
  try {
   const res = await fetch('/api/proxy', { method: 'POST' });

    console.log("Fetch status:", res.status);

    if (res.ok) {
      const blob = await res.blob();
      const objectUrl = URL.createObjectURL(blob);
      blobObjectUrls.value.push(objectUrl);
      blobObjectUrls.value.push(objectUrl);
    } else {
      console.error("Response not OK:", res.status);
    }
  } catch (err) {
    console.error("Fetch failed:", err);
  }
});
</script>

<template>
  <div class="h-screen w-full bg-gradient-to-br from-violet-300 via-pink-200 to-orange-100">
    <div class="flex justify-center">
      <div v-for="blobObjectUrl in blobObjectUrls" class="m-10">
        <Card :image_url="blobObjectUrl" />
      </div>   
    </div>
  </div>
</template>

