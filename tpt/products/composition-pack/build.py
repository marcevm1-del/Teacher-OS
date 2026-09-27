"""Build the Composition Pack: content.py -> pack.html -> PDF."""
import pathlib, re, sys
from content import SETS, MODELS, UPGRADES
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import common

HERE = pathlib.Path(__file__).parent
OUT_PDF = HERE.parent.parent / "IGCSE-0500-Composition-Pack-2027.pdf"
TITLE = "IGCSE 0500 Composition Pack"

def words(paras):
    return len(re.sub(r"<[^>]+>", " ", " ".join(paras)).split())

def prompt_pages():
    cards = []
    for s in SETS:
        items = "".join(f'<div class="q"><div class="qn">{i}</div><div class="qt"><span class="tag {k[0]}">{k}</span>{t}</div><div class="qm">[40]</div></div>'
                        for i, (k, t) in enumerate([("Descriptive", s["d"][0]), ("Descriptive", s["d"][1]),
                                                    ("Narrative", s["s"][0]), ("Narrative", s["s"][1])], 1))
        cards.append(f'<div class="set"><h3>Practice Set {s["n"]}</h3>{items}</div>')
    rub = '<div class="rubric"><b>Section B · Composition · 40 marks · about 1 hour.</b> Answer <b>one</b> question from the set. Write about <b>350 to 450 words</b>. Marks are awarded for content and structure and for style and accuracy. Spend about 10 minutes planning.</div>'
    return [f'''<section class="page"><div class="eyebrow">Practice prompts</div><h2>20 exam-style titles</h2>{rub}{"".join(cards[:3])}</section>''',
            f'''<section class="page"><div class="eyebrow">Practice prompts</div><h2>20 exam-style titles (continued)</h2>{"".join(cards[3:])}
<div class="tip"><b>HOW TO CHOOSE IN THE EXAM:</b> Spend one minute on each title. Pick the one where you can already <i>see</i> a place or a moment, not the one with the most exciting plot. A simple idea written with control scores more than an ambitious one that runs out of time.</div></section>''']

def model_pages():
    out = []
    for m in MODELS:
        body = "".join(f"<p>{p}</p>" for p in m["text"])
        notes = "".join(f"<li>{n}</li>" for n in m["notes"])
        out.append(f'''<section class="page">
<div class="eyebrow">Model composition · {m["kind"]}</div>
<h2>{m["title"]}</h2>
<p class="note">From Practice Set {m["set"]} · a top-band response ({words(m["text"])} words). Read it after planning your own answer. It shows one strong way to answer the title, not the only one.</p>
<div class="model">{body}</div>
<h3>What makes it work</h3><ul class="why">{notes}</ul></section>''')
    return out

def upgrade_pages():
    ex = "".join(f'<tr><td class="ql">{i}</td><td>{w}</td><td class="blank"></td></tr>' for i, (w, _, _) in enumerate(UPGRADES, 1))
    ans = "".join(f'<tr><td class="ql">{i}</td><td><i>{s}</i><div class="tech">{t}</div></td></tr>' for i, (_, s, t) in enumerate(UPGRADES, 1))
    return [f'''<section class="page"><div class="eyebrow">Workshop</div><h2>Sentence upgrade workshop</h2>
<p>Each sentence below is accurate but flat. Rewrite it so that it would impress an examiner. Aim to <b>show</b> rather than tell, use precise nouns and verbs, and bring in at least one sense.</p>
<table class="up"><tr><th></th><th>Flat sentence</th><th>Your upgrade</th></tr>{ex}</table></section>''',
            f'''<section class="page ms"><div class="eyebrow">Workshop answers</div><h2>Model upgrades</h2>
<p class="note">One possible upgrade for each sentence, with the technique it shows. Accept any version that uses the technique well.</p>
<table class="mst">{ans}</table>
<div class="tip"><b>TRY THIS:</b> Choose one paragraph of your last composition. Find the three flattest sentences and upgrade them using the techniques above.</div></section>''']

