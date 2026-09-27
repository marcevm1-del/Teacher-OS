"""Make square TPT preview images and a free preview PDF from a product PDF.

Usage: python3 make_previews.py  (edit PRODUCTS below to add a product)
"""
import pathlib
import pymupdf

HERE = pathlib.Path(__file__).parent
W = H = 1000
NAVY, GOLD, WHITE = (0.09, 0.15, 0.27), (0.95, 0.72, 0.20), (1, 1, 1)
A4 = 595 / 842

PRODUCTS = {
    "IGCSE-0500-Paper-1-Practice-Pack-2027.pdf": dict(
        out="previews/paper1-pack", banner="Cambridge IGCSE 0500 · New 2027 format · 29-page PDF",
        free_pages=[1, 2, 4, 7],
        slides=[
            ("IGCSE 0500 Paper 1 Practice Pack", "3 full papers in the new 2027 format", [1]),
            ("9 original texts + full question papers", "Every question in the new 4 × 20-mark format", [4, 7]),
            ("Detailed mark schemes", "Answers, summary points & indicative content", [9, 10]),
            ("Marking bands + score tracker", "Ready for mocks, homework and tutoring", [2, 27, 28]),
        ]),
    "IGCSE-0500-Paper-1-Practice-Pack-Vol-2-2027.pdf": dict(
        out="previews/paper1-pack-vol2", banner="Cambridge IGCSE 0500 · New 2027 format · 29-page PDF",
        free_pages=[1, 2, 4, 8],
        slides=[
            ("IGCSE 0500 Paper 1 Practice Pack 2", "3 more full papers: Sets 4–6", [1]),
            ("9 new original texts + question papers", "Journeys · The Natural World · Belonging", [12, 8]),
            ("Detailed mark schemes", "Answers, summary points & indicative content", [9, 10]),
            ("Q4 in new forms: interview, speech, article", "Plus marking bands and score tracker", [16, 27, 28]),
        ]),
    "IGCSE-0500-Paper-2-Directed-Writing-Pack-2027.pdf": dict(
        out="previews/paper2-pack", banner="Cambridge IGCSE 0500 · New 2027 format · 27-page PDF",
        free_pages=[1, 2, 3, 7],
        slides=[
            ("IGCSE 0500 Paper 2 Directed Writing", "4 Section A tasks: speech, letter, article, report", [1]),
            ("Original texts + full question papers", "New 1(a) evaluation question + 1(b) directed writing", [5, 7]),
            ("Annotated model answers", "Top-band responses with mark schemes", [9, 8]),
            ("Toolkit, planning frame & marking bands", "Teach students to evaluate, not repeat", [3, 4, 25]),
        ]),
    "IGCSE-0500-Paper-2-Directed-Writing-Pack-Vol-2-2027.pdf": dict(
        out="previews/paper2-pack-vol2", banner="Cambridge IGCSE 0500 · New 2027 format · 27-page PDF",
        free_pages=[1, 2, 3, 7],
        slides=[
            ("IGCSE 0500 Paper 2 Directed Writing 2", "4 more Section A tasks: Tasks 5–8", [1]),
            ("New topics, texts & question papers", "Exams vs coursework · space · car-free towns · teen jobs", [5, 7]),
            ("Annotated model answers", "Article, speech, letter and report", [9, 8]),
            ("Toolkit, planning frame & marking bands", "Teach students to evaluate, not repeat", [3, 4, 25]),
        ]),
    "IGCSE-0500-Composition-Pack-2027.pdf": dict(
        out="previews/composition-pack", banner="Cambridge IGCSE 0500 · Paper 2 Section B · 17-page PDF",
        free_pages=[1, 2, 3, 5],
        slides=[
            ("IGCSE 0500 Composition Pack", "Descriptive & narrative writing for Paper 2 Section B", [1]),
            ("Descriptive & narrative toolkits", "Structures, techniques and traps to avoid", [3, 4]),
            ("4 annotated model compositions", "Two descriptive, two narrative, with notes", [11, 13]),
            ("20 titles, planning sheets & workshop", "Ready for lessons, homework and tutoring", [5, 7, 9]),
        ]),
    "FREE-IGCSE-0500-2027-Changes-Teacher-Briefing.pdf": dict(
        out="previews/teacher-briefing", banner="FREE · Cambridge IGCSE 0500 · 2027 changes briefing",
        free_pages=[1, 2],
        slides=[
            ("FREE: What Changes in 2027", "A teacher's briefing on the new IGCSE 0500 exam", [1]),
            ("Both papers + the six changes that matter", "With a classroom action for each change", [2, 3]),
            ("Planning map, starters & checklist", "Ready for your next department meeting", [4, 5]),
        ]),
    "IGCSE-0500-Revision-Flashcards-2027.pdf": dict(
        out="previews/revision-cards", banner="Cambridge IGCSE 0500 · 32 printable cards · 7-page PDF",
        free_pages=[1, 2, 3],
        slides=[
            ("IGCSE 0500 Revision Flashcards", "Every question, form and technique on 32 cards", [1]),
            ("Colour-coded by topic", "Paper 1 · Paper 2 · Composition · Language · Technique", [3, 4]),
            ("Print, cut, revise", "8 cards per A4 page", [5, 6]),
        ]),
}

def fit(pg, rect, text, size, font, color):
    """Insert text, shrinking the font until it fits (insert_textbox silently drops overflow)."""
    while pg.insert_textbox(rect, text, fontsize=size, fontname=font, color=color, align=1) < 0:
        size -= 1
        assert size > 10, text

def box(x, y, h):
    return (x, y, x + h * A4, y + h)

def slide(src, path, title, sub, pages, banner):
    doc = pymupdf.open(); pg = doc.new_page(width=W, height=H)
    pg.draw_rect(pg.rect, color=None, fill=NAVY)
    fit(pg, pymupdf.Rect(30, 30, W - 30, 100), title, 38, "hebo", WHITE)
    fit(pg, pymupdf.Rect(40, 95, W - 40, 140), sub, 22, "helv", GOLD)
    n = len(pages)
    h = {1: 760, 2: 600, 3: 420}[n]
    gap = 40 if n == 2 else 24
    total = n * h * A4 + (n - 1) * gap
    x0, y0 = (W - total) / 2, 160 + (H - 60 - 160 - h) / 2 if n > 1 else 160
    for i, pno in enumerate(pages):
        r = pymupdf.Rect(*box(x0 + i * (h * A4 + gap), y0, h))
        pg.draw_rect(r + (6, 6, 6, 6), color=None, fill=(0, 0, 0), fill_opacity=0.35)
        pg.draw_rect(r, color=None, fill=WHITE)
        pg.show_pdf_page(r, src, pno - 1)
    pg.draw_rect(pymupdf.Rect(0, H - 60, W, H), color=None, fill=GOLD)
    fit(pg, pymupdf.Rect(20, H - 48, W - 20, H - 10), banner, 22, "hebo", NAVY)
    pg.get_pixmap(dpi=144).save(path)

for pdf, cfg in PRODUCTS.items():
    src = pymupdf.open(HERE / pdf)
    out = HERE / cfg["out"]; out.mkdir(parents=True, exist_ok=True)
    for i, (t, s, pages) in enumerate(cfg["slides"], 1):
        slide(src, out / f"TPT-preview-{i}.png", t, s, pages, cfg["banner"])
    free = pymupdf.open()
    for p in cfg["free_pages"]:
        free.insert_pdf(src, from_page=p - 1, to_page=p - 1)
    free.save(out / "FREE-PREVIEW.pdf", garbage=3, deflate=True)
    print("built", out)
