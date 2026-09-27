"""Build the Summary Writing Workbook: content.py -> pack.html -> PDF."""
import pathlib, sys
from content import ARTICLES, SWAPS, UMBRELLAS
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import common

HERE = pathlib.Path(__file__).parent
OUT_PDF = HERE.parent.parent / "IGCSE-0500-Summary-Writing-Workbook-2027.pdf"

def article_pages(a):
    ps = "".join(f'<p><span class="pn">{i}</span>{p}</p>' for i, p in enumerate(a["paras"], 1))
    qs = f'''<div class="q"><div class="qn">(a)</div><div class="qt">According to the text, what are {a["focus"]}? Write a summary in continuous prose, using your own words as far as possible. Your summary should be no more than <b>120 words</b>.</div><div class="qm">[15]</div></div>
<div class="q"><div class="qn">(b)</div><div class="qt">{a["q2b"]}</div><div class="qm">[5]</div></div>'''
    tag = "Guided practice" if a["guided"] else "Independent practice"
    first = f'''<section class="page"><div class="eyebrow">Article {a["n"]} · {tag}</div><h2>{a["title"]}</h2>
<div class="extract">{ps}</div><h3>Questions</h3>{qs}</section>'''
    if a["guided"]:
        rows = "".join(f"<tr><td class='pl'>{i}</td><td></td><td></td></tr>" for i in range(1, 11))
        second = f'''<section class="page frame-page"><div class="eyebrow">Article {a["n"]} · Guided plan</div><h2>Plan your summary</h2>
<table class="plan"><tr><td>Step 1 · Focus heading</td><td>{a["focus"].capitalize()}</td></tr></table>
<h3>Step 2 · Harvest the points</h3>
<table class="harvest"><tr><th>#</th><th>Point in the text (paragraph)</th><th>My own words</th></tr>{rows}</table>
<h3>Step 3 · Group under umbrella words</h3>
<table class="plan"><tr><td>Group A</td><td></td></tr><tr><td>Group B</td><td></td></tr><tr><td>Group C</td><td></td></tr></table>
<p class="checks"><b>Step 4 ·</b> Write 100–115 words. &nbsp; <b>Step 5 ·</b> Count: ______ words. Cross out any copied phrases. &nbsp; ☐ No examples ☐ No opinions ☐ Third person</p></section>'''
    else:
        second = f'''<section class="page"><div class="eyebrow">Article {a["n"]} · Your answer</div><h2>Write your answers</h2>
<h3>(a) Summary <span class="on">max 120 words · aim for 100–115</span></h3><div class="lines">{"<div></div>" * 13}</div>
<h3>(b) Attitude <span class="on">attitude + evidence + explanation</span></h3><div class="lines">{"<div></div>" * 7}</div></section>'''
    return [first, second]

def answer_page(a):
    pts = "".join(f"<li>{p}</li>" for p in a["points"])
    return f'''<section class="page ms"><div class="eyebrow">Answers · Article {a["n"]}</div><h2>{a["title"]}: answers</h2>
<h3>(a) Points to credit <span class="on">1 mark each, up to 10 for reading</span></h3><ol class="pts">{pts}</ol>
<h3>Model summary <span class="on">{len(a["summary"].split())} words</span></h3><div class="model"><p>{a["summary"]}</p></div>
<h3>(b) Model answer <span class="on">5 marks</span></h3><div class="model"><p>{a["model2b"]}</p></div></section>'''

