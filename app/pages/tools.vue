<script setup lang="ts">
import jobs from '~/data/jobs.json'
import tools from '~/data/tools.json'
import { createDirectorySearch } from '../../lib/tool-search'

useHead({ title: 'Find a tool for the job · The AI Toolkit' })
const query = ref('')
const category = ref('All tasks')
const view = ref<'needs' | 'tools'>('needs')
const categories = ['All tasks', ...new Set(jobs.map(job => job.category))]
const tool = (name: string) => tools.find(item => item.name === name)!
const relatedJobs = (name: string) => jobs.filter(job => job.options.some(option => option[0] === name))
const searchJobs = createDirectorySearch(jobs.map(job => ({
  item: job, title: job.title, keywords: job.keywords, category: job.category,
  names: job.options.map(option => option[0]!),
  description: [job.outcome, job.recommendation, job.workflow.trigger, job.workflow.inputs].join(' '),
})))
const searchTools = createDirectorySearch(tools.map(item => ({
  item, title: item.name, keywords: item.keywords, category: item.kind,
  names: relatedJobs(item.name).map(job => job.title),
  description: [item.capability, item.fit, ...relatedJobs(item.name).map(job => job.keywords)].join(' '),
})))
const filteredJobs = computed(() => searchJobs(query.value).filter(job => category.value === 'All tasks' || job.category === category.value))
const filteredTools = computed(() => searchTools(query.value).filter(item => category.value === 'All tasks' || relatedJobs(item.name).some(job => job.category === category.value)))
const count = computed(() => view.value === 'needs' ? filteredJobs.value.length : filteredTools.value.length)
function reset() { query.value = ''; category.value = 'All tasks' }
function showJob(id: string) { reset(); view.value = 'needs'; nextTick(() => document.getElementById(id)?.scrollIntoView({ behavior: 'auto', block: 'start' })) }
function showToolJobs(name: string) { reset(); query.value = name; view.value = 'needs'; nextTick(() => document.getElementById('directory-results')?.scrollIntoView({ block: 'start' })) }
function routine(job: typeof jobs[number]) {
  const w = job.workflow
  return `${job.title.toUpperCase()}\nWhen: ${w.trigger}\nBring: ${w.inputs}\n\n${w.steps.map((step, i) => `${i + 1}. ${step}`).join('\n')}\n4. Save and use again: ${w.save}\n\nPerson responsible: ${w.owner}\nMeasure: ${w.measure}\nBefore using the result: ${job.check}\n\nSAVED PROMPT\n${job.prompt}`
}
</script>

