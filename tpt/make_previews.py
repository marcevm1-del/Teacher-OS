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
}

def box(x, y, h):
    return (x, y, x + h * A4, y + h)

def slide(src, path, title, sub, pages, banner):
    doc = pymupdf.open(); pg = doc.new_page(width=W, height=H)
    pg.draw_rect(pg.rect, color=None, fill=NAVY)
    pg.insert_textbox(pymupdf.Rect(30, 30, W - 30, 100), title, fontsize=38, fontname="hebo", color=WHITE, align=1)
    pg.insert_textbox(pymupdf.Rect(40, 95, W - 40, 140), sub, fontsize=22, fontname="helv", color=GOLD, align=1)
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
    pg.insert_textbox(pymupdf.Rect(20, H - 48, W - 20, H - 10), banner, fontsize=22, fontname="hebo", color=NAVY, align=1)
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
