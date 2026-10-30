import { spawnSync } from 'node:child_process'
import { fileURLToPath } from 'node:url'
import { resolve } from 'node:path'
const root = fileURLToPath(new URL('../', import.meta.url))
const result = spawnSync(resolve(root, 'node_modules/.bin/slidev'), [
  'build', resolve(root, 'slides/slides.md'), '--base', '/slides/',
  '--out', resolve(root, 'public/slides'),
], { cwd: root, stdio: 'inherit' })
process.exit(result.status ?? 1)
