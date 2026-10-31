---
theme: unicorn
title: The AI Toolkit
titleTemplate: '%s · DADA HUB'
author: Cedrouseroll Omondi
info: |
  A practical 60-minute session for business owners at DADA HUB, Parklands.
  Saturday 31 October 2026, 9:20–10:20 AM EAT.
  ChatGPT, Codex and NotebookLM.
colorSchema: light
layout: intro
introImage: /images/ced-illustrated.png
logoHeader: /favicon.svg
website: 'DADA HUB · 31 October 2026'
aspectRatio: 16/9
canvasWidth: 980
routerMode: hash
fonts:
  sans: DM Sans
  provider: none
defaults:
  layout: default
  logoHeader: /favicon.svg
  website: 'The AI Toolkit · Cedrouseroll Omondi'
  transition: fade
drawings:
  enabled: true
  persist: false
duration: 60min
timer: countdown
presenter: true
browserExporter: true
selectable: true
download: false
exportFilename: the-ai-toolkit
favicon: /favicon.svg
---

# The AI<br>Toolkit

<div class="subtitle">AI for your everyday<br>business tasks.</div>
<div class="speaker">Cedrouseroll Omondi</div>
<div class="event">DADA HUB, Parklands<br>31 October 2026 · 9:20–10:20 AM EAT</div>

<!--
09:20–09:21:30. Say: “Before I introduce myself, imagine this enquiry has arrived while you are out on a job. Can we give a useful reply without promising something we cannot deliver?” Switch to the prepared ChatGPT tab and run the opening hook from /rehearsal. Allow 30 seconds, then use the saved rehearsal output if needed. Check budget, date and windows with the room.
Introduce yourself in one sentence before the next two company slides. The illustrated portrait uses the speaker's supplied photo. Full minute-by-minute script: https://dadahubaitoolkit.vercel.app/rehearsal
-->

---
class: company-flowt
title: Flowt
logoHeader: ''
---

<h1 class="company-heading"><img class="company-flowt-logo" src="/brands/flowt.png" alt="Flowt" /></h1>

<div class="company-intro">
<div>
<p class="company-statement">Financial intelligence that unlocks capital for small &amp; <span style="white-space:nowrap">mid-size</span> businesses in emerging markets</p>
</div>
<figure class="company-qr">
<a href="https://flowt.africa/" target="_blank" rel="noopener noreferrer" aria-label="Visit Flowt at flowt.africa"><img src="/qr/flowt.png" alt="QR code linking to https://flowt.africa/" width="296" height="296" /></a>
<figcaption><span>Scan to explore</span><a href="https://flowt.africa/" target="_blank" rel="noopener noreferrer">flowt.africa ↗</a></figcaption>
</figure>
</div>

<!--
09:21:30–09:21:50. "Financial intelligence that unlocks capital for small & mid-size businesses in emerging markets." Keep this introduction to 20 seconds. The QR and clickable link go directly to https://flowt.africa/. Use the user's corrected description; do not describe Flowt as generic business software or add financing rates or eligibility claims.
-->

---
class: company-schoolbooks
title: SchoolBooks
logoHeader: ''
---

<h1 class="company-heading"><img class="company-schoolbooks-logo" src="/brands/schoolbooks.svg" alt="" /><span>SchoolBooks</span></h1>

<div class="company-intro">
<div>
<p class="company-statement">AI agents for school<br>finance and operations.</p>
<p class="company-note">Accounting, fees, payroll and everyday administration, with your team in control.</p>
</div>
<figure class="company-qr">
<a href="https://www.schoolbooks.ke/" target="_blank" rel="noopener noreferrer" aria-label="Visit SchoolBooks at schoolbooks.ke"><img src="/qr/schoolbooks.png" alt="QR code linking to https://www.schoolbooks.ke/" width="296" height="296" /></a>
<figcaption><span>Scan to explore</span><a href="https://www.schoolbooks.ke/" target="_blank" rel="noopener noreferrer">schoolbooks.ke ↗</a></figcaption>
</figure>
</div>

<!--
09:21:50–09:22:10. Introduce SchoolBooks as a separate part of your work: AI agents for school finance and operations. The website describes connected accounting, fees, people, payroll and operations, with human approvals. The QR and clickable link go directly to https://www.schoolbooks.ke/. Keep this to 20 seconds and transition: "Let’s get the session toolkit open on your phones."
-->

