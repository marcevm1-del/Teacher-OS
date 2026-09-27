"""Build the Paper 2 Directed Writing Pack: content.py -> pack.html -> PDF."""
import pathlib, re, sys
from content import TASKS
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from common import CSS, render_pdf

HERE = pathlib.Path(__file__).parent
OUT_PDF = HERE.parent.parent / "IGCSE-0500-Paper-2-Directed-Writing-Pack-2027.pdf"
TITLE = "IGCSE 0500 Paper 2 Directed Writing Pack"

def words(html):
    return len(re.sub(r"<[^>]+>", " ", html).split())

def q(num, text, marks):
    return f'<div class="q"><div class="qn">{num}</div><div class="qt">{text}</div><div class="qm">[{marks}]</div></div>'

def insert_pages(t):
    out, multi = [], len(t["texts"]) > 1
    for i, tx in enumerate(t["texts"], 1):
        ps = "".join(f'<p><span class="pn">{k}</span>{p}</p>' for k, p in enumerate(tx["paras"], 1))
        label = f"Text {i}" if multi else "Text"
        out.append(f'''<section class="page text">
<div class="eyebrow">Task {t["n"]} · Insert · {t["topic"]}</div>
<h2><span class="tl">{label}</span> {tx["title"]}</h2>
<div class="kind">{tx["kind"]}</div><div class="body">{ps}</div></section>''')
    return out

def question_page(t):
    both = "both texts" if len(t["texts"]) > 1 else "the text"
    (a1, m1), (a2, m2) = t["q1a"]
    bl = "".join(f"<li>{b}</li>" for b in t["bullets"])
    total = sum(words("".join(x["paras"])) for x in t["texts"])
    return f'''<section class="page qp">
<div class="eyebrow">Task {t["n"]} · Question paper</div>
<h2>Paper 2 Section A · Task {t["n"]}: {t["topic"]}</h2>
<div class="rubric"><b>Section A · 40 marks · about 1 hour.</b> Read {both} in the insert (about {round(total, -1)} words), then answer Question 1(a) and Question 1(b).
Suggested timing: read and answer 1(a) 15 min · plan 1(b) 8 min · write 1(b) 35 min · check 2 min.</div>
<h3>Question 1(a) <span class="on">5 marks</span></h3>
{q("(i)", a1, m1)}
{q("(ii)", a2, m2)}
<h3>Question 1(b) <span class="on">35 marks</span></h3>
{q("", f"{t['task']}<br>In your {t['form']} you should:<ul>{bl}</ul>Base your {t['form']} on what you have read in {both}, but be careful to use your own words. Address both bullet points. Write about <b>250 to 350 words</b>. Up to 10 marks are available for the content of your answer and up to 25 marks for the quality of your writing.", 35)}
<div class="tip"><b>BEFORE YOU WRITE:</b> Use the planning frame. Circle the form, audience and purpose, and mark each argument in the text: agree, disagree or “yes, but…”.</div>
</section>'''

def mark_scheme(t):
    ms1 = "".join(f"<tr><td class='ql'>1(a)({r})</td><td>{a}</td><td class='mk'>{m}</td></tr>" for r, a, (_, m) in zip(["i", "ii"], t["q1a_ms"], t["q1a"]))
    ideas = "".join(f"<div class='ind'><b>{h}.</b> {x}</div>" for h, x in t["ideas"])
    return f'''<section class="page ms">
<div class="eyebrow">Task {t["n"]} · Mark scheme</div>
<h2>Mark scheme · Task {t["n"]}</h2>
<h3>Question 1(a) <span class="on">5 marks</span></h3>
<table class="mst">{ms1}</table>
<h3>Question 1(b) · Reading <span class="on">10 marks</span></h3>
<p class="note">Mark with the Reading bands on the Marking Guidance page. The top bands need candidates to <b>evaluate</b> the ideas in the text, not just repeat them. Indicative content:</p>
{ideas}
<h3>Question 1(b) · Writing <span class="on">25 marks</span></h3>
<p class="note">Mark with the Writing bands. Check the conventions of a {t["form"]} (see the Form Toolkit), register suited to the audience, a clear structure, and accurate, varied sentences and vocabulary.</p>
</section>'''

def model_page(t):
    why = "".join(f"<li>{w}</li>" for w in t["why"])
    return f'''<section class="page">
<div class="eyebrow">Task {t["n"]} · Model answer</div>
<h2>Model {t["form"]} · Task {t["n"]}</h2>
<p class="note">A top-band response ({words(t["model"])} words). Use it after students have tried the task themselves. It shows one strong answer, not the only one.</p>
<div class="model">{t["model"]}</div>
<h3>Why this scores highly</h3>
<ul class="why">{why}</ul>
</section>'''

