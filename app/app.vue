<template>
  <div>
    <a class="skip-link" href="#main">Skip to content</a>
    <header class="site-header">
      <NuxtLink to="/" class="wordmark" aria-label="The AI Toolkit home"><img src="/favicon.svg" width="32" height="32" alt="" />AI TOOLKIT<span class="wordmark-dot">/</span><span class="wordmark-event">DADA HUB</span></NuxtLink>
      <nav aria-label="Main navigation">
        <NuxtLink to="/toolkit#sessions">The demos</NuxtLink>
        <NuxtLink to="/toolkit#resources">Resources</NuxtLink>
        <a href="/slides/index.html" class="nav-present">Open slides <span aria-hidden="true">↗</span></a>
      </nav>
    </header>
    <NuxtPage />
    <footer class="site-footer"><span>The AI Toolkit <span class="muted">with Cedrouseroll Omondi</span></span><span>DADA HUB, Parklands <span class="muted">31 October 2026</span></span></footer>
  </div>
</template>
