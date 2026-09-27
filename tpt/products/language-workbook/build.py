"""Build the Language Analysis Workbook: content.py -> pack.html -> PDF."""
import pathlib, re, sys
from content import EXTRACTS, MISTAKES
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import common

HERE = pathlib.Path(__file__).parent
OUT_PDF = HERE.parent.parent / "IGCSE-0500-Language-Analysis-Workbook-2027.pdf"

def words(paras):
    return len(re.sub(r"<[^>]+>", " ", " ".join(paras)).split())

def extract_page(e):
    ps = "".join(f'<p><span class="pn">{i}</span>{p}</p>' for i, p in enumerate(e["paras"], 1))
    task = (f"Re-read the extract. Explain how the writer uses language to convey <b>{e['focus'][0]}</b> in paragraph 1 "
            f"and <b>{e['focus'][1]}</b> in paragraph 2. Select three or four powerful words or phrases from each paragraph. "
            f"Write about <b>200 to 250 words</b>.")
    if e["guided"]:
        c, l, k, f = e["example"]
        rows = "".join(f"<tr><td class='pl'>Paragraph {p}</td><td></td><td></td><td></td><td></td></tr>" * 1 for p in (1, 1, 1, 2, 2, 2))
        scaffold = f'''<h3>Step 1: Choose → Zoom → Connect</h3>
<table class="zoom"><tr><th></th><th>Choice (1–4 words)</th><th>Literal meaning</th><th>Connotations</th><th>Effect on the reader</th></tr>
<tr class="ex"><td class='pl'>Example</td><td>{c}</td><td>{l}</td><td>{k}</td><td>{f}</td></tr>{rows}</table>
<p class="note"><b>Step 2:</b> Turn your table into two paragraphs, one per paragraph of the extract, and finish with one sentence on the overall effect.</p>'''
        tag = "Guided practice"
    else:
        scaffold = '<div class="lines">' + "<div></div>" * 12 + '</div><p class="note">Continue on lined paper. Aim for 3–4 choices per paragraph and an overall-effect sentence.</p>'
        tag = "Independent practice"
    return f'''<section class="page">
<div class="eyebrow">Extract {e["n"]} · {tag}</div>
<h2>{e["title"]}</h2>
<div class="extract">{ps}</div>
<div class="task"><b>Task [10 marks]:</b> {task}</div>
{scaffold}</section>'''

def model_pages():
    out = []
    for i in range(0, len(EXTRACTS), 2):
        blocks = ""
        for e in EXTRACTS[i:i + 2]:
            body = "".join(f"<p>{p}</p>" for p in e["model"])
            blocks += f'<h3>Extract {e["n"]}: {e["title"]} <span class="on">{words(e["model"])} words</span></h3><div class="model">{body}</div>'
        out.append(f'<section class="page"><div class="eyebrow">Model answers</div><h2>Model answers · Extracts {EXTRACTS[i]["n"]}–{EXTRACTS[min(i + 1, len(EXTRACTS) - 1)]["n"]}</h2>{blocks}</section>')
    return out

def mistakes_page():
    rows = "".join(f"<tr><td class='ql'>{t}</td><td class='weak'>{w}</td><td class='strong'>{s}</td></tr>" for t, w, s in MISTAKES)
    return f'''<section class="page"><div class="eyebrow">Avoid these</div><h2>Six mistakes that cost marks</h2>
<table class="mk"><tr><th>Mistake</th><th>Weak</th><th>Strong</th></tr>{rows}</table>
<div class="tip"><b>THE GOLDEN RULE:</b> Every choice needs three things: the <b>words</b> (short quotation), the <b>meaning or connotation</b>, and the <b>effect</b> on the reader. The marks come from the explanation.</div></section>'''

COVER = '''<section class="cover"><div class="frame">
<div class="brand">PASSWITHPURPOSE</div>
<div class="badge"><small>NEW</small>2027<small>FORMAT</small></div>
<div class="kicker">CAMBRIDGE IGCSE · FIRST LANGUAGE ENGLISH · 0500</div>
<h1>Language Analysis<br><em>Workbook</em></h1>
<p class="lede">Step-by-step practice for the Paper 1 Question 3 language task (200–250 words, 10 marks): six original extracts, a guided method and model answers for every one.</p>
<ul class="feat">
<li>6 original extracts</li><li>3 guided, 3 independent</li>
<li>Choose → Zoom → Connect tables</li><li>Worked example for each</li>
<li>6 model answers</li><li>Six mistakes that cost marks</li>
<li>Effect phrase bank</li><li>Marking bands &amp; tracker</li>
</ul>
<div class="author"><b>Marcé van Moerkerken</b><br>PGCE Secondary English (Summa Cum Laude)<br>International school English teacher, UAE</div>
<div class="disc">For exams in 2027, 2028 and 2029. Independent practice material; not produced or endorsed by Cambridge University Press &amp; Assessment. All extracts are original.</div>
</div></section>'''

