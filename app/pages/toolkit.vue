<script setup lang="ts">
import demos from '~/data/demos.json'
const illustrated = ref(true)
const commitment = ref('')
const saved = ref(false)
const saveError = ref(false)
onMounted(() => { try { commitment.value = localStorage.getItem('dada-monday-task') || '' } catch { /* Storage may be unavailable. */ } })
function saveCommitment() {
  if (!commitment.value.trim()) return
  try { localStorage.setItem('dada-monday-task', commitment.value.trim()); saved.value = true; saveError.value = false }
  catch { saveError.value = true; saved.value = false }
}
</script>

<template>
  <main id="main" class="wrap">
    <section class="hero toolkit-hero">
      <div>
        <span class="pill"><span class="pill-dot" /> DADA HUB · 31 October 2026</span>
        <h1 class="display gradient-title">AI for your everyday business tasks.</h1>
        <p class="hero-summary">Follow a day at Safi Services & Supplies. Try the work, check the result, then adapt it to your business.</p>
        <div class="hero-actions"><a class="button button-primary" href="#sessions">Explore the demos <span aria-hidden="true">↓</span></a><a class="button button-secondary" href="#resources">Get resources <span aria-hidden="true">↓</span></a></div>
        <div class="hero-meta"><span>9:20–10:20 AM EAT</span><span>Parklands, Nairobi</span></div>
      </div>
      <div class="portrait-scene">
        <span class="orbit-label orbit-one"><span>✦</span> Your business. Your brief.</span>
        <div class="portrait-ring"><picture><source media="(max-width: 640px)" srcset="/images/ced-illustrated.png" /><img :src="illustrated ? '/images/ced-illustrated.png' : '/images/ced-original.jpg'" :class="{ original: !illustrated }" alt="Portrait of Cedrouseroll Omondi" width="480" height="480" decoding="async" /></picture></div>
        <span class="orbit-label orbit-two"><span>✓</span> You check. You decide.</span>
        <div class="portrait-caption"><b>Cedrouseroll Omondi</b><span class="muted">Flowt & SchoolBooks</span></div>
        <div class="portrait-switch" role="group" aria-label="Speaker portrait style"><button :aria-pressed="illustrated" @click="illustrated = true">Illustrated</button><button :aria-pressed="!illustrated" @click="illustrated = false">Original photo</button></div>
      </div>
    </section>

    <div class="session-strip"><div><b>60</b><span>minutes together</span></div><div><b>04</b><span>business demos</span></div><div><b>03</b><span>ways to work with AI</span></div><div><b>01</b><span>task to try on Monday</span></div></div>

    <section id="sessions" class="section">
      <div class="section-heading"><div><p class="eyebrow">Watch. Try. Check.</p><h2 class="display">A toolkit for actual work.</h2></div><p class="section-intro">Open a demo for the exact prompt, the sample material and what to check.</p></div>
      <div class="demo-list"><NuxtLink v-for="demo in demos" :key="demo.slug" :to="`/demos/${demo.slug}`" class="demo-row"><span class="demo-number">{{ demo.number }}</span><div><span class="category">{{ demo.category }} · {{ demo.minutes }}</span><h3>{{ demo.title }}</h3><span class="tool-label">Live demo: {{ demo.tool }}</span><div class="alternative-tags"><span class="also-label">Also try</span><span v-for="name in demo.alternatives" :key="name">{{ name }}</span></div></div><p>{{ demo.description }}</p><div class="demo-end"><span class="demo-arrow" aria-hidden="true">↗</span></div></NuxtLink></div><p class="directory-link"><NuxtLink class="text-link" to="/tools">Compare these tools and explore more everyday tasks ↗</NuxtLink></p>
    </section>

    <section class="brief-panel"><div><p class="eyebrow">The briefing formula</p><h2 class="display">A better brief.<br />A better first draft.</h2></div><div class="brief-steps"><div v-for="step in [{title:'Role',body:'Who should help?'},{title:'Context',body:'What do they need to know?'},{title:'Task',body:'What should they do?'},{title:'Format',body:'How should it look?'},{title:'Check',body:'What must be verified?'}]" :key="step.title" class="brief-step"><b>{{ step.title }}</b><span>{{ step.body }}</span></div></div></section>

    <section id="resources" class="section"><div class="section-heading"><div><p class="eyebrow">Keep these close</p><h2 class="display">Your session resources.</h2></div><p class="section-intro">Prompts, source documents and tools.<br />Everything you need to follow along.</p></div><div class="resource-grid"><NuxtLink class="resource-card" to="/workflow"><span class="resource-icon">TRY THE WORKFLOW</span><h3>An enquiry, handled</h3><p>Watch a local form create a record and a draft. Test missing information and human approval.</p><span class="text-link">Open the workflow lab ↗</span></NuxtLink><NuxtLink class="resource-card" to="/tools"><span class="resource-icon">FIND A TOOL</span><h3>More everyday tasks</h3><p>Task-based recommendations, alternatives, starter prompts and official sources.</p><span class="text-link">Browse the tools ↗</span></NuxtLink><NuxtLink class="resource-card" to="/rehearsal"><span class="resource-icon">FOLLOW THE SESSION</span><h3>The rehearsal guide</h3><p>What to say, what to click, expected results and fallbacks for every demo.</p><span class="text-link">Open the guide ↗</span></NuxtLink>
      <a class="resource-card" href="/resources/dada-hub-demo-kit.zip" download><span class="resource-icon">01 / DOWNLOAD</span><h3>The complete demo kit</h3><p>PDF handouts, exact prompts, the source RFQ and answer keys, plus a CSV and offline calculator.</p><span class="text-link">Download PDF kit (ZIP) ↗</span></a>
      <a class="resource-card" href="/resources/03-cleaning-rfq.pdf" download><span class="resource-icon">02 / SOURCE MATERIAL</span><h3>The cleaning RFQ</h3><p>A clearly laid-out PDF for the NotebookLM demo, with numbered sections and details worth asking about.</p><span class="text-link">Download RFQ PDF ↗</span></a>
      <NuxtLink class="resource-card" to="/calculator"><span class="resource-icon">03 / WORKING EXAMPLE</span><h3>The quote calculator</h3><p>Estimate monthly cleaning costs from floor area, visits and window cleaning.</p><span class="text-link">Try the calculator ↗</span></NuxtLink>
    </div><p class="demo-launch" style="margin-top: 24px"><a class="text-link" href="/slides/index.html">Open the presentation ↗</a><a class="text-link" href="/resources/the-ai-toolkit.pdf" download>Download the presentation PDF ↗</a></p></section>

    <section class="commitment"><p class="eyebrow">Monday, 2 November</p><h2 class="display">What will you try first?</h2><p>Choose one task that takes time each week. Give it 15 minutes, then check whether the result is useful.</p><form @submit.prevent="saveCommitment"><label class="sr-only" for="commitment">My first AI task</label><input id="commitment" v-model="commitment" required maxlength="200" placeholder="I’ll use AI to help me…" @input="saved = false" /><button class="button button-primary" type="submit">Save my first step</button></form><div class="save-feedback" aria-live="polite">{{ saved ? 'Saved on this browser. Your first step stays with you.' : saveError ? 'Browser storage is unavailable. Copy your task into your notes.' : 'Stored only in this browser. Nothing is sent to a server.' }}</div></section>
  </main>
</template>