COVER = '''<section class="cover"><div class="frame">
<div class="brand">PASSWITHPURPOSE</div>
<div class="badge"><small>NEW</small>2027<small>FORMAT</small></div>
<div class="kicker">CAMBRIDGE IGCSE · FIRST LANGUAGE ENGLISH · 0500</div>
<h1>Summary Writing<br><em>Workbook</em></h1>
<p class="lede">Step-by-step practice for Paper 1 Question 2: the 120-word summary (15 marks) and the new 2(b) attitudes question (5 marks), with six original articles and model answers for every one.</p>
<ul class="feat">
<li>6 original articles</li><li>3 guided, 3 independent</li>
<li>5-step summary method</li><li>Own-words toolkit</li>
<li>Points lists for every article</li><li>6 model summaries (≤120 words)</li>
<li>6 model 2(b) answers</li><li>Mistakes page &amp; tracker</li>
</ul>
<div class="author"><b>Marcé van Moerkerken</b><br>PGCE Secondary English (Summa Cum Laude)<br>International school English teacher, UAE</div>
<div class="disc">For exams in 2027, 2028 and 2029. Independent practice material; not produced or endorsed by Cambridge University Press &amp; Assessment. All articles are original.</div>
</div></section>'''

def howto():
    swaps = "".join(f"<li>“{a}” → {b}</li>" for a, b in SWAPS)
    ums = "".join(f"<li>{a} → <b>{b}</b></li>" for a, b in UMBRELLAS)
    return f'''<section class="page"><div class="eyebrow">Start here</div><h2>The method</h2>
<p>Question 2 is based on Text B. Part (a) asks for a selective summary in continuous prose of no more than 120 words: 10 marks for reading (the points) and 5 for writing (clarity, concision, own words). Part (b) asks about the writer’s attitudes or opinions, for 5 marks.</p>
<table class="glance">
<tr><td>1 Lock the focus</td><td>Rewrite the question’s focus as a heading. Only points that answer it count.</td></tr>
<tr><td>2 Harvest</td><td>Number every relevant point in the margin. Ignore examples, statistics and anecdotes unless they <i>are</i> the point.</td></tr>
<tr><td>3 Group</td><td>Merge related points under an umbrella word.</td></tr>
<tr><td>4 Write once, tightly</td><td>100–115 words, no introduction, no conclusion, no opinions.</td></tr>
<tr><td>5 Check</td><td>Count the words. Cross out any phrase copied from the text.</td></tr>
</table>
<h3>Own-words toolkit</h3>
<div class="two"><div class="col"><h4>Swap the phrase</h4><ul class="kit">{swaps}</ul></div>
<div class="col"><h4>Use umbrella words</h4><ul class="kit">{ums}</ul></div></div>
<h3>2(b): one structure, every time</h3>
<div class="tip"><b>ATTITUDE + EVIDENCE + EXPLANATION:</b> “The writer is <i>sceptical</i> of fashion companies: saying they ‘insist’ they are changing suggests the writer does not believe them.” Useful attitude words: admiring, critical, sceptical, sympathetic, dismissive, balanced, optimistic, cynical.</div></section>'''

MISTAKES = '''<section class="page"><div class="eyebrow">Avoid these</div><h2>Five mistakes that cost summary marks</h2>
<table class="mk"><tr><th>Mistake</th><th>Weak</th><th>Strong</th></tr>
<tr><td class="ql">Copying</td><td class="weak">Dyes and chemicals from factories often pour into rivers, turning them strange colours.</td><td class="strong">Factory chemicals contaminate rivers.</td></tr>
<tr><td class="ql">Examples</td><td class="weak">A single pair of jeans can require thousands of litres of water.</td><td class="strong">Producing clothes consumes vast amounts of water.</td></tr>
<tr><td class="ql">Note form</td><td class="weak">• water • chemicals • plastic • wages</td><td class="strong">Continuous prose linked with connectives: “also”, “in addition”, “finally”.</td></tr>
<tr><td class="ql">Opinions</td><td class="weak">I think fast fashion is terrible and everyone should stop buying it.</td><td class="strong">No opinions: report the text’s points only.</td></tr>
<tr><td class="ql">Too long</td><td class="weak">An introduction, every point in detail, a conclusion: 170 words.</td><td class="strong">100–115 words. Anything over 120 is not credited.</td></tr>
</table>
<div class="tip"><b>QUICK CHECK:</b> Could someone who had never read the article understand your summary? Does every sentence answer the focus? If yes to both, you are on track.</div></section>'''

