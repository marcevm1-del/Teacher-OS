# TPT / PassWithPurpose product pipeline

The first 2027 syllabus exams are in **June 2027**, so now is the best time to be early: there are few up-to-date 0500 resources yet. Launch fast, then build a small **0500 product line** that can be bundled, rather than lots of unrelated one-off products.

## Launch #1: ready to publish now

Everything is in this folder:

| File | Use |
|---|---|
| `IGCSE-0500-Complete-Exam-Guide-2027.pdf` | The product file (14 pages) |
| `listing-launch-1.md` | Title, price, grades, description, tags. Paste as is |
| `previews/TPT-preview-1.png` … `-4.png` | Upload in order 1–4. #1 is the thumbnail |
| `FREE-PREVIEW-pages-1-4.pdf` | Upload as the TPT "preview file" |

Publish checklist:
- [ ] Seller account set up (Basic or Premium; compare the fees first)
- [ ] Store name: **PassWithPurpose**, with a store banner using the same navy/gold as the guide
- [ ] Upload the PDF, the 4 previews and the preview file; paste the listing
- [ ] Post the link in UAE/international-school English teacher Facebook groups and on LinkedIn (a short "I wrote this for the new 2027 spec" post)
- [ ] Also list it on a platform where you keep more of the money (e.g. Payhip, Gumroad or Shopify) and sell a **school/department licence** there (e.g. $39–$49)

## Next products (each one is small, and they all build up to one bundle)

| # | Product | Size | Price | Target date |
|---|---|---|---|---|
| 2 | ✅ **Paper 1 Practice Pack**: 3 original sets of Texts A/B/C, question papers + mark schemes. **BUILT**: `IGCSE-0500-Paper-1-Practice-Pack-2027.pdf`, listing in `listing-launch-2.md` | 29 pp | $9.99 | **Ready now** |
| 3 | ✅ **Paper 2 Directed Writing Pack**: 4 original Section A tasks (speech, letter, article, report), mark schemes, annotated model answers, toolkit, planning frame. **BUILT**: `IGCSE-0500-Paper-2-Directed-Writing-Pack-2027.pdf`, listing in `listing-launch-3.md` | 27 pp | $9.99 | **Ready now** |
| 4 | **Composition Pack**: 10 descriptive + 10 narrative prompts, planning sheets, 4 model compositions | 15 pp | $6.99 | Dec 2026 |
| 5 | **2027 Syllabus Changes: teacher briefing slides** (free, or $3). Gets people into the shop and brings in followers | 10 slides | Free/$3 | Oct 2026 |
| 6 | **0500 Starter Bundle** (#1 + #2). Listing in `listing-launch-2.md` | — | $18.99 | **As soon as #1 and #2 are live** |
| 6b | **0500 Complete Bundle** (#1 + #2 + #3). Listing in `listing-launch-3.md` | 70 pp | $24.99 | **As soon as #1–#3 are live** |
| 7 | Exam-season **revision booklet** for students (a cut-down version of #1 + practice) | 12 pp | $5.99 | Mar 2027 |

Every product must use **original texts only**. Don't copy Cambridge past papers or mark schemes. Keep the "not endorsed by Cambridge" disclaimer on each one.

Rule of thumb: **one product every 2–3 weeks**, worked on during the Wednesday evening block. Add a short note at the end of each product pointing to the next one (and to the bundle).

## Rebuilding products

- Product sources: `products/<product>/` (text in `content.py`). To rebuild a PDF, run `NODE_PATH=$(npm root -g) python3 build.py` in that folder (needs Playwright and PyMuPDF). Shared styling, fonts and rendering are in `products/common.py`, `products/fonts/` and `products/render.js`.
- Previews + free preview PDF: `python3 make_previews.py` (add new products to `PRODUCTS`).