def build():
    pages = [HOWTO, TOOLKIT, FRAME]
    for t in TASKS:
        pages += insert_pages(t) + [question_page(t), mark_scheme(t), model_page(t)]
    pages += [BANDS, TRACKER, END]
    render_pdf(HERE, "".join(pages), COVER, OUT_PDF, TITLE)
    for t in TASKS:
        print(f"task {t['n']}: insert {sum(words(''.join(x['paras'])) for x in t['texts'])} words, model {words(t['model'])} words")

COVER = '''<section class="cover"><div class="frame">
<div class="brand">PASSWITHPURPOSE</div>
<div class="badge"><small>NEW</small>2027<small>FORMAT</small></div>
<div class="kicker">CAMBRIDGE IGCSE · FIRST LANGUAGE ENGLISH · 0500</div>
<h1>Paper 2<br><em>Directed Writing</em></h1>
<p class="lede">Four complete Section A tasks for the new 2027 exam, covering the 1(a) structured question and 1(b) directed writing, with model answers for a speech, a letter, an article and a report.</p>
<ul class="feat">
<li>4 full Section A tasks (160 marks)</li><li>6 original source texts</li>
<li>New 1(a) evaluation questions</li><li>1(b) in all four forms</li>
<li>4 annotated model answers</li><li>Mark schemes & indicative content</li>
<li>Planning frame & form toolkit</li><li>Evaluation phrase bank</li>
</ul>
<div class="author"><b>Marcé van Moerkerken</b><br>PGCE Secondary English (Summa Cum Laude)<br>International school English teacher, UAE</div>
<div class="disc">For exams in 2027, 2028 and 2029. Independent practice material; not produced or endorsed by Cambridge University Press &amp; Assessment. All texts are original.</div>
</div></section>'''

HOWTO = '''<section class="page">
<div class="eyebrow">Start here</div>
<h2>How to use this pack</h2>
<p>From June 2027, Section A of Cambridge IGCSE First Language English (0500) Paper 2 gives candidates one or two texts (about 550–650 words in total) and two linked questions. This pack gives you four complete tasks in that format, one for each form candidates may be asked to write.</p>
<table class="glance">
<tr><th>Question</th><th>What candidates do</th><th>Marks</th></tr>
<tr><td>1(a)</td><td>Short structured answers: analyse and evaluate the ideas in the text(s), including how the writer tries to influence readers</td><td>5</td></tr>
<tr><td>1(b)</td><td>Directed writing: a speech, letter, article or report of 250–350 words that uses, develops and <b>evaluates</b> the ideas in the text(s)</td><td>35<br><small>10 R + 25 W</small></td></tr>
</table>
<h3>The four tasks</h3>
<table class="glance">
<tr><td>Task 1</td><td>Phones in Schools</td><td>Two texts</td><td>Speech</td></tr>
<tr><td>Task 2</td><td>Paying for Paradise</td><td>One text</td><td>Letter</td></tr>
<tr><td>Task 3</td><td>Compulsory School Sport</td><td>Two texts</td><td>Article</td></tr>
<tr><td>Task 4</td><td>The Future of the Library</td><td>One text</td><td>Report</td></tr>
</table>
<h3>The five-step method for 1(b)</h3>
<table class="glance">
<tr><td>1 Decode</td><td>Circle the form, audience, purpose and the position you will take.</td></tr>
<tr><td>2 Map</td><td>List every argument in the text(s). Mark each one: agree, disagree or “yes, but…”.</td></tr>
<tr><td>3 Evaluate</td><td>Question the evidence: Is it reliable? Is it biased? What is missing? Do the texts contradict each other?</td></tr>
<tr><td>4 Plan</td><td>Hook, three developed paragraphs drawn from the texts, a clear conclusion or call to action.</td></tr>
<tr><td>5 Write &amp; check</td><td>250–350 words in the right form and register. Leave time to proofread.</td></tr>
</table>
<div class="uses">
<div><b>Timed practice</b><br>Print the insert and question paper. Allow about one hour for Section A.</div>
<div><b>Teach the form</b><br>Study the model answer and its notes first, then set a different task in the same form.</div>
<div><b>Tutoring</b><br>Use Task 1 to diagnose, then work on the weakest strand: evaluation, form or accuracy.</div>
</div>
</section>'''

