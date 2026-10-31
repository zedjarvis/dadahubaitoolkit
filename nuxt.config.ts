import tailwindcss from '@tailwindcss/vite'

export default defineNuxtConfig({
  compatibilityDate: '2026-10-31',
  devtools: { enabled: false },
  routeRules: {
    '/resources/03-fictional-cleaning-rfq.pdf': { redirect: { to: '/resources/03-cleaning-rfq.pdf', statusCode: 301 } },
  },
  css: ['~/assets/css/main.css'],
  vite: { plugins: [tailwindcss()] },
  app: {
    head: {
      title: 'The AI Toolkit · DADA HUB',
      htmlAttrs: { lang: 'en' },
      meta: [{ name: 'description', content: 'Your practical AI session companion. Prompts, source material and live demos with Cedrouseroll Omondi at DADA HUB.' }],
      link: [{ rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }],
    },
  },
})
