#!/usr/bin/env python3
"""Build the workshop's print-ready PDF handouts and distribution ZIP.

Requires Python 3, reportlab and pypdf. Uses embedded Lato fonts when installed,
or ReportLab's bundled Vera family. No network access or external services.
"""
from pathlib import Path
import csv, json, re, zipfile
from html import escape
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
    Spacer, Table, TableStyle, PageBreak, KeepTogether, Flowable)
from pypdf import PdfReader
import reportlab

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public/resources'
SRC = ROOT / 'resources/source'
PURPLE = colors.HexColor('#8720A8')
INK = colors.HexColor('#291D35')
MUTED = colors.HexColor('#6F6477')
PALE = colors.HexColor('#F5EFF9')
LINE = colors.HexColor('#DDD0E5')
WHITE = colors.white
W, H = A4
M = 46
CW = W - M * 2
BASE = 'https://dadahubaitoolkit.vercel.app'

font_dir = Path('/usr/share/fonts/truetype/lato')
fallback = Path(reportlab.__file__).parent / 'fonts'
for name, lato, vera in [('Body','Lato-Regular.ttf','Vera.ttf'),('Bold','Lato-Bold.ttf','VeraBd.ttf'),('Italic','Lato-Italic.ttf','VeraIt.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(font_dir/lato if (font_dir/lato).exists() else fallback/vera)))
pdfmetrics.registerFontFamily('Body', normal='Body', bold='Bold', italic='Italic', boldItalic='Bold')

styles = {
    'body': ParagraphStyle('body', fontName='Body', fontSize=10.5, leading=15, textColor=INK, spaceAfter=8, allowWidows=0, allowOrphans=0),
    'small': ParagraphStyle('small', fontName='Body', fontSize=9, leading=12.5, textColor=MUTED, spaceAfter=6),
    'title': ParagraphStyle('title', fontName='Bold', fontSize=29, leading=32, textColor=INK, spaceAfter=12, keepWithNext=True),
    'h1': ParagraphStyle('h1', fontName='Bold', fontSize=21, leading=25, textColor=INK, spaceAfter=12, keepWithNext=True),
    'h2': ParagraphStyle('h2', fontName='Bold', fontSize=13, leading=17, textColor=PURPLE, spaceBefore=10, spaceAfter=7, keepWithNext=True),
    'label': ParagraphStyle('label', fontName='Bold', fontSize=8.5, leading=12, textColor=PURPLE, spaceAfter=8, charSpace=1),
    'quote': ParagraphStyle('quote', fontName='Body', fontSize=13, leading=19, textColor=INK, spaceAfter=8),
    'prompt': ParagraphStyle('prompt', fontName='Body', fontSize=10, leading=14, textColor=INK, spaceAfter=8),
    'cell': ParagraphStyle('cell', fontName='Body', fontSize=9, leading=12, textColor=INK, spaceAfter=0),
    'th': ParagraphStyle('th', fontName='Bold', fontSize=8.5, leading=11, textColor=WHITE, spaceAfter=0),
}

def clean(s):
    return str(s).replace('\u2011','-').replace('\u2013','-').replace('\u2014','-').replace('\u2212','-').replace('\u200b','').replace('\u2061','').replace('💡','Note:')

def p(s, style='body'):
    return Paragraph(escape(clean(s)).replace('\n','<br/>'), styles[style])

def link(label, url, style='small'):
    return Paragraph(f'<link href="{escape(url,quote=True)}" color="#8720A8"><u>{escape(clean(label))}</u></link>',styles[style])

def heading(s): return p(s,'h2')

def box(title, text):
    t=Table([[p(title.upper(),'label')],[p(text)]],colWidths=[CW-24])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),PALE),('BOX',(0,0),(-1,-1),0.6,LINE),('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),12),('TOPPADDING',(0,0),(-1,0),10),('BOTTOMPADDING',(0,-1),(-1,-1),7)]))
    return KeepTogether([t,Spacer(1,10)])

def table(headers,rows,widths=None,compact=False):
    if widths is None: widths=[CW/len(headers)]*len(headers)
    data=[[p(x,'th') for x in headers]]+[[p(x,'cell') for x in r] for r in rows]
    t=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),PURPLE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),('ROWBACKGROUNDS',(0,1),(-1,-1),[WHITE,PALE]),('LINEBELOW',(0,1),(-1,-1),0.4,LINE)]))
    if compact:t.setStyle(TableStyle([('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
    return t

class WritingLines(Flowable):
    def __init__(self,label,lines=2):
        super().__init__(); self.label=label; self.width=CW; self.height=31+lines*23; self.lines=lines
    def draw(self):
        c=self.canv;c.setFont('Bold',11);c.setFillColor(INK);c.drawString(0,self.height-14,self.label)
        c.setStrokeColor(LINE);c.setLineWidth(0.6)
        for i in range(self.lines):c.line(0,self.height-34-i*23,CW,self.height-34-i*23)

class Doc(BaseDocTemplate):
    def __init__(self,path,title,kind):
        super().__init__(str(path),pagesize=A4,leftMargin=M,rightMargin=M,topMargin=68,bottomMargin=53,title=title,author='DADA HUB | The AI Toolkit',subject=kind,pageCompression=1)
        self.doc_title=title; self.kind=kind
        self.addPageTemplates(PageTemplate(id='main',frames=[Frame(M,53,CW,H-121,id='main',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=self.chrome))
    def chrome(self,c,d):
        c.saveState();c.setFillColor(PURPLE);c.roundRect(M,H-41,18,18,4,fill=1,stroke=0)
        c.setFillColor(WHITE);c.setFont('Bold',13);c.drawCentredString(M+9,H-37,'+')
        c.setFillColor(INK);c.setFont('Bold',9);c.drawString(M+27,H-35,'THE AI TOOLKIT')
        c.setFillColor(MUTED);c.setFont('Body',8);c.drawRightString(W-M,H-35,'DADA HUB  /  31 OCTOBER 2026')
        c.setStrokeColor(LINE);c.setLineWidth(.6);c.line(M,41,W-M,41)
        c.setFont('Body',8);c.setFillColor(MUTED);c.drawString(M,27,self.doc_title)
        c.drawRightString(W-M,27,f'{d.page:02d}')
        c.linkURL(BASE+'/toolkit',(M,H-44,M+145,H-25),relative=0)
        c.restoreState()
    def afterFlowable(self,f):
        if isinstance(f,Paragraph) and f.style.name in ('title','h1','h2'):
            title=f.getPlainText(); key=f'page-{self.page}-{id(f)}';self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(title,key,0,False)

def intro(code,title,desc):
    return [p(code.upper(),'label'),p(title,'title'),p(desc),Spacer(1,8)]

def write(stem,title,story):
    path=OUT/(stem+'.pdf');Doc(path,title,stem).build(story)
    reader=PdfReader(path)
    assert all((pg.extract_text() or '').strip() for pg in reader.pages),stem
    print(f'{path.name}: {len(reader.pages)} pages')

def paragraphs(text,style='body'):
    return [p(re.sub(r'\s*\n\s*',' ',q).strip(),style) for q in re.split(r'\n\s*\n',text.strip()) if q.strip()]

def read(stem):return (SRC/(stem+'.txt')).read_text()

def make_rfq():
    raw=read('03-cleaning-rfq')
    parts=re.split(r'SECTION (\d) [—-] ([^\n]+)\n',raw)
    sections=[(parts[i],parts[i+1],parts[i+2].replace('END OF DOCUMENT','').strip()) for i in range(1,len(parts),3)]
    s=intro('03 / Source material','Office cleaning\nRequest for quotations','Parklands Learning Centre\nReference: RFQ-2026-001  |  Issued: 31 October 2026')

    for num,title,text in sections:
        if num=='4':s += [PageBreak(),p('03 / Source material - continued','label'),p('Submission & clarifications','h1')]
        s.append(heading(f'Section {num}  /  {title.title()}'))
        if num in ('2','5'):
            text=re.sub(r'\n(?!\d\.\d)', ' ',text)
            items=re.split(r'(?=\b'+num+r'\.\d )',text)
            for item in items:
                if item.strip():s.append(p(item.strip()))
        else:s += paragraphs(text)
    s += [Spacer(1,12),p('End of document','label')]
    write('03-cleaning-rfq','Cleaning RFQ',s)

def make_run_sheet(rehearsal):
    s=intro('01 / Presenter','Your session run sheet','Exact spoken cues, stage actions, checks and fallbacks.\n31 October 2026  |  09:20-10:20 EAT  |  60 minutes')
    s.append(box('Before the room','Open ChatGPT, the prepared notebook, Codex in an empty demo folder, the workflow lab and the offline calculator. Download the kit. Clear welcome dialogs, hide unrelated chats, and check the projector and hotspot.'))
    s.append(table(['Time (EAT)','Segment'],[[x['time'],x['title']] for x in rehearsal],[90,CW-90]))
    s += [Spacer(1,12),box('Keep the room moving','Allow 30 seconds for the opener and 45 seconds for later generations. One recovery attempt, then the prepared fallback. Cut optional chart generation and the print enhancement first. Protect participant practice and the 10:20 finish.')]
    for x in rehearsal:
        s += [PageBreak(),p(x['time']+' EAT  /  '+x['duration'],'label'),p(x['title'],'h1'),heading('Say'),p(x['say'],'quote'),heading('Do')]
        for i,step in enumerate(x['steps'],1):s.append(p(f'{i}. {step}'))
        s += [heading('What success looks like'),p(x['pass']),box('If the demo fails',x['fallback'])]
    write('01-presenter-run-sheet','Presenter run sheet',s)

def prompt_body(text):
    # Preserve wording, list/data rows and paragraphs; reflow editorial hard wraps.
    blocks=[]
    for block in text.split('\n\n'):
        if '\nTest the actual implemented' in block:
            before,after=block.split('\nTest the actual implemented',1)
            block=before+'\nTest the actual implemented'+' '.join(after.splitlines())
        lines=block.splitlines()
        if not any(re.match(r'^(?:- |\d+\. |\d+ m2|Blank,|Product,)',line) for line in lines):
            block=' '.join(lines)
        blocks.append(p(block,'prompt'))
    return blocks

def make_prompts(demos,hook):
    s=intro('02 / Copy, run, check','Exact live prompts','Select and copy the prompt text, or use the Copy buttons in the online guide.')
    s += [link('Open the online rehearsal guide',BASE+'/rehearsal'),heading('Opening hook')]+prompt_body(hook['prompt'])
    s += [box('Opening check','The budget remains a budget. The requested date stays conditional. Window count, size and height are requested.')]
    for d in demos:
        s += [PageBreak(),p(d['number']+' / '+d['tool'],'label'),p(d['title'],'h1')]
        if d['slug']=='research':s.append(p('Before starting: select only 03-cleaning-rfq.pdf in your notebook.','small'))
        s += [heading('Main prompt')]+prompt_body(d['prompt'])
        s += [heading('Follow-up prompt')]+prompt_body(d['followup'])
        checks=d.get('checks',[])
        if checks:s.append(KeepTogether([heading('Check the output')]+[p('• '+x) for x in checks]))
    write('02-live-prompts','Exact live prompts',s)

def make_reference():
    s=intro('04 / Take it into your business','Your everyday AI toolkit','Start with one repeated task. Give it a clear brief, then check the result.')
    s += [table(['Business day','What changes'],[['08:00','Enquiry → validate → record → draft → human review.'],['08:15','Draft a client reply from facts and constraints.'],['10:00','Inspect an RFQ and the passages supporting the answer.'],['13:00','Analyse supplies and independently check the numbers.'],['15:00','Build a tool from explicit rules and known test cases.'],['17:00','Choose a workflow to test in your own business.']],[78,CW-78]),heading('Three different things'),p('An AI draft: you request an output and review it.\nA reusable tool: the calculator applies agreed rules when you use it.\nA connected automation: an event triggers work across configured apps.'),box('What today demonstrates','The workshop workflow lab uses local rules and a fixed template. It has no AI or email connection and sends nothing. A completed plan is not an installed integration.'),heading('Keep these close')]
    for label,path in [('Toolkit and demos','/toolkit'),('Tools by task','/tools'),('Your workflow plan','/workflow'),('Exact prompts and rehearsal','/rehearsal')]:s.append(link(label,BASE+path))
    s += [PageBreak(),p('04 / Participant worksheet','label'),p('Your first workflow','h1'),p('Choose one 15-minute experiment for Monday, 2 November. Use authorised information and decide what a useful result looks like before starting.')]
    for label in ['1. Trigger - what starts the work?','2. Steps - what happens next?','3. Reviewer - who checks what?','4. Exceptions - what happens when information is missing?','5. Measure - what will you check over the first five runs?']:s.append(WritingLines(label,2))
    s += [p('Compare accuracy, edits needed, time and cost before adding a subscription.','small'),PageBreak(),p('04 / Checked reference values','label'),p('Keep a number you can check.','h1'),table(['Example','Checked result'],[['Stock revenue','KES 179,640'],['Cost of goods sold','KES 149,345'],['Gross profit','KES 30,295'],['Floor cleaner contribution','KES 9,100'],['100 m² / 3 visits / windows','KES 34,104'],['400 m² / 3 visits / windows','KES 115,536']],[CW*.55,CW*.45]),Spacer(1,14),box('Before using a result','Overheads are absent, so net profit is unknown. Confirm rates and the 16% tax assumption before issuing a quotation. Unresolved window scope must be clarified before a real quotation.'),heading('RFQ facts'),p('Submission: 6 November 2026, noon EAT.\nSite visit: optional.\nWindow count, size, height and external access: not specified.'),p('Use the numbered source sections in the RFQ PDF to verify each claim.','small')]
    write('04-participant-reference','Participant reference & worksheet',s)

def structured_source(stem,title,desc):
    raw=read(stem); lines=raw.splitlines();s=intro(stem[:2]+' / Workshop reference',title,desc)
    body='\n'.join(lines[1:]).strip()
    for block in re.split(r'\n\s*\n',body):
        lines=block.splitlines()
        if stem=='07-automation-recipe' and lines[0]=='FIVE TESTS BEFORE REAL USE':
            s += [PageBreak(),p('07 / Test before connecting','label'),p('Make failure visible.','h1')]
        if stem=='08-rehearsal-checks' and lines[0] in ('OBSERVED PRODUCT REHEARSAL','IMPLEMENTATION REVIEW AND FIXES'):
            s += [PageBreak(),p('08 / Review record - continued','label')]
        if stem=='05-prepared-fallbacks' and lines[0]=='QUOTE CHECKS':
            s += [PageBreak(),p('05 / Prepared reference - continued','label'),p('Check the estimate.','h1')]
        if lines[0].isupper() or re.match(r'^\d+\. [A-Z ]+$',lines[0]):
            s.append(heading(lines.pop(0).title()))
        for line in lines:
            if line.startswith('- '):s.append(p('• '+line[2:]))
            elif line.startswith(('Make: https','Zapier: https','n8n: https')):
                label,url=line.split(': ',1);s.append(link(label+' - official setup reference',url))
            else:s.append(p(line))
    write(stem,title,s)

def make_stock(rows):
    s=intro('06 / Independent answer key','Check the stock numbers.','Safi Services & Supplies  |  30-day sales\nAll monetary values are KES. The CSV is included for spreadsheet use.')
    s.append(table(['Revenue','Cost of goods sold','Gross profit'],[['179,640','149,345','30,295']],[CW/3]*3))
    s += [heading('Input data'),table(['Product','Opening','Sold','Unit cost','Price'],[[r['Product'],r['Opening'],r['Sold'],r['Unit cost KES'],r['Selling price KES']] for r in rows],[CW-226,54,48,62,62],True),heading('The calculation rules'),p('Revenue = units sold × selling price\nCOGS = units sold × unit cost\nGross profit = units sold × (selling price - unit cost)\nClosing stock = opening stock - units sold\nSell-through = units sold ÷ opening stock × 100\nTop-up = max(0, units sold - closing stock)'),heading('Check two rows yourself'),p('Floor cleaner: 70 × (850 - 720) = KES 9,100.\nMultipurpose cleaner: 95 × (380 - 310) = KES 6,650.')]
    s += [PageBreak(),p('06 / Independent answer key - continued','label'),p('Profit, stock & assumptions','h1'),heading('Profit contribution'),table(['Product','Revenue','COGS','Gross profit'],[[r['Product'],f"{int(r['Revenue KES']):,}",f"{int(r['COGS KES']):,}",f"{int(r['Gross profit KES']):,}"] for r in rows],[CW-210,70,70,70],True),heading('Closing stock and simple top-ups'),table(['Product','Closing','Sell-through','Top-up'],[[r['Product'],r['Closing stock'],r['Sell-through %']+'%',r['Simple top-up']] for r in rows],[CW-202,56,84,62],True),Spacer(1,12),box('Calculation assumptions','No restocking, returns, shrinkage, price changes or stockouts. Next-month demand is unchanged; delivery is instant and safety stock is zero. Real decisions need lead times, cash, demand, storage and accurate stock records. Overheads are absent: net profit is unknown.')]
    write('06-stock-answer-key','Stock answer key',s)

def make_tools(jobs,tools):
    lookup={x['name']:x for x in tools}
    s=intro('10 / Tools by business task','Start with the job.','14 everyday tasks. 24 tools to consider.\nOfficial source review: 31 October 2026.')
    s.append(box('How to use this directory','These are conditional recommendations, not benchmark rankings. Start with the tools and approved information you already have. Check current plan, account access, usage costs, hosting and setup before paying. Each task includes a starting point, alternatives, a prompt and a check.'))
    s.append(table(['No.','Task'],[[f'{i:02}',x['title']] for i,x in enumerate(jobs,1)],[40,CW-40]))
    s += [Spacer(1,10),link('Search and filter the live directory',BASE+'/tools')]
    for i,j in enumerate(jobs,1):
        s += [PageBreak(),p(f'{i:02} / '+j['category'],'label'),p(j['title'],'h1'),p(j['outcome']),p('Where I would start: '+j['recommendation'])]
        for name,reason in j['options']:
            t=lookup[name]
            s += [heading(name),p(reason+' '+t['access'],'small'),Paragraph(f'<link href="{escape(t["url"],quote=True)}" color="#8720A8"><u>Open {escape(name)}</u></link>    |    <link href="{escape(t["source"],quote=True)}" color="#8720A8"><u>Official source &amp; requirements</u></link>',styles['small'])]
        s += [heading('Starter prompt'),p(j['prompt'],'prompt'),box('Before using the result',j['check'])]
    write('10-tools-by-task','Tools by business task',s)

def make_observed():
    raw=read('09-observed-rehearsal-outputs')
    s=intro('09 / Actual rehearsal responses','Observed outputs','31 October 2026  |  Safi Services & Supplies\nThese are visible product responses from rehearsal, not guaranteed future outputs.')
    s.append(box('About this edition','The observed wording is retained apart from scenario labels; table cells and equations are re-typeset for reading. Interface controls and duplicated chart accessibility labels are omitted. Citation numbers refer to the original notebook response, not links inside this PDF. See 08-rehearsal-checks.pdf for failures and limitations.'))
    email=raw.split('CORRECTED CHATGPT EMAIL\n',1)[1].split('FOLLOW-UP PROMPT:',1)[0]
    main,internal=email.split('Internal checks — remove before sending',1)
    s += [heading('Corrected ChatGPT email')]+paragraphs(main)
    s += [PageBreak(),p('09 / ChatGPT client reply','label'),p('Internal checks & follow-up','h1'),heading('Internal checks - remove before sending')]+paragraphs(internal)
    whatsapp=raw.split('OBSERVED WHATSAPP OUTPUT:',1)[1].split('NOTEBOOK CHECKLIST',1)[0]
    s += [heading('Observed WhatsApp output')]+paragraphs(whatsapp)
    notebook=raw.split('NOTEBOOK CHECKLIST',1)[1].split('NOTEBOOK MISSING-WINDOWS ANSWER',1)[0]
    tab,rest=notebook.split('2. Explicit Rejection Grounds',1)
    vals=[x.strip() for x in tab.splitlines() if x.strip()]
    vals=vals[5:] # discard heading and four column labels
    nrows=[];i=0
    while i<len(vals):
        row=vals[i:i+4];i+=4
        cites=[]
        while i<len(vals) and vals[i].isdigit():cites.append(vals[i]);i+=1
        row[-1]+=' [citations '+', '.join(cites)+']';nrows.append(row)
    assert len(nrows)==9 and all(len(r)==4 for r in nrows)
    s += [PageBreak(),p('09 / Notebook response','label'),p('RFQ checklist','h1'),p('Citation numbers below are recorded labels. Inspect the original source passage before relying on a claim.','small'),table(['Requirement','Mandatory / optional','Deadline & format','Citation & section'],nrows,[110,110,150,CW-370])]
    # Join isolated citation-number lines to the text they support.
    def join_cites(text):
        text=re.sub(r'\n((?:\d+\n)+)\.',lambda m:' ['+', '.join(m.group(1).split())+'].',text)
        text=re.sub(r'\n((?:\d+\n)+)',lambda m:' ['+', '.join(m.group(1).split())+'] ',text)
        return text
    s += [PageBreak(),p('09 / Notebook response - continued','label'),p('Rejections & missing information','h1'),heading('2. Explicit rejection grounds')]
    for line in join_cites(rest).splitlines():
        if line.strip():s.append(p(line.strip()))
    missing=raw.split('NOTEBOOK MISSING-WINDOWS ANSWER',1)[1].split('SUCCESSFUL CHATGPT STOCK ANALYSIS',1)[0]
    s += [heading('Observed missing-windows answer')]+paragraphs(join_cites(missing))
    stock=raw.split('SUCCESSFUL CHATGPT STOCK ANALYSIS',1)[1]
    first,tail=stock.split('1. Product performance',1)
    s += [PageBreak(),p('09 / ChatGPT stock response','label'),p('30-day sales analysis','h1'),box('Presenter annotation','The model said it used Python. We independently reconciled the visible results, but did not inspect the execution trace. Do not treat that sentence alone as evidence of tool use.')]+paragraphs(first)
    product_part,after=tail.split('The top-up column',1)
    vals=[x.strip() for x in product_part.splitlines() if x.strip()]
    start=vals.index('Product'); vals=vals[start+7:]
    assert len(vals)==63,(len(vals),vals[:8])
    s.append(table(['Product','Revenue','COGS','Profit','Closing','Sell-through','Top-up'],[vals[i:i+7] for i in range(0,63,7)],[123,62,62,59,48,65,CW-419]))
    s += [p('The top-up column'+after.split('2. Highest gross-profit contributors',1)[0])]
    ranking=after.split('The top three are',1)[1].split('3. Slow-moving products',1)[0]
    s += [PageBreak(),p('09 / ChatGPT stock response - continued','label'),p('Rankings & worked examples','h1'),heading('2. Highest gross-profit contributors')]+paragraphs('The top three are'+ranking)
    s += [heading('3. Slow-moving products'),p('Using the lowest sell-through percentage as the definition:'),table(['Rank','Product','Sell-through'],[['1','Laundry soap bar','17.50%'],['2 (tie)','Microfibre pack','20.00%'],['2 (tie)','Bin liner box','20.00%']],[60,CW-150,90])]
    slow=after.split('These are the bottom three products',1)[1].split('4. Formulas and worked calculations',1)[0]
    s += paragraphs('These are the bottom three products'+slow)
    s += [heading('4. Formulas and worked calculations'),p('For each product, let O be opening stock, S units sold, C unit cost, and P selling price.'),p('Revenue = S × P\nCOGS = S × C\nGross profit = S × (P - C)\nClosing stock = O - S\nSell-through = (S ÷ O) × 100\nTop-up = max(0, S - (O - S))')]
    worked=after.split('Multipurpose cleaner 2L',1)[1].split('5. Recommended next actions',1)[0]
    worked='Multipurpose cleaner 2L'+worked
    worked=re.sub(r'(?<=[0-9%a-z])(?=(?:COGS|Gross profit|Closing stock|Sell-through|Top-up) =)','\n',worked)
    s += paragraphs(worked)
    actions=after.split('5. Recommended next actions',1)[1]
    s += [PageBreak(),p('09 / ChatGPT stock response - continued','label'),p('Actions & limitations','h1'),heading('5. Recommended next actions')]
    actions,limitations=actions.split('6. Limitations and information required',1)
    s += paragraphs(actions)+[heading('6. Limitations and information required')]+paragraphs(limitations)
    write('09-observed-rehearsal-outputs','Observed rehearsal outputs',s)

def make_start():
    s=intro('Start here / Session pack','AI for your everyday\nbusiness tasks.','DADA HUB  |  31 October 2026  |  09:20-10:20 EAT\nUseful prompts. Clear checks. A repeatable way of working.')
    s.append(box('Download once, keep it close','The written handouts are PDFs with selectable text. The CSV opens in a spreadsheet, and quote-calculator.html works offline in a browser. Live AI products and the published website still need their usual access.'))
    s.append(table(['File','What it is for'],[
        ['01 / Presenter run sheet','Spoken cues, stage actions, timing and fallbacks.'],['02 / Live prompts','Complete prompts and follow-ups to copy and adapt.'],['03 / cleaning RFQ','The PDF source for the NotebookLM demonstration.'],['04 / Participant reference','The business day, checked values and a workflow worksheet.'],['05 / Prepared fallbacks','Checked reference answers, clearly labelled.'],['06 / Stock answer key','A print-ready PDF plus the original spreadsheet CSV.'],['07 / Automation recipe','A setup and testing plan for a connected workflow.'],['08 / Rehearsal checks','Observed passes, corrections, failures and venue preflight.'],['09 / Observed outputs','Actual responses from the product rehearsals.'],['10 / Tools by task','14 task guides with alternatives and official source links.'],['Quote calculator / HTML','A working offline estimate calculator.'],['Presentation / PDF','The static 27-slide presentation fallback.']],[146,CW-146]))
    s += [Spacer(1,12),link('Open the attendee toolkit',BASE+'/toolkit'),link('Open the presenter rehearsal',BASE+'/rehearsal'),link('Browse the tools directory',BASE+'/tools')]
    write('START-HERE','Session pack guide',s)

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    demos=json.loads((ROOT/'app/data/demos.json').read_text())
    rehearsal=json.loads((ROOT/'app/data/rehearsal.json').read_text())
    jobs=json.loads((ROOT/'app/data/jobs.json').read_text())
    tools=json.loads((ROOT/'app/data/tools.json').read_text())
    hook=json.loads((ROOT/'app/data/hook.json').read_text())
    rows=list(csv.DictReader((OUT/'06-stock-answer-key.csv').open()))[:-1]
    make_start();make_run_sheet(rehearsal);make_prompts(demos,hook);make_rfq();make_reference()
    structured_source('05-prepared-fallbacks','Prepared fallback answers','Checked teaching references. These are not live AI output.')
    make_stock(rows)
    structured_source('07-automation-recipe','Your first connected workflow','A configuration and testing recipe. This is not an installed integration or an importable template.')
    structured_source('08-rehearsal-checks','Rehearsal & implementation review','31 October 2026. A record of checks actually performed and the limits of those checks.')
    make_observed();make_tools(jobs,tools)
    files=sorted(OUT.glob('*.pdf'))+[OUT/'06-stock-answer-key.csv',OUT/'quote-calculator.html']
    with zipfile.ZipFile(OUT/'dada-hub-demo-kit.zip','w',zipfile.ZIP_DEFLATED) as z:
        for path in files:z.write(path,path.name)
    with zipfile.ZipFile(OUT/'dada-hub-demo-kit.zip') as z:
        assert z.testzip() is None
        assert not any(n.endswith('.txt') for n in z.namelist())
        print(f'ZIP: {len(z.namelist())} files; integrity passed; no TXT files')

if __name__=='__main__':main()