---
class: follow-along
title: Scan to follow along
---

<div class="follow-along-grid">
<div>
<div class="kicker">Your session toolkit</div>
<h1>Scan to<br>follow along.</h1>
<p class="lead">The prompts, demo files and tools<br>are here for you to use.</p>
<p class="small">Open your phone camera and tap the link.<br>Keep the page open — we’ll use it together.</p>
</div>
<figure class="follow-along-qr">
<a href="https://dadahubaitoolkit.vercel.app/toolkit" target="_blank" rel="noopener noreferrer" aria-label="Open the session toolkit"><img src="/qr/session.png" alt="Scan to open dadahubaitoolkit.vercel.app/toolkit" width="340" height="340" /></a>
<figcaption>Opens straight to the toolkit.</figcaption>
</figure>
</div>
<a class="follow-along-url" href="https://dadahubaitoolkit.vercel.app/toolkit" target="_blank" rel="noopener noreferrer">dadahubaitoolkit.vercel.app/toolkit</a>

<!--
09:22:10–09:22:40. Leave this slide up for about 30 seconds. Say: “Scan this to follow along. The prompts, demo files and tools are all here, so you can try things with me and keep them afterwards. Open your camera, tap the link, and keep the toolkit open.” The QR opens /toolkit directly, not the welcome QR page. If scanning is difficult, read the visible URL and ask someone nearby to share the link. Then introduce Safi Services & Supplies. Keep the opening within three minutes.
-->

---

<div class="kicker">One business / one working day</div>

# Meet Safi Services & Supplies.
<p class="lead">Office cleaning. Cleaning supplies.<br>A small team with a full day ahead.</p>
<div class="four-beats"><div><span class="label">Morning</span><p>Enquiries, marketing and an RFQ.</p></div><div><span class="label">Afternoon</span><p>Stock decisions and an estimate.</p></div></div>
<p class="small mt-7">Leave with a checked draft and a routine you can reuse.</p>

<!--
09:22:40–09:23. The client is Parklands Learning Centre. Explain that the business-day clock shows the sequence of work; the session clock remains 09:20–10:20. This is not a product tour or an installation clinic.
-->

---

<div class="kicker">08:00 / An enquiry arrives</div>

# When the same steps repeat.
<div class="flow"><div class="flow-step">Enquiry<small>A clear trigger</small></div><span class="flow-arrow">→</span><div class="flow-step">Record<small>Check for duplicates</small></div><span class="flow-arrow">→</span><div class="flow-step">Draft<small>Pause if facts are missing</small></div><span class="flow-arrow">→</span><div class="flow-step">Review<small>A person approves</small></div></div>
<a class="live-link" href="https://dadahubaitoolkit.vercel.app/workflow" target="_blank">Open the working local example ↗</a>
<p class="small">Fixed rules in the browser. No AI or email connection. Nothing is sent.</p>

<!--
09:23–09:26. Open /workflow. Submit SAFI-001 with windows blank: a record and template draft appear, held for clarification. Approval is disabled. Resubmit same ID: duplicate rejected. Resolve the held record with confirmed window details; the same ID is preserved. Review and explicitly approve the revised draft. The browser automates these local steps. Explain the lack of external app connections rather than implying a connected Make/Gmail workflow. If unavailable, trace the three cases on this slide and label it a walkthrough.
-->

---

# Three different ways to get help.
<div class="three"><div class="rule"><h2>A draft</h2><p class="small">You ask.<br>The AI suggests.<br>You review.</p></div><div class="rule"><h2>A tool</h2><p class="small">You open it.<br>It applies agreed rules.<br>You check the result.</p></div><div class="rule"><h2>A workflow</h2><p class="small">An event starts it.<br>Connected steps run.<br>Exceptions reach a person.</p></div></div>
<p class="small mt-8">Make · Zapier · n8n can connect authorised apps after setup.</p>

<!--
09:26–09:27. Keep this distinction to one minute. Distinguish a diagram, the local demonstration, and a fully connected automation. Never suggest that copying a prompt installs an integration. Explain that rules often handle the reliable steps; AI is useful where language and judgment assistance are needed. Tool sources and setup considerations are on /tools#automation.
-->

---
class: scenario-slide
---

<div class="kicker">08:15 / Sales & marketing · ChatGPT</div>

