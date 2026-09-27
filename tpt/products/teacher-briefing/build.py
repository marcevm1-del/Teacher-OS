"""Build the free 2027 changes teacher briefing (lead magnet). Facts follow the Complete Exam Guide."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import common

HERE = pathlib.Path(__file__).parent
OUT_PDF = HERE.parent.parent / "FREE-IGCSE-0500-2027-Changes-Teacher-Briefing.pdf"

COVER = '''<section class="cover"><div class="frame">
<div class="brand">PASSWITHPURPOSE</div>
<div class="badge"><small>FREE</small>2027<small>BRIEFING</small></div>
<div class="kicker">CAMBRIDGE IGCSE · FIRST LANGUAGE ENGLISH · 0500</div>
<h1>What Changes<br><em>in 2027</em></h1>
<p class="lede">A teacher’s briefing on the new 0500 exam: what is different, what it means for your classroom, and what to do this term.</p>
<ul class="feat">
<li>Both papers at a glance</li><li>The six changes that matter</li>
<li>Classroom actions for each change</li><li>Year 10–11 planning map</li>
<li>Five ready-to-use lesson starters</li><li>Department meeting checklist</li>
</ul>
<div class="author"><b>Marcé van Moerkerken</b><br>PGCE Secondary English (Summa Cum Laude)<br>International school English teacher, UAE</div>
<div class="disc">For exams from June 2027. Based on the published 2027–2029 syllabus. Independent; not produced or endorsed by Cambridge University Press &amp; Assessment. Always confirm details against the current syllabus document.</div>
</div></section>'''

GLANCE = '''<section class="page">
<div class="eyebrow">Section 1</div>
<h2>The new exam at a glance</h2>
<p>Two written papers, each 2 hours and 80 marks, each worth 50% of the grade. Some centres enter candidates for the Coursework Portfolio (Component 3) instead of Paper 2.</p>
<h3>Paper 1 · Reading <span class="on">three texts, about 1,400 words</span></h3>
<table class="glance">
<tr><th>Question</th><th>Text</th><th>Task</th><th>Marks</th></tr>
<tr><td>Q1</td><td>A</td><td>Comprehension: explicit and implicit meaning (tests all five reading skills)</td><td>20</td></tr>
<tr><td>Q2(a)</td><td>B</td><td>Selective summary, max 120 words</td><td>15 (10R + 5W)</td></tr>
<tr><td>Q2(b)</td><td>B</td><td><b>New:</b> writer’s attitudes and opinions</td><td>5</td></tr>
<tr><td>Q3</td><td>C</td><td>Short answers, including <b>2-mark</b> word meanings (key words in bold)</td><td>10</td></tr>
<tr><td>Q3</td><td>C</td><td>Language task, 200–250 words</td><td>10</td></tr>
<tr><td>Q4</td><td>C</td><td>Extended response (letter, report, journal, speech, interview or article), 250–300 words</td><td>20 (10R + 10W)</td></tr>
</table>
<h3>Paper 2 · Directed Writing and Composition</h3>
<table class="glance">
<tr><th>Question</th><th>Task</th><th>Marks</th></tr>
<tr><td>1(a)</td><td><b>New:</b> structured question on 1–2 texts (550–650 words): analyse and evaluate ideas, including how the writer influences readers</td><td>5</td></tr>
<tr><td>1(b)</td><td>Directed writing: speech, letter, article or report, 250–350 words</td><td>35 (10R + 25W)</td></tr>
<tr><td>Section B</td><td>Composition: one of four titles (two descriptive, two narrative), 350–450 words</td><td>40</td></tr>
</table>
</section>'''

CHANGES = [
 ("Paper 1 has four equal questions",
  "Q1–Q4 are each worth 20 marks. Students who spend too long on the early questions will lose the most at the end.",
  "Teach “marks = minutes”. Run a timed session where students must move on when the timer sounds, then compare the Q4 answers with untimed ones."),
 ("Q1 tests all five reading skills",
  "Comprehension is no longer only retrieval. Inference and explanation questions sit alongside “give” and “identify”.",
  "Label every Q1 practice question as SAYS (explicit) or SUGGESTS (implicit) before students answer. Knowing the type tells them how to answer."),
 ("A new summary question, 2(b)",
  "Five marks for identifying a writer’s attitudes or opinions and explaining how we can tell.",
  "Drill one structure: attitude + evidence + brief explanation. Use opinion columns and editorials. Ten minutes a week is enough."),
 ("Word meanings are worth 2 marks",
  "Key words appear in bold. With two marks available, a vague one-word answer may not be enough: students need a precise meaning that fits the context.",
  "Teach the swap test: put your meaning back into the sentence. If it does not fit exactly, refine it."),
 ("Shorter writing targets",
  "Language task: 200–250 words. Q4: 250–300 words. Directed writing: 250–350 words.",
  "Shorter means selection matters more. Practise cutting a 400-word answer down to the target without losing marks. It forces students to prioritise."),
 ("Paper 2 now assesses evaluation of how writers influence readers",
  "Question 1(a) asks students to analyse and evaluate the texts directly, and the reading marks in 1(b) reward evaluation over repetition.",
  "Build a “repeat → use → develop → evaluate” ladder into every directed writing lesson. Give students texts with deliberately weak evidence to question."),
]

def changes_pages():
    rows = "".join(f'''<div class="chg"><div class="num">{i}</div><div><h4>{t}</h4><p><b>What it means:</b> {m}</p><p class="act"><b>Do this:</b> {a}</p></div></div>'''
                   for i, (t, m, a) in enumerate(CHANGES, 1))
    return f'''<section class="page"><div class="eyebrow">Section 2</div><h2>Six changes that matter, and what to do</h2>{rows}</section>'''

PLAN = '''<section class="page">
<div class="eyebrow">Section 3</div>
<h2>A Year 10–11 planning map</h2>
<p>One way to sequence a two-year course so that every question type is taught, practised and revisited before the exam.</p>
<table class="glance">
<tr><th>Term</th><th>Reading focus</th><th>Writing focus</th></tr>
<tr><td>Y10 Autumn</td><td>Q1 explicit/implicit; word meanings in context</td><td>Descriptive composition: senses, structure, imagery</td></tr>
<tr><td>Y10 Spring</td><td>Q3 language task: Choose → Zoom → Connect</td><td>Narrative composition: story mountain, show don’t tell</td></tr>
<tr><td>Y10 Summer</td><td>Q2(a) summary and Q2(b) attitudes</td><td>Directed writing forms: letter and article</td></tr>
<tr><td>Y11 Autumn</td><td>Q4 extended response in all six forms</td><td>Directed writing forms: speech and report; 1(a) evaluation</td></tr>
<tr><td>Y11 Spring</td><td>Full Paper 1 mocks, timed</td><td>Full Paper 2 mocks, timed</td></tr>
<tr><td>Y11 Summer</td><td>Targeted revision from mock data</td><td>Targeted revision from mock data</td></tr>
</table>
<h3>Five lesson starters for the new questions</h3>
<table class="glance">
<tr><td>Says or suggests?</td><td>Show five Q1-style questions. Students sort them into explicit and implicit in two minutes.</td></tr>
<tr><td>Swap test</td><td>One bold word in a sentence. Students write a meaning, swap it in, and vote on which meanings fit exactly.</td></tr>
<tr><td>Attitude in 3</td><td>Read one paragraph of an opinion piece. Write one sentence: attitude + evidence + explanation.</td></tr>
<tr><td>Spot the weak evidence</td><td>Show a persuasive paragraph with an unsourced statistic and a single anecdote. Students name what is missing.</td></tr>
<tr><td>120-word squeeze</td><td>Give students a 160-word summary. They cut it to 120 without losing a single point.</td></tr>
</table>
<h3>Department meeting checklist</h3>
<p class="checks">☐ Everyone has read the 2027–2029 syllabus &nbsp; ☐ Old past papers flagged as “old format” &nbsp; ☐ Mock papers rewritten in the new format &nbsp; ☐ Mark schemes updated for 2-mark word meanings and Q2(b) &nbsp; ☐ Paper 2 lessons include explicit evaluation &nbsp; ☐ Students told which Paper 2 route they are taking</p>
</section>'''

END = '''<section class="page end">
<div class="eyebrow">Ready-made resources</div>
<h2>Save hours of planning</h2>
<p>If you’d like the practice material done for you, every PassWithPurpose resource is written for the new 2027 format, with original texts and full mark schemes:</p>
<table class="glance">
<tr><td>Complete Exam Guide</td><td>The method for every question on both papers, with model answers and timing plans</td></tr>
<tr><td>Paper 1 Practice Pack</td><td>Three full Paper 1 papers: nine original texts, question papers and mark schemes</td></tr>
<tr><td>Paper 2 Directed Writing Pack</td><td>Four Section A tasks with 1(a) questions and annotated model answers</td></tr>
<tr><td>Composition Pack</td><td>Descriptive and narrative toolkits, 20 titles and four model compositions</td></tr>
</table>
<p>Search <b>PassWithPurpose</b> on Teachers Pay Teachers, and <b>follow the store</b> to hear when new 2027 resources are released.</p>
<div class="tip"><b>FOUND THIS USEFUL?</b> A quick rating on TPT helps other 0500 teachers find it.</div>
<p class="small">© 2026 Marcé van Moerkerken · PassWithPurpose. Free to share with colleagues in your department. Based on the published Cambridge IGCSE First Language English 0500 syllabus for 2027–2029. Always confirm details against the current syllabus document. Not produced, endorsed or approved by Cambridge University Press &amp; Assessment.</p>
</section>'''

CSS_EXTRA = '''
.chg{display:grid;grid-template-columns:10mm 1fr;gap:3mm;padding:7px 0;border-top:1px solid var(--line);page-break-inside:avoid}
.chg .num{font:600 20pt Lora;color:var(--gold);line-height:1}
.chg h4{margin-bottom:3px}.chg p{margin:0 0 3px;font-size:9.8pt}
.chg .act{background:var(--pale);padding:4px 8px;border-left:2px solid var(--gold);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.checks{font-size:9.8pt;line-height:1.8}
'''

if __name__ == "__main__":
    common.CSS += CSS_EXTRA
    common.render_pdf(HERE, GLANCE + changes_pages() + PLAN + END, COVER, OUT_PDF, "The 2027 0500 Changes · Free Teacher Briefing")
