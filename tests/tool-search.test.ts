import test from 'node:test'
import assert from 'node:assert/strict'
import fs from 'node:fs'
import { createDirectorySearch } from '../lib/tool-search.ts'

const jobs = JSON.parse(fs.readFileSync(new URL('../app/data/jobs.json', import.meta.url), 'utf8'))
const tools = JSON.parse(fs.readFileSync(new URL('../app/data/tools.json', import.meta.url), 'utf8'))
const search = createDirectorySearch(jobs.map((job: any) => ({ item: job, title: job.title, keywords: job.keywords, category: job.category, names: job.options.map((o: string[]) => o[0]), description: [job.outcome, job.recommendation, job.workflow.trigger, job.workflow.inputs].join(' ') })))
const toolSearch = createDirectorySearch(tools.map((tool: any) => ({ item: tool, title: tool.name, keywords: tool.keywords, category: tool.kind, names: [], description: tool.capability })))

test('business misspellings return the intended task first', () => {
  for (const [query, id] of [['markting', 'marketing'], ['invocies', 'invoices'], ['email campain', 'email-campaigns'], ['product catlog', 'product-listings'], ['staff traning', 'staff-training']]) {
    assert.equal((search(query!) as any[])[0]?.id, id, query)
  }
})
test('multi-word queries narrow results regardless of word order', () => {
  assert.equal((search('leads follow up') as any[])[0]?.id, 'sales-followups')
  assert.deepEqual(search('email marketing'), search('marketing email'))
  assert.ok(search('email marketing').length < search('marketing').length)
})
test('tool aliases and typos work in both directory views', () => {
  assert.equal((toolSearch('notbook lm') as any[])[0]?.name, 'NotebookLM')
  assert.equal((toolSearch('chat gpt') as any[])[0]?.name, 'ChatGPT')
  assert.equal((toolSearch('mail chimp') as any[])[0]?.name, 'Mailchimp')
  assert.ok((search('notbook lm') as any[]).some(job => job.id === 'documents'))
})
test('empty search restores order and unrelated or punctuation-only queries stay empty', () => {
  assert.deepEqual(search('  '), jobs)
  assert.deepEqual(search('zzzxxyy'), [])
  assert.deepEqual(search('...'), [])
  assert.equal((search('  INVOICES  ') as any[])[0]?.id, 'invoices')
})
test('every workflow has usable guidance and points to known tools with official sources', () => {
  const names = new Set(tools.map((tool: any) => tool.name))
  assert.equal(new Set(jobs.map((job: any) => job.id)).size, jobs.length)
  for (const job of jobs) {
    assert.equal(job.workflow.steps.length, 3, job.id)
    for (const field of ['trigger', 'inputs', 'save', 'owner', 'measure']) assert.ok(job.workflow[field]?.trim(), `${job.id}: ${field}`)
    for (const [name] of job.options) assert.ok(names.has(name), `${job.id}: ${name}`)
  }
  for (const tool of tools) {
    assert.match(tool.source, /^https:\/\//)
    for (const field of ['capability', 'fit', 'firstStep', 'access', 'limit']) assert.ok(tool[field]?.trim(), `${tool.name}: ${field}`)
  }
})