# A lead waiting. A quiet business page.
<div class="two"><div><p class="lead">The owner is out on a job.<br>A contract enquiry sits in WhatsApp.</p><p class="small">Safi needs to reply today and keep attracting suitable customers next week.</p></div><div class="rule"><h2>Two useful results</h2><p class="small">A reply that moves the enquiry forward.<br>Three posts built around customer questions.<br>One saved brief for the next run.</p></div></div>
<p class="small mt-7">Same method: an interior-design proposal, an admissions enquiry or a retail campaign.</p>

<!--
09:27–09:28. Say: “You’re on a job, a promising enquiry lands in WhatsApp, and your business page has gone quiet. Let’s move the client forward, then plan this week’s marketing.” Give the context before showing the tool. The goal is a next step and suitable enquiries, not simply polished wording.
-->
---

# Give the client a useful next step.
<div class="note-sheet">400 m² · three evenings a week<br>Monthly windows · details still missing<br><strong>KES 120,000 is the client’s budget</strong><br>16 November is a requested start date</div>
<a class="live-link" href="https://dadahubaitoolkit.vercel.app/demos/proposal" target="_blank">Copy the full client-reply prompt ↗</a>

<!--
09:28–09:30. Run the full revised prompt. Check that the five-section email stays under 180 words, budget is not a quote, date is conditional and home cleaning is absent from the customer email. Show internal checks separately. Keep WhatsApp, shortening and price-objection follow-ups on the page as take-home options. The rehearsal originally mentioned home cleaning in the email; the revised prompt explicitly excludes it. Use the saved corrected run if stalled longer than 45 seconds.
-->

---

<div class="kicker">08:45 / Bring in the next enquiry</div>

# Who is this post for?
<div class="four-beats"><div><span class="label">Audience</span><p>Office managers in Parklands.</p></div><div><span class="label">Offer</span><p>Office cleaning, scoped before pricing.</p></div><div><span class="label">Next step</span><p>DM OFFICE + location, area, schedule.</p></div><div><span class="label">Measure</span><p>Qualified enquiries after seven days.</p></div></div>
<a class="live-link" href="https://dadahubaitoolkit.vercel.app/demos/proposal#marketing" target="_blank">Run the weekly marketing brief ↗</a>
<p class="small">Aim for three qualified enquiries. A target, not a promise.</p>

<!--
09:30–09:31. The same business needs new leads. Keep private client details out of public copy. Run the full marketing prompt, which includes the approved facts. Ask: “Who is this for and what should they do next?” Instagram and WhatsApp Status are the channels for this experiment; participants should use channels their own customers already use.
-->

---

# Three posts. Three different jobs.
<div class="three"><div class="rule"><h2>Monday</h2><p class="small"><strong>Answer a question.</strong><br>What details help us quote?<br>A simple checklist graphic.</p></div><div class="rule"><h2>Wednesday</h2><p class="small"><strong>Explain the process.</strong><br>How do we plan around office hours?<br>Your own equipment photo.</p></div><div class="rule"><h2>Friday</h2><p class="small"><strong>Invite an enquiry.</strong><br>Planning regular cleaning?<br>DM OFFICE with three details.</p></div></div>
<p class="lead mt-7">A useful answer. A clear next step.</p>
<p class="small">Check facts and the image. Publish manually. Record actual enquiries.</p>

<!--
09:31–09:33. Inspect the generated Monday caption or show the worked example on the page. Read the opening and CTA only. Point to the visual brief, the shorter WhatsApp Status version and enquiry-tracking columns. Three posts give the audience a repeatable marketing process; extra captions alone do not. Do not generate an image on stage. The Canva brief is available as an optional follow-up. If the response stalls, use the prepared plan and caption and identify them as prepared.
-->

---

<div class="kicker">Keep it / Sales & Content Kit</div>

# Next week should start here.
<div class="three"><div class="rule"><h2>Save</h2><p class="small">One business brief.<br>Two prompts.<br>One approved example.</p></div><div class="rule"><h2>Update</h2><p class="small">New client notes or a new weekly goal.<br>Keep private notes out of public copy.</p></div><div class="rule"><h2>Review</h2><p class="small">Check the draft.<br>Publish yourself.<br>Record enquiries and next steps.</p></div></div>
<a class="live-link" href="https://dadahubaitoolkit.vercel.app/demos/proposal#keep-it" target="_blank">Copy the kit & get the editable planner ↗</a>
<p class="small">Keep it in a document you can open on your phone. Name the person responsible.</p>

