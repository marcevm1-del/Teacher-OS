"""Build the 0500 Revision Flashcards: 32 printable cards, 8 per A4 page."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import common

HERE = pathlib.Path(__file__).parent
OUT_PDF = HERE.parent.parent / "IGCSE-0500-Revision-Flashcards-2027.pdf"

# (category, title, lines)
CARDS = [
 ("P1", "Paper 1 at a glance", ["2 hours · 80 marks · 3 texts (A, B, C)", "Q1 Text A · 20 marks", "Q2 Text B · 15 + 5 marks", "Q3 Text C · 10 + 10 marks", "Q4 Text C · 20 marks", "Read all texts first: 15 min"]),
 ("P1", "Q1 Comprehension", ["<b>Find</b> the key word, then locate the lines", "<b>Prove:</b> for “suggest”, say what the detail <i>shows</i>", "<b>Phrase</b> in your own words", "One clear point per mark", "Questions follow the order of the text"]),
 ("P1", "Says or suggests?", ["<b>SAYS</b> (explicit): give, identify, what does the writer tell us", "→ precise, no commentary", "<b>SUGGESTS</b> (implicit): suggest, explain how, what does this show", "→ inference + anchor it to a detail"]),
 ("P1", "Q2(a) Summary: 5 steps", ["1 Lock the focus as a heading", "2 Number every relevant point", "3 Group points under umbrella words", "4 Write 100–115 words of continuous prose", "5 Count words; cross out copied phrases"]),
 ("P1", "Q2(a) Summary: rules", ["✔ Own words ✔ Connectives", "✔ Cover the whole text ✔ Third person", "✘ Examples and statistics (unless they are the point)", "✘ Bullet points ✘ Opinions", "✘ More than 120 words"]),
 ("P1", "Q2(b) Attitudes · 5 marks", ["Attitude + evidence + explanation", "“The writer is <i>critical</i> of…: calling it ‘baffling’ shows…”", "Useful attitude words: admiring, critical, sympathetic, sceptical, hopeful, dismissive"]),
 ("P1", "Q3 Word meanings · 2 marks", ["Read the whole sentence + the one before", "Write a precise meaning for <i>this</i> context", "<b>Swap test:</b> put it back in the sentence", "Vague one-word answers risk losing a mark"]),
 ("P1", "Q3 Language task", ["200–250 words · 10 marks", "<b>Choose</b> 3–4 short choices per paragraph", "<b>Zoom</b>: literal meaning → connotations", "<b>Connect</b>: effect on the reader and why", "Never “vivid imagery” without explaining it"]),
 ("P1", "Q4 Extended response", ["250–300 words · 10R + 10W", "<b>Mine</b> details for every bullet", "<b>Stretch</b>: develop and infer", "<b>Voice</b>: right person, form, audience", "Plan in 3 columns, one per bullet"]),
 ("P1", "Q4 forms", ["Letter: greeting, purpose, sign-off", "Report: title, subheadings, recommendations", "Journal: first person, date, reflection", "Speech: address audience, strong close", "Interview: speaker labels · Article: headline"]),
 ("P2", "Paper 2 at a glance", ["2 hours · 80 marks", "Section A: 1(a) 5 marks + 1(b) 35 marks", "Texts: 550–650 words", "Section B composition: 40 marks", "350–450 words, 1 of 4 titles"]),
 ("P2", "1(a) Structured question", ["Name the technique or claim precisely", "Quote briefly", "Explain the effect on the reader", "or judge how convincing it is", "Keep it short: 5 marks only"]),
 ("P2", "1(b) Directed writing: 5 steps", ["1 Decode: form, audience, purpose, position", "2 Map: agree / disagree / “yes, but…”", "3 Evaluate: reliable? biased? missing?", "4 Plan 4–5 paragraphs", "5 Write 250–350 words; proofread"]),
 ("P2", "Repeat → Evaluate", ["<b>Repeat:</b> “The text says…”", "<b>Use:</b> put the idea in your argument", "<b>Develop:</b> “This matters because…”", "<b>Evaluate:</b> “However, the evidence…”", "Evaluation lifts the reading marks"]),
 ("P2", "Questioning evidence", ["Statistic with no source?", "Only one example or story?", "Small or one-sided survey?", "Do the texts contradict each other?", "What has the writer left out?"]),
 ("P2", "Speech & article", ["<b>Speech:</b> greet the audience, hook, “we”, direct address, memorable close, thanks", "<b>Article:</b> headline, attention-grabbing opening, lively paragraphs, strong final line"]),
 ("P2", "Letter & report", ["<b>Letter:</b> “Dear…”, purpose in paragraph 1, polite call to action, “Yours sincerely/faithfully”", "<b>Report:</b> title, purpose, subheadings, balanced findings, numbered recommendations, no emotive language"]),
 ("C", "Descriptive: structure", ["1 Wide view: place, time, mood", "2 Zoom in on one detail", "3 A person or movement", "4 A shift: time, weather, light", "5 Return to the wide view, changed"]),
 ("C", "Descriptive: do & don't", ["✔ All five senses, specific", "✔ One controlling image", "✔ One-line paragraph for impact", "✘ Plot creep ✘ Clichés", "✘ “I could see… I could hear…”"]),
 ("C", "Narrative: story mountain", ["1 Hook in the middle of the action", "2 Context: who, where, what they want", "3 Complication", "4 Climax: slow down here", "5 Resolution: show the change"]),
 ("C", "Narrative: do & don't", ["✔ One event, 2–3 characters", "✔ Show, don’t tell", "✔ A returning object", "✘ “It was all a dream”", "✘ Rushed endings"]),
 ("L", "Imagery", ["<b>Simile:</b> comparison with like/as", "<b>Metaphor:</b> says one thing <i>is</i> another", "<b>Personification:</b> human qualities to things", "Always explain the <i>picture</i> and <i>why</i>"]),
 ("L", "Words and sounds", ["<b>Connotation:</b> the feelings a word carries", "<b>Onomatopoeia:</b> word sounds like its meaning", "<b>Alliteration / sibilance:</b> repeated sounds", "Link the sound to the mood"]),
 ("L", "Structure and contrast", ["<b>Juxtaposition:</b> opposites placed together", "<b>Short sentence:</b> impact, shock, finality", "<b>List:</b> abundance, chaos, build-up", "<b>Pathetic fallacy:</b> weather mirrors mood"]),
 ("L", "Persuasive devices", ["Direct address (“you”)", "Rule of three", "Rhetorical question", "Statistic or expert", "Counter-argument + rebuttal", "Emotive language"]),
 ("L", "Explaining effect", ["“…suggests that…”", "“…carries connotations of…”", "“…implies…”", "“…so the reader feels…”", "“…emphasising how…”", "“…creating a sense of…”"]),
 ("X", "Command words (1)", ["<b>Analyse:</b> examine how the parts work", "<b>Evaluate:</b> judge quality or value", "<b>Explain:</b> give reasons, how or why", "<b>Identify:</b> name it, briefly"]),
 ("X", "Command words (2)", ["<b>Give:</b> produce an answer from the text", "<b>Describe:</b> state the main features", "<b>Suggest:</b> a reasonable idea", "<b>Justify:</b> support with evidence"]),
 ("X", "Paper 1 timing", ["Read all texts: 15 min", "Q1: 20 min", "Q2: 25 min", "Q3: 25 min", "Q4: 30 min", "Check: 5 min"]),
 ("X", "Paper 2 timing", ["Read texts + 1(a): 15 min", "Plan 1(b): 8 min", "Write 1(b): 35 min", "Plan composition: 10 min", "Write composition: 45 min", "Check: 7 min"]),
 ("X", "Top mistakes (1)", ["Copying phrases from the text", "Ignoring a Q4 bullet", "Adding ideas not in the text", "Naming techniques without explaining", "Poor timing"]),
 ("X", "Top mistakes (2)", ["Examples in the summary", "Repeating texts in directed writing", "A story for a descriptive title", "Word meanings that don’t fit", "Slipping tenses; careless punctuation"]),
]

LABEL = {"P1": "Paper 1", "P2": "Paper 2 · Section A", "C": "Composition", "L": "Language", "X": "Exam technique"}

def card(c, t, lines):
    li = "".join(f"<li>{x}</li>" for x in lines)
    return f'<div class="card {c}"><div class="cat">{LABEL[c]}</div><h4>{t}</h4><ul>{li}</ul><div class="brandmark">PASSWITHPURPOSE · 0500</div></div>'

def card_pages():
    out = []
    for i in range(0, len(CARDS), 8):
        cells = "".join(card(*c) for c in CARDS[i:i + 8])
        out.append(f'<section class="page cards"><div class="grid">{cells}</div></section>')
    return out

COVER = '''<section class="cover"><div class="frame">
<div class="brand">PASSWITHPURPOSE</div>
<div class="badge"><small>NEW</small>2027<small>FORMAT</small></div>
<div class="kicker">CAMBRIDGE IGCSE · FIRST LANGUAGE ENGLISH · 0500</div>
<h1>Revision<br><em>Flashcards</em></h1>
<p class="lede">32 printable revision cards covering every question on both papers: the method, the forms, the techniques, the command words and the timing.</p>
<ul class="feat">
<li>10 Paper 1 method cards</li><li>7 Paper 2 Section A cards</li>
<li>4 composition cards</li><li>5 language technique cards</li>
<li>2 command word cards</li><li>2 timing cards</li>
<li>2 top-mistakes cards</li><li>Colour-coded by topic</li>
</ul>
<div class="author"><b>Marcé van Moerkerken</b><br>PGCE Secondary English (Summa Cum Laude)<br>International school English teacher, UAE</div>
<div class="disc">For exams in 2027, 2028 and 2029. Independent revision material; not produced or endorsed by Cambridge University Press &amp; Assessment.</div>
</div></section>'''

HOWTO = '''<section class="page">
<div class="eyebrow">Start here</div>
<h2>How to use these cards</h2>
<p><b>Print</b> pages 2–5 on card or thick paper (A4, 100% scale) and cut along the dashed lines. Each page holds eight cards.</p>
<table class="glance">
<tr><th>Colour</th><th>Topic</th><th>Cards</th></tr>
<tr><td><span class="sw P1"></span>Navy</td><td>Paper 1 Reading methods</td><td>10</td></tr>
<tr><td><span class="sw P2"></span>Gold</td><td>Paper 2 Section A: directed writing</td><td>7</td></tr>
<tr><td><span class="sw C"></span>Green</td><td>Paper 2 Section B: composition</td><td>4</td></tr>
<tr><td><span class="sw L"></span>Red</td><td>Language techniques and explaining effect</td><td>5</td></tr>
<tr><td><span class="sw X"></span>Grey</td><td>Command words, timing and top mistakes</td><td>6</td></tr>
</table>
<h3>Five ways to revise with them</h3>
<table class="glance">
<tr><td>Cover and recall</td><td>Read the title, cover the card, say the method aloud, then check.</td></tr>
<tr><td>Pair quiz</td><td>A partner reads a title; you explain it in 30 seconds.</td></tr>
<tr><td>Before every practice question</td><td>Pull out the card for that question and follow it step by step.</td></tr>
<tr><td>Exam week</td><td>Read the timing and top-mistakes cards the night before each paper.</td></tr>
<tr><td>Classroom</td><td>Display the set as a wall, or use one card as a lesson starter.</td></tr>
</table>
<div class="tip"><b>FOR TEACHERS:</b> Your licence covers printing a set for each student in your class.</div>
</section>'''

END = '''<section class="page end">
<div class="eyebrow">Next step</div>
<h2>Practise what the cards teach</h2>
<p>The cards give students the method. The PassWithPurpose packs give them the practice: original texts, full question papers, mark schemes and model answers for the new 2027 format.</p>
<table class="glance">
<tr><td>Complete Exam Guide</td><td>Every question explained, with worked examples</td></tr>
<tr><td>Paper 1 Practice Pack</td><td>Three full Paper 1 practice papers</td></tr>
<tr><td>Paper 2 Directed Writing Pack</td><td>Four Section A tasks with model answers</td></tr>
<tr><td>Composition Pack</td><td>Toolkits, 20 titles and four model compositions</td></tr>
</table>
<p>Search <b>PassWithPurpose</b> on Teachers Pay Teachers.</p>
<p class="small">© 2026 Marcé van Moerkerken · PassWithPurpose. Licensed for use by one teacher/classroom (including a printed set per student) or one student. Not produced, endorsed or approved by Cambridge University Press &amp; Assessment.</p>
</section>'''

CSS_EXTRA = '''
.cards{padding:0}
.grid{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(4,62mm);gap:0;border:1px dashed #b9b2a3}
.card{border:1px dashed #b9b2a3;padding:5mm 6mm 4mm;position:relative;overflow:hidden;border-top:6px solid var(--navy);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.card.P2{border-top-color:var(--gold)}.card.C{border-top-color:#2f6b4f}.card.L{border-top-color:#9b3b32}.card.X{border-top-color:#6b7385}
.card .cat{font:700 6.5pt Lato;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.card h4{font:600 12pt Lora;margin:1mm 0 2mm;color:var(--navy)}
.card ul{margin:0;padding-left:14px;font-size:9pt;line-height:1.42}
.card li{margin-bottom:1px}
.brandmark{position:absolute;bottom:2.5mm;right:5mm;font:700 5.5pt Lato;letter-spacing:.14em;color:#b9b2a3}
.sw{display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:6px;vertical-align:middle;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.sw.P1{background:var(--navy)}.sw.P2{background:var(--gold)}.sw.C{background:#2f6b4f}.sw.L{background:#9b3b32}.sw.X{background:#6b7385}
'''

if __name__ == "__main__":
    assert len(CARDS) == 32, len(CARDS)
    common.CSS += CSS_EXTRA
    common.render_pdf(HERE, HOWTO + "".join(card_pages()) + END, COVER, OUT_PDF, "IGCSE 0500 Revision Flashcards")
