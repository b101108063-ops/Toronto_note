#!/usr/bin/env python3
"""Fix the corrupted first section of Neurosurgery translation."""

original = open('translated/Neurosurgery.md').read()

# The corrupted first section (lines 1-150 approximately)
# Replace the garbled content with properly formatted Traditional Chinese

replacement = """# 神經外科 (Neurosurgery)

*Toronto Notes 2025*

---

## 導讀摘要

本 章節涵蓋以下核心主題：

- **顱內壓升高（Elevated ICP）**：治療原則、藥物處置、去顱骨減壓術
- **自發性顱內低壓（Spontaneous Intracranial Hypotension）**：診斷與治療
- **水腦症（Hydrocephalus）**：分類、临床表现、治疗與併發症
- **腦腫瘤（Brain Tumours）**：分類、WHO 2021 分級、診斷與治療
- **腦膿瘡（Cerebral Abscess）**：致病菌、治療療程
- **顱內出血（Intracranial Hemorrhage）**：硬膜外、硬膜下、蜘蛛膜下腔、腦內出血
- **腦血管疾病（Cerebrovascular Disease）**：缺血性中風、顱內出血、血管瘤
- **癲癇與功能性疾病（Epilepsy and Functional Disorders）**：癲癇手術、疼痛治療、立體定位放射手術
- **創傷性腦損傷（Traumatic Brain Injury）**：GCS 評分、CT 分類、顱內壓監測
- **兒童神經外科（Pediatric Neurosurgery）**：腦室內出血、水腦症、脊柱裂、Chiari 畸形

---

## 顱內壓升高（Elevated ICP）之治療

### 治療原則

+ **治療原發病因**為首要原則（例如：移除佔位性病變、確保足夠通氣，如急性呼吸窘迫症候群 ARDS）
+ 若升高之顱內壓在治療原發病因後仍持續，考慮在 **ICP >20 mmHg** 時開始治療
+ **治療目標**：
  - ICP <20 mmHg
  - CPP（腦灌流壓）60-70 mmHg
  - 收縮壓 sBP：50-69 歲者 >100 mmHg；<50 歲或 >70 歲者 >110 mmHg
  - （目標應根據病患臨床表現、病程進展及治療醫師之判斷進行個體化調整）

### 表 6. 顱內壓升高之處置

| 處置類別 | 考量因素 | 介入措施 | 原理 |
|---------|---------|---------|------|
| **保守治療** ||||
| | 姿勢 | 將床頭抬高 30° | 增加顱內靜脈回流 |
| | | 維持頸部中立位置 | 1. 頸靜脈通暢 2. 對 MAP 影響最小的顱內靜脈流出 |
| | 發燒控制 | Acetaminophen 或物理冷卻 | 降低基礎代謝率與氧氣需求，最大程度減少腦損傷 |
| | 預防低血壓 | 必要時：輸液、血管加壓劑（如 dopamine、norepinephrine）| 維持腦血流 |
| | 正常碳酸血症 | 維持 pCO₂ 35-40 mmHg | 預防血管擴張 |
| | 充足氧合 | 目標 SpO₂ >60 mmHg | 預防缺氧性腦損傷 |
| | 滲透性利尿 | Mannitol 20% IV 1-1.5 g/kg，之後 0.25 g/kg q6h 維持，至血清滲透壓 315-320 mOsm/L | 增加血清滲透壓，滲透性利尿將水分導出腦組織；15-30 分鐘起效，維持 BP >100 mmHg；3% 高張鹽水效果與 mannitol 相當 |
| | 皮質類固醇 | Dexamethasone | 數天後減少腦腫瘤、膿瘡、血腫周圍之血管性水腫；對頭部外傷或中風無證實效益 |
| **積極治療** ||||
| | 鎮靜 | 通常使用 Propofol | 降低交感神經張力 |
| | | 其他：barbiturates、codeine、fentanyl、MgSO₄ | 減少肌肉收縮誘發之高血壓 |
| | | 輕度：barbiturates/codeine | |
| | | 重度：fentanyl/MgSO₄ | |
| | 癱瘓 | Vecuronium | 降低交感神經張力；減少肌肉收縮誘發之高血壓 |
| | Barbiturate 誘導昏迷（難治性 ICP） | Phenobarbital 10 mg/kg 30 分鐘靜脈注射，之後 1 mg/kg 連續輸注 | 降低腦血流與代謝；降低死亡率，但對神經學預後無影響；頭部外傷不建議使用低體溫治療 |
| | 過度換氣 | 目標 pCO₂ 30-35 mmHg | 降低腦血流與 ICP，但僅適用於短期；在創傷後 24 小時內避免使用 |
| | 引流腦脊髓液 | 放置 EVD（若為急性或已有 shunt） | 減少顱內容積；引流 3-5 mL CSF |
| | 減壓手術 | 去顱骨減壓術 | 允許腦組織腫脹，同時降低腦脫出風險 |

### 去顱骨減壓術治療創傷性顱內高血壓（DECRA Trial）

**來源**：NEJM 2016;375:119-130

**目的**：比較去顱骨減壓術與藥物治療對創傷性腦損傷（TBI）合併難治性顱內高血壓患者臨床預後之療效。

**方法**：TBI 合併顱內壓 >25 mmHg 之患者，随機分配至去顱骨減壓術組或持續藥物治療組。主要結局為 6 個 月時之 Extended Glasgow Outcome Scale。

**結果**：去顱骨減壓術組之死亡率較低（26.9% vs. 48.9%），但植物人狀態（8.5% vs. 2.1%）及重度殘障比率較高（下重度殘障 21% vs. 14.7%；上重度殘障 15.4% vs. 8%）。

**結論**：與藥物治療相比，去顱骨減壓術治療 TBI 合併難治性顱內高血壓可降低死亡率，但增加植物人狀態與重度殘障之比率。

---

## 特發性顱內高血壓（Idiopathic Intracranial Hypertension）

又稱：**假性腦瘤（Pseudotumour Cerebri）**

### 定義

+ **顱內壓升高**合併視乳頭水腫（papilledema），但**無**：佔位性病變、水腦症、感染或高血壓性腦病變
+（即：排除性診斷）
+ 透過改良 Dandy 診斷標準確診

### 病因

+ 大多數為特發性，但可能與以下因素相關：
  - **血管性**：硬膜靜脈竇血栓（dural venous sinus thrombosis）
  - **體質/飲食**：肥胖、甲狀腺維生素 A 過多症
  - **內分泌**：生育年齡、月經失調、Addison/Cushing 病
  - **血液性**：缺鐵性貧血、真性紅血球增多症
  - **藥物**：類固醇停藥、四環黴素、amiodarone、lithium、nalidixic acid、口服避孕藥、生長激素、retinoids
+ 風險因子與靜脈竇血栓相似；與膽結石風險因子相似（「肥胖（Fat）、女性（Female）、多產（Fertile）、四十歲（Forties）」）

### 流行病學

+ 發生率：一般人口每年約 1-2/100,000；合併肥胖之生育年齡女性每年約 19-21/100,000

### 改良 Dandy 診斷標準

1. 顱內壓升高之症狀
2. 無局部神經學徵象（第六對腦神經麻痺除外）
3. 病患清醒且警覺
4. 神經影像學正常，無血栓證據
5. 腰椎穿刺腦壓 >25 cm H₂O，腦脊髓液正常
6. 無其他解釋顱內壓升高之更好原因

### 臨床表現

+ **症狀**：頭痛（>90%）、噁心、短暫視覺障礙、搏動性耳鳴、複視（第六對腦神經麻痺時可見）、頸部/背部疼痛
+ **徵象**：第六對腦神經麻痺（其他情況無神經學缺陷）、視力與視野缺損、視乳頭水腫、視神經萎縮
+ **併發症**：失明與嚴重視覺障礙之風險（6-24%）是特發性顱內高血壓之主要併發症，但與病程長短、症狀或臨床過程無可靠相關性
+ **病程**：通常為自限性，10% 復發，部分為慢性

### 診斷

+ **MRI 腦部**（有/無顯影）：裂隙狀腦室與 distended perioptic subarachnoid space，但其他正常
  - 需排除：靜脈竇血栓、佔位性病變、感染、水腦症
+ **腰椎穿刺**：
  - 開放壓 >25 cmH₂O
  - 腦脊髓液分析正常
+ **眼科**：視野、視力、視乳頭水腫

### 治療

+ **生活型態改變**：鼓勵減重、限制液體與鹽分攝取
+ **藥物治療**：
  - Acetazolamide（減少腦脊髓液分泌）
  - Thiazide 利尿劑或 furosemide
  - 停用任何可能导致病況之藥物
+ **手術**（若上述治療無效）：
  - 間歇性腰椎穿刺（暫時性處置）
  - 視神經鞘開窗術（若視力進行性惡化）
  - 分流術置放（VP shunt、lumboperitoneal shunt）
+ **長期追蹤**：2 年追蹤、重複影像檢查以排除隱匿性腫瘤、眼科追蹤

---

## 顱內壓升高之緊急處置（ICP HEAD）

1. **I** - Intubate（插管）
2. **C** - Calm/Sedate/Coma（鎮靜/昏迷）
3. **P** - Place drain/Paralysis（放置引流管/癱瘓）
4. **H** - Hyperventilate（過度換氣）
5. **E** - Elevate head（抬高頭部）
6. **A** - Adequate BP（維持足夠血壓）
7. **D** - Diuretic (mannitol)（利尿劑/甘露醇）

如有需要考慮：去顱骨減壓術（Decompressive craniectomy）

---

## Page 941

NS0 神經外科

"""

# Find where the original content starts (after "## Page 941")
marker = "## Page 941"
idx = original.find(marker)

if idx == -1:
    print("ERROR: Could not find marker")
    exit(1)

new_content = replacement + original[idx:]
with open('translated/Neurosurgery.md', 'w') as f:
    f.write(new_content)

print(f"Fixed! Replaced first {idx} characters with properly formatted content")
