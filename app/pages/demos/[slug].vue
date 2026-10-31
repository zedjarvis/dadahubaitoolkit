<script setup lang="ts">
import demos from '~/data/demos.json'
import { inventory } from '../../../lib/business'
const route = useRoute()
const demo = computed(() => demos.find(item => item.slug === route.params.slug))
if (!demo.value) throw createError({ statusCode: 404, statusMessage: 'Demo not found' })
useHead(() => ({ title: `${demo.value?.title} · The AI Toolkit` }))
const profitRows = [...inventory].sort((a, b) => b.profit - a.profit)
</script>

<template>
  <main v-if="demo" id="main" class="wrap demo-page">
    <div class="page-intro">
      <NuxtLink class="back-link" to="/toolkit#sessions">← All demos</NuxtLink>
      <div class="eyebrow">Demo {{ demo.number }} / {{ demo.category }}</div>
      <h1 class="display gradient-title">{{ demo.title }}</h1>
      <p class="lead">{{ demo.description }}</p>
      <span class="tool-label">{{ demo.tool }}</span><span class="muted text-xs ml-4">{{ demo.time }} EAT</span>
    </div>
    <nav class="demo-section-nav" aria-label="On this demo page">
      <a href="#situation">The situation</a><a href="#try-it">Try it</a>
      <a v-if="demo.marketing" href="#marketing">Marketing</a><a href="#keep-it">Use it again</a>
    </nav>
    <section id="situation" class="demo-context">
      <p class="eyebrow">The work behind the prompt</p><h2 class="display">{{ demo.context.title }}</h2>
      <p class="context-story">{{ demo.context.story }}</p>
      <div class="context-grid">
        <div><h3>What we’re trying to do</h3><p>{{ demo.context.goal }}</p><h3>What we have</h3><ul><li v-for="input in demo.context.inputs" :key="input">{{ input }}</li></ul></div>
        <div><h3>What we want back</h3><p>{{ demo.context.output }}</p><h3>The decision afterwards</h3><p>{{ demo.context.decision }}</p></div>
      </div>
      <p class="context-transfer"><b>In your business</b> {{ demo.context.transfer }}</p>
    </section>
    <section id="try-it" class="demo-try">
      <div class="section-heading"><div><p class="eyebrow">Try the work</p><h2 class="display">{{ demo.marketing ? 'First, move the enquiry forward.' : 'Give it a clear brief.' }}</h2></div></div>
      <div class="demo-launch" aria-label="Demo tools">
        <a v-if="demo.download" class="button button-secondary" :href="'/resources/' + demo.download" download>Download the RFQ PDF ↓</a>
        <NuxtLink v-if="demo.slug === 'calculator'" class="button button-primary" to="/calculator">Try the quote calculator ↗</NuxtLink>
        <a v-if="demo.slug === 'proposal' || demo.slug === 'stock'" class="button button-primary" href="https://chatgpt.com/" target="_blank" rel="noopener noreferrer">Open ChatGPT ↗</a>
        <a v-if="demo.slug === 'research'" class="button button-primary" href="https://notebook.google.com/" target="_blank" rel="noopener noreferrer">Open NotebookLM ↗</a>
      </div>
      <div class="demo-alternatives"><span>Also try</span><span v-for="name in demo.alternatives" :key="name" class="tool-label">{{ name }}</span><NuxtLink :to="'/tools#' + demo.toolkitCategory" class="text-link">Compare options ↗</NuxtLink></div>
      <div class="demo-detail">
        <div>
          <DemoPrompt :text="demo.prompt" label="Main demo prompt" />
          <NuxtLink :to="'/rehearsal#' + demo.slug" class="text-link">What to say & a fallback ↗</NuxtLink>
          <h3 class="detail-heading">One useful follow-up</h3><DemoPrompt :text="demo.followup" label="Follow-up prompt" />
          <details v-for="followup in demo.extraFollowups" :key="followup.title"><summary>{{ followup.title }}</summary><DemoPrompt :text="followup.body" :label="followup.title" /></details>
          <details><summary>The checks before using the result</summary><p v-for="check in demo.checks" :key="check">{{ check }}</p>
            <div v-if="demo.slug === 'stock'" class="stock-chart" aria-label="Gross profit by product"><div v-for="row in profitRows" :key="row.name" class="stock-chart-row"><span>{{ row.name }}</span><div class="chart-bar" :style="{ width: row.profit / 9100 * 100 + '%' }" /><b>{{ row.profit.toLocaleString() }}</b></div><p>Gross profit in KES from 30-day data.</p></div>
          </details>
        </div>
        <aside><div class="aside-block"><h3>The problem</h3><p>{{ demo.problem }}</p></div><div class="aside-block"><h3>Where AI helps</h3><p>{{ demo.opportunity }}</p></div><div class="aside-block"><h3>Your first step</h3><p>{{ demo.firstStep }}</p></div></aside>
      </div>
    </section>
    <section v-if="demo.marketing" id="marketing" class="marketing-section">
      <p class="eyebrow">Sales & marketing / Part two</p><h2 class="display">{{ demo.marketing.title }}</h2><p class="section-lead">{{ demo.marketing.intro }}</p>
      <div class="campaign-brief"><div v-for="fact in demo.marketing.brief" :key="fact.label"><span>{{ fact.label }}</span><b>{{ fact.value }}</b></div></div>
      <DemoPrompt :text="demo.marketing.prompt" label="Weekly marketing prompt" />
      <h3 class="detail-heading">A worked example: three posts, three jobs.</h3>
      <p class="section-note">Use this prepared plan if the live response stalls, or as a starting point for your own business. The goal is three qualified enquiries in a week; results are still to be recorded.</p>
      <div class="campaign-posts"><article v-for="post in demo.marketing.plan" :key="post.day"><p class="eyebrow">{{ post.day }}</p><h4>{{ post.job }}</h4><p>{{ post.idea }}</p><p><b>Visual to prepare</b><br>{{ post.visual }}</p><p class="post-action">{{ post.action }}</p></article></div>
      <div class="campaign-copy"><div><h3>Monday’s Instagram caption</h3><blockquote>{{ demo.marketing.caption }}</blockquote></div><div><h3>The WhatsApp Status version</h3><blockquote>{{ demo.marketing.status }}</blockquote><p class="section-note">Use your own Status. Nothing here posts or messages on your behalf.</p></div></div>
      <details class="demo-extra"><summary>Turn the post into a simple graphic</summary><DemoPrompt :text="demo.marketing.followup" label="Simple graphic brief" /></details>
      <div class="publishing-check"><h3>Before publishing</h3><ul><li v-for="check in demo.marketing.checks" :key="check">{{ check }}</li></ul></div>
      <a class="button button-secondary" href="/resources/12-weekly-marketing-planner.csv" download>Download the editable weekly planner ↓</a>
      <p class="section-note">Opens in Excel or Google Sheets. Includes the three post ideas; owners and result columns are blank for you to fill. Use Instagram or WhatsApp only if your customers already hear from you there.</p>
    </section>
    <section id="keep-it" class="reuse-section">
      <p class="eyebrow">Keep it. Use it again.</p><h2 class="display">{{ demo.reuse.title }}</h2><p class="section-lead">{{ demo.reuse.intro }}</p>
      <dl class="reuse-facts"><div><dt>Set up</dt><dd>{{ demo.reuse.setup }}</dd></div><div><dt>Use again</dt><dd>{{ demo.reuse.cadence }}</dd></div><div><dt>Person responsible</dt><dd>{{ demo.reuse.owner }}</dd></div></dl>
      <ol class="reuse-steps"><li v-for="(step,index) in demo.reuse.steps" :key="step.title"><span class="reuse-number" aria-hidden="true">{{ String(index + 1).padStart(2,'0') }}</span><div><h3>{{ step.title }}</h3><p>{{ step.body }}</p></div></li></ol>
      <div class="reuse-next"><h3>Your next run</h3><p>{{ demo.reuse.nextRun }}</p><h3>How you’ll know it helps</h3><p>{{ demo.reuse.measure }}</p></div>
      <h3 class="detail-heading">Copy this into your saved document.</h3><p class="section-note">Replace the square brackets with your details. Keep the original as your master; make a dated copy for new work.</p>
      <DemoPrompt :text="demo.reuse.template" label="Reusable workflow template" />
      <div class="demo-launch"><a class="button button-secondary" href="/resources/11-reusable-workflows.pdf" download>Download the keep-and-reuse guide (PDF) ↓</a><a class="text-link" href="#situation">Back to the situation ↑</a></div>
      <details class="demo-extra"><summary>Setup references</summary><p class="section-note">These are practical starter routines, using saved instructions, current inputs, review and a named owner. Product features vary by account. Guidance checked 31 October 2026.</p><p v-for="source in demo.reuse.sources" :key="source.url"><a class="text-link" :href="source.url" target="_blank" rel="noopener noreferrer">{{ source.label }} ↗</a></p></details>
    </section>
  </main>
</template>
