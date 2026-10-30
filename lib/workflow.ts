export type Enquiry = { id: string; client: string; area: string; windows: string }
export type RecordItem = { id: string; client: string; area: number; draft: string; status: 'Needs clarification' | 'Awaiting review' | 'Approved locally'; missing: boolean }
export function processEnquiry(input: Enquiry, existing: RecordItem[]) {
  const id = input.id.trim(), client = input.client.trim(), area = Number(input.area)
  if (!id || !client || !input.area.trim() || !Number.isFinite(area) || area <= 0) return { error: 'Enter an enquiry ID, client and floor area greater than zero.' }
  if (existing.some(row => row.id.toLowerCase() === id.toLowerCase())) return { error: 'Duplicate enquiry ID: no second record or draft was created.' }
  const missing = !input.windows.trim()
  const draft = `Hello ${client}, thank you for your enquiry about cleaning ${area} m². ` + (missing ? 'Please confirm the window count, dimensions, height and access requirements so we can prepare a costed proposal.' : `We have recorded these window details for review: ${input.windows.trim()}. We will check the scope and availability before preparing a costed proposal.`) + ' No price or start date is confirmed yet.'
  return { record: { id, client, area, draft, missing, status: missing ? 'Needs clarification' : 'Awaiting review' } as RecordItem }
}
export function approveEnquiry(record: RecordItem): RecordItem {
  if (record.missing) return record
  return { ...record, status: 'Approved locally' }
}

export function resolveEnquiry(record: RecordItem, windows: string): RecordItem {
  if (!windows.trim() || !record.missing) return record
  return processEnquiry({ id: record.id, client: record.client, area: String(record.area), windows }, []).record!
}