<!--
09:33–09:35. Copy the reusable template into a prepared document or note. Show its name and where to reopen it. A ChatGPT Project is optional for shared context; a saved document works too. Demonstrate the actual saving step rather than just advising “save it”. Do not start a new account or connect a publishing app. Owner reviews the brief each week; measure qualified enquiries, site visits and quote requests, not made-up reach or sales.
-->

---
layout: center
---

<div class="kicker">Your turn / 3 minutes</div>

# One draft you can use again.
<p class="lead">Choose a reply or a post.<br>Change the brief.<br>Check one claim. Save the result.</p>
<p class="small mt-7">No account open? Pair up or edit the prepared reply.</p>

<!--
09:35–09:38. Give three full minutes for a reply or one post. At 09:38 take one example and ask where they will save it. Ask what they edited before using it. The participant leaves with a useful output rather than only watching. Protect this exercise if running late. End at 09:39.
-->

---
class: scenario-slide
---

<div class="kicker">10:00 / The RFQ arrives · NotebookLM</div>

# A good proposal can still lose.
<div class="two"><div><p class="lead">The client now wants a formal bid.</p><p class="small">A missing document or a misunderstood deadline can undo the work. Window scope still needs an answer.</p></div><div class="rule"><h2>What we need back</h2><p class="small">A checklist tied to the current RFQ.<br>Only the stated rejection grounds.<br>Questions, owners and due dates.</p></div></div>
<p class="small mt-7">The decision: can we submit a complete bid, and what must we clarify first?</p>

<!--
09:39–09:40. Give the business consequence before opening the preloaded notebook. Select only the current RFQ. The presenting account may label the product Gemini Notebook. Do not spend stage time uploading. A citation is an invitation to inspect the evidence, not proof that the interpretation is right.
-->
---

# Where does that answer come from?
<div class="two"><div><div class="big-value">6 Nov</div><p class="stat-label">12:00 noon EAT</p><p class="small">Submission deadline · Section 4</p></div><div class="rule"><h2>Open the citation.</h2><p class="lead">Read the passage.<br>Check the interpretation.</p><p class="small">The site visit is optional.</p></div></div>
<a class="live-link" href="https://dadahubaitoolkit.vercel.app/demos/research" target="_blank">Open the source & compact checklist prompt ↗</a>

<!--
09:40–09:44. Ask for the compact checklist. Open the deadline citation and read the original Section 4. Check optional site visit, six mandatory items and only the four explicit rejection grounds. Text source sections are not PDF page numbers. The rehearsal revealed an ambiguous phrase “mandatory insurance coverage” for an absent condition; the revised prompt excludes that inference. Cite, inspect, then decide.
-->

---

# “Not specified” is useful.
<div class="prompt-excerpt">How many windows?<br>What size and height?<br>Can we safely reach them?</div>
<p class="lead mt-8">The source does not establish those answers.</p>
<p class="small">Ask a clarification question before quoting.</p>

<!--
09:44–09:46. Run the missing-window follow-up. Open Section 1 or 6 to confirm missing details. Ask the room whether they would quote now. If the product fails, use the local source and prepared checklist; do not simulate model citations. The distinction between missing facts and a plausible answer is the learning point.
-->

---

<div class="kicker">Keep it / RFQ Review Folder</div>

# A checklist someone can act on.
<div class="three"><div class="rule"><h2>Keep the source</h2><p class="small">One notebook per opportunity.<br>Current RFQ and official updates.</p></div><div class="rule"><h2>Assign the work</h2><p class="small">Requirement → evidence.<br>Owner → internal due date → status.</p></div><div class="rule"><h2>Recheck changes</h2><p class="small">An addendum changes the evidence.<br>Review the affected answers again.</p></div></div>
<a class="live-link" href="https://dadahubaitoolkit.vercel.app/demos/research#keep-it" target="_blank">Save your RFQ review routine ↗</a>

<!--
09:46–09:47. Save the checked checklist into a document or sheet with owner and internal due date left for a person to fill. Bookmark the notebook and checklist. A saved generated answer does not automatically become current after a source changes. Keep one opportunity separate from the next. Then start Codex at 09:47 as planned.
-->

---

