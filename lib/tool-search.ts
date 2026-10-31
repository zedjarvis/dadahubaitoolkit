import Fuse from 'fuse.js'

export interface DirectoryEntry<T> {
  item: T
  title: string
  keywords: string
  category: string
  names: string[]
  description: string
}

// Search only useful visible content and curated synonyms, never URLs or JSON keys.
// Reuse this index across keystrokes; filtering by work happens after ranking.
export function createDirectorySearch<T>(entries: DirectoryEntry<T>[]) {
  const index = new Fuse(entries, {
    useTokenSearch: true,
    tokenMatch: 'all',
    threshold: 0.32,
    ignoreLocation: true,
    ignoreDiacritics: true,
    keys: [
      { name: 'title', weight: 5 },
      { name: 'names', weight: 4 },
      { name: 'keywords', weight: 3 },
      { name: 'category', weight: 2 },
      { name: 'description', weight: 1 },
    ],
  })
  return (query: string): T[] => {
    const clean = query.trim().replace(/\s+/g, ' ')
    if (!clean) return entries.map(entry => entry.item)
    if (!/[\p{L}\p{N}]/u.test(clean)) return []
    return index.search(clean).map(result => result.item.item)
  }
}