def build():
    pages = [HOWTO, DESC, NARR] + prompt_pages() + [PLAN_D, PLAN_N] + upgrade_pages() + model_pages() + [BANDS, CHECK, END]
    common.CSS += CSS_EXTRA
    common.render_pdf(HERE, "".join(pages), COVER, OUT_PDF, TITLE)
    print("model words:", [words(m["text"]) for m in MODELS])

COVER = '''<section class="cover"><div class="frame">
<div class="brand">PASSWITHPURPOSE</div>
<div class="badge"><small>NEW</small>2027<small>FORMAT</small></div>
<div class="kicker">CAMBRIDGE IGCSE · FIRST LANGUAGE ENGLISH · 0500</div>
<h1>Paper 2<br><em>Composition Pack</em></h1>
<p class="lede">Everything students need for Section B: descriptive and narrative toolkits, 20 exam-style titles, planning sheets, a sentence-upgrade workshop and four annotated model compositions.</p>
<ul class="feat">
<li>Descriptive writing toolkit</li><li>Narrative writing toolkit</li>
<li>20 exam-style titles in 5 sets</li><li>2 photocopiable planning sheets</li>
<li>Sentence upgrade workshop</li><li>4 annotated model compositions</li>
<li>Marking bands (40 marks)</li><li>Self-assessment checklist</li>
</ul>
<div class="author"><b>Marcé van Moerkerken</b><br>PGCE Secondary English (Summa Cum Laude)<br>International school English teacher, UAE</div>
<div class="disc">For exams in 2027, 2028 and 2029. Independent practice material; not produced or endorsed by Cambridge University Press &amp; Assessment. All writing is original.</div>
</div></section>'''

HOWTO = '''<section class="page">
<div class="eyebrow">Start here</div>
<h2>How to use this pack</h2>
<p>In Section B of Cambridge IGCSE First Language English (0500) Paper 2, candidates choose <b>one</b> of four titles: two descriptive and two narrative. They write about 350–450 words. There is no reading text, so every mark is for writing.</p>
<table class="glance">
<tr><th>Strand</th><th>What examiners look for</th><th>Marks</th></tr>
<tr><td>Content &amp; structure</td><td>Ideas that are engaging and developed; a clear, deliberate structure; paragraphs that build an effect</td><td>16</td></tr>
<tr><td>Style &amp; accuracy</td><td>Precise, ambitious vocabulary; varied sentences; control of tense and punctuation; accurate spelling and grammar</td><td>24</td></tr>
</table>
<h3>Descriptive or narrative?</h3>
<table class="glance">
<tr><td>Descriptive</td><td>Creates a vivid <b>picture and atmosphere</b>. Little or no plot. The biggest mistake is turning it into a story.</td></tr>
<tr><td>Narrative</td><td>Tells a <b>story</b> with one central event, a small cast and a satisfying ending. The biggest mistake is too much plot and too little feeling.</td></tr>
</table>
<h3>A sequence that works</h3>
<table class="glance">
<tr><td>Lesson 1</td><td>Descriptive toolkit → Upgrade workshop → Plan a descriptive title from Set 1</td></tr>
<tr><td>Lesson 2</td><td>Read a descriptive model → Write the Set 1 descriptive piece → Self-assess with the checklist</td></tr>
<tr><td>Lesson 3</td><td>Narrative toolkit → Plan a narrative title from Set 1 using the story mountain</td></tr>
<tr><td>Lesson 4</td><td>Read a narrative model → Write the piece → Peer-mark with the bands</td></tr>
<tr><td>Then</td><td>Sets 2–5 for timed practice: 10 minutes planning, 45 minutes writing, 5 minutes checking</td></tr>
</table>
<div class="tip"><b>BEFORE YOU START:</b> This pack uses the 16/24 split from recent 0500 composition marking. Check the split for 2027 in the current syllabus. The bands in this pack are written for practice marking and are not official Cambridge descriptors.</div>
</section>'''

