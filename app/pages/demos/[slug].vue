<script setup lang="ts">
import demos from '~/data/demos.json'
import { inventory } from '../../../lib/business'
const route = useRoute()
const demo = computed(() => demos.find(item => item.slug === route.params.slug))
if (!demo.value) throw createError({ statusCode: 404, statusMessage: 'Demo not found' })
useHead(() => ({ title: `${demo.value?.title} · The AI Toolkit` }))
const copied = ref(false)
const copyError = ref(false)
async function copyPrompt() {
  try { await navigator.clipboard.writeText(demo.value!.prompt); copied.value = true; copyError.value = false }
  catch { copyError.value = true }
}
const profitRows = [...inventory].sort((a, b) => b.profit - a.profit)
</script>

<template>
  <main v-if="demo" id="main" class="wrap">
    <div class="page-intro"><NuxtLink class="back-link" to="/toolkit#sessions">← All demos</NuxtLink><div class="eyebrow">Demo {{ demo.number }} / {{ demo.category }}</div><h1 class="display gradient-title">{{ demo.title }}</h1><p class="lead">{{ demo.description }}</p><span class="tool-label">{{ demo.tool }}</span><span class="muted text-xs ml-4">{{ demo.time }} EAT</span></div>
    <div class="demo-launch" aria-label="Demo tools">
      <a v-if="demo.download" class="button button-secondary" :href="`/resources/${demo.download}`" download>Download the RFQ PDF ↓</a>
      <NuxtLink v-if="demo.slug === 'calculator'" class="button button-primary" to="/calculator">Try the quote calculator ↗</NuxtLink>
      <a v-if="demo.slug === 'proposal' || demo.slug === 'stock'" class="button button-primary" href="https://chatgpt.com/" target="_blank" rel="noopener noreferrer">Open ChatGPT ↗</a>
      <a v-if="demo.slug === 'research'" class="button button-primary" href="https://notebook.google.com/" target="_blank" rel="noopener noreferrer">Open NotebookLM ↗</a>
    </div>
    <div class="demo-alternatives"><span>Also try</span><span v-for="name in demo.alternatives" :key="name" class="tool-label">{{ name }}</span><NuxtLink :to="`/tools#${demo.toolkitCategory}`" class="text-link">Compare options ↗</NuxtLink></div>
    <div class="demo-detail">
      <div><div class="prompt-area"><div class="prompt-toolbar"><span>Your copy-and-paste prompt</span><button class="copy-button" aria-live="polite" @click="copyPrompt">{{ copied ? 'Copied ✓' : 'Copy prompt' }}</button></div><pre class="prompt-text" tabindex="0">{{ demo.prompt }}</pre></div><p v-if="copyError" role="status" class="fine-print">Clipboard access is unavailable. Select the prompt text and copy it manually.</p>
        <NuxtLink :to="`/rehearsal#${demo.slug}`" class="text-link">Rehearsal script & fallback ↗</NuxtLink><h2 class="detail-heading">One useful follow-up</h2><div class="followup">{{ demo.followup }}</div>
        <details><summary>The checks to make before using the result</summary><p v-for="check in demo.checks" :key="check">{{ check }}</p>
          <div v-if="demo.slug === 'stock'" class="stock-chart" aria-label="Gross profit by product"><div v-for="row in profitRows" :key="row.name" class="stock-chart-row"><span>{{ row.name }}</span><div class="chart-bar" :style="{ width: `${row.profit / 9100 * 100}%` }" /><b>{{ row.profit.toLocaleString() }}</b></div><p>Gross profit in KES from fictional 30-day data.</p></div>
        </details>
      </div>
      <aside><div class="aside-block"><h2>The problem</h2><p>{{ demo.problem }}</p></div><div class="aside-block"><h2>The AI opportunity</h2><p>{{ demo.opportunity }}</p></div><div class="aside-block"><h2>Your first step</h2><p>{{ demo.firstStep }}</p></div><p class="fine-print">Workshop data is fictional. Review generated work before using it in your business.</p></aside>
    </div>
  </main>
</template>
