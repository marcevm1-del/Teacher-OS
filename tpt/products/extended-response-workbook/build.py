"""Build the Extended Response Workbook: content.py -> pack.html -> PDF."""
import pathlib, re, sys
from content import PASSAGES, LADDER
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import common

HERE = pathlib.Path(__file__).parent
OUT_PDF = HERE.parent.parent / "IGCSE-0500-Extended-Response-Workbook-2027.pdf"

def words(paras):
    return len(re.sub(r"<[^>]+>", " ", " ".join(paras)).split())

def passage_pages(p):
    ps = "".join(f'<p><span class="pn">{i}</span>{x}</p>' for i, x in enumerate(p["paras"], 1))
    bl = "".join(f"<li>{b}</li>" for b in p["bullets"])
    task = f'''<div class="task"><b>Task [20 marks: 10 reading + 10 writing]:</b> {p["task"]}<br>In your {p["form"]} you should:<ul>{bl}</ul>
Base your {p["form"]} on what you have read, but be careful to use your own words. Address each bullet point. Write about <b>250 to 300 words</b>.</div>'''
    tag = "Guided practice" if p["guided"] else "Independent practice"
    first = f'''<section class="page"><div class="eyebrow">Passage {p["n"]} · {tag} · {p["form"].capitalize()}</div><h2>{p["title"]}</h2>
<div class="extract">{ps}</div>{task}</section>'''
    if p["guided"]:
        heads = "".join(f"<th>Bullet {i}</th>" for i in (1, 2, 3))
        second = f'''<section class="page frame-page"><div class="eyebrow">Passage {p["n"]} · Guided plan</div><h2>Plan in three columns</h2>
<table class="cols"><tr><th></th>{heads}</tr>
<tr><td class="rl">Details from the text (Mine)</td><td></td><td></td><td></td></tr>
<tr><td class="rl">Inference / development (Stretch)</td><td></td><td></td><td></td></tr></table>
<table class="plan"><tr><td>Voice: who am I, and how do I feel?</td><td></td></tr>
<tr><td>Form features I must include</td><td></td></tr>
<tr><td>Opening line</td><td></td></tr><tr><td>Closing line</td><td></td></tr></table>
<p class="checks">☐ All three bullets &nbsp; ☐ At least two developed inferences &nbsp; ☐ Own words &nbsp; ☐ Right form and register &nbsp; ☐ 250–300 words</p></section>'''
    else:
        second = f'''<section class="page"><div class="eyebrow">Passage {p["n"]} · Your answer</div><h2>Write your {p["form"]}</h2>
<p class="note">Plan for 5 minutes (three columns, one per bullet), then write for 25 minutes.</p><div class="lines">{"<div></div>" * 22}</div></section>'''
    return [first, second]

def answer_pages(p):
    ideas = "".join(f"<div class='ind'><b>{h}.</b> {t}</div>" for h, t in p["ideas"])
    model = "".join(f"<p>{x}</p>" for x in p["model"])
    why = "".join(f"<li>{w}</li>" for w in p["why"])
    return [f'''<section class="page ms"><div class="eyebrow">Answers · Passage {p["n"]}</div><h2>{p["title"]}: model {p["form"]}</h2>
<h3>Indicative content</h3>{ideas}
<h3>Model answer <span class="on">{words(p["model"])} words</span></h3><div class="model">{model}</div>
<h3>Why it scores highly</h3><ul class="why">{why}</ul></section>''']

COVER = '''<section class="cover"><div class="frame">
<div class="brand">PASSWITHPURPOSE</div>
<div class="badge"><small>NEW</small>2027<small>FORMAT</small></div>
<div class="kicker">CAMBRIDGE IGCSE · FIRST LANGUAGE ENGLISH · 0500</div>
<h1>Extended Response<br><em>Workbook</em></h1>
<p class="lede">Step-by-step practice for Paper 1 Question 4 (250–300 words, 20 marks): six original passages, one in each exam form, with a model answer for every one.</p>
<ul class="feat">
<li>6 original passages</li><li>All six Q4 forms</li>
<li>Mine → Stretch → Voice</li><li>Three-column planning pages</li>
<li>Indicative content per bullet</li><li>6 model answers (250–300 words)</li>
<li>Retell → develop ladder</li><li>Marking bands &amp; tracker</li>
</ul>
<div class="author"><b>Marcé van Moerkerken</b><br>PGCE Secondary English (Summa Cum Laude)<br>International school English teacher, UAE</div>
<div class="disc">For exams in 2027, 2028 and 2029. Independent practice material; not produced or endorsed by Cambridge University Press &amp; Assessment. All passages are original.</div>
</div></section>'''

