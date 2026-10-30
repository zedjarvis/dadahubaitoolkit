<script setup lang="ts">
import { inventory } from '../../lib/business'
const rows = [...inventory].sort((a, b) => b.profit - a.profit)
</script>
<template><div class="profit-chart" role="img" aria-label="Gross profit by product: floor cleaner 9,100; multipurpose cleaner 6,650; toilet paper 5,740; bleach 3,520; hand soap and bin liners 1,600 each; microfibre packs 1,560; laundry soap 525 Kenyan shillings."><div v-for="row in rows" :key="row.name" class="profit-row"><span>{{ row.name }}</span><div class="profit-track"><div :style="{ width: `${row.profit / 9100 * 100}%` }" /></div><b>{{ row.profit.toLocaleString() }}</b></div></div></template>
<style scoped>.profit-chart{margin-top:20px}.profit-row{display:grid;grid-template-columns:180px 1fr 65px;gap:18px;align-items:center;font-size:16px;margin:16px 0}.profit-row span{color:#7b608c}.profit-row b{font-size:17px;color:#6b21a8}.profit-track{height:15px;background:#f0e4fa;border-radius:0 4px 4px 0}.profit-track>div{height:100%;background:linear-gradient(90deg,#a21caf,#6d28d9);border-radius:0 4px 4px 0}</style>
