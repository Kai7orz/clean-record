<template>
    <div id="app>
    <div class="preview_zone">
        <img src="" alt="プレビューが表示">
        <img :src="url" alt="ここにプレビューが表示">
    </div>
    <div class="upload_zone">
        <input type="file" class="input_fils
        <input type="file" class="input_file" ref="preview" @change="previewImage">
        <div class="drop_zone"> 
        ここにファイルをドラッグ & ドロップ
        </div>
    </div>
</template> 

<script>
  const app = new Vue