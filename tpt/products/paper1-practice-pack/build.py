"""Build a Paper 1 Practice Pack volume: content.py -> pack.html -> PDF.

Usage: python3 build.py [content_dir]   (default: this folder = Volume 1)
The content folder holds content.py with SETS and optional META.
"""
import html, pathlib, re, subprocess, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from common import CSS, render_pdf

HERE = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
import content
SETS = content.SETS
META = dict(out="IGCSE-0500-Paper-1-Practice-Pack-2027.pdf", title="Practice Pack", footer="IGCSE 0500 Paper 1 Practice Pack")
META.update(getattr(content, "META", {}))
OUT_PDF = pathlib.Path(__file__).parent.parent.parent / META["out"]
NUMS = [s["n"] for s in SETS]

def words(paras):
    return sum(len(re.sub(r"<[^>]+>", "", p).split()) for p in paras)

def text_page(set_n, letter, t, extra=""):
    ps = "".join(f'<p><span class="pn">{i}</span>{p}</p>' for i, p in enumerate(t["paras"], 1))
    return f'''<section class="page text">
<div class="eyebrow">Set {set_n} · Insert</div>
<h2><span class="tl">Text {letter}</span> {t["title"]}</h2>
<div class="kind">{t["kind"]}{extra}</div>
<div class="body">{ps}</div></section>'''

def q(num, text, marks):
    return f'<div class="q"><div class="qn">{num}</div><div class="qt">{text}</div><div class="qm">[{marks}]</div></div>'

def answer_lines(n):
    return '<div class="lines">' + '<div></div>' * n + '</div>'

def question_paper(s):
    letters = "abcdefghij"
    q1, i, parts = [], 0, []
    for text, m in s["Q1"]:
        if text.startswith("(ii)"):
            parts.append(q("", text, m))
        else:
            parts.append(q(f"({letters[i]})", text, m)); i += 1
    q1 = "".join(parts)
    q3, i, parts = "", 0, []
    for text, m in s["Q3s"]:
        if text.startswith("(ii)"):
            parts.append(q("", text, m))
        else:
            parts.append(q(f"({letters[i]})", text, m)); i += 1
    q3 = "".join(parts)
    task, bullets, form, _ = s["Q4"]
    bl = "".join(f"<li>{b}</li>" for b in bullets)
    return f'''<section class="page qp">
<div class="eyebrow">Set {s["n"]} · Question paper</div>
<h2>Paper 1 Reading · Practice Set {s["n"]}</h2>
<div class="rubric"><b>2 hours · 80 marks.</b> Answer <b>all</b> questions. The texts are in the insert (Texts A, B and C).
Spend about 15 minutes reading before you write. Dictionaries are not allowed.</div>

<h3>Question 1 <span class="on">Text A: {s["A"]["title"]}</span></h3>
{q1}
<div class="total">Total for Question 1: [20]</div>

<h3>Question 2 <span class="on">Text B: {s["B"]["title"]}</span></h3>
{q("(a)", s["Q2a"][0] + "<br>You must use continuous writing (not note form) and your own words as far as possible. Your summary should not be more than <b>120 words</b>. Up to 10 marks are available for the content of your answer and up to 5 marks for the quality of your writing.", 15)}
{q("(b)", s["Q2b"][0], 5)}
<div class="total">Total for Question 2: [20]</div>

<h3>Question 3 <span class="on">Text C: {s["C"]["title"]}</span></h3>
{q3}
{q(f"({letters[i]})", s["Q3l"][0] + " Select three or four powerful words or phrases from <b>each</b> paragraph and explain how they are used effectively. Write about <b>200 to 250 words</b>.", 10)}
<div class="total">Total for Question 3: [20]</div>

<h3>Question 4 <span class="on">Text C: {s["C"]["title"]}</span></h3>
{q("", s["Q4"][0] + f"<br>In your {form} you should:<ul>{bl}</ul>Base your {form} on what you have read in Text C, but be careful to use your own words. Address each of the three bullet points. Begin your {form} appropriately. Write about <b>250 to 300 words</b>. Up to 10 marks are available for the content of your answer and up to 10 marks for the quality of your writing.", 20)}
<div class="total">Total for Question 4: [20]</div>
</section>'''

