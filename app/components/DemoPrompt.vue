<script setup lang="ts">
const props = defineProps<{ text: string; label: string }>()
const copied = ref(false)
const error = ref(false)
watch(() => props.text, () => { copied.value = false; error.value = false })
async function copy() {
  try { await navigator.clipboard.writeText(props.text); copied.value = true; error.value = false }
  catch { error.value = true }
}
</script>
<template>
  <div class="prompt-area">
    <div class="prompt-toolbar"><span>{{ label }}</span><button class="copy-button" :aria-label="'Copy ' + label" @click="copy">{{ copied ? 'Copied ✓' : 'Copy' }}</button></div>
    <pre class="prompt-text" tabindex="0" :aria-label="label">{{ text }}</pre>
    <p v-if="copied || error" class="copy-status" role="status">{{ error ? 'Select the text above and copy it manually; clipboard access is unavailable.' : 'Copied. Paste it into your chat or saved document.' }}</p>
  </div>
</template>