# Start a task. Inspect it later.
<div class="four-beats"><div><span class="label">Goal</span><p>A cleaning quote calculator.</p></div><div><span class="label">Rules</span><p>Area, visits, windows, tax assumption.</p></div><div><span class="label">Deliverable</span><p>One offline HTML file.</p></div><div><span class="label">Checks</span><p>Known totals and invalid inputs.</p></div></div>
<a class="live-link" href="https://dadahubaitoolkit.vercel.app/demos/calculator" target="_blank">Copy the Codex brief ↗</a>

<!--
09:47–09:48. In an already prepared empty folder, submit the complete task to Codex. Say: “We’ll inspect its result after the stock exercise.” No deployment or external sending is requested. Setup or permissions problems trigger the checked fallback later; do not solve them on stage.
-->

---
class: scenario-slide
---

<div class="kicker">13:00 / Stock & money · ChatGPT</div>

# Sales are up. Is the cash working?
<div class="two"><div><p class="lead">The owner needs to buy stock again.</p><p class="small">Some supplies sell quickly. Others tie up cash on the shelf. The sales sheet has eight products and 30 days of figures.</p></div><div class="rule"><h2>What we need back</h2><p class="small">Profit contribution and slow movers.<br>Calculations we can reconcile.<br>Questions to resolve before ordering.</p></div></div>
<p class="small mt-7">The decision: what to replenish, hold or investigate after checking cash and lead times.</p>

<!--
09:48–09:49. Ask which product contributes most gross profit. A high unit price or margin percentage is not the same as total profit contribution. Introduce the buying decision and the missing constraints before asking the tool for calculations.
-->
---

# Which product earns the most?
| Product | Sold | Cost / unit | Price / unit |
|---|---:|---:|---:|
| Multipurpose cleaner 2L | 95 | 310 | 380 |
| Floor cleaner 5L | 70 | 720 | 850 |
| Bleach 1L | 88 | 170 | 210 |
| Microfibre pack | 12 | 350 | 480 |
| Toilet paper 10 pack | 82 | 380 | 450 |
<p class="small">Selected rows from the 30-day dataset. Amounts in KES.</p>
<a class="live-link" href="https://dadahubaitoolkit.vercel.app/demos/stock" target="_blank">Open all eight rows & the analysis prompt ↗</a>

<!--
09:49–09:51. Paste the full dataset and prompt. Claim calculation-tool use only if visible in the interface. No restocking, returns, shrinkage, price changes or stockouts are assumed. Top-ups additionally assume unchanged demand, instant delivery and no safety stock. If generation stalls or disagrees with the key, use the checked CSV and do one row together.
-->

---

# Floor cleaner contributes the most.
<ProfitChart />
<p class="tiny">Gross profit from units sold, in KES. Independently checked reference chart.</p>

<!--
09:51–09:53. Top three: floor cleaner 9,100; multipurpose cleaner 6,650; toilet paper 5,740. Microfibre packs have a higher margin percentage than floor cleaner but less total contribution. This is a prepared reference chart, not a live model output. Generating another chart is optional and is cut first if behind.
-->

---

# Check a row. Check the label.
<div class="two"><div><div class="big-value">30,295</div><p class="stat-label">KES gross profit</p></div><div class="rule"><p class="small">Revenue <strong>KES 179,640</strong><br>Cost of units sold <strong>KES 149,345</strong></p><p class="lead">Overheads are missing.<br>Net profit is unknown.</p></div></div>
<p class="small mt-7">Floor cleaner: 70 × (850 − 720) = KES 9,100</p>

<!--
09:53–09:56. Give pairs two minutes to calculate floor cleaner and multipurpose cleaner (95 × 70 = 6,650). Correct rows do not prove all totals; reconcile the whole table with the key. Ask what matters before ordering: lead time, future demand, storage and cash. Simple top-ups: multipurpose cleaner70, floor cleaner60, bleach76, toilet paper74. They are quantities based on the stated assumptions, not a final ordering instruction. Return to Codex at 09:57.
-->

---

<div class="kicker">Keep it / Monthly Stock Review</div>

# Same review. Fresh numbers.
<div class="three"><div class="rule"><h2>Duplicate</h2><p class="small">A master spreadsheet.<br>A dated source export.<br>The same saved questions.</p></div><div class="rule"><h2>Reconcile</h2><p class="small">Totals and two worked rows.<br>Check restocks, returns and price changes.</p></div><div class="rule"><h2>Record</h2><p class="small">Buy, wait or investigate.<br>Reason, approver and review date.</p></div></div>
<a class="live-link" href="https://dadahubaitoolkit.vercel.app/demos/stock#keep-it" target="_blank">Copy the monthly review template ↗</a>