def mark_scheme(s):
    letters = "abcdefghij"
    rows, i = [], 0
    for (text, m), ans in zip(s["Q1"], s["Q1_ms"]):
        if text.startswith("(ii)"):
            lab = f"({letters[i-1]})(ii)"
        else:
            lab = f"({letters[i]})" + ("(i)" if "(i)" in text else ""); i += 1
        rows.append(f"<tr><td class='ql'>{lab}</td><td>{ans}</td><td class='mk'>{m}</td></tr>")
    q1 = "".join(rows)
    pts = "".join(f"<li>{p}</li>" for p in s["Q2a"][1])
    att = "".join(f"<li>{p}</li>" for p in s["Q2b"][1])
    rows, i = [], 0
    for (text, m), ans in zip(s["Q3s"], s["Q3s_ms"]):
        if text.startswith("(ii)"):
            lab = f"({letters[i-1]})(ii)"
        else:
            lab = f"({letters[i]})" + ("(i)" if "(i)" in text else ""); i += 1
        rows.append(f"<tr><td class='ql'>{lab}</td><td>{ans}</td><td class='mk'>{m}</td></tr>")
    q3 = "".join(rows)
    lang = "".join(f"<div class='col'><h4>{h}</h4><ul>{''.join(f'<li>{x}</li>' for x in xs)}</ul></div>" for h, xs in s["Q3l"][1])
    q4 = "".join(f"<div class='ind'><b>{h}.</b> {t}</div>" for h, t in s["Q4"][3])
    form = s["Q4"][2]
    conv = {"letter": "greeting, clear purpose in the opening, suitable sign-off; informal register to a friend",
            "report": "title, clear subheadings, objective and formal tone, recommendations",
            "journal": "first person, date or time, reflective and personal tone",
            "interview": "clear speaker labels, purposeful questions, developed answers in a natural but controlled voice",
            "speech": "address to the audience, direct appeals, signposting and a strong close",
            "article": "headline, engaging opening, clear paragraphs, lively but controlled tone"}[form]
    return f'''<section class="page ms">
<div class="eyebrow">Set {s["n"]} · Mark scheme</div>
<h2>Mark scheme · Practice Set {s["n"]}</h2>
<p class="note">Accept any valid alternative that is rooted in the text. Answers must be in the candidate’s own words where the question says so.</p>
<h3>Question 1 <span class="on">20 marks</span></h3>
<table class="mst">{q1}</table>
<h3>Question 2(a) <span class="on">15 marks = 10 Reading + 5 Writing</span></h3>
<p class="note"><b>Reading:</b> award 1 mark per relevant point, up to 10. <b>Writing:</b> use the Summary Writing bands on the Marking Guidance page.</p>
<ol class="pts">{pts}</ol>
<h3>Question 2(b) <span class="on">5 marks</span></h3>
<p class="note">Award 1 mark per developed point (attitude + evidence + brief explanation), up to 5. Indicative content:</p>
<ul class="pts">{att}</ul>
<h3>Question 3 short answers <span class="on">10 marks</span></h3>
<table class="mst">{q3}</table>
<h3>Question 3 language task <span class="on">10 marks</span></h3>
<p class="note">Mark with the Language Task bands. Indicative content. Reward any well-explained choice; do not reward technique-spotting without explanation.</p>
<div class="two">{lang}</div>
<h3>Question 4 <span class="on">20 marks = 10 Reading + 10 Writing</span></h3>
<p class="note">Mark with the Extended Response bands. Form conventions for a {form}: {conv}. Indicative content:</p>
{q4}
</section>'''