<template>
  <main id="main" class="wrap directory">
    <div class="page-intro">
      <NuxtLink to="/toolkit" class="back-link">← Back to the toolkit</NuxtLink>
      <p class="eyebrow">Beyond today’s demos</p><h1 class="display gradient-title">Start with the job.</h1>
      <p class="lead">{{ jobs.length }} everyday tasks. {{ tools.length }} tools to consider. Find what each does well, choose a fit for your business, and leave with a routine you can use again.</p>
      <a class="text-link" href="/resources/10-tools-by-task.pdf" download>Keep the tools & workflow guide (PDF) ↓</a>
    </div>
    <div class="directory-path" aria-label="How to use this directory">
      <p><span>01 / Find</span>Start with the work you need done.</p>
      <p><span>02 / Choose</span>Compare the output, setup and fit.</p>
      <p><span>03 / Repeat</span>Save the routine. Name its owner.</p>
    </div>
    <details class="directory-note"><summary>How to choose · sources checked 31 Oct 2026</summary>
      <p>Start with the tool you already have. Compare one small task: does it produce the right output, can you check it, and will the person doing the work actually use it?</p>
      <p>These are practical fit recommendations based on official product sources, not benchmark rankings. Product capabilities come from the linked documentation; the starter routines are our suggested ways to use them. Only the session tools have been rehearsed here.</p>
      <p>Check the specific plan, supported languages, account permissions and total cost before paying. A saved prompt, a reusable tool and a connected automation need different amounts of setup.</p>
    </details>
    <div class="directory-controls">
      <div class="directory-switch" role="group" aria-label="Browse the directory">
        <button type="button" :aria-pressed="view === 'needs'" @click="view = 'needs'">By business need <span>{{ jobs.length }}</span></button>
        <button type="button" :aria-pressed="view === 'tools'" @click="view = 'tools'">By tool <span>{{ tools.length }}</span></button>
      </div>
      <form class="tool-filters" @submit.prevent>
        <label>Find a task or tool<input v-model="query" type="search" placeholder="Try marketing, invoices, NotebookLM…" aria-describedby="search-help" /></label>
        <label>Filter by work<select v-model="category"><option v-for="item in categories" :key="item">{{ item }}</option></select></label>
      </form>
      <p id="search-help" class="section-note">Search by job, tool or everyday words. Small spelling mistakes are okay.</p>
      <div class="search-suggestions" aria-label="Search ideas"><span>Try</span><button v-for="term in ['Marketing', 'Invoices', 'Sales follow-ups', 'Staff training']" :key="term" type="button" @click="query = term">{{ term }}</button></div>
      <div id="directory-results" class="directory-results"><p class="result-count" role="status" aria-live="polite">{{ count }} {{ view === 'needs' ? (count === 1 ? 'task' : 'tasks') : (count === 1 ? 'tool' : 'tools') }} shown<span v-if="query.trim()"> · closest matches first</span></p><button v-if="query || category !== 'All tasks'" class="copy-button" type="button" @click="reset">Clear search & filter</button></div>
    </div>
    <div v-if="view === 'needs'" class="job-grid">
      <article v-for="job in filteredJobs" :id="job.id" :key="job.id" class="job-card">
        <p class="eyebrow">{{ job.category }}</p><h2>{{ job.title }}</h2><p class="job-outcome">{{ job.outcome }}</p><p><b>Where I’d start:</b> {{ job.recommendation }}</p>
        <ul class="tool-options"><li v-for="option in job.options" :key="option[0]"><a :href="tool(option[0]!).url" target="_blank" rel="noopener noreferrer">{{ option[0] }} ↗</a><span>{{ option[1] }}</span></li></ul>
        <details class="job-routine"><summary>Put it into your workflow</summary>
          <p><b>When:</b> {{ job.workflow.trigger }}</p><p><b>Have ready:</b> {{ job.workflow.inputs }}</p>
          <ol><li v-for="step in job.workflow.steps" :key="step">{{ step }}</li><li><b>Save and use again.</b> {{ job.workflow.save }}</li></ol>
          <p><b>Person responsible:</b> {{ job.workflow.owner }}</p><p><b>How you’ll know it helps:</b> {{ job.workflow.measure }}</p>
          <details class="save-routine"><summary>Copy this routine into your own notes</summary><DemoPrompt :text="routine(job)" :label="job.title + ' routine'" /></details>
        </details>
        <details><summary>Starter prompt, setup & sources</summary><DemoPrompt :text="job.prompt" :label="job.title + ' prompt'" /><div v-for="option in job.options" :key="option[0]" class="source-entry"><b>{{ option[0] }}</b><p>{{ tool(option[0]!).access }}</p><a :href="tool(option[0]!).source" target="_blank" rel="noopener noreferrer">Official documentation ↗</a></div></details>
        <p class="job-check"><b>Before using the result</b><br />{{ job.check }}</p>
      </article>
    </div>
    <div v-else class="job-grid">
      <article v-for="item in filteredTools" :key="item.name" class="job-card tool-profile">
        <p class="eyebrow">{{ item.kind }}</p><h2>{{ item.name }}</h2><p class="job-outcome">{{ item.capability }}</p>
        <p><b>A good fit when</b><br />{{ item.fit }}</p><p><b>Try it first with</b><br />{{ item.firstStep }}</p>
        <p class="tool-setup"><b>What you’ll need</b><br />{{ item.access }}</p>
        <div class="tool-job-links"><p>See it in a business workflow</p><button v-for="job in relatedJobs(item.name).slice(0, 4)" :key="job.id" class="tool-job-link" type="button" @click="showJob(job.id)">{{ job.title }} ↗</button><button v-if="relatedJobs(item.name).length > 4" class="tool-job-link" type="button" @click="showToolJobs(item.name)">See all {{ relatedJobs(item.name).length }} workflows ↗</button></div>
        <details><summary>What to watch & official source</summary><p>{{ item.limit }}</p><a class="text-link" :href="item.source" target="_blank" rel="noopener noreferrer">Read the official documentation ↗</a></details>
        <a class="text-link" :href="item.url" target="_blank" rel="noopener noreferrer">Visit {{ item.name }} ↗</a>
      </article>
    </div>
    <p v-if="!count" class="empty-state">No close match in this view<span v-if="category !== 'All tasks'"> within {{ category }}</span>. Try fewer words or clear the filter. <button class="copy-button" @click="reset">Show all {{ view === 'needs' ? 'tasks' : 'tools' }}</button></p>
    <section class="brief-panel"><div><p class="eyebrow">Your first week</p><h2 class="display">Choose one task.<br />Keep what works.</h2></div><div><p>Pick a repeated job and one person to own it. Save the inputs and prompt. Review the first five results, noting time, edits and mistakes. Add app connections only when the steps are dependable.</p><NuxtLink class="button button-secondary" to="/workflow">Map your first workflow ↗</NuxtLink></div></section>
  </main>
</template>