DESC = '''<section class="page">
<div class="eyebrow">Toolkit</div>
<h2>Descriptive writing toolkit</h2>
<h3>A five-part structure</h3>
<table class="glance">
<tr><td>1 Wide view</td><td>Establish the place, time and mood in a few strong sentences.</td></tr>
<tr><td>2 Zoom in</td><td>Focus closely on one small, specific detail: an object, a texture, a sound.</td></tr>
<tr><td>3 Person or movement</td><td>Bring in a figure or some motion to give the scene life, without starting a plot.</td></tr>
<tr><td>4 Shift</td><td>Change something: time passes, the weather turns, the light fades, the mood alters.</td></tr>
<tr><td>5 Return</td><td>Go back to the wide view, now changed. Echo your opening.</td></tr>
</table>
<h3>Techniques that lift a description</h3>
<div class="two">
<div class="col"><ul>
<li><b>Use all five senses</b>, and make them specific: not “a nice smell”, but “cardamom and diesel”.</li>
<li><b>Precise nouns and verbs</b> do more than adjectives: “the shutters <i>rattled</i>” beats “the very loud shutters”.</li>
<li><b>One controlling image</b> (e.g. the market as a sleeping animal) holds the piece together.</li></ul></div>
<div class="col"><ul>
<li><b>Vary sentences:</b> a one-line paragraph for impact; long, flowing sentences for movement.</li>
<li><b>Contrast:</b> light/dark, noise/silence, past/present.</li>
<li><b>Present tense</b> creates immediacy. Whichever tense you choose, keep it consistent.</li></ul></div>
</div>
<h3>Avoid</h3>
<table class="glance">
<tr><td>Plot creep</td><td>If a crime, chase or rescue appears, you are writing a story.</td></tr>
<tr><td>Cliché</td><td>“Blood-red sun”, “deafening silence”, “the wind howled like a wolf”.</td></tr>
<tr><td>Adjective piles</td><td>“The dark, gloomy, scary, eerie house”: choose one precise word instead.</td></tr>
<tr><td>Lists of senses</td><td>“I could see… I could hear… I could smell…” Weave the senses in naturally.</td></tr>
</table>
</section>'''

NARR = '''<section class="page">
<div class="eyebrow">Toolkit</div>
<h2>Narrative writing toolkit</h2>
<h3>The story mountain</h3>
<table class="glance">
<tr><td>1 Hook</td><td>Start in the middle of something: an action, a line of dialogue, a strange detail.</td></tr>
<tr><td>2 Context</td><td>Who, where, and what the character wants. Keep backstory short.</td></tr>
<tr><td>3 Complication</td><td>Something goes wrong or changes. Tension rises.</td></tr>
<tr><td>4 Climax</td><td>The turning point. Slow it down: this is where the detail belongs.</td></tr>
<tr><td>5 Resolution</td><td>Show how things have changed. A reflective, circular or twist ending.</td></tr>
</table>
<h3>Four ways to open</h3>
<table class="glance">
<tr><td>Dialogue</td><td>“Don’t open it,” she said, but I already had.</td></tr>
<tr><td>Action</td><td>The ferry lurched, and my suitcase slid across the deck towards the rail.</td></tr>
<tr><td>Strange detail</td><td>The letter was shorter than I remembered, and the handwriting was enormous.</td></tr>
<tr><td>Short statement</td><td>Nobody believed me about the lake.</td></tr>
</table>
<h3>Craft essentials</h3>
<div class="two">
<div class="col"><ul>
<li><b>Show, don’t tell:</b> not “I was scared” but “My hand froze on the door handle.”</li>
<li><b>One central event, two or three characters.</b> 450 words is not a novel.</li>
<li><b>Build tension</b> with short sentences, delay and sensory focus at the key moment.</li></ul></div>
<div class="col"><ul>
<li><b>Dialogue:</b> new speaker, new line; punctuation inside the speech marks; use it sparingly.</li>
<li><b>An object</b> that returns at the end (a candle, a letter, a key) gives shape and meaning.</li>
<li><b>Avoid</b> “it was all a dream”, rushed endings and action with no feeling.</li></ul></div>
</div>
</section>'''