BANDS = '''<section class="page ms">
<div class="eyebrow">For teachers, tutors & students</div>
<h2>Marking guidance</h2>
<p class="note">These bands are written for this pack to support consistent practice marking. They follow the published assessment objectives but are not official Cambridge descriptors. Choose the band that best fits, then the mark within it.</p>
<h3>Summary writing <span class="on">Q2(a) · 5 marks</span></h3>
<table class="bands">
<tr><td class="bd">5</td><td>Wholly relevant, concise and well organised; ideas skilfully grouped and linked; consistently own words.</td></tr>
<tr><td class="bd">4</td><td>Mostly focused and fluent; ideas clearly organised; mostly own words.</td></tr>
<tr><td class="bd">3</td><td>Generally clear; some repetition, lifting or loosely relevant material; some attempt to organise.</td></tr>
<tr><td class="bd">1–2</td><td>Limited clarity; much lifting, listing or note form; may be over-long or include opinion.</td></tr>
<tr><td class="bd">0</td><td>Wholly copied or no relevant response.</td></tr>
</table>
<h3>Language task <span class="on">Q3 · 10 marks</span></h3>
<table class="bands">
<tr><td class="bd">9–10</td><td>A wide range of precise, well-chosen selections from both paragraphs; detailed, perceptive explanation of meaning <i>and</i> effect, including connotations; links to the writer’s overall purpose.</td></tr>
<tr><td class="bd">7–8</td><td>A good range of relevant choices; clear explanations of connotations and effects, several developed.</td></tr>
<tr><td class="bd">5–6</td><td>Some appropriate choices; explanations generally accurate but sometimes general or uneven between paragraphs.</td></tr>
<tr><td class="bd">3–4</td><td>Limited selection; some meanings explained; effects vague, or mainly technique labels.</td></tr>
<tr><td class="bd">1–2</td><td>Few choices; largely repeats the text or labels devices with no explanation.</td></tr>
</table>
<h3>Extended response <span class="on">Q4 · 10 Reading + 10 Writing</span></h3>
<table class="bands">
<tr><th></th><th>Reading (10)</th><th>Writing (10)</th></tr>
<tr><td class="bd">9–10</td><td>All three bullets addressed thoroughly; ideas developed with convincing, text-based inferences; a sustained, credible voice.</td><td>Confident, fluent style; register and form fully appropriate; well-structured; wide vocabulary; highly accurate.</td></tr>
<tr><td class="bd">7–8</td><td>All bullets addressed; some development and inference beyond the text’s surface.</td><td>Clear, varied style; appropriate register; well organised; mostly accurate.</td></tr>
<tr><td class="bd">5–6</td><td>Relevant ideas for each bullet but mainly retold; occasional inference.</td><td>Generally clear; some sense of form and audience; errors do not impede meaning.</td></tr>
<tr><td class="bd">3–4</td><td>Uneven coverage; relies on retelling or lifting; one bullet thin or missing.</td><td>Simple style; limited structure; errors sometimes distract.</td></tr>
<tr><td class="bd">1–2</td><td>Little relevant use of the text.</td><td>Frequent errors; little control of form or register.</td></tr>
</table>
</section>'''

def build():
    pages = [HOWTO]
    for s in SETS:
        total = words(s["A"]["paras"]) + words(s["B"]["paras"]) + words(s["C"]["paras"])
        pages += [f'''<section class="page divider"><div class="eyebrow gold">Practice Set {s["n"]}</div>
<h1>{s["theme"]}</h1><div class="dl">
<div><b>Text A</b> {s["A"]["title"]} <i>({s["A"]["kind"].lower()})</i></div>
<div><b>Text B</b> {s["B"]["title"]} <i>({s["B"]["kind"].lower()})</i></div>
<div><b>Text C</b> {s["C"]["title"]} <i>({s["C"]["kind"].lower()})</i></div>
<div class="wc">Insert: about {round(total, -1):,} words · Question paper · Mark scheme</div></div></section>''',
                  text_page(s["n"], "A", s["A"]), text_page(s["n"], "B", s["B"]), text_page(s["n"], "C", s["C"]),
                  question_paper(s), mark_scheme(s)]
    pages += [BANDS, TRACKER, END]
    import common
    common.CSS += META.get("extra_css", "")
    render_pdf(HERE, "".join(pages), COVER, OUT_PDF, META["footer"])

    print("words per set:", [words(s["A"]["paras"]) + words(s["B"]["paras"]) + words(s["C"]["paras"]) for s in SETS])

