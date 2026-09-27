#!/usr/bin/env bash
# Rebuild every PassWithPurpose product PDF, then all previews and the bundle thumbnail.
# Usage: bash tpt/build_all.sh   (needs Node Playwright + Python PyMuPDF)
set -euo pipefail
cd "$(dirname "$0")/products"
export NODE_PATH="$(npm root -g)"
(cd paper1-practice-pack && python3 build.py && python3 build.py ../paper1-practice-pack-vol2)
(cd paper2-directed-writing-pack && python3 build.py && python3 build.py ../paper2-directed-writing-vol2)
for p in composition-pack language-workbook summary-workbook extended-response-workbook revision-cards teacher-briefing department-offer; do
  (cd "$p" && python3 build.py)
done
cd .. && python3 make_previews.py
echo "All products rebuilt."
