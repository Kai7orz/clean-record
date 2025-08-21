<template>
  <v-app theme="dark">
    <NuxtLayout>
      <div>
        <div class="polygon-bg">
          <div class="polygon"></div>
          <div class="polygon"></div>
          <div class="polygon"></div>
        </div>
        <v-main class="my-10">
          <NuxtPage />
        </v-main>
      </div>
    </NuxtLayout>
  </v-app>
</template>

<script setup lang="ts">
const alert = (msg: string) => {
  window.alert(msg);
};

</script>

<style>
.v-application {
  background-color: black;
}

  .polygon-bg {
    position: absolute;
    inset: 0;
    overflow: hidden;
    z-index: 0;
  }

  .content {
    position: relative;
    z-index: 1;
    color: white;
  }

  /* ポリゴンアニメーション */
  .polygon {
    position: absolute;
    width: 200px;
    height: 200px;
    background: rgba(0, 150, 255, 0.4);
    clip-path: polygon(50% 0%, 100% 38%, 82% 100%, 18% 100%, 0% 38%);
    animation: float 6s ease-in-out infinite;
    top: 40%;
    left: 20%;
  }

  .polygon:nth-child(2) {
    width: 300px;
    height: 300px;
    background: rgba(255, 0, 150, 0.3);
    animation-duration: 8s;
    animation-delay: -2s;
    top: 10%;
    left: 60%;
  }

  .polygon:nth-child(3) {
    width: 150px;
    height: 150px;
    background: rgba(0, 255, 200, 0.3);
    animation-duration: 10s;
    animation-delay: -4s;
    top: 70%;
    left: 50%;
  }

  @keyframes float {
    0%   { transform: translateY(0) rotate(0deg); }
    50%  { transform: translateY(-50px) rotate(180deg); }
    100% { transform: translateY(0) rotate(360deg); }
  }
</style>