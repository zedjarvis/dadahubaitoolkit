<script setup lang="ts">
import jobs from '~/data/jobs.json'
import tools from '~/data/tools.json'
useHead({ title: 'Find a tool for the job · The AI Toolkit' })
const query = ref('')
const category = ref('All tasks')
const categories = ['All tasks', ...new Set(jobs.map(job => job.category))]
const filtered = computed(() => jobs.filter(job => (category.value === 'All tasks' || job.category === category.value) && JSON.stringify(job).toLowerCase().includes(query.value.toLowerCase().trim())))
const tool = (name: string) => tools.find(item => item.name === name)
const copied = ref('')
const copyError = ref(false)
async function copy(id: string, prompt: string) { try { await navigator.clipboard.writeText(prompt); copied.value = id; copyError.value = false } catch { copyError.value = true } }
</script>
<template>
<main id="main" class="wrap directory">
  <div class="page-intro"><NuxtLink to="/toolkit" class="back-link">← Back to the toolkit</NuxtLink><p class="eyebrow">Beyond today’s demos</p><h1 class="display gradient-title">Start with the job.</h1><p class="lead">{{ jobs.length }} everyday tasks. {{ tools.length }} tools to consider. Choose one that fits the work and the tools you already use.</p></div>
  <details class="directory-note"><summary>How this list was chosen · checked 31 Oct 2026</summary><p>Task fit, useful outputs, setup effort and the ability to check the work. Recommendations are our editorial judgment, based on the linked first-party documentation—not a performance ranking. Only the session tools are rehearsed here.</p><p>Sources checked 31 October 2026. Features, pricing, language support and account access change. Check the current plan before paying. Compare subscription, usage, hosting and setup costs—not just the headline price.</p></details>
  <form class="tool-filters" @submit.prevent><label>Find a task or tool<input v-model="query" type="search" placeholder="Try invoices, marketing, Claude…" /></label><label>Filter by work<select v-model="category"><option v-for="item in categories" :key="item">{{ item }}</option></select></label></form>
  <p class="result-count" role="status">{{ filtered.length }} {{ filtered.length === 1 ? 'task' : 'tasks' }} shown</p>
  <div class="job-grid">
    <article v-for="job in filtered" :id="job.id" :key="job.id" class="job-card">
      <p class="eyebrow">{{ job.category }}</p><h2>{{ job.title }}</h2><p class="job-outcome">{{ job.outcome }}</p><p><b>Where I’d start:</b> {{ job.recommendation }}</p>
      <ul class="tool-options"><li v-for="option in job.options" :key="option[0]"><a :href="tool(option[0]!)?.url" target="_blank" rel="noopener noreferrer">{{ option[0] }} ↗</a><span>{{ option[1] }}</span></li></ul>
      <details><summary>Starter prompt, setup & sources</summary><div class="prompt-toolbar"><span>Adapt this to your business</span><button class="copy-button" @click="copy(job.id, job.prompt)">{{ copied === job.id ? 'Copied ✓' : 'Copy prompt' }}</button></div><pre class="prompt-text">{{ job.prompt }}</pre><div v-for="option in job.options" :key="option[0]" class="source-entry"><b>{{ option[0] }}</b><p>{{ tool(option[0]!)?.access }}</p><a :href="tool(option[0]!)?.source" target="_blank" rel="noopener noreferrer">Official documentation ↗</a></div></details>
      <p class="job-check"><b>Before using the result</b><br />{{ job.check }}</p>
    </article>
  </div><p v-if="!filtered.length" class="empty-state">No match yet. Try “sales”, “documents” or a tool name. <button class="copy-button" @click="query = ''; category = 'All tasks'">Show all tasks</button></p><p v-if="copyError" role="status">Clipboard access is unavailable. Select and copy the visible prompt.</p>
  <section class="brief-panel"><div><p class="eyebrow">A sensible first experiment</p><h2 class="display">One task.<br />One useful result.</h2></div><div><p>Use information you are authorised to share. Try the same small task in a tool you already have. Compare accuracy, edits needed, time and cost before adding another subscription.</p><NuxtLink class="button button-secondary" to="/workflow">Map your first workflow ↗</NuxtLink></div></section>
</main>
</template>
