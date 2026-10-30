import test from 'node:test'
import assert from 'node:assert/strict'
import { readFileSync } from 'node:fs'
import { runInNewContext } from 'node:vm'
test('the offline file uses calculation code that passes the known cases', () => {
 const html=readFileSync(new URL('../public/resources/quote-calculator.html', import.meta.url),'utf8')
 const actual=html.split('<script>')[1]!.split('const area =')[0]!
 const calculate=runInNewContext(actual+'; calculateQuote')
 assert.equal(calculate(100,3,true).total,34104)
 assert.equal(calculate(100,3,false).total,27144)
 assert.equal(calculate(400,3,true).total,115536)
 for(const area of [0,-1,NaN,Infinity,Number.MAX_VALUE]) assert.equal(calculate(area,3,true),null)
 assert.doesNotMatch(html, /<script[^>]+src=|<link[^>]+href=/)
})
