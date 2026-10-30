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
    <section class="hero">
      <div>
        <span class="pill"><span class="pill-dot" /> A practical session for business owners</span>
        <h1 class="display gradient-title">The AI<br />Toolkit.</h1>
        <p class="hero-summary">AI for your everyday<br />business tasks.</p>
        <div class="hero-actions"><a class="button button-primary" href="/slides/index.html">Start the presentation <span aria-hidden="true">↗</span></a><a class="button button-secondary" href="#sessions">Explore the demos <span aria-hidden="true">↓</span></a></div>
        <div class="hero-meta"><span>31 October 2026</span><span>9:20–10:20 AM EAT</span><span>Parklands, Nairobi</span></div>
      </div>
      <div class="portrait-scene">
        <span class="orbit-label orbit-one"><span>✦</span> Your business. Your brief.</span>
        <div class="portrait-ring"><img :src="illustrated ? '/images/ced-illustrated.png' : '/images/ced-original.jpg'" :class="{ original: !illustrated }" :alt="illustrated ? 'Illustrated portrait of Cedrouseroll Omondi' : 'Photograph of Cedrouseroll Omondi'" width="480" height="480" fetchpriority="high" /></div>
        <span class="orbit-label orbit-two"><span>✓</span> You check. You decide.</span>
        <div class="portrait-caption"><b>Cedrouseroll Omondi</b><span class="muted">Flowt & SchoolBooks</span></div>
        <div class="portrait-switch" role="group" aria-label="Speaker portrait style"><button :aria-pressed="illustrated" @click="illustrated = true">Illustrated</button><button :aria-pressed="!illustrated" @click="illustrated = false">Original photo</button></div>
      </div>
    </section>

    <div class="session-strip"><div><b>60</b><span>minutes together</span></div><div><b>04</b><span>business demos</span></div><div><b>03</b><span>ways to work with AI</span></div><div><b>01</b><span>task to try on Monday</span></div></div>

    <section id="sessions" class="section">
      <div class="section-heading"><div><p class="eyebrow">Watch. Try. Check.</p><h2 class="display">A toolkit for actual work.</h2></div><p class="section-intro">Open a demo for the exact prompt, the sample material and what to check.</p></div>
      <div class="demo-list"><NuxtLink v-for="demo in demos" :key="demo.slug" :to="`/demos/${demo.slug}`" class="demo-row"><span class="demo-number">{{ demo.number }}</span><div><span class="category">{{ demo.category }} · {{ demo.minutes }}</span><h3>{{ demo.title }}</h3></div><p>{{ demo.description }}</p><div class="demo-end"><span class="tool-label">{{ demo.tool }}</span><span class="demo-arrow" aria-hidden="true">↗</span></div></NuxtLink></div>
    </section>

    <section class="brief-panel"><div><p class="eyebrow">The briefing formula</p><h2 class="display">A better brief.<br />A better first draft.</h2></div><div class="brief-steps"><div v-for="step in [{title:'Role',body:'Who should help?'},{title:'Context',body:'What do they need to know?'},{title:'Task',body:'What should they do?'},{title:'Format',body:'How should it look?'},{title:'Check',body:'What must be verified?'}]" :key="step.title" class="brief-step"><b>{{ step.title }}</b><span>{{ step.body }}</span></div></div></section>

    <section id="resources" class="section"><div class="section-heading"><div><p class="eyebrow">Keep these close</p><h2 class="display">Your session resources.</h2></div><p class="section-intro">Fictional examples you can use safely.<br />No client or student records needed.</p></div><div class="resource-grid">
      <a class="resource-card" href="/resources/dada-hub-demo-kit.zip" download><span class="resource-icon">01 / DOWNLOAD</span><h3>The complete demo kit</h3><p>Prompts, presenter run sheet, fictional RFQ and a take-home reference.</p><span class="text-link">Download ZIP ↗</span></a>
      <a class="resource-card" href="/resources/03-fictional-cleaning-rfq.txt" download><span class="resource-icon">02 / SOURCE MATERIAL</span><h3>The cleaning RFQ</h3><p>One short document for the NotebookLM demo. Includes a few details worth asking about.</p><span class="text-link">Download source ↗</span></a>
      <NuxtLink class="resource-card" to="/calculator"><span class="resource-icon">03 / WORKING EXAMPLE</span><h3>The quote calculator</h3><p>A checked fallback for the Codex demo. Change the inputs and follow the calculation.</p><span class="text-link">Try the calculator ↗</span></NuxtLink>
    </div><p style="margin-top: 24px"><a class="text-link" href="/resources/the-ai-toolkit.pdf" download>Download the presentation PDF ↗</a></p></section>

    <section class="commitment"><p class="eyebrow">Monday, 2 November</p><h2 class="display">What will you try first?</h2><p>Choose one task that takes time each week. Give it 15 minutes, then check whether the result is useful.</p><form @submit.prevent="saveCommitment"><label class="sr-only" for="commitment">My first AI task</label><input id="commitment" v-model="commitment" required maxlength="200" placeholder="I’ll use AI to help me…" @input="saved = false" /><button class="button button-primary" type="submit">Save my first step</button></form><div class="save-feedback" aria-live="polite">{{ saved ? 'Saved on this browser. Your first step stays with you.' : saveError ? 'Browser storage is unavailable. Copy your task into your notes.' : 'Stored only in this browser. Nothing is sent to a server.' }}</div></section>
  </main>
</template>