PLAN_D = '''<section class="page frame-page"><div class="eyebrow">Photocopiable</div><h2>Descriptive planning sheet</h2>
<table class="plan"><tr><td>Title</td><td colspan="3"></td></tr>
<tr><td>Place &amp; time</td><td></td><td>Mood</td><td></td></tr>
<tr><td>Controlling image</td><td colspan="3"></td></tr></table>
<h3>Five-part structure</h3>
<table class="plan para">
<tr><td>1 Wide view</td><td></td></tr><tr><td>2 Zoom in</td><td></td></tr>
<tr><td>3 Person / movement</td><td></td></tr><tr><td>4 Shift</td><td></td></tr><tr><td>5 Return, changed</td><td></td></tr></table>
<h3>Senses bank</h3>
<table class="plan senses"><tr><td>Sight</td><td></td><td>Sound</td><td></td></tr>
<tr><td>Smell</td><td></td><td>Touch / taste</td><td></td></tr></table>
<p class="checks">Five ambitious words I will use: ____________ · ____________ · ____________ · ____________ · ____________</p>
</section>'''

PLAN_N = '''<section class="page frame-page"><div class="eyebrow">Photocopiable</div><h2>Narrative planning sheet</h2>
<table class="plan"><tr><td>Title</td><td colspan="3"></td></tr>
<tr><td>Main character</td><td></td><td>Wants / fears</td><td></td></tr>
<tr><td>Setting</td><td></td><td>Central event</td><td></td></tr></table>
<h3>Story mountain</h3>
<table class="plan para">
<tr><td>1 Hook</td><td></td></tr><tr><td>2 Context</td><td></td></tr>
<tr><td>3 Complication</td><td></td></tr><tr><td>4 Climax (slow down)</td><td></td></tr><tr><td>5 Resolution</td><td></td></tr></table>
<table class="plan"><tr><td>First line</td><td colspan="3"></td></tr>
<tr><td>Last line</td><td colspan="3"></td></tr>
<tr><td>Returning object</td><td colspan="3"></td></tr></table>
</section>'''

BANDS = '''<section class="page ms">
<div class="eyebrow">For teachers, tutors &amp; students</div>
<h2>Marking guidance · Composition</h2>
<p class="note">These bands are written for this pack to support consistent practice marking. They follow the published assessment objectives but are not official Cambridge descriptors. Mark each strand separately, then add them together.</p>
<h3>Content &amp; structure <span class="on">16 marks</span></h3>
<table class="bands">
<tr><td class="bd">14–16</td><td>Highly engaging, original ideas, fully developed. Structure is deliberate and controlled: a descriptive piece builds a sustained atmosphere; a narrative has well-managed tension and a satisfying ending.</td></tr>
<tr><td class="bd">11–13</td><td>Interesting, well-developed ideas; clear, effective structure; paragraphs build an overall effect.</td></tr>
<tr><td class="bd">7–10</td><td>Relevant ideas with some development; a recognisable structure; descriptive pieces may drift into plot, or narratives may be rushed at the end.</td></tr>
<tr><td class="bd">4–6</td><td>Simple ideas; limited development; structure is loose or list-like.</td></tr>
<tr><td class="bd">1–3</td><td>Very limited ideas; little sense of organisation.</td></tr>
</table>
<h3>Style &amp; accuracy <span class="on">24 marks</span></h3>
<table class="bands">
<tr><td class="bd">21–24</td><td>Precise, ambitious vocabulary used with control; sentences varied for deliberate effect; fresh imagery; almost error-free spelling, punctuation and grammar.</td></tr>
<tr><td class="bd">16–20</td><td>Effective vocabulary and some varied sentence structures; imagery mostly fresh; generally accurate with occasional slips.</td></tr>
<tr><td class="bd">11–15</td><td>Some good vocabulary choices; limited sentence variety; some clichés; errors present but meaning clear.</td></tr>
<tr><td class="bd">6–10</td><td>Plain vocabulary; repetitive sentences; frequent errors, including tense and sentence boundaries.</td></tr>
<tr><td class="bd">1–5</td><td>Errors often obscure meaning; very limited vocabulary.</td></tr>
</table>
</section>'''

