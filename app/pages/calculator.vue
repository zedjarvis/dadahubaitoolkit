<script setup lang="ts">
import QuoteCalculator from '../../lib/components/QuoteCalculator.vue'
useHead({ title: 'Cleaning quote calculator · The AI Toolkit' })
</script>
<template><main id="main" class="calc-page"><div class="page-intro"><NuxtLink class="back-link" to="/demos/calculator">← Back to the Codex demo</NuxtLink><div class="eyebrow">Checked workshop example</div><h1 class="display gradient-title">A quote in a few clicks.</h1><p class="lead">A working fallback for the live build. Change the plan and inspect how the estimate adds up.</p></div><QuoteCalculator /><p class="fine-print">Check case: 100 m², 3 visits per week, windows included = KES 34,104.00. This is a fictional estimate, not a final commercial quotation.</p></main></template>