HOWTO = '''<section class="page">
<div class="eyebrow">Start here</div>
<h2>How to use this workbook</h2>
<p>In Paper 1 Question 3, students analyse how a writer uses language in two named paragraphs of Text C, in about 200–250 words, for 10 marks. The skill improves quickly with focused, repeated practice. This workbook provides it.</p>
<h3>The method: Choose → Zoom → Connect</h3>
<table class="glance">
<tr><td>Choose</td><td>Pick three or four short, powerful choices from <b>each</b> paragraph: single words and short phrases work best.</td></tr>
<tr><td>Zoom</td><td>Explain the literal meaning, then the connotations: the feelings and images the words carry.</td></tr>
<tr><td>Connect</td><td>Explain the effect on the reader: what picture or mood is created, and why the writer wants it.</td></tr>
</table>
<h3>The route through the book</h3>
<table class="glance">
<tr><td>Extracts 1–3</td><td><b>Guided.</b> Fill in the Choose → Zoom → Connect table (a worked example is given), then write it up.</td></tr>
<tr><td>Extracts 4–6</td><td><b>Independent.</b> Plan quickly, then write 200–250 words in about 25 minutes, as in the exam.</td></tr>
<tr><td>After each one</td><td>Compare with the model answer. Highlight one explanation in the model that is better than yours, and rewrite one of your own sentences in the same way.</td></tr>
</table>
<h3>Phrases for explaining effect</h3>
<div class="two">
<div class="col"><ul><li>“…suggests that…”</li><li>“…carries connotations of…”</li><li>“…implies…”</li><li>“…personifies… as…”</li></ul></div>
<div class="col"><ul><li>“…so the reader feels…”</li><li>“…emphasising how…”</li><li>“…creating a sense of…”</li><li>“…contrasts with…, highlighting…”</li></ul></div>
</div>
</section>'''

BANDS = '''<section class="page ms">
<div class="eyebrow">For teachers, tutors &amp; students</div>
<h2>Marking guidance &amp; tracker</h2>
<p class="note">Bands written for this workbook to support consistent practice marking; not official Cambridge descriptors.</p>
<table class="bands">
<tr><td class="bd">9–10</td><td>A wide range of precise selections from both paragraphs; detailed, perceptive explanation of meaning and effect, including connotations; links to the writer’s overall purpose.</td></tr>
<tr><td class="bd">7–8</td><td>A good range of relevant choices; clear explanations of connotations and effects, several developed.</td></tr>
<tr><td class="bd">5–6</td><td>Some appropriate choices; explanations generally accurate but sometimes general or uneven between paragraphs.</td></tr>
<tr><td class="bd">3–4</td><td>Limited selection; some meanings explained; effects vague, or mainly technique labels.</td></tr>
<tr><td class="bd">1–2</td><td>Few choices; largely repeats the text or labels devices with no explanation.</td></tr>
</table>
<h3>My progress</h3>
<table class="track">
<tr><th>Extract</th><th>Mark /10</th><th>Choices P1</th><th>Choices P2</th><th>One thing to improve</th></tr>
<tr><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td></td><td></td><td></td><td></td></tr>
<tr><td>3</td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td></td><td></td><td></td><td></td></tr>
<tr><td>5</td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td></td><td></td><td></td><td></td></tr>
</table>
</section>'''

END = '''<section class="page end">
<div class="eyebrow">Next step</div>
<h2>Put the skill into a full paper</h2>
<p>The <b>Paper 1 Practice Packs 1 &amp; 2</b> include a full language task in each of six practice papers, with indicative content for every paragraph. The <b>Complete Exam Guide</b> explains the method for every other question on both papers.</p>
<p>Search <b>PassWithPurpose</b> on Teachers Pay Teachers.</p>
<div class="tip"><b>ENJOYED THIS WORKBOOK?</b> A short review on TPT helps other teachers find it.</div>
<p class="small">© 2026 Marcé van Moerkerken · PassWithPurpose. Licensed for use by one teacher/classroom (including copies for each student) or one student. Not produced, endorsed or approved by Cambridge University Press &amp; Assessment. All extracts are original.</p>
</section>'''

CSS_EXTRA = '''
.extract{border:1px solid var(--line);background:var(--pale);padding:10px 14px 4px;font:10.4pt/1.55 Lora,serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.extract p{position:relative;padding-left:7mm;margin:0 0 8px}
.task{margin:10px 0;font-size:10pt;border-left:3px solid var(--gold);padding:4px 10px}
.zoom td{border:1px solid var(--line);height:12mm;font-size:8.8pt;vertical-align:top}
.zoom th{font-size:8.5pt}
.zoom .pl{width:17mm;font-weight:700;color:var(--navy);font-size:8pt}
.zoom .ex td{background:#f3ead6;height:auto;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.lines div{border-bottom:1px solid var(--line);height:9mm}
.model{border-left:3px solid var(--gold);padding:2px 0 2px 12px;font:9.6pt/1.5 Lora,serif}
.model p{margin:0 0 6px}
.mk td{font-size:9.2pt}.mk .ql{width:30mm;font-weight:700;color:var(--navy)}
.mk .weak{color:#9b3b32;width:33%}.mk .strong{color:#2f6b4f}
.track td{height:10mm}
'''

if __name__ == "__main__":
    common.CSS += CSS_EXTRA
    pages = [HOWTO, mistakes_page()] + [extract_page(e) for e in EXTRACTS] + model_pages() + [BANDS, END]
    common.render_pdf(HERE, "".join(pages), COVER, OUT_PDF, "IGCSE 0500 Language Analysis Workbook")
    print("model words:", [words(e["model"]) for e in EXTRACTS], "extract words:", [words(e["paras"]) for e in EXTRACTS])