CHECK = '''<section class="page">
<div class="eyebrow">Self-assessment</div>
<h2>Composition checklist &amp; tracker</h2>
<div class="two">
<div class="col"><h4>Descriptive</h4><ul class="cl">
<li>☐ No plot: atmosphere, not events</li><li>☐ Five-part structure with a shift</li>
<li>☐ At least four senses, specific</li><li>☐ One controlling image</li>
<li>☐ A one-line paragraph for impact</li><li>☐ Ending echoes the opening</li></ul></div>
<div class="col"><h4>Narrative</h4><ul class="cl">
<li>☐ Hook in the first line</li><li>☐ One central event, few characters</li>
<li>☐ Feelings shown, not told</li><li>☐ Climax slowed down with detail</li>
<li>☐ Dialogue punctuated correctly</li><li>☐ Ending not rushed</li></ul></div>
</div>
<h4 style="margin-top:10px">Both</h4>
<p class="checks">☐ 350–450 words &nbsp; ☐ Consistent tense &nbsp; ☐ Varied sentence openings &nbsp; ☐ No clichés &nbsp; ☐ Paragraphs &nbsp; ☐ Proofread for full stops and commas</p>
<h3>Score tracker</h3>
<table class="track">
<tr><th>Set</th><th>Title chosen</th><th>Content &amp; structure /16</th><th>Style &amp; accuracy /24</th><th>Total /40</th></tr>
<tr><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td></td><td></td><td></td><td></td></tr>
<tr><td>3</td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td></td><td></td><td></td><td></td></tr>
<tr><td>5</td><td></td><td></td><td></td><td></td></tr>
</table>
</section>'''

END = '''<section class="page end">
<div class="eyebrow">Next step</div>
<h2>Complete your 0500 preparation</h2>
<p><b>IGCSE 0500 Complete Exam Guide (2027):</b> the method for every question on both papers.</p>
<p><b>Paper 1 Practice Pack:</b> three full Paper 1 Reading practice papers with mark schemes.</p>
<p><b>Paper 2 Directed Writing Pack:</b> four Section A tasks with annotated model answers.</p>
<p>Search <b>PassWithPurpose</b> on Teachers Pay Teachers.</p>
<div class="tip"><b>ENJOYED THIS PACK?</b> A short review on TPT helps other teachers find it, and earns you TPT credits towards your next purchase.</div>
<p class="small">© 2026 Marcé van Moerkerken · PassWithPurpose. Licensed for use by one teacher/classroom or one student. Please do not share or upload to public websites. Based on the published Cambridge IGCSE First Language English 0500 syllabus for 2027–2029. This is independent practice material and is not produced, endorsed or approved by Cambridge University Press &amp; Assessment. All writing is original.</p>
</section>'''

CSS_EXTRA = '''
.model{border-left:3px solid var(--gold);padding:4px 0 4px 14px;font:9.9pt/1.5 Lora,serif}
.model p{margin:0 0 7px}
.why{font-size:9.3pt;padding-left:18px;margin:4px 0 0}.why li{margin-bottom:2px}
.set{margin-bottom:6px}.set h3{margin-top:10px}
.tag{display:inline-block;font:700 7pt Lato;letter-spacing:.08em;text-transform:uppercase;padding:1px 6px;border-radius:3px;margin-right:6px;color:#fff;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.tag.D{background:var(--navy)}.tag.N{background:var(--gold)}
.plan td{border:1px solid var(--line);height:10mm}
.plan td:nth-child(odd){width:30mm;font-weight:700;color:var(--navy);background:var(--pale);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.plan.para td{height:21mm}.plan.para td:first-child{width:38mm}
.plan.senses td{height:18mm}
.checks{font-size:10pt;margin-top:10px}
.up td{height:22mm}.up .blank{width:55%;border-left:1px solid var(--line)}
.up .ql,.mst .ql{width:8mm;font-weight:700;color:var(--gold)}
.tech{font:700 8pt Lato;color:var(--muted);margin-top:3px}
.mst td{padding:6px 7px}
.cl{list-style:none;padding:0;font-size:10pt}.cl li{margin-bottom:4px}
.track td{height:10mm}
'''

if __name__ == "__main__":
    build()