BANDS = '''<section class="page ms"><div class="eyebrow">For teachers, tutors &amp; students</div><h2>Marking guidance &amp; tracker</h2>
<p class="note">Bands written for this workbook to support consistent practice marking; not official Cambridge descriptors.</p>
<h3>2(a) Reading <span class="on">10 marks</span></h3><p>Award 1 mark per relevant point from the points list (or any valid equivalent), up to 10.</p>
<h3>2(a) Writing <span class="on">5 marks</span></h3>
<table class="bands">
<tr><td class="bd">5</td><td>Wholly relevant, concise and well organised; ideas skilfully grouped and linked; consistently own words.</td></tr>
<tr><td class="bd">4</td><td>Mostly focused and fluent; ideas clearly organised; mostly own words.</td></tr>
<tr><td class="bd">3</td><td>Generally clear; some repetition, lifting or loosely relevant material.</td></tr>
<tr><td class="bd">1–2</td><td>Much lifting, listing or note form; may be over-long or include opinion.</td></tr>
</table>
<h3>2(b) <span class="on">5 marks</span></h3><p>1 mark per developed point: attitude + evidence + brief explanation.</p>
<h3>My progress</h3>
<table class="track"><tr><th>Article</th><th>Points /10</th><th>Writing /5</th><th>2(b) /5</th><th>Words</th><th>One thing to improve</th></tr>
''' + "".join(f"<tr><td>{i}</td><td></td><td></td><td></td><td></td><td></td></tr>" for i in range(1, 7)) + '''</table></section>'''

END = '''<section class="page end"><div class="eyebrow">Next step</div><h2>Put the skill into a full paper</h2>
<p>The <b>Paper 1 Practice Packs 1 &amp; 2</b> include a full Question 2 in each of six practice papers. The <b>Language Analysis Workbook</b> does for Question 3 what this workbook does for Question 2.</p>
<p>Search <b>PassWithPurpose</b> on Teachers Pay Teachers.</p>
<div class="tip"><b>ENJOYED THIS WORKBOOK?</b> A short review on TPT helps other teachers find it.</div>
<p class="small">© 2026 Marcé van Moerkerken · PassWithPurpose. Licensed for use by one teacher/classroom (including a copy for each student) or one student. Not produced, endorsed or approved by Cambridge University Press &amp; Assessment. All articles are original.</p></section>'''

CSS_EXTRA = '''
.extract{border:1px solid var(--line);background:var(--pale);padding:10px 14px 4px;font:10.2pt/1.52 Lora,serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.extract p{position:relative;padding-left:7mm;margin:0 0 7px}
.plan td{border:1px solid var(--line);height:11mm}
.plan td:first-child{width:38mm;font-weight:700;color:var(--navy);background:var(--pale);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.harvest td{border:1px solid var(--line);height:10.5mm}.harvest .pl{width:8mm;font-weight:700;color:var(--gold)}
.lines div{border-bottom:1px solid var(--line);height:9mm}
.model{border-left:3px solid var(--gold);padding:2px 0 2px 12px;font:9.8pt/1.5 Lora,serif}
.pts{font-size:9.4pt;columns:2;column-gap:8mm;padding-left:18px}.pts li{break-inside:avoid;margin-bottom:2px}
.kit{font-size:9.2pt;padding-left:16px;margin:4px 0}.kit li{margin-bottom:4px}
.mk td{font-size:9.2pt}.mk .ql{width:24mm;font-weight:700;color:var(--navy)}.mk .weak{color:#9b3b32;width:40%}.mk .strong{color:#2f6b4f}
.track td{height:10mm}
.checks{font-size:9.6pt;margin-top:8px}
'''

if __name__ == "__main__":
    common.CSS += CSS_EXTRA
    pages = [howto(), MISTAKES]
    for a in ARTICLES:
        pages += article_pages(a)
    pages += [answer_page(a) for a in ARTICLES] + [BANDS, END]
    common.render_pdf(HERE, "".join(pages), COVER, OUT_PDF, "IGCSE 0500 Summary Writing Workbook")
