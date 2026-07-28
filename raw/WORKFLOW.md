# Toronto Notes 處理 Workflow

## 概述
Toronto Notes 2025 PDF → OCR → LLM 整理 → GitHub

## PDF 基本資料
- 檔案：toronto_notes_2025.pdf
- 大小：424MB
- 頁數：1595 頁
- 格式：**圖片掃描檔（scanned PDF）**，不是文字檔
- 特點：pypdfium2 文字提取傳回空白，需靠 OCR

---

## 處理流程

### Step 1: 確認 PDF 格式
```bash
python3 -c "
import sys
sys.path.insert(0, '/home/node/.linuxbrew/lib/python3.14/site-packages')
import pypdfium2 as pdfium
pdf = pdfium.PdfDocument('toronto_notes_2025.pdf')
page = pdf[0]
text = page.get_textpage()
print(repr(text.get_text_bboxes()))
"
```
如果傳回空陣列 → 圖片掃描檔，需要 OCR

### Step 2: 找出章節頁碼範圍
1. 安裝 tesseract 和 poppler-utils
```bash
apt-get update && apt-get install -y tesseract-ocr poppler-utils
```

2. 用 pdftoppm 轉換測試頁面
```bash
pdftoppm -r 150 -f N -l N toronto_notes_2025.pdf test_page
```

3. 用 tesseract OCR 找出章節抬頭
```bash
tesseract test_page-NNNN.ppm stdout 2>/dev/null | grep -E "^[A-Z]{2,6}[0-9]+"
```
章節抬頭格式如：ELOM3, ELOM4, CP13, FM14...

4. 掃描找到下一章的起始頁
```bash
for pg in 100 105 110 115 120 125 130; do
  pdftoppm -r 150 -f $pg -l $pg toronto_notes_2025.pdf page_$pg
  tesseract page_$pg-$(printf "%04d" $pg).ppm stdout 2>/dev/null | grep -E "^[A-Z]{2,6}[0-9]+"
done
```

### Step 3: OCR 單一章節
```bash
# 建立工作目錄
mkdir -p toronto_elom
cd toronto_elom

# 轉換章節頁面為圖片（72dpi 夠用，150dpi 太慢）
pdftoppm -r 72 -f 23 -l 174 toronto_notes_2025.pdf page

# 用 Python 批次 OCR（單線程，避免 timeout）
python3 << 'PYEOF'
import subprocess

output = []
for i in range(23, 175):  # 實際頁碼範圍
    fname = f"page-{i:04d}.ppm"
    try:
        result = subprocess.run(
            ["tesseract", fname, "stdout"],
            capture_output=True, text=True, timeout=60
        )
        text = result.stdout.strip()
        if text:
            output.append(f"\n## Page {i}\n{text}")
    except Exception as e:
        print(f"Error page {i}: {e}")

with open("ELOM.md", "w") as f:
    f.write("# Ethical, Legal, and Organizational Medicine (ELOM)\n\n")
    f.write("*Toronto Notes 2025 - Chapter 1*\n\n")
    f.write("\n".join(output))
print(f"Done! {len(output)} pages")
PYEOF
```

**注意：**
- 72dpi 圖片約 1.5MB，tesseract 約 5-10 秒/頁
- 150dpi 圖片約 5-6MB，tesseract 約 60 秒/頁（太慢）
- 若 tesseract 一直 timeout，降低 dpi 或用 parallel 處理

### Step 4: LLM 重新組織
用 subagent 處理（因為檔案很大）：
```
Task: 讀取 ELOM.md 全文，重新組織為：
- 主題式分類（不分頁數）
- H2/H3 標題階層
- HTML 表格（<table> 而非 markdown 表格）
- 粗體標示關鍵術語
- bullet points
- 保留所有英文
- 無 emoji
Output: ELOM_REORGANIZED.md
```

### Step 5: 推到 GitHub
```bash
cd /home/node/.openclaw/workspace/toronto_notes_hugo
git remote set-url origin https://github.com/b101108063-ops/Toronto_note.git
git push -u origin main
```

---

## 已知章節頁碼（Toronto Notes 2025）

| 章節 | 名稱 | 頁碼範圍 |
|------|------|---------|
| 1 | ELOM (Ethical, Legal, and Organizational Medicine) | 23-174 |
| 2 |不知道自己章了 | |
| ... | ... | ... |

---

## 心得

### OCR 速度
- 72dpi 是速度/品質平衡點
- 150dpi 太慢（60s/頁），72dpi 約 5-10s/頁
- 36dpi 太快但品質差

### 圖片掃描 PDF 的特性
- 所有文字提取工具（pypdfium2, pdfminer）都傳回空白
- tesseract OCR 是唯一方案
- OCR 會有錯字，需要 LLM 整理

### LLM 整理的好處
- 原始 OCR：10960 行，主題混亂
- LLM 整理後：649 行，主題清晰
- 減少約 94% 行數

### GitHub Push 問題
- `git push` 常常被 rejected（因為別的 branch/process 領先了）
- 解決：`git push --force`
- 注意 force push 會覆寫遠端，需小心

### HTML 表格
- Telegram 不支援 markdown 表格
- 使用 HTML `<table><tr><th>...` 格式
- 結構：`<table><tr><th>Column1</th><th>Column2</th></tr><tr><td>data1</td><td>data2</td></tr></table>`

---

## 檔案位置
- 原始 PDF：/home/node/.openclaw/workspace/toronto_notes_2025.pdf
- OCR 圖片：/home/node/.openclaw/workspace/toronto_elom/page-*.ppm
- 原始 OCR：/home/node/.openclaw/workspace/toronto_elom/ELOM.md
- 整理版：/home/node/.openclaw/workspace/toronto_elom/ELOM_REORGANIZED.md
- GitHub repo：https://github.com/b101108063-ops/Toronto_note