<!--
09:56–09:57. Show where the source, checked result and decision log live together. New period, new inputs and assumptions. A correct row does not prove the whole sheet: reconcile totals. Do not turn the calculated top-up into an order without lead times, cash and demand.
-->

---
class: scenario-slide
---

<div class="kicker">15:00 / A reusable estimate · Codex</div>

# Tomorrow brings another enquiry.
<div class="two"><div><p class="lead">Stop copying the same formula.</p><p class="small">Safi needs an estimate the team can reopen, change and check on a phone. The rules must be agreed before the tool is built.</p></div><div class="rule"><h2>What we need back</h2><p class="small">A working calculator file.<br>Clear rates and assumptions.<br>Known totals and invalid-input checks.</p></div></div>
<p class="small mt-7">The decision: is this approved for estimating, and what remains before a final quote?</p>

<!--
09:57–09:58. Inspect the task started at 09:47. If unfinished, identify and open the prepared offline fallback. Show the delivered file and checks, not a code lecture. An attractive screen alone is not acceptance.
-->
---

# The work includes the checks.
<div class="flow"><div class="flow-step">Brief<small>Goal and rules</small></div><span class="flow-arrow">→</span><div class="flow-step">Build<small>Actual files</small></div><span class="flow-arrow">→</span><div class="flow-step">Test<small>Known cases</small></div><span class="flow-arrow">→</span><div class="flow-step">Review<small>Your decision</small></div></div>
<p class="lead mt-10">A finished-looking screen still needs testing.</p>

<!--
09:58–09:59. Show actual delivery summary and performed tests, not source code. Explain average monthly visits = weekly visits × 52 / 12. Explain the rates and the 16% tax assumption used in the estimate. Do not claim that ChatGPT cannot build tools or that an agent is infallible.
-->

---

# A quote in a few clicks.
<WorkshopCalculator />

<!--
09:59–10:03. Prefer the live delivered file, otherwise label this as a prepared checked example. Test 100m²,3visits,windows =34,104; windows off=27,144; blank area=no valid quote. Back to400m² with windows=115,536. Ask someone to identify the tax and window line items. Offline fallback: quote-calculator.html in the downloaded kit.
-->

---

# Under budget is not ready to send.
<div class="two"><div><div class="big-value">115,536</div><p class="stat-label">KES monthly estimate</p><p class="small">KES 4,464 below the client’s budget.</p></div><div class="rule"><h2>What is still unknown?</h2><p class="lead">Window scope.<br>Safe access.<br>Availability.</p></div></div>

<!--
10:03–10:05. Tie the calculator back to NotebookLM’s missing facts. A correct formula does not validate commercial assumptions. Keep the print-button enhancement as a take-home follow-up. This is the perspective shift: useful work combines generation, rules, evidence and a responsible reviewer.
-->

---

<div class="kicker">Keep it / Saved Estimate Calculator</div>

# One approved copy. Easy to reopen.
<div class="three"><div class="rule"><h2>Keep</h2><p class="small">The checked file and backup.<br>A bookmark or reviewed team URL.</p></div><div class="rule"><h2>Own</h2><p class="small">Rates, assumptions and review date.<br>One person responsible for pricing.</p></div><div class="rule"><h2>Retest</h2><p class="small">Known totals after every rule change.<br>Missing inputs must still show errors.</p></div></div>
<a class="live-link" href="https://dadahubaitoolkit.vercel.app/demos/calculator#keep-it" target="_blank">Copy the simple calculator handover ↗</a>
<p class="small">A local file is not automatically a website. Test the actual link you share.</p>

<!--
10:05–10:07. Demonstrate reopening the approved file or bookmarked workshop URL. Explain how to keep a rate card and how to request a change. A helper can publish a reviewed calculator for team access if needed. Do not set up hosting on stage. The print enhancement is optional take-home work.
-->

---

<div class="kicker">17:00 / Your business</div>

# Design one repeatable workflow.
<div class="commit-lines"><p>What starts it? What happens next?</p><p>Who checks it? What could go wrong?</p><p>What will you measure in the first five runs?</p></div>
<a class="live-link" href="https://dadahubaitoolkit.vercel.app/workflow" target="_blank">Write your workflow plan ↗</a>

