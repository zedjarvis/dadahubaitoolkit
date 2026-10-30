<template>
  <main id="main" class="wrap welcome-page">
    <section class="welcome-grid" aria-labelledby="welcome-title">
      <div class="welcome-copy">
        <p class="eyebrow">DADA HUB · 31 October 2026</p>
        <h1 id="welcome-title" class="display gradient-title">The AI<br />Toolkit.</h1>
        <p class="welcome-summary">AI for your everyday<br />business tasks.</p>
        <p class="welcome-instruction">Scan the code to open the prompts, examples and session resources on your phone.</p>
        <div class="welcome-actions">
          <NuxtLink class="button button-primary" to="/toolkit">Open the toolkit <span aria-hidden="true">↗</span></NuxtLink>
          <a class="text-link" href="/slides/index.html">Start the presentation ↗</a>
        </div>
        <p class="welcome-speaker">With Cedrouseroll Omondi</p>
        <div class="welcome-brands" aria-label="Flowt and SchoolBooks">
          <a href="https://flowt.africa/" target="_blank" rel="noopener noreferrer" aria-label="Visit Flowt"><img class="welcome-flowt" src="/brands/flowt.png" alt="Flowt" width="512" height="512" /></a>
          <a class="welcome-schoolbooks" href="https://www.schoolbooks.ke/" target="_blank" rel="noopener noreferrer"><img src="/brands/schoolbooks.svg" width="40" height="40" alt="" /><span>SchoolBooks</span></a>
        </div>
      </div>
      <div class="welcome-code">
        <p class="eyebrow">Scan to follow along</p>
        <a href="https://dadahubaitoolkit.vercel.app/toolkit" class="welcome-qr" aria-label="Open the AI Toolkit"><img src="/qr/session.png" alt="QR code for the AI Toolkit at dadahubaitoolkit.vercel.app/toolkit" width="1080" height="1080" fetchpriority="high" /></a>
        <a class="welcome-url" href="https://dadahubaitoolkit.vercel.app/toolkit">dadahubaitoolkit.vercel.app</a>
        <span class="welcome-code-note">Prompts · Examples · Resources</span>
      </div>
    </section>
  </main>
</template>
