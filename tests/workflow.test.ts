import test from 'node:test'
import assert from 'node:assert/strict'
import { processEnquiry, approveEnquiry, resolveEnquiry } from '../lib/workflow.ts'
const sample = { id: 'SAFI-001', client: 'Fictional client', area: '400', windows: '' }
test('missing window details create a hold and cannot be approved', () => {
 const result = processEnquiry(sample, []); assert.ok(result.record)
 assert.equal(result.record.status, 'Needs clarification')
 assert.equal(approveEnquiry(result.record).status, 'Needs clarification')
})
test('complete enquiries require explicit review and duplicate IDs do not create drafts', () => {
 const result = processEnquiry({ ...sample, windows: '10 ground-floor windows, dimensions supplied' }, []); assert.ok(result.record)
 assert.equal(result.record.status, 'Awaiting review')
 assert.equal(approveEnquiry(result.record).status, 'Approved locally')
 assert.match(processEnquiry({ ...sample, id: ' safi-001 ' }, [result.record]).error!, /Duplicate/)
})
test('missing or invalid fields create no record', () => {
 for (const area of ['', '0', '-1', 'NaN', 'Infinity']) assert.ok(processEnquiry({ ...sample, area }, []).error)
 assert.ok(processEnquiry({ ...sample, client: ' ' }, []).error)
})

test('clarification updates the same enquiry and still requires review', () => {
 const held = processEnquiry(sample, []).record!
 assert.equal(resolveEnquiry(held, ' ').status, 'Needs clarification')
 const resolved = resolveEnquiry(held, '10 ground-floor windows, 1 × 1 m; safe access confirmed')
 assert.equal(resolved.id, held.id)
 assert.equal(resolved.status, 'Awaiting review')
 assert.equal(resolved.missing, false)
 assert.match(resolved.draft, /10 ground-floor/)
})
