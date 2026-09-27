"""Shared styling and PDF rendering for PassWithPurpose products."""
import pathlib, subprocess
import pymupdf

HERE = pathlib.Path(__file__).parent

CSS = '''
@font-face{font-family:'Lato';font-style:italic;font-weight:400;src:url('../fonts/Lato-400i.ttf')}
@font-face{font-family:'Lato';font-style:normal;font-weight:400;src:url('../fonts/Lato-400.ttf')}
@font-face{font-family:'Lato';font-style:normal;font-weight:700;src:url('../fonts/Lato-700.ttf')}
@font-face{font-family:'Lora';font-style:italic;font-weight:500;src:url('../fonts/Lora-500i.ttf')}
@font-face{font-family:'Lora';font-style:normal;font-weight:500;src:url('../fonts/Lora-500.ttf')}
@font-face{font-family:'Lora';font-style:normal;font-weight:600;src:url('../fonts/Lora-600.ttf')}
@font-face{font-family:'Lora';font-style:normal;font-weight:700;src:url('../fonts/Lora-700.ttf')}
@page{size:A4;margin:18mm 18mm 20mm}
:root{--navy:#16233f;--gold:#c49a3c;--ink:#1e2430;--muted:#5b6475;--pale:#f6f3ec;--line:#e2dccf}
*{box-sizing:border-box}
body{margin:0;font:10.4pt/1.5 Lato,Carlito,sans-serif;color:var(--ink)}
.page{page-break-after:always}
.eyebrow{font:700 7.5pt Lato;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);margin-bottom:4px}
h1,h2,h3,h4{font-family:Lora,serif;color:var(--navy);margin:0}
h2{font-size:19pt;font-weight:600;padding-bottom:8px;margin-bottom:12px;border-bottom:1.5px solid var(--gold)}
h3{font-size:12pt;margin:16px 0 6px;font-weight:600;page-break-after:avoid}
h3 .on{font:italic 9.5pt Lato;color:var(--muted);margin-left:6px}
h4{font-size:10.5pt;margin:0 0 4px}
p{margin:0 0 8px}
.cover{background:var(--navy);height:297mm;overflow:hidden;padding:16mm;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.cover .frame{border:1px solid rgba(196,154,60,.6);height:100%;padding:18mm 16mm;position:relative;color:#fff}
.cover .brand{font:700 8pt Lato;letter-spacing:.35em;color:var(--gold)}
.cover .badge{position:absolute;right:16mm;top:14mm;width:30mm;height:30mm;border:1px solid var(--gold);border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;font:600 16pt Lora;color:#fff}
.cover .badge small{font:700 6.5pt Lato;letter-spacing:.15em;color:var(--gold)}
.cover .kicker{margin-top:48mm;font:400 8pt Lato;letter-spacing:.3em;color:#c9cfdb}
.cover h1{color:#fff;font:600 44pt/1.05 Lora;margin:8mm 0}
.cover h1 em{color:var(--gold);font-weight:500}
.cover .lede{font-size:12pt;color:#e6e9ef;max-width:140mm}
.cover .feat{list-style:none;padding:0;margin:12mm 0 0;display:grid;grid-template-columns:1fr 1fr;gap:3mm 8mm;font-size:10.5pt;color:#e6e9ef}
.cover .feat li:before{content:"◆ ";color:var(--gold);font-size:8pt}
.cover .author{position:absolute;bottom:18mm;left:16mm;font-size:9.5pt;color:#c9cfdb;line-height:1.6}
.cover .author b{color:#fff;font-size:11pt}
.cover .disc{position:absolute;bottom:18mm;right:16mm;width:70mm;text-align:right;font-size:7.5pt;color:#9aa3b5}
.divider{display:flex;flex-direction:column;justify-content:center;min-height:240mm}
.divider h1{font:600 36pt Lora;margin:4mm 0 10mm}
.divider .dl div{font-size:12pt;padding:4mm 0;border-top:1px solid var(--line)}
.divider .dl b{display:inline-block;width:22mm;color:var(--gold);font-size:9pt;letter-spacing:.1em;text-transform:uppercase}
.divider .dl .wc{color:var(--muted);font-size:10pt}
.text h2 .tl{display:inline-block;background:var(--navy);color:#fff;font:700 9pt Lato;letter-spacing:.1em;padding:3px 8px;border-radius:3px;vertical-align:middle;margin-right:6px;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.kind{font:italic 10pt Lato;color:var(--muted);margin:-6px 0 12px}
.text .body{font:11pt/1.62 Lora,serif}
.text .body p{position:relative;margin:0 0 9px;padding-left:9mm}
.text .body b{font-weight:700}
.pn{position:absolute;left:0;top:2px;font:700 7.5pt Lato;color:var(--gold)}
.rubric{background:var(--pale);border-left:3px solid var(--gold);padding:8px 12px;font-size:9.5pt;margin-bottom:6px;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.q{display:grid;grid-template-columns:9mm 1fr 10mm;gap:2mm;margin:0 0 7px;page-break-inside:avoid}
.qn{font-weight:700;color:var(--navy)}
.qm{text-align:right;font-weight:700;color:var(--muted)}
.q ul{margin:4px 0 4px 16px;padding:0}
.total{text-align:right;font:700 8.5pt Lato;color:var(--gold);letter-spacing:.05em;margin:2px 0 4px}
.note{font-size:9.3pt;color:var(--muted)}
table{border-collapse:collapse;width:100%;font-size:9.4pt;margin-bottom:6px}
td,th{padding:5px 7px;border-bottom:1px solid var(--line);vertical-align:top;text-align:left}
th{background:var(--navy);color:#fff;font-weight:700;-webkit-print-color-adjust:exact;print-color-adjust:exact}
tr{page-break-inside:avoid}
.mst .ql{width:14mm;font-weight:700;color:var(--navy);white-space:nowrap}
.mst .mk{width:8mm;text-align:right;font-weight:700;color:var(--muted)}
.pts{font-size:9.4pt;columns:2;column-gap:8mm;margin:0 0 4px;padding-left:18px}
.pts li{break-inside:avoid;margin-bottom:2px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:6mm;font-size:9.2pt}
.two ul{padding-left:14px;margin:0}.two li{margin-bottom:3px}
.ind{font-size:9.4pt;margin-bottom:5px;page-break-inside:avoid}
.bands .bd{width:13mm;font-weight:700;color:var(--navy);white-space:nowrap}
.glance td:first-child{font-weight:700;color:var(--navy);white-space:nowrap}
.uses{display:grid;grid-template-columns:1fr 1fr 1fr;gap:4mm;font-size:9.4pt}
.uses div{background:var(--pale);padding:8px 10px;border-top:2px solid var(--gold);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.tip{background:#f3ead6;border-left:3px solid var(--gold);padding:8px 12px;font-size:9.4pt;margin:10px 0;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.tip b{color:#8a6a22;letter-spacing:.08em;font-size:8pt}
.track td{height:9mm}.track td:nth-child(n+3){width:22mm}
.track .tot td{font-weight:700;background:var(--pale);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.small{font-size:8pt;color:var(--muted);margin-top:14mm}
.end{padding-top:30mm}
.ms table{font-size:8.9pt}.ms td{padding:3px 6px}.ms h3{margin:10px 0 4px}.ms .note{margin-bottom:5px}.ms .pts,.ms .ind{font-size:8.9pt}.ms .two{font-size:8.7pt}.ms .two li{margin-bottom:1px}
'''

def render_pdf(product_dir, body_html, cover_html, out_pdf, footer_title):
    """Render the cover (full bleed, no footer) and the body (with footer), then merge."""
    doc = lambda body, extra="": f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}{extra}</style></head><body>{body}</body></html>"
    (product_dir / "pack.html").write_text(doc(body_html))
    (product_dir / "cover.html").write_text(doc(cover_html, "@page{margin:0}"))
    tmp = product_dir / "_body.pdf", product_dir / "_cover.pdf"
    subprocess.run(["node", str(HERE / "render.js"), str(product_dir / "pack.html"), str(tmp[0]), footer_title], check=True)
    subprocess.run(["node", str(HERE / "render.js"), str(product_dir / "cover.html"), str(tmp[1])], check=True)
    out = pymupdf.open(tmp[1]); out.insert_pdf(pymupdf.open(tmp[0])); out.save(out_pdf, garbage=3, deflate=True)
    for t in tmp: t.unlink()
    print(out_pdf.name, "pages:", len(out))
