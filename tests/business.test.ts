import test from 'node:test'
import assert from 'node:assert/strict'
import { calculateQuote, inventory } from '../lib/business.ts'

test('known quote cases reconcile to independently checked totals', () => {
  assert.equal(calculateQuote(100, 3, true)?.total, 34104)
  assert.equal(calculateQuote(100, 3, false)?.total, 27144)
  assert.equal(calculateQuote(400, 3, true)?.total, 115536)
  assert.equal(calculateQuote(100, 1, false)?.total.toFixed(2), '9048.00')
  assert.equal(calculateQuote(100, 5, false)?.total.toFixed(2), '45240.00')
})
test('invalid input never produces a valid quote', () => {
  for (const area of [0, -1, NaN, Infinity, Number.MAX_VALUE]) assert.equal(calculateQuote(area, 3, true), null)
  assert.equal(calculateQuote(100, 2, false), null)
})
test('stock analysis matches the session answer key', () => {
  assert.equal(inventory.reduce((sum, row) => sum + row.profit, 0), 30295)
  assert.equal(inventory.reduce((sum, row) => sum + row.revenue, 0), 179640)
  assert.deepEqual(inventory.map(row => row.reorder), [70, 60, 0, 0, 76, 0, 74, 0])
})
