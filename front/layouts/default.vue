<template>
 <div>
  <HeaderSection /> 
  <div class="main-contents">
   <nuxt />
  </div>
  <FooterSection />
 </div>
</template>

<script>
import HeaderSection from "~/components/Header.vue";
import FooterSection from "~/components/Footer.vue";
</script>