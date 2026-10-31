<template>
  <div>
    <a class="skip-link" href="#main">Skip to content</a>
    <header class="site-header">
      <NuxtLink to="/toolkit" class="wordmark" aria-label="The AI Toolkit at DADA HUB home">
        <img src="/favicon.svg" width="32" height="32" alt="" />
        <span class="wordmark-name">AI TOOLKIT</span>
        <span class="wordmark-dot" aria-hidden="true">/</span>
        <img class="wordmark-event-logo" src="/brands/dada-hub.png" width="72" height="41" alt="DADA HUB" />
      </NuxtLink>
      <nav aria-label="Main navigation">
        <NuxtLink to="/toolkit#sessions">Demos</NuxtLink>
        <NuxtLink to="/tools">Tools</NuxtLink>
        <NuxtLink to="/toolkit#resources">Resources</NuxtLink>
        <a href="/slides/index.html" class="nav-present"><span class="nav-slides-label">Open slides</span><span class="nav-slides-short">Slides</span><span aria-hidden="true">↗</span></a>
      </nav>
    </header>
    <NuxtPage />
    <footer class="site-footer"><span>The AI Toolkit <span class="muted">with Cedrouseroll Omondi</span></span><span>DADA HUB, Parklands <span class="muted">31 October 2026</span></span></footer>
  </div>
</template>
