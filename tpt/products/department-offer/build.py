"""Build the two-page Department Licence offer sheet (attach to school outreach emails)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import common

HERE = pathlib.Path(__file__).parent
OUT_PDF = HERE.parent.parent.parent / "money" / "PassWithPurpose-Department-Licence-Offer.pdf"

# Edit these, then rebuild: NODE_PATH=$(npm root -g) python3 build.py
PRICE_LICENCE = "750"
PRICE_LICENCE_CPD = "1,250"
CONTACT = "[your email] · [your WhatsApp number]"

COVER = '''<section class="cover"><div class="frame">
<div class="brand">PASSWITHPURPOSE</div>
<div class="badge"><small>FOR</small>2027<small>EXAMS</small></div>
<div class="kicker">FOR HEADS OF ENGLISH · CAMBRIDGE IGCSE 0500</div>
<h1>The 0500<br><em>Department Pack</em></h1>
<p class="lede">Ready-to-teach resources for the new 2027 Cambridge IGCSE First Language English exam, licensed for your whole department.</p>
<ul class="feat">
<li>Complete Exam Guide</li><li>6 full Paper 1 practice papers</li>
<li>8 Paper 2 Section A tasks</li><li>Composition, Q2 &amp; Q3 workbooks</li>
<li>32 revision flashcards</li><li>Every teacher, every class</li>
<li>Print for every student</li><li>Free updates to 2029</li>
</ul>
<div class="author"><b>Marcé van Moerkerken</b><br>PGCE Secondary English (Summa Cum Laude)<br>International school English teacher, UAE</div>
<div class="disc">Independent resources based on the published 2027–2029 syllabus; not produced or endorsed by Cambridge University Press &amp; Assessment.</div>
</div></section>'''

BODY = f'''<section class="page">
<div class="eyebrow">The offer</div>
<h2>Why departments are updating now</h2>
<p>From June 2027 the 0500 exam changes: four 20-mark questions in Paper 1, a new attitudes question (2b), 2-mark word meanings, and a split Paper 2 directed writing task that now assesses how writers influence readers. Past papers from earlier years no longer match, and writing new mocks takes a department many hours.</p>
<h3>What your department receives</h3>
<table class="glance">
<tr><th>Resource</th><th>Contents</th><th>Pages</th></tr>
<tr><td>Complete Exam Guide</td><td>Method for every question on both papers, weak vs strong answers, timing plans</td><td>14</td></tr>
<tr><td>Paper 1 Practice Packs 1 &amp; 2</td><td>6 full papers in the new format, 18 original texts, mark schemes, marking bands</td><td>58</td></tr>
<tr><td>Paper 2 Directed Writing 1 &amp; 2</td><td>8 Section A tasks (speeches, letters, articles, reports), annotated model answers</td><td>54</td></tr>
<tr><td>Summary &amp; Language Workbooks</td><td>Twelve texts with guided practice and model answers for Q2 and Q3</td><td>37</td></tr>
<tr><td>Composition Pack</td><td>Descriptive and narrative toolkits, 20 titles, 4 annotated model compositions</td><td>17</td></tr>
<tr><td>Revision Flashcards</td><td>32 printable cards covering every method, form and timing plan</td><td>7</td></tr>
</table>
<h3>Licence options</h3>
<table class="glance price">
<tr><th>Option</th><th>Includes</th><th>Price</th></tr>
<tr><td>Department Licence</td><td>All nine resources for every English teacher in one school; unlimited printing for your students; free updates for the 2027–2029 syllabus</td><td><b>{PRICE_LICENCE} AED</b></td></tr>
<tr><td>Department Licence + CPD</td><td>Everything above plus a 60-minute online session for your team: “Teaching the 2027 0500 changes”</td><td><b>{PRICE_LICENCE_CPD} AED</b></td></tr>
<tr><td>Group of schools</td><td>Licences for several schools in one group</td><td>On request</td></tr>
</table>
<div class="tip"><b>TRY BEFORE YOU BUY:</b> I’m happy to send a free sample (one full Paper 1 practice set and the free 2027 changes briefing) so your team can judge the quality first.</div>
<h3>How it works</h3>
<p>1. Reply to confirm the option you’d like. &nbsp;2. I send an invoice to your finance team. &nbsp;3. On payment, you receive all PDFs and a licence certificate for your school.</p>
<p><b>Contact:</b> Marcé van Moerkerken · {CONTACT}</p>
<p class="small">All texts are original. Resources are independent and are not produced, endorsed or approved by Cambridge University Press &amp; Assessment. Licence covers one school site; resources may not be shared outside the school or uploaded to public websites.</p>
</section>'''

if __name__ == "__main__":
    common.CSS += ".price td:last-child{white-space:nowrap}"
    common.render_pdf(HERE, BODY, COVER, OUT_PDF, "0500 Department Pack · Licence offer")