def howto():
    ladder = "".join(f"<tr><td>{a}</td><td>“{b}”</td></tr>" for a, b in LADDER)
    return f'''<section class="page"><div class="eyebrow">Start here</div><h2>The method</h2>
<p>In Question 4 candidates write 250–300 words in a given form, usually in the voice of someone connected to Text C, responding to three bullet points. Reading and writing earn 10 marks each. The biggest trap is <b>retelling the text in order</b> with a greeting on top.</p>
<table class="glance">
<tr><td>Mine</td><td>Treat each bullet as its own mini-question. Find every relevant detail in the text for it.</td></tr>
<tr><td>Stretch</td><td>Top answers go beyond the text: they develop ideas and make reasonable inferences rooted in it.</td></tr>
<tr><td>Voice</td><td>Write convincingly as the given person, in the given form, for the given audience.</td></tr>
</table>
<h3>From retelling to developing</h3><table class="glance">{ladder}</table>
<h3>The six forms</h3>
<table class="glance">
<tr><td>Journal</td><td>Date or time; first person; private, reflective, honest</td></tr>
<tr><td>Report</td><td>Title; purpose; subheadings; objective tone; recommendations</td></tr>
<tr><td>Interview</td><td>Speaker labels; purposeful questions; developed answers</td></tr>
<tr><td>Speech</td><td>Address the audience; direct appeals; strong close</td></tr>
<tr><td>Letter</td><td>Greeting; clear purpose; register to suit the reader; sign-off</td></tr>
<tr><td>Article</td><td>Headline; engaging opening; lively paragraphs; final line</td></tr>
</table>
<p class="note">Passages 1–3 are guided (with a planning page). Passages 4–6 are independent. Model answers follow at the back.</p></section>'''

MISTAKES = '''<section class="page"><div class="eyebrow">Avoid these</div><h2>Five mistakes that cost Q4 marks</h2>
<table class="mk"><tr><th>Mistake</th><th>Weak</th><th>Strong</th></tr>
<tr><td class="ql">Retelling in order</td><td class="weak">A greeting, then the story from start to finish.</td><td class="strong">Reorganise the details around the three bullets.</td></tr>
<tr><td class="ql">Missing a bullet</td><td class="weak">Two bullets developed; the third squeezed into one sentence.</td><td class="strong">Plan three columns and give each bullet real space.</td></tr>
<tr><td class="ql">Wrong voice</td><td class="weak">A lighthouse keeper who sounds like a student writing an essay.</td><td class="strong">Short, understated sentences; echoes of his own words.</td></tr>
<tr><td class="ql">Contradicting the text</td><td class="weak">“The engineers were rude and kept me waiting.”</td><td class="strong">Inferences must fit the text: “polite and young and in a hurry”.</td></tr>
<tr><td class="ql">Copying</td><td class="weak">Lifting whole sentences from the passage.</td><td class="strong">Reshape details in the character’s own words.</td></tr>
</table>
<div class="tip"><b>THE TEST:</b> If you removed the greeting and sign-off, would your answer still be clearly a letter, speech or journal? The form should show in every paragraph, not just at the top.</div></section>'''