COVER = f'''<section class="cover"><div class="frame">
<div class="brand">PASSWITHPURPOSE</div>
<div class="badge"><small>NEW</small>2027<small>FORMAT</small></div>
<div class="kicker">CAMBRIDGE IGCSE · FIRST LANGUAGE ENGLISH · 0500</div>
<h1>Paper 1<br><em>{META["title"]}</em></h1>
<p class="lede">Three complete Paper 1 Reading practice papers in the new 2027 format, each with original texts, a full question paper and a detailed mark scheme.</p>
<ul class="feat">
<li>3 full practice papers (240 marks)</li><li>9 original reading texts</li>
<li>All four 20-mark questions</li><li>New Q2(b) attitudes question</li>
<li>2-mark word-meaning questions</li><li>Indicative content for every task</li>
<li>Marking bands for writing</li><li>Student score tracker</li>
</ul>
<div class="author"><b>Marcé van Moerkerken</b><br>PGCE Secondary English (Summa Cum Laude)<br>International school English teacher, UAE</div>
<div class="disc">For exams in 2027, 2028 and 2029. Independent practice material; not produced or endorsed by Cambridge University Press &amp; Assessment. All texts are original.</div>
</div></section>'''

HOWTO = f'''<section class="page">
<div class="eyebrow">Start here</div>
<h2>How to use this pack</h2>
<p>Each practice set follows the structure of the Cambridge IGCSE First Language English (0500) Paper 1 Reading exam from June 2027: three texts, four compulsory questions of 20 marks each, 80 marks in total, 2 hours.</p>
<table class="glance">
<tr><th>Question</th><th>Text</th><th>Task</th><th>Marks</th></tr>
<tr><td>Q1</td><td>A</td><td>Comprehension: explicit and implicit meaning</td><td>20</td></tr>
<tr><td>Q2(a)</td><td>B</td><td>Summary, max 120 words</td><td>15</td></tr>
<tr><td>Q2(b)</td><td>B</td><td>Writer’s attitudes and opinions</td><td>5</td></tr>
<tr><td>Q3</td><td>C</td><td>Short answers incl. 2-mark word meanings</td><td>10</td></tr>
<tr><td>Q3</td><td>C</td><td>Language task, 200–250 words</td><td>10</td></tr>
<tr><td>Q4</td><td>C</td><td>Extended response, 250–300 words</td><td>20</td></tr>
</table>
<h3>Three ways to use it</h3>
<div class="uses">
<div><b>Full mock</b><br>Print the insert and question paper. Set a strict 2-hour timer. Mark with the scheme and record scores on the tracker.</div>
<div><b>Question by question</b><br>Use one question as a lesson or homework. Mark it together, then rewrite the weakest answer.</div>
<div><b>Tutoring &amp; intervention</b><br>Diagnose with Set {NUMS[0]}, teach the weakest skill, and use Sets {NUMS[1]} and {NUMS[2]} to measure progress.</div>
</div>
<h3>Suggested timing (120 minutes)</h3>
<p>Read all texts 15 min · Q1 20 min · Q2 25 min · Q3 25 min · Q4 30 min · Check 5 min. Each question is worth the same 20 marks, so don’t let one question take time from the next.</p>
<div class="tip"><b>BEFORE YOU MARK:</b> The mark schemes give indicative content, not a list of the only right answers. Credit any valid point that is clearly rooted in the text.</div>
<h3>Contents</h3>
<table class="glance">
{"".join(f'<tr><td>Practice Set {x["n"]}</td><td>{x["theme"]}</td></tr>' for x in SETS)}
<tr><td>Marking guidance</td><td>Bands for Q2(a) writing, Q3 language task and Q4</td></tr>
<tr><td>Score tracker</td><td>Record and compare results across all three sets</td></tr>
</table>
</section>'''

