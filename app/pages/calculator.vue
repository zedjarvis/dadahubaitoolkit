<script setup lang="ts">
import QuoteCalculator from '../../lib/components/QuoteCalculator.vue'
useHead({ title: 'Cleaning quote calculator · The AI Toolkit' })
</script>
<template><main id="main" class="calc-page"><div class="page-intro"><NuxtLink class="back-link" to="/demos/calculator">← Back to the Codex demo</NuxtLink><div class="eyebrow">Safi Services & Supplies</div><h1 class="display gradient-title">A quote in a few clicks.</h1><p class="lead">Change the service plan and see how the monthly estimate adds up.</p></div><QuoteCalculator /><p class="fine-print">Check case: 100 m², 3 visits per week, windows included = KES 34,104.00. This is an estimate; confirm scope and availability before issuing a quotation.</p></main></template>
