import { defineConfig } from 'unocss'

// Unicorn 1.1.2 was authored with Windi CSS. These shortcuts preserve its
// original typography/background in current Slidev's UnoCSS environment.
export default defineConfig({
  shortcuts: {
    'bg-main': 'bg-gradient-to-r from-white to-purple-50 text-gray-900',
    'font-title': 'font-[Gilroy_Bold]',
  },
  theme: { fontFamily: { title: '"Gilroy Bold", sans-serif' } },
})
