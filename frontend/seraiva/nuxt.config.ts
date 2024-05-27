export default defineNuxtConfig({
  devtools: { enabled: true },
  typescript: {
    typeCheck: true
  },
  modules: [
    'nuxt-primevue',
    '@sidebase/nuxt-auth',
    '@pinia/nuxt'
  ],
  primevue: {
    components: {
      include: ['Button', 'Avatar', 'InputText', 'FloatLabel', 'Menubar', 'DataTable', 'Checkbox', 'Toast', 'ProgressSpinner', 'Message', 'OverlayPanel']
    }
  },
  css: [
    'primeicons/primeicons.css',
    'primevue/resources/themes/aura-light-green/theme.css',
    'primeflex/primeflex.css',
    '~/assets/global.scss',
  ],
  auth: {
    baseURL: 'http://localhost:8000',
    provider: {
      type: 'local',
      endpoints: {
        signIn: { path: '/token/login', method: 'post' },
        signOut: { path: '/token/logout', method: 'post' },
        getSession: { path: '/usuarios', method: 'get' },
      },
      token: { signInResponseTokenPointer: '/auth_token', type: 'Token' },
      pages: { login: '/' },
      sessionDataType: {
        results: 'Array'
      }
    }
  }
})