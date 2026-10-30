export function calculateQuote(area: number, visits: number, windows: boolean) {
  if (!Number.isFinite(area) || area <= 0 || ![1, 3, 5].includes(visits)) return null
  const monthlyVisits = visits * 52 / 12
  const cleaning = area * 18 * monthlyVisits
  const windowFee = windows ? 6000 : 0
  const subtotal = cleaning + windowFee
  const tax = subtotal * 0.16
  const total = subtotal + tax
  if (![cleaning, subtotal, tax, total].every(Number.isFinite)) return null
  return { monthlyVisits, cleaning, windowFee, subtotal, tax, total }
}

export const inventory = [
  { name: 'Multipurpose cleaner 2L', opening: 120, sold: 95, cost: 310, price: 380 },
  { name: 'Floor cleaner 5L', opening: 80, sold: 70, cost: 720, price: 850 },
  { name: 'Hand soap 1L', opening: 150, sold: 40, cost: 260, price: 300 },
  { name: 'Laundry soap bar', opening: 200, sold: 35, cost: 45, price: 60 },
  { name: 'Bleach 1L', opening: 100, sold: 88, cost: 170, price: 210 },
  { name: 'Microfibre pack', opening: 60, sold: 12, cost: 350, price: 480 },
  { name: 'Toilet paper 10 pack', opening: 90, sold: 82, cost: 380, price: 450 },
  { name: 'Bin liner box', opening: 40, sold: 8, cost: 900, price: 1100 },
].map(row => ({ ...row, revenue: row.sold * row.price, profit: row.sold * (row.price - row.cost), closing: row.opening - row.sold, reorder: Math.max(0, 2 * row.sold - row.opening), sellThrough: row.sold / row.opening * 100 }))

export function kes(value: number) {
  return new Intl.NumberFormat('en-KE', { style: 'currency', currency: 'KES', maximumFractionDigits: 2, minimumFractionDigits: 2 }).format(value)
}