TOOLKIT = '''<section class="page">
<div class="eyebrow">Toolkit</div>
<h2>Form toolkit &amp; evaluation phrase bank</h2>
<table class="glance">
<tr><th>Form</th><th>Must include</th><th>Register</th></tr>
<tr><td>Speech</td><td>Greeting to the audience; a hook; signposting (“First… Finally…”); direct address and inclusive “we”; a memorable close and thanks</td><td>Engaging, rhetorical, suited to listeners</td></tr>
<tr><td>Letter</td><td>“Dear…”; purpose stated in the first paragraph; one main point per paragraph; polite request or call to action; “Yours sincerely/faithfully”</td><td>Formal to officials; warmer to people you know</td></tr>
<tr><td>Article</td><td>Headline (and optional subheading); an opening that grabs attention; lively paragraphs; a strong final line</td><td>Informative and lively; suited to the publication</td></tr>
<tr><td>Report</td><td>Title; “To/From” or purpose line; clear subheadings; balanced findings; numbered recommendations; conclusion</td><td>Objective, clear and formal; no emotive language</td></tr>
</table>
<h3>From repeating to evaluating</h3>
<table class="glance">
<tr><td>Repeating</td><td>“The text says visitor numbers have fallen by forty per cent.”</td></tr>
<tr><td>Using</td><td>“Visitor numbers have fallen sharply, which worries the council.”</td></tr>
<tr><td>Developing</td><td>“If fewer people visit, the library may struggle to justify its costs.”</td></tr>
<tr><td>Evaluating</td><td>“However, opening hours were halved, so the fall may reflect closed doors rather than lost interest.”</td></tr>
</table>
<h3>Evaluation phrase bank</h3>
<div class="two">
<div class="col"><h4>Questioning evidence</h4><ul>
<li>“This statistic proves less than it seems because…”</li>
<li>“The writer relies on a single example…”</li>
<li>“We are not told who carried out this research…”</li>
<li>“This may be true for one school, but…”</li></ul></div>
<div class="col"><h4>Weighing arguments</h4><ul>
<li>“The strongest point here is… because…”</li>
<li>“This is a fair concern, but it is not a reason to…”</li>
<li>“Both writers agree that…; they differ only on…”</li>
<li>“A more balanced view would recognise that…”</li></ul></div>
</div>
</section>'''

FRAME = '''<section class="page frame-page">
<div class="eyebrow">Photocopiable</div>
<h2>1(b) planning frame</h2>
<table class="plan">
<tr><td>Form</td><td></td><td>Audience</td><td></td></tr>
<tr><td>Purpose</td><td></td><td>My position</td><td></td></tr>
</table>
<h3>Map the text(s)</h3>
<table class="plan map">
<tr><th>Argument / idea</th><th>Text</th><th>Agree / disagree / yes, but…</th><th>Evaluation: reliable? biased? missing?</th></tr>
<tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr>
</table>
<h3>Paragraph plan</h3>
<table class="plan para">
<tr><td>Opening / hook</td><td></td></tr>
<tr><td>Point 1 + evaluation</td><td></td></tr>
<tr><td>Point 2 + evaluation</td><td></td></tr>
<tr><td>Point 3 + evaluation</td><td></td></tr>
<tr><td>Conclusion / call to action</td><td></td></tr>
</table>
<h3>Final check</h3>
<p class="checks">☐ Correct form conventions &nbsp; ☐ Both bullets addressed &nbsp; ☐ At least two evaluative points &nbsp; ☐ Own words &nbsp; ☐ 250–350 words &nbsp; ☐ Proofread</p>
</section>'''