<!--
10:07–10:11. Two quiet minutes to fill the five fields on /workflow or paper, then two minutes comparing with a neighbour. Each person names one detail that must never be invented and one exception for a human. Protect this exercise even if earlier demos ran late.
-->

---

# Start with the job.
<div class="two"><div class="rule"><h2>Use what you have.</h2><p class="small">Try a small task.<br>Check accuracy and edits.<br>Compare time and total cost.</p></div><div class="rule"><h2>Explore what comes next.</h2><p class="small">More marketing and presentations.<br>Meetings and procedures.<br>Support, research and translation.</p></div></div>
<a class="live-link" href="https://dadahubaitoolkit.vercel.app/tools" target="_blank">20 tasks · 27 tools · official sources ↗</a>

<!--
10:11–10:13. Show the directory briefly, not every tool. Recommendations are conditional fit judgments, not head-to-head benchmark rankings. Each card has a prompt, setup considerations, checks and official sources, checked31Oct2026. Start with one internal record or notification before connecting AI and outbound communication. Close exercise at10:13.
-->

---
layout: center
---

# What does your business need done?
<p class="lead">The task.<br>The information you have.<br>The result you would check.</p>

<!--
10:13–10:18. Take two or three concrete questions. Use /tools to identify a starting point. Do not start a new account setup or an unprepared build. A connected automation needs configured accounts, permissions, failure handling and a cost owner. Remind participants to use authorised data. If quiet, ask which weekly step involves copying the same information twice.
-->

---
layout: center
---

# One task on Monday.
<p class="lead">A clear brief. A check. A person responsible.</p>
<p class="small mt-8">dadahubaitoolkit.vercel.app/toolkit</p>
<p class="small">Prompts · marketing planner · reusable guides · offline kit</p>

<!--
10:18–10:20. Say: “At the start we asked AI for a reply. Now we have a sales brief, marketing plan, RFQ checklist, stock review and a calculator we can reopen. The useful change is from asking AI occasionally to designing a repeatable way of working. Start with one task on Monday.” Confirm organiser handoff details before naming the next speaker. Thank the room and finish at10:20.
-->

---

<div class="kicker">Appendix / fallback route</div>

# Keep the lesson. Change the screen.
<div class="two"><div class="rule"><h2>If a tool stalls</h2><p class="small">Opening: allow 30 seconds.<br>Later responses: 45 seconds.<br>One recovery attempt.<br>Then identify the prepared fallback.</p></div><div class="rule"><h2>If time runs short</h2><p class="small">Skip chart generation.<br>Skip the print enhancement.<br>Protect participant practice.<br>Finish at 10:20.</p></div></div>
<a class="live-link" href="https://dadahubaitoolkit.vercel.app/rehearsal" target="_blank">Exact words, prompts and fallbacks ↗</a>

<!--
Appendix only. The PDF is static. The downloaded standalone calculator works offline; ChatGPT and notebook need network and account access. Prepared reference answers are labelled separately from observed rehearsal outputs. Rehearse the projector and room network before attendees arrive.
-->

---

<div class="kicker">Appendix / evidence and assumptions</div>

# Sources and further options
<div class="source-list">

- [Tool directory: task fit, setup and official sources](https://dadahubaitoolkit.vercel.app/tools)
- [Google: notebook chat and source citations](https://support.google.com/gemininotebook/answer/16179559?hl=en)
- [OpenAI: what ChatGPT Work can do](https://learn.chatgpt.com/docs/use-chatgpt)
- [OpenAI: projects and reusable context](https://learn.chatgpt.com/docs/projects)
- [Mailchimp: content planning and measurement](https://mailchimp.com/resources/content-calendar/)
- [Make: visual workflow platform](https://www.make.com/en/product)
- [Slidev: work with AI](https://sli.dev/guide/work-with-ai) · [Unicorn theme](https://github.com/dawntraoz/slidev-theme-unicorn)

</div>
<p class="tiny mt-8">Confirm rates, demand and applicable taxes before using an estimate. Source review: 31 October 2026. Product access varies. Tool-fit recommendations are editorial judgments, not measured rankings. The portrait is AI-stylised from the speaker’s photograph.</p>

<!--
Appendix only. Read the rehearsal audit for what was actually tested. No connected external automation is claimed. The local workflow and offline calculator are implemented and checked artifacts.
-->
