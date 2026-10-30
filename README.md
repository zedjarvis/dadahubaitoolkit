# The AI Toolkit

The session site and Slidev presentation for Cedrouseroll Omondi at DADA HUB,
Parklands, on **31 October 2026, 9:20–10:20 AM EAT**.

## Public site

The workshop is published at https://dadahubaitoolkit.vercel.app/.
The welcome page has a QR code that opens `/toolkit` directly on attendees' phones.
The toolkit, demos, resources and calculator are available without an account.
The presentation is at `/slides/index.html` and uses hash navigation so slide
links work on the deployed host.

## Phone experience

The welcome QR encodes `https://dadahubaitoolkit.vercel.app/toolkit`, so scanning
opens the attendee toolkit directly. The site logo also returns to `/toolkit`.
The QR welcome page remains at `/` for the presenter to display.

Phone navigation keeps Demos, Resources and Slides visible. The toolkit uses a
compact introduction, readable demo descriptions, large touch controls and a
single-column prompt view. Source downloads and AI-tool links appear before the
prompt. Form text is at least 16px on phones to avoid automatic input zoom.

## Run locally

Use Node.js 24 and npm. The calculation tests use Node's built-in TypeScript support.

```bash
npm install
npm run dev
```

Open `http://localhost:3000`. In a second terminal:

```bash
npm run slides
```

Open `http://localhost:3030`. Press **P** for presenter mode, **Space** to advance
and **O** for the overview. Speaker notes contain the timing, demo sequence,
expected answers and fallback cues. The two appendix slides follow the close: 25 session slides and 2 appendix slides in total.

The site's **Start the presentation** button uses the static deck built into `public/slides`.
If you have just changed the slides, rebuild that copy:

```bash
npm run slides:build
```

For a production build of both:

```bash
npm run build:all
npm run preview
```

No accounts, API keys or live AI integrations are required to use the session site.
The session site helps you copy prompts into your signed-in ChatGPT, Codex and
NotebookLM accounts. The chart and calculator are prepared reference examples.

## Stack and structure

- Nuxt **4.6.3**, Vue 3 and Tailwind CSS **4.3.3** via `@tailwindcss/vite`.
- Slidev **53.0.0**, with the requested **slidev-theme-unicorn 1.1.2**.
- `app/`: responsive session site, prompt pages and calculator route.
- `slides/slides.md`: editable presentation with speaker notes.
- `slides/uno.config.ts`: current UnoCSS equivalents for Unicorn's legacy Windi shortcuts.
- `slides/layouts/table-contents.vue`: the original Unicorn layout with its missing header prop declared.
- `slides/style.css`: session-specific layout sizing, retaining Unicorn's purple palette and Gilroy headings.
- `lib/`: the calculation logic and Vue calculator used by both the app and slides.
- `public/resources/`: the demo kit, fictional source document and participant reference.
- `docs/`: asset provenance and third-party notices.
- `tests/business.test.ts`: actual calculation checks against independent answers.

Tailwind styles the Nuxt site. Slidev uses its own UnoCSS integration so the
Unicorn theme can keep its expected styling without two CSS resets competing.
The lockfile pins Floating Vue 5.2.2 for the tooltip API used by Slidev's Twoslash integration.
All fonts and images are local. No external image or font fetch is needed to
view the site or deck after starting the local server.

## Portrait options

The opening slide uses `slides/public/images/ced-illustrated.png`, made with the
built-in image generation tool from the supplied photograph, following the
Unicorn example's illustrated treatment.

To use the original, change the first slide's `introImage`:

```yaml
introImage: /images/ced-original.jpg
```

On phones, the toolkit always shows the illustrated portrait. The **Original photo**
toggle remains available on larger screens. Both assets are included locally.

## Company introductions

Flowt and SchoolBooks each have a dedicated slide with a clickable website link
and their official logos and brand-coloured QR codes. The codes point directly to `https://flowt.africa/`
and `https://www.schoolbooks.ke/`; no URL shortener or tracking service is used.

## Working with AI in Slidev

This project follows [Slidev's AI workflow](https://sli.dev/guide/work-with-ai).
The presentation stays in Markdown and Vue so an agent can edit the actual source.
The Slidev skill already available in this environment guided authoring.

When the Slidev development server is running, its MCP endpoint is:

```text
http://localhost:3030/__mcp
```

A standalone stdio server is also available:

```bash
npm run slides:mcp
```

Connect either endpoint through your agent's supported MCP settings. This project
does not modify global agent settings or claim that an MCP connection is already
registered. The original upstream theme is
[Dawntraoz/slidev-theme-unicorn](https://github.com/dawntraoz/slidev-theme-unicorn).

## Validation and PDF fallback

```bash
npm test
npm run typecheck
npm run build:all
npm run slides:export -- --executable-path /usr/bin/google-chrome
```

If Chrome is installed elsewhere, adjust the executable path. The standard
Slidev exporter uses Playwright. `exports/the-ai-toolkit.pdf` is a static backup
and does not include interactive calculator behaviour. The editable deck and
presenter notes remain in `slides/slides.md`.

The stock dataset is fictional. The calculator assumes KES 18/m²/visit,
52/12 weeks per month, KES 6,000/month for windows and an illustrative 16% VAT
on the subtotal. These are explicit teaching assumptions, not verified market
rates or advice on real tax treatment.

## Rehearsal

1. Open the site and slides on the actual presenting laptop.
2. Sign in to ChatGPT, Codex and NotebookLM / Gemini Notebook.
3. Import the fictional RFQ before the session.
4. Run every prompt once and save the actual outputs locally.
5. Start the Codex calculator task at the end of the document demo. Review it
   after the stock demo.
6. If the live build stalls, identify the prepared calculator as the fallback.
7. Protect the workflow exercise at 10:07, questions at 10:13 and the handover at 10:20.

Share https://dadahubaitoolkit.vercel.app/toolkit with attendees, or display the welcome
page so they can scan the QR. All presentation demo links use the public address.

The site saves a participant's Monday commitment only in their browser's local
storage. It does not send that field anywhere.

## Vercel

`vercel.json` uses Vercel's Nuxt framework support and builds Slidev before Nuxt.
The install step skips Playwright's browser download; Chrome is only needed for
local PDF exports. The published site serves the already exported PDF.

```bash
vercel --prod
```

The public GitHub repository is `zedjarvis/dadahubaitoolkit`.
Local preparation notes, the original source playbook, generated build directories,
Vercel connection state and environment files are excluded from version control.

## Revised business-day session

The 27-slide deck follows fictional Safi Services & Supplies. `/rehearsal` has the exact 60-minute run sheet, spoken cues, full prompts and failure routes. `/workflow` is a browser-only rule-based intake demo with duplicate detection, missing-information holds and deliberate approval. It does not call AI or connect to email. `/tools` contains 14 tasks, 24 tools, conditional recommendations and first-party sources checked on 31 October 2026.

The standalone `public/resources/quote-calculator.html` works offline. The demo kit includes prepared answers and separately labelled observed rehearsal notes. Workflow plans and Monday commitments are stored only in the current browser; demo intake records are memory-only.