BANDS = '''<section class="page ms">
<div class="eyebrow">For teachers, tutors &amp; students</div>
<h2>Marking guidance · Question 1(b)</h2>
<p class="note">These bands are written for this pack to support consistent practice marking. They follow the published assessment objectives but are not official Cambridge descriptors. Choose the band that best fits, then the mark within it.</p>
<h3>Reading <span class="on">10 marks</span></h3>
<table class="bands">
<tr><td class="bd">9–10</td><td>Thorough, perceptive evaluation of ideas from the text(s); evidence questioned and weighed; ideas developed and combined into a convincing argument.</td></tr>
<tr><td class="bd">7–8</td><td>Clear evaluation of several ideas; a range of ideas used and developed with purpose.</td></tr>
<tr><td class="bd">5–6</td><td>A range of relevant ideas used, some development; evaluation is occasional or simple.</td></tr>
<tr><td class="bd">3–4</td><td>Some relevant ideas, mostly repeated rather than developed; little or no evaluation.</td></tr>
<tr><td class="bd">1–2</td><td>Limited use of the text(s); may copy or misunderstand.</td></tr>
</table>
<h3>Writing <span class="on">25 marks</span></h3>
<table class="bands">
<tr><td class="bd">22–25</td><td>Highly effective style and register for the audience; confident command of the form; well-structured, persuasive argument; wide, precise vocabulary; varied sentences; very accurate.</td></tr>
<tr><td class="bd">17–21</td><td>Effective style and appropriate register; secure form; clear, logical structure; good vocabulary; mostly accurate.</td></tr>
<tr><td class="bd">12–16</td><td>Generally appropriate style; some awareness of form and audience; ideas mostly organised; some errors that do not impede meaning.</td></tr>
<tr><td class="bd">7–11</td><td>Simple style; inconsistent register; limited structure; errors sometimes distract.</td></tr>
<tr><td class="bd">1–6</td><td>Little sense of form or audience; weak organisation; frequent errors that impede meaning.</td></tr>
</table>
<div class="tip"><b>QUICK CHECK:</b> An answer that only repeats the text rarely scores above 6 for Reading, however well it is written. Look for the words “however”, “but”, “this suggests” and “this overlooks”. They usually mark where the evaluation is.</div>
</section>'''

TRACKER = '''<section class="page">
<div class="eyebrow">Progress</div>
<h2>Score tracker</h2>
<table class="track">
<tr><th>Part</th><th>Max</th><th>Task 1</th><th>Task 2</th><th>Task 3</th><th>Task 4</th></tr>
<tr><td>1(a) Analysis &amp; evaluation</td><td>5</td><td></td><td></td><td></td><td></td></tr>
<tr><td>1(b) Reading</td><td>10</td><td></td><td></td><td></td><td></td></tr>
<tr><td>1(b) Writing</td><td>25</td><td></td><td></td><td></td><td></td></tr>
<tr class="tot"><td>Total</td><td>40</td><td></td><td></td><td></td><td></td></tr>
</table>
<h3>If your lowest score is…</h3>
<table class="glance">
<tr><td><b>1(a)</b></td><td>Name the technique or claim, quote briefly, then say how it affects the reader or whether it convinces you.</td></tr>
<tr><td><b>1(b) Reading</b></td><td>You are probably repeating. Add a “yes, but…” to every idea you use, and question at least two pieces of evidence.</td></tr>
<tr><td><b>1(b) Writing</b></td><td>Check the form toolkit. Match your register to the audience, plan four or five paragraphs, and save three minutes to proofread.</td></tr>
</table>
</section>'''

END = '''<section class="page end">
<div class="eyebrow">Next step</div>
<h2>Complete your 0500 preparation</h2>
<p><b>IGCSE 0500 Complete Exam Guide (2027):</b> the method for every question on both papers, with model answers, timing plans and the top 10 mark-losing mistakes.</p>
<p><b>IGCSE 0500 Paper 1 Practice Pack (2027):</b> three full Paper 1 Reading practice papers with original texts and detailed mark schemes.</p>
<p>Search <b>PassWithPurpose</b> on Teachers Pay Teachers.</p>
<div class="tip"><b>ENJOYED THIS PACK?</b> A short review on TPT helps other teachers find it, and earns you TPT credits towards your next purchase.</div>
<p class="small">© 2026 Marcé van Moerkerken · PassWithPurpose. Licensed for use by one teacher/classroom or one student. Please do not share or upload to public websites. Based on the published Cambridge IGCSE First Language English 0500 syllabus for 2027–2029. This is independent practice material and is not produced, endorsed or approved by Cambridge University Press &amp; Assessment. All texts, people and places are fictional.</p>
</section>'''

CSS_EXTRA = '''
.model{border-left:3px solid var(--gold);padding:4px 0 4px 14px;font:10.2pt/1.55 Lora,serif}
.model p{margin:0 0 7px}.model .hl{font-size:13pt;margin-bottom:6px}
.model .small-meta{font:italic 9pt Lato;color:var(--muted)}
.model .recs{margin:0 0 7px;padding-left:20px}
.why{font-size:9.6pt;padding-left:18px}.why li{margin-bottom:3px}
.plan td{border:1px solid var(--line);height:9mm}
.plan td:nth-child(odd){width:24mm;font-weight:700;color:var(--navy);background:var(--pale);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.plan.map td{height:12mm;background:none !important}
.plan.map td:nth-child(2){width:14mm}
.plan.para td{height:14mm}.plan.para td:first-child{width:42mm}
.checks{font-size:10pt}
'''

if __name__ == "__main__":
    import common
    common.CSS += CSS_EXTRA
    CSS = common.CSS
    build()