BANDS = '''<section class="page ms"><div class="eyebrow">For teachers, tutors &amp; students</div><h2>Marking guidance &amp; tracker</h2>
<p class="note">Bands written for this workbook to support consistent practice marking; not official Cambridge descriptors.</p>
<table class="bands"><tr><th></th><th>Reading (10)</th><th>Writing (10)</th></tr>
<tr><td class="bd">9–10</td><td>All three bullets addressed thoroughly; ideas developed with convincing, text-based inferences; a sustained, credible voice.</td><td>Confident, fluent style; register and form fully appropriate; well structured; wide vocabulary; highly accurate.</td></tr>
<tr><td class="bd">7–8</td><td>All bullets addressed; some development and inference beyond the surface.</td><td>Clear, varied style; appropriate register; well organised; mostly accurate.</td></tr>
<tr><td class="bd">5–6</td><td>Relevant ideas for each bullet but mainly retold; occasional inference.</td><td>Generally clear; some sense of form and audience; errors do not impede meaning.</td></tr>
<tr><td class="bd">3–4</td><td>Uneven coverage; relies on retelling or lifting; one bullet thin or missing.</td><td>Simple style; limited structure; errors sometimes distract.</td></tr>
<tr><td class="bd">1–2</td><td>Little relevant use of the text.</td><td>Frequent errors; little control of form or register.</td></tr></table>
<h3>My progress</h3>
<table class="track"><tr><th>Passage</th><th>Form</th><th>Reading /10</th><th>Writing /10</th><th>One thing to improve</th></tr>
''' + "".join(f"<tr><td>{p['n']}</td><td>{p['form'].capitalize()}</td><td></td><td></td><td></td></tr>" for p in PASSAGES) + '''</table></section>'''

END = '''<section class="page end"><div class="eyebrow">Next step</div><h2>Complete the Paper 1 skill set</h2>
<p>The <b>Summary Writing Workbook</b> (Q2) and the <b>Language Analysis Workbook</b> (Q3) complete the Paper 1 skill series. The <b>Paper 1 Practice Packs 1 &amp; 2</b> put all four questions together in six full papers.</p>
<p>Search <b>PassWithPurpose</b> on Teachers Pay Teachers.</p>
<div class="tip"><b>ENJOYED THIS WORKBOOK?</b> A short review on TPT helps other teachers find it.</div>
<p class="small">© 2026 Marcé van Moerkerken · PassWithPurpose. Licensed for use by one teacher/classroom (including a copy for each student) or one student. Not produced, endorsed or approved by Cambridge University Press &amp; Assessment. All passages are original.</p></section>'''

CSS_EXTRA = '''
.extract{border:1px solid var(--line);background:var(--pale);padding:10px 14px 4px;font:10.2pt/1.52 Lora,serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.extract p{position:relative;padding-left:7mm;margin:0 0 7px}
.task{margin:10px 0;font-size:9.8pt;border-left:3px solid var(--gold);padding:4px 10px}.task ul{margin:3px 0 3px 16px;padding:0}
.cols td{border:1px solid var(--line);height:62mm;vertical-align:top}.cols .rl{width:26mm;font-weight:700;color:var(--navy);font-size:8.5pt;background:var(--pale);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.plan td{border:1px solid var(--line);height:11mm}
.plan td:first-child{width:52mm;font-weight:700;color:var(--navy);background:var(--pale);font-size:8.8pt;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.lines div{border-bottom:1px solid var(--line);height:9.5mm}
.model{border-left:3px solid var(--gold);padding:2px 0 2px 12px;font:9.3pt/1.45 Lora,serif}.model p{margin:0 0 5px}
.ind{font-size:8.9pt;margin-bottom:4px}
.why{font-size:8.9pt;padding-left:16px;margin:2px 0}
.mk td{font-size:9.2pt}.mk .ql{width:30mm;font-weight:700;color:var(--navy)}.mk .weak{color:#9b3b32;width:38%}.mk .strong{color:#2f6b4f}
.track td{height:10mm}.checks{font-size:9.6pt;margin-top:8px}
'''

if __name__ == "__main__":
    common.CSS += CSS_EXTRA
    pages = [howto(), MISTAKES]
    for p in PASSAGES:
        pages += passage_pages(p)
    for p in PASSAGES:
        pages += answer_pages(p)
    pages += [BANDS, END]
    common.render_pdf(HERE, "".join(pages), COVER, OUT_PDF, "IGCSE 0500 Extended Response Workbook")