TRACKER = f'''<section class="page">
<div class="eyebrow">Progress</div>
<h2>Score tracker</h2>
<p>Record your mark for each part. Look for the column that stays lowest: that is the skill to practise next.</p>
<table class="track">
<tr><th>Part</th><th>Max</th>{''.join(f'<th>Set {n}</th>' for n in NUMS)}</tr>
<tr><td>Q1 Comprehension</td><td>20</td><td></td><td></td><td></td></tr>
<tr><td>Q2(a) Summary: reading</td><td>10</td><td></td><td></td><td></td></tr>
<tr><td>Q2(a) Summary: writing</td><td>5</td><td></td><td></td><td></td></tr>
<tr><td>Q2(b) Attitudes</td><td>5</td><td></td><td></td><td></td></tr>
<tr><td>Q3 Short answers</td><td>10</td><td></td><td></td><td></td></tr>
<tr><td>Q3 Language task</td><td>10</td><td></td><td></td><td></td></tr>
<tr><td>Q4 Reading</td><td>10</td><td></td><td></td><td></td></tr>
<tr><td>Q4 Writing</td><td>10</td><td></td><td></td><td></td></tr>
<tr class="tot"><td>Total</td><td>80</td><td></td><td></td><td></td></tr>
</table>
<h3>If your lowest score is…</h3>
<table class="glance">
<tr><td><b>Q1</b></td><td>Count the marks and give one point per mark. For “suggest” questions, say what the detail <i>shows</i>, not just what it says.</td></tr>
<tr><td><b>Q2(a)</b></td><td>Lock the focus, number the points in the margin, group them under umbrella words, then write 100–115 words.</td></tr>
<tr><td><b>Q2(b)</b></td><td>Attitude + evidence + brief explanation, every time.</td></tr>
<tr><td><b>Q3 words</b></td><td>Swap your meaning back into the sentence to test it.</td></tr>
<tr><td><b>Q3 language</b></td><td>Choose → Zoom → Connect. Never write “vivid imagery” without explaining what the image is and why the writer uses it.</td></tr>
<tr><td><b>Q4</b></td><td>Plan in three columns, one per bullet. Develop, infer, and stay in role.</td></tr>
</table>
</section>'''

END = '''<section class="page end">
<div class="eyebrow">Next step</div>
<h2>Want the method behind every answer?</h2>
<p>The <b>IGCSE 0500 Complete Exam Guide (2027)</b> covers both papers question by question, with step-by-step frameworks, weak vs strong model answers, command words, timing plans and the top 10 mark-losing mistakes. It pairs with this pack: learn the method in the guide, then practise it here.</p>
<p>The <b>Paper 1 Practice Pack</b> series has two volumes, Sets 1–3 and Sets 4–6: six full practice papers in all.</p>
<p>The <b>IGCSE 0500 Paper 2 Directed Writing Pack (2027)</b> gives four complete Section A tasks – speech, letter, article and report – with annotated model answers.</p>
<p>Search <b>PassWithPurpose</b> on Teachers Pay Teachers.</p>
<div class="tip"><b>ENJOYED THIS PACK?</b> A short review on TPT helps other teachers find it, and earns you TPT credits towards your next purchase.</div>
<p class="small">© 2026 Marcé van Moerkerken · PassWithPurpose. Licensed for use by one teacher/classroom or one student. Please do not share or upload to public websites. Based on the published Cambridge IGCSE First Language English 0500 syllabus for 2027–2029. This is independent practice material and is not produced, endorsed or approved by Cambridge University Press &amp; Assessment. All texts and characters are original.</p>
</section>'''



if __name__ == "__main__":
    build()
