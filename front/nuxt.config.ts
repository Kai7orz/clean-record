import vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'

export default defineNuxtConfig({

  compatibilityDate: '2025-05-15',
  // モジュールに Vuetify Vite プラグインを追加
  modules: [
    "@nuxt/image",
    "@uploadthing/nuxt",
    "@nuxtjs/tailwindcss",
    "@pinia/nuxt",
    "nuxt-swiper",

  ],

  // Vuetify 用に必要な Vite 設定
  vite: {
    vue: {
      template: {
        transformAssetUrls,
      },
    },
    plugins: [
      vuetify({autoImport: true})
    ]
  },

  // Vuetify のためのビルド設定
  build: {
    transpile: ['vuetify'],
  },
})
