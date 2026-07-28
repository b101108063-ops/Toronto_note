# Toronto Notes 2025 工作規劃

## 現況總覽

### 已完成章節（已整理，英文）
| 章節 | 名稱 | 檔案 | 狀態 |
|------|------|------|------|
| CH01 | ELOM (Ethical, Legal, Organizational Medicine) | `CH01_ELOM.md` | ✅ 已整理 |
| CH02 | CP (Clinical Pharmacology) | `CH02_CP.md` | ✅ 已整理 |
| CH03 | ER (Emergency Medicine) | `CH03_ER.md` | ✅ 已整理 |

### PDF 基本資料
- **檔案**：toronto_notes_2025.pdf
- **大小**：424MB
- **總頁數**：1595 頁
- **格式**：圖片掃描檔（scanned PDF），需要 OCR

### OCR 進度
| 章節 | PDF 頁碼範圍 | OCR 狀態 | 整理狀態 |
|------|-------------|---------|---------|
| ELOM (CH01) | 23-174 | ✅ 完成 | ✅ 完成 |
| CP (CH02) | 176-249 | ✅ 完成 | ✅ 完成 |
| ER (CH03) | 250-400 | ✅ 完成 | ✅ 完成 |

---

## Toronto Notes 章節結構（預估）

根據 PDF 和現有資料，主要章節如下：

| 編號 | 名稱 | 預估頁碼範圍 | 狀態 |
|------|------|-------------|------|
| 01 | ELOM (Ethical, Legal, Organizational Medicine) | 23-174 | ✅ 完成 |
| 02 | Clinical Pharmacology | 176-249 | ✅ 完成 |
| 03 | Emergency Medicine | 250-400 | ✅ 完成 |
| 04 | Internal Medicine / Cardiology | ~401-550 | ❌ 待處理 |
| 05 | Neurology | ~551-650 | ❌ 待處理 |
| 06 | Gastroenterology | ~651-750 | ❌ 待處理 |
| 07 | Pulmonology | ~751-850 | ❌ 待處理 |
| 08 | Nephrology | ~851-950 | ❌ 待處理 |
| 09 | Endocrinology | ~951-1050 | ❌ 待處理 |
| 10 | Hematology | ~1051-1100 | ❌ 待處理 |
| 11 | Infectious Disease | ~1101-1150 | ❌ 待處理 |
| 12 | Oncology | ~1151-1200 | ❌ 待處理 |
| 13 | Dermatology | ~1201-1250 | ❌ 待處理 |
| 14 | Surgery | ~1251-1350 | ❌ 待處理 |
| 15 | Pediatrics | ~1351-1450 | ❌ 待處理 |
| 16 | Psychiatry | ~1451-1500 | ❌ 待處理 |
| 17 | OB/GYN | ~1501-1550 | ❌ 待處理 |
| 18 | Radiology | ~1551-1595 | ❌ 待處理 |

---

## 工作流程

### Phase 1：清理與組織（已完成）
- [x] 整理檔案結構
- [x] 將原始檔案移至 `/raw` 目錄
- [x] 重新命名整理後的檔案

### Phase 2：翻譯（待執行）
- [ ] CH01 ELOM 翻譯成繁體中文
- [ ] CH02 CP 翻譯成繁體中文
- [ ] CH03 ER 翻譯成繁體中文

### Phase 3：Hugo 網站架設（待執行）
- [ ] 建立 Hugo 網站架構
- [ ] 設定主題
- [ ] 設定搜尋功能
- [ ] 設定 dark mode

### Phase 4：處理剩餘章節（待執行）
- [ ] 確認各章節的 PDF 頁碼範圍
- [ ] OCR 各章節
- [ ] LLM 整理
- [ ] 翻譯
- [ ] 加入 Hugo 網站

---

## 翻譯原則

1. **敘述性文字** → 繁體中文
2. **醫學術語** → 保留英文（如：myocardial infarction, hypertension, diabetes, ARDS, etc.）
3. **藥物名稱** → 保留英文（如：morphine, propofol, norepinephrine, etc.）
4. **劑量、數值、單位** → 保留原樣
5. **表格** → 使用 HTML 格式（Telegram 顯示需要）

---

## 翻譯輸出格式（LLM 處理）

```
## 導讀摘要
[章節重點摘要，3-5 個 bullet points]

## 主題 1
### 小節 1.1
內容...

### 小節 1.2
內容...

## 主題 2
### 小節 2.1
內容...
```

---

## GitHub 網站
- **Repo**：https://github.com/b101108063-ops/Toronto_note
- **目前進度**：3/18 章節完成 OCR 和整理

---

## 備註

- PDF 是圖片掃描檔，需要用 tesseract OCR
- 72dpi 是速度/品質平衡點（5-10秒/頁）
- LLM 整理可減少約 94% 行數
