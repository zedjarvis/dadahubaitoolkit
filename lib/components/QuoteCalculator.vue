<script setup lang="ts">
import { computed, ref } from 'vue'
import { calculateQuote, kes } from '../business'
defineProps<{ compact?: boolean }>()
const area = ref<number | string>(400)
const visits = ref(3)
const windows = ref(true)
const result = computed(() => calculateQuote(Number(area.value), Number(visits.value), windows.value))
function printEstimate() { window.print() }
</script>

<template>
  <section class="quote-calculator" :class="{ compact }" aria-label="Cleaning quote calculator">
    <div class="quote-inputs">
      <div class="quote-label">YOUR CLEANING PLAN</div>
      <label class="quote-field">Floor area <span>square metres</span><input v-model="area" type="number" min="0.01" step="any" inputmode="decimal" :aria-invalid="!result" :aria-describedby="!result ? 'quote-error' : undefined" /></label>
      <label class="quote-field">Visits per week<select v-model="visits"><option :value="1">1 visit per week</option><option :value="3">3 visits per week</option><option :value="5">5 visits per week</option></select></label>
      <label class="quote-checkbox"><input v-model="windows" type="checkbox" /><span>Include monthly window cleaning<small>KES 6,000 per month</small></span></label>
      <p v-if="!result" id="quote-error" role="alert" class="quote-error">Enter a valid floor area greater than zero.</p>
    </div>
    <div class="quote-result" aria-live="polite" aria-atomic="true">
      <template v-if="result"><div class="quote-label">ESTIMATED MONTHLY TOTAL</div><strong class="quote-total">{{ kes(result.total) }}</strong><p class="quote-average">{{ result.monthlyVisits.toFixed(2).replace('.00', '') }} average visits per month</p><dl><div><dt>Routine cleaning</dt><dd>{{ kes(result.cleaning) }}</dd></div><div><dt>Windows</dt><dd>{{ kes(result.windowFee) }}</dd></div><div class="subtotal"><dt>Subtotal</dt><dd>{{ kes(result.subtotal) }}</dd></div><div><dt>Illustrative VAT (16%)</dt><dd>{{ kes(result.tax) }}</dd></div></dl><button v-if="!compact" type="button" class="quote-print" @click="printEstimate">Print estimate ↗</button></template>
      <div v-else class="quote-empty">Your estimate will appear here once the floor area is valid.</div>
    </div>
    <p class="quote-note">Training example. KES 18/m²/visit, 52 ÷ 12 weeks/month. The illustrative 16% VAT applies to both cleaning and windows. Actual visits, scope and applicable taxes need confirmation.</p>
  </section>
</template>

<style scoped>
.quote-calculator{display:grid;grid-template-columns:1fr 1fr;border:1px solid #ddcce8;border-radius:14px;overflow:hidden;background:#fff;color:#2d193b;font-family:'DM Sans',sans-serif;text-align:left;font-size:14px}.quote-inputs{padding:32px}.quote-label{font-size:10px;letter-spacing:.12em;font-weight:700;color:#9168a5;margin-bottom:25px}.quote-field{display:block;font-size:13px;font-weight:600;margin-bottom:22px}.quote-field>span{float:right;color:#9c89a6;font-weight:400;font-size:11px}.quote-field input,.quote-field select{width:100%;box-sizing:border-box;display:block;border:1px solid #d7c4e3;border-radius:7px;padding:12px;background:#fff;color:#3e2350;font:inherit;margin-top:10px;min-height:45px}.quote-field input:focus,.quote-field select:focus{outline:2px solid #a21caf;outline-offset:2px}.quote-checkbox{display:flex;gap:12px;align-items:start;font-size:12px;line-height:1.7;cursor:pointer}.quote-checkbox input{accent-color:#7e22ce;width:18px;height:18px;margin-top:1px}.quote-checkbox small{display:block;color:#8f789d}.quote-result{background:#f6effc;padding:32px;display:flex;flex-direction:column;justify-content:center}.quote-total{font-size:34px;line-height:1.2;letter-spacing:-.035em;color:#6b21a8;font-weight:700;white-space:nowrap}.quote-average{font-size:11px;color:#9475a6;margin:12px 0 24px}.quote-result dl{margin:0}.quote-result dl>div{display:flex;justify-content:space-between;gap:12px;font-size:12px;margin:13px 0}.quote-result dt{color:#81668f}.quote-result dd{margin:0;font-weight:600}.quote-result .subtotal{padding-top:16px;border-top:1px solid #decce9}.quote-note{grid-column:1/-1;padding:17px 25px;background:#fcfaff;font-size:10px;line-height:1.7;color:#967ba5;margin:0;border-top:1px solid #e9dff0}.quote-print{border:1px solid #d7bfe7;background:white;color:#722da1;padding:10px;border-radius:6px;font:inherit;font-size:12px;cursor:pointer;margin-top:15px}.quote-print:focus-visible{outline:3px solid #a21caf;outline-offset:3px}.quote-error{font-size:12px;color:#b42318;margin-top:18px}.quote-empty{font-size:14px;line-height:1.8;color:#9374a4}.compact .quote-inputs,.compact .quote-result{padding:23px}.compact .quote-label{margin-bottom:16px}.compact .quote-field{margin-bottom:15px}.compact .quote-field input,.compact .quote-field select{padding:7px;min-height:34px;margin-top:6px}.compact .quote-total{font-size:30px}.compact .quote-note{padding:10px 20px;font-size:9px}.compact .quote-result dl>div{margin:9px 0}.compact .quote-average{margin-bottom:14px}
@media(max-width:600px){.quote-calculator{grid-template-columns:1fr}.quote-inputs,.quote-result{padding:25px}.quote-total{font-size:30px}}@media print{.quote-print{display:none}.quote-calculator{break-inside:avoid;border:1px solid #777}.quote-result{background:white}.quote-note{color:#333}.quote-field input,.quote-field select{border-color:#aaa}}
</style>
