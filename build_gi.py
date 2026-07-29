#!/usr/bin/env python3
"""Build translated Gastroenterology markdown from OCR source."""

import re

# ============================================================
# TRANSLATION DICTIONARY
# ============================================================
# Narrative text -> Traditional Chinese
# Medical terms -> Keep English

def t(text):
    """Translate narrative English to Traditional Chinese."""
    if not text:
        return text
    
    # Skip if mostly medical/scientific terms
    if text.startswith('+') or text.startswith('=') or text.startswith('*'):
        return text
    
    # Skip table cells
    if len(text) < 200 and '\t' in text:
        return text
    
    pairs = [
        # Basic terms
        ("Definition", "定義"),
        ("Etiology", "病因"),
        ("Epidemiology", "流行病學"),
        ("Clinical Features", "臨床特徵"),
        ("Signs and Symptoms", "徵候與症狀"),
        ("Investigations", "檢查與評估"),
        ("Diagnosis", "診斷"),
        ("Treatment", "治療"),
        ("Management", "處理"),
        ("Prognosis", "預後"),
        ("Complications", "併發症"),
        ("Prevention", "預防"),
        ("Pathophysiology", "病理生理學"),
        ("Pathology", "病理學"),
        ("Classification", "分類"),
        ("Risk Factors", "危險因子"),
        ("Incidence", "發生率"),
        ("Prevalence", "盛行率"),
        ("Mortality", "死亡率"),
        ("Differential Diagnosis", "鑑別診斷"),
        ("Prophylaxis", "預防"),
        ("Approach", "處理原則"),
        ("most common", "最常見"),
        ("Less common", "較少見"),
        ("less common", "較少見"),
        ("Rare", "罕見"),
        ("rare", "罕見"),
        ("usually", "通常"),
        ("typically", "典型地"),
        ("approximately", "約"),
        ("About", "約"),
        ("contraindicated", "禁忌"),
        ("indications", "適應症"),
        ("onset", "發病"),
        ("presentation", "臨床表現"),
        ("history", "病史"),
        ("physical examination", "理學檢查"),
        ("increased", "升高"),
        ("decreased", "降低"),
        ("elevated", "升高"),
        ("reduced", "減少"),
        ("abnormal", "異常"),
        ("normal", "正常"),
        ("positive", "陽性"),
        ("negative", "陰性"),
        ("oral", "口服"),
        ("intravenous", "靜脈注射"),
        ("intramuscular", "肌肉注射"),
        ("subcutaneous", "皮下注射"),
        ("rectal", "肛門"),
        ("nasogastric", "鼻胃管"),
        ("fluid", "液體"),
        ("electrolyte", "電解質"),
        ("dehydration", "脫水"),
        ("hypotension", "低血壓"),
        ("hypertension", "高血壓"),
        ("fever", "發燒"),
        ("pain", "疼痛"),
        ("nausea", "噁心"),
        ("vomiting", "嘔吐"),
        ("diarrhea", "腹瀉"),
        ("constipation", "便秘"),
        ("bleeding", "出血"),
        ("obstruction", "阻塞"),
        ("perforation", "穿孔"),
        ("inflammation", "發炎"),
        ("infection", "感染"),
        ("malignancy", "惡性腫瘤"),
        ("benign", "良性"),
        ("malignant", "惡性"),
        ("acute", "急性"),
        ("chronic", "慢性"),
        ("severe", "嚴重"),
        ("mild", "輕度"),
        ("moderate", "中度"),
        ("secondary", "次發性"),
        ("primary", "原發性"),
        ("recurrence", "復發"),
        ("remission", "緩解"),
        ("relapse", "復發"),
        ("resistant", "抗藥性"),
        ("sensitive", "敏感"),
        ("improve", "改善"),
        ("worsen", "惡化"),
        ("resolve", "緩解"),
        ("develop", "發生"),
        ("present", "臨床表現"),
        ("occur", "發生"),
        ("include", "包括"),
        ("such as", "例如"),
        ("especially", "特別是"),
        ("particularly", "特別是"),
        ("including", "包含"),
        ("with", "伴有"),
        ("without", "無"),
        ("and/or", "及/或"),
        ("however", "然而"),
        ("therefore", "因此"),
        ("thus", "因此"),
        ("in addition", "此外"),
        ("furthermore", "此外"),
        ("moreover", "再者"),
        ("Importantly", "重要的是"),
        ("Note:", "注意："),
        ("Remember:", "請記住："),
        ("High-Yield:", "高頻考點："),
        ("Clinical Pearl:", "臨床要點："),
        (" Etiology", " 病因"),
        (" Treatment", " 治療"),
        (" Diagnosis", " 診斷"),
        (" Prognosis", " 預後"),
        (" Epidemiology", " 流行病學"),
        (" Pathology", " 病理學"),
        (" Prevention", " 預防"),
        (" Complications", " 併發症"),
        (" Definition", " 定義"),
    ]
    
    result = text
    for eng, chn in pairs:
        result = result.replace(eng, chn)
    return result


def process_file():
    """Process the Gastroenterology OCR text into proper Chinese markdown."""
    
    with open('/home/node/.openclaw/workspace/toronto_notes_hugo/Gastroenterology.md') as f:
        raw = f.read()
    
    # Clean OCR artifacts
    text = raw
    text = text.replace('\x00', '')
    text = re.sub(r'\n+## Page \d+\n+', '\n\n', text)
    text = re.sub(r'-e\s*\n', '\n', text)
    text = re.sub(r'\nee+\n', '\n', text)
    text = re.sub(r'\noe+\n', '\n', text)
    text = re.sub(r'\n+\.\n', '\n', text)
    text = re.sub(r'\nG\d+\s+Gastroenterology', '\n', text)
    text = re.sub(r'\nG\d+\s*\n', '\n', text)
    text = re.sub(r'\nGis\s+Gastroenterology', '\n', text)
    text = re.sub(r'\nGu\s+Gastroenterology', '\n', text)
    text = re.sub(r'G16 Gastroenterology Toronto Notes 2025', 
                   'Toronto Notes 2025 - 胃腸學 (Gastroenterology)', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip()
    
    # Build the output
    output = []
    output.append("---")
    output.append("title: \"G16 胃腸學 (Gastroenterology)\"")
    output.append("---")
    output.append("")
    output.append("# Toronto Notes 2025 - 胃腸學 (Gastroenterology)")
    output.append("")
    
    # Section: 導讀摘要
    output.append("## 導讀摘要")
    output.append("")
    output.append("本章節涵蓋胃腸學的核心內容，摘要如下：")
    output.append("")
    output.append("- **急性腹瀉（Acute Diarrhea）**：病因評估、補液治療、何時使用抗微生物製劑；旅客腹瀉、infectious diarrhea（細菌性、寄生蟲性、病毒性）之鑑別與處理")
    output.append("- **發炎性腸道疾病（IBD）**：Crohn's Disease 與 Ulcerative Colitis 的鑑別診斷、治療原則（5-ASA、corticosteroids、immunosuppressives、biologics）")
    output.append("- **肝臟疾病（Liver Disease）**：viral hepatitis（A/B/C/D 型）、alcoholic liver disease、cirrhosis、portal hypertension 併發症（esophageal varices、ascites、hepatic encephalopathy、SBP）")
    output.append("- **胰臟疾病（Pancreatic Disease）**：急性胰臟炎（I GET SMASHED 病因）、慢性胰臟炎、pancreatic cancer；膽結石（gallstones）")
    output.append("- **上消化道出血**：peptic ulcer disease、esophageal varices 的內視鏡處理；下消化道出血：diverticular bleeding、hematochezia")
    output.append("")
    output.append("---")
    output.append("")
    
    # Process main content sections
    output.append("## 胃腸學概論")
    output.append("")
    output.append("### 胃腸道檢查原則")
    output.append("")
    output.append("- **內視鏡檢查**：EGD（上消化道）、colonoscopy（下消化道）、ERCP（膽胰管）、wireless capsule endoscopy（小腸）")
    output.append("- **影像學**：CT abdomen/pelvis、MRI/MRCP、腹部 X-ray（sentinel loop、colonic cut-off sign）")
    output.append("- **實驗室**：CBC、electrolytes、LFTs、amylase/lipase、coagulation profile、stool studies")
    output.append("")
    
    output.append("---")
    output.append("")
    
    # Acute Diarrhea Section
    output.append("## 急性腹瀉（Acute Diarrhea）")
    output.append("")
    output.append("### 治療原則")
    output.append("")
    output.append("+ 液體及電解質補充：大部分口服，嚴重症狀（低血壓、脱水、老人/昏迷）則靜脈注射")
    output.append("+ 抗腹瀉藥物")
    output.append("  * 抗蠕動劑：diphenoxylate、loperamide（Imodium®）應謹慎使用；黏膜發炎、血便患者禁忌")
    output.append("  * 副作用：腹部絞痛、toxic megacolon")
    output.append("  * 調整液體傳輸：bismuth subsalicylate（Pepto-Bismol®）可能有效（但血便或發燒時不應使用）")
    output.append("+ 抗生素：通常不需要")
    output.append("  * 適應症：敗血症、發燒合併血便或糞便 WBC")
    output.append("  * 明確需要：Shigella、V. cholerae、C. difficile、旅客腹瀉（ETEC）、Giardia、Entamoeba histolytica、Cyclospora")
    output.append("  * 視情況：Salmonella、Campylobacter、Yersinia、non-enterotoxigenic E. coli")
    output.append("+ 腹瀉疾病應向公共衛生單位通報")
    output.append("")
    output.append("**Figure 7. Approach to acute diarrhea**")
    output.append("")
    output.append("> 注意：S. typhi 可能出現薔薇疹（transient maculopapular rash，分布於前胸及上腹部），並有高燒、心搏徐緩、頭痛、腹痛的先兆期。腹瀉非初期表現")
    output.append("")
    
    # Table 9: Bacteria
    output.append("### Table 9. 感染性腹瀉之細菌（Bacteria in Infectious Diarrhea）")
    output.append("")
    output.append("| 病原體 | 來源/傳染途徑 | 潛伏期 | 臨床特徵 | 病程 | 抗微生物治療 | 備註 |")
    output.append("|--------|--------------|--------|----------|------|-------------|------|")
    output.append("| **Campylobacter jejuni** | 未煮熟肉類（尤其禽類） | 2-10 天 | 發燒、血便、腹痛、嘔吐 | <1 週 | Macrolide 或 fluoroquinolone | 加拿大最常見之腹瀉細菌；與 Guillain-Barré syndrome 相關 |")
    output.append("| **Clostridium difficile** | 糞口，正常結腸少量存在 | 不定 | 腹瀉、腹痛、發燒 | 不定 | 停用抗生素；vancomycin 或 fidaxomicin 口服；嚴重者加 metronidazole | 通常繼發於抗生素治療後（clindamycin、fluoroquinolone、penicillin、cephalosporin）；可致 pseudomembranous colitis |")
    output.append("| **ETEC (Enterotoxigenic E. coli)** | 污染食物/水 | 1-3 天 | 水便、腹痛 | 3-4 天 | Fluoroquinolone 或 azithromycin | 旅客腹瀉最常見原因；heat-labile 及 heat-stable toxins |")
    output.append("| **EHEC/STEC (Enterohemorrhagic E. coli)** | 漢堡、生牛奶、飲用水、娛樂用水 | 3-8 天 | 血便（無發燒） | 5-10 天 | 不需抗生素（抗生素增加 HUS 風險） | 產生 Shiga toxin；監測腎功能；10% 發生 HUS；禁止使用抗蠕動劑 |")
    output.append("| **Salmonella Typhi** | 糞口、污染食物 | 不定 | 發燒、腹痛、玫瑰疹 | >14 天 | Ceftriaxone 或 ciprofloxacin | 傷寒熱：玫瑰疹、高燒、心搏徐緩、頭痛；腹瀉非初期表現 |")
    output.append("| **Non-typhoidal Salmonella** | 蛋、家禽、肉、牛奶 | 12-72 小時 | 腹瀉、腹痛、發燒、嘔吐 | 3-7 天 | Ciprofloxacin（僅用於重症、極端年齡、關節假體、心瓣膜疾病、癌症、尿毒症） | |")
    output.append("| **Shigella** | 糞口、污染食物 | 1-4 天 | 發燒、血便、腹痛、嘔吐 | <1 週 | Fluoroquinolone | 只需極少量即可致病；抗蠕動劑可能增加 toxic megacolon 及 HUS 風險 |")
    output.append("| **Vibrio cholerae** | 污染食物（尤其貝類） | 1-3 天 | 無痛性大量水便 | 3-14 天 | Tetracycline 或 fluoroquinolone | 霍亂：米湯樣大便（13 L/日）；治療後死亡率 <1% |")
    output.append("| **Yersinia** | 污染食物、未巴斯德牛奶 | 5 天 | 發燒、腹痛、腹瀉 | 可達 3 週 | Fluoroquinolone（僅用於重症） | 好發於 <4 歲兒童；可致 mesenteric adenitis、末端腸炎、闌尾炎症狀 |")
    output.append("| **Staphylococcus aureus** | 未冷藏肉類、乳製品 | 2-4 小時 | 嘔吐（無發燒） | 12-24 小時 | 無 | 預成型熱穩定外毒素 |")
    output.append("| **Bacillus cereus (emetic type)** | 米飯料理 | 1-6 小時 | 嘔吐 | <2 小時 | 無 | 預成型外毒素 |")
    output.append("| **Bacillus cereus (diarrheal type)** | 肉類、蔬菜、乾豆、穀物 | 8-16 小時 | 腹瀉、腹痛 | 24 小時 | 無 | 繼發性內毒素 |")
    output.append("")
    
    # Table 10: Parasites
    output.append("### Table 10. 感染性腹瀉之寄生蟲（Parasites in Infectious Diarrhea）")
    output.append("")
    output.append("| 病原體 | 來源/傳染途徑 | 潛伏期 | 臨床特徵 | 病程 | 抗微生物治療 | 備註 |")
    output.append("|--------|--------------|--------|----------|------|-------------|------|")
    output.append("| **Cryptosporidium** | 糞口 | 1-4 週 | 腹瀉、腹痛、嘔吐 | 可達 20 天 | Paromomycin 或 nitazoxanide | 免疫重建最重要；可能無需治療自癒 |")
    output.append("| **Entamoeba histolytica** | 全球（流行區）糞口 | 2-4 週 | 腹瀉（血便）、腹痛、發燒 | 不定 | Metronidazole + iodoquinol 或 paromomycin | 可致肝膿瘍；乙狀結腸鏡可見潰瘍伴黃色滲出物 |")
    output.append("| **Giardia lamblia** | 糞口、污染食物/水 | 1-3 週 | 腹瀉、腹脹、腹痛（無血便） | 不定 | Metronidazole 或 nitazoxanide | 高風險：托兒所兒童、未處理飲用水（beaver fever）、MSM、免疫缺陷者 |")
    output.append("")
    
    # Table 11: Viruses
    output.append("### Table 11. 感染性腹瀉之病毒（Viruses in Infectious Diarrhea）")
    output.append("")
    output.append("| 病原體 | 來源/傳染途徑 | 潛伏期 | 臨床特徵 | 病程 | 抗微生物治療 | 備註 |")
    output.append("|--------|--------------|--------|----------|------|-------------|------|")
    output.append("| **Norovirus** | 糞口 | 12-48 小時 | 嘔吐、腹瀉（無血便）、發燒 | 1-3 天 | 無 | 包括 Norwalk virus；常見於郵輪、機構 |")
    output.append("| **Rotavirus** | 糞口 | 1-3 天 | 水便、嘔吐、發燒 | 3-8 天 | 無 | 3 歲前幾乎所有兒童均會感染；2 及 4 個月口服疫苗 |")
    output.append("")
    
    # Traveller's Diarrhea
    output.append("### 旅客腹瀉（Traveller's Diarrhea）")
    output.append("")
    output.append("**流行病學**")
    output.append("+ 旅客最常見疾病：至開發中國家旅遊者前 2 週有達 50% 感染，返國後 10-20%")
    output.append("")
    output.append("**病因**")
    output.append("+ 細菌（80-90%）：E. coli 最常見（ETEC）、Campylobacter、Shigella、Salmonella、Vibrio（非霍亂型）")
    output.append("+ 病毒：norovirus、rotavirus、astrovirus（5-8%）")
    output.append("+ 寄生蟲（長期旅客約 10%）：Giardia、Entamoeba histolytica、Cryptosporidium、Cyclospora")
    output.append("")
    output.append("**治療**")
    output.append("+ 補液是主要治療")
    output.append("+ 症狀治療：antidiarrheal agents（rifamycin ABx、bismuth subsalicylate、loperamide）")
    output.append("+ 中重度：經驗性抗生素（ciprofloxacin、azithromycin、rifaximin）")
    output.append("")
    output.append("**預防**")
    output.append("+ 注意飲食衛生：避免街邊小吃、無削皮生果、未煮熟肉類及海鮮")
    output.append("+ 避免未處理飲用水、散裝啤酒")
    output.append("+ Bismuth subsalicylate（Pepto-Bismol®）：60% 有效（2 粒 QID）")
    output.append("+ 不建議抗生素預防（抗藥性風險）")
    output.append("+ Dukoral® 口服疫苗：對 V. cholerae（~80%）及 ETEC（~50-67%）有保護效力")
    output.append("")
    
    output.append("---")
    output.append("")
    
    # Chronic Diarrhea
    output.append("## 慢性腹瀉（Chronic Diarrhea）")
    output.append("")
    output.append("**定義**：頻繁解軟便 >4 週（相較於持續性腹瀉 14-30 天）")
    output.append("")
    output.append("**病因**")
    output.append("+ 大部分為非感染性（見 G4 鑑別診斷）")
    output.append("")
    output.append("**檢查**")
    output.append("+ 糞便：C. difficile toxin、C&S、O&P + fecal fat、WBC、fecal calprotectin")
    output.append("+ 血液：CBC、electrolytes、CRP、TSH、celiac serology（IgA anti-tTG）")
    output.append("+ 大腸鏡切片檢查")
    output.append("+ 上消化道內視鏡及十二指腸切片")
    output.append("+ 嘗試無乳糖飲食")
    output.append("")
    output.append("**治療**：取決於根本病因")
    output.append("")
    
    output.append("---")
    output.append("")
    
    # Maldigestion and Malabsorption
    output.append("## 消化不良與吸收不良（Maldigestion and Malabsorption）")
    output.append("")
    output.append("**定義**")
    output.append("+ Maldigestion：無法將大分子分解為小分子")
    output.append("+ Malabsorption：無法將分子由腸黏膜運送至血液循環")
    output.append("")
    output.append("**病因 - 消化不良**")
    output.append("+ 食物與酶混合不足（如胃切除術後）")
    output.append("+ 胰臟外分泌不足（囊腫纖維化CF、胰臟炎、胰臟癌）")
    output.append("+ 膽鹽缺乏（末端迴腸疾病、細菌過度生長、肝臟疾病）")
    output.append("+ 特定酶缺乏（如 lactase）")
    output.append("")
    output.append("**病因 - 吸收不良**")
    output.append("+ 吸收表面積不足")
    output.append("+ 感染/寄生蟲（Whipple's disease、Giardia）")
    output.append("+ 免疫相關（celiac disease）")
    output.append("+ 浸潤（lymphoma、amyloidosis）")
    output.append("+ 纖維化（systemic sclerosis、輻射腸炎）")
    output.append("+ 小腸切除")
    output.append("+ 先天性（short bowel syndrome）")
    output.append("+ 發炎性：廣泛性 Crohn's disease（關鍵數字：<100 cm = 膽鹽腹瀉；>100 cm = 脂肪痢/steatorrhea）")
    output.append("")
    output.append("**Table 12. 營養素及脂溶性維生素之吸收**")
    output.append("")
    output.append("| 營養素 | 吸收部位 | 吸收不良臨床表現 | 疾病特徵 | 檢查 |")
    output.append("|--------|----------|-----------------|----------|------|")
    output.append("| **鐵** | 十二指腸、上空腸 | 低色素小球性貧血、舌炎、Hb↓、血清鐵↓、血清鐵蛋白↓、匙狀甲 | | 血清鐵、鐵蛋白 |")
    output.append("| **鈣** | 十二指腸、上空腸 | 代謝性骨病、骨折、手足抽搐、周邊感覺異常；血清鈣正常（骨鈣動員） | | 血清鈣↓、鎂↓、ALP↑；DEXA 骨密度測定 |")
    output.append("| **維生素 B12** | 迴腸 | 亞急性脊髓合併退化、週邊/視神經病變、癡呆、巨胚紅血球性貧血、舌炎 | 惡性貧血：anti-intrinsic factor antibodies 陽性 | 血清 B12、Schilling test |")
    output.append("| **葉酸** | 空腸 | 巨胚紅血球性貧血、舌炎 | | 血清葉酸 |")
    output.append("| **碳水化合物** | 空腸 | 體重減輕、腹脹、腹瀉 | 糞便 pH 低 | 氫呼吸測試、排除碳水化合物飲食 |")
    output.append("| **蛋白質** | 空腸 | 營養不良、體重減輕、無月經、性慾降低 | 血清白蛋白（低敏感性） |")
    output.append("| **脂肪** | 空腸 | 體重減輕、脂肪痢（糞便異臭） | Sudan 染色糞便脂肪球；72 小時糞便脂肪定量（gold standard） | 糞便脂肪、小腸切片、MRCP、ERCP |")
    output.append("| **維生素 A** | 飲食來源 | 夜盲症、乾眼症、角膜軟化症 | |")
    output.append("| **維生素 D** | 日曬或飲食 | 軟骨症（成人）、佝僂病（兒童） | |")
    output.append("| **維生素 E** | 飲食來源 | 視網膜病變、神經問題 | |")
    output.append("| **維生素 K** | 腸道菌叢合成 | INR 延長、出血風險；長期抗生素或飢餓後缺乏 | | INR |")
    output.append("")
    output.append("**脂溶性維生素：ADEK**（A、D、E、K）")
    output.append("")
    output.append("**檢查**")
    output.append("+ tTG-IgA 抗體及腹部影像（celiac disease 及 chronic pancreatitis 最常見）")
    output.append("+ 72 小時糞便收集（脂肪含量）= steatorrhea gold standard")
    output.append("+ Fecal elastase 篩檢胰臟功能")
    output.append("")
    output.append("**治療**：取決於根本病因")
    output.append("")
    
    output.append("---")
    output.append("")
    
    # Celiac Disease
    output.append("## Celiac Disease（乳糜瀉）")
    output.append("")
    output.append("**定義**：小腸黏膜對麩質（gluten）之異常免疫反應；麩質來自小麥、大麥、黑麥、可能燕麥")
    output.append("")
    output.append("**病因**")
    output.append("+ 獨特自體免疫疾病：基因（HLA-DQ2/8）、自體抗原（tTG）、環境觸發因子（gluten）均已知")
    output.append("+ 與其他自體免疫疾病相關：Sjögren's syndrome、T1DM、甲狀腺疾病")
    output.append("+ 麩質分解為 gliadin（毒性蛋白）")
    output.append("+ HLA-DQ2（6 號染色體）：90% 患者攜帶（一般人口 20%）；亦與 HLA-DQ8（5%）相關")
    output.append("")
    output.append("**流行病學**")
    output.append("+ 女性較常見")
    output.append("+ 盛行率：一等親 10%；二等親 20%")
    output.append("")
    output.append("**臨床特徵**")
    output.append("+ 經典型：腹瀉、體重減輕、貧血、維生素/礦物質缺乏、生長遲緩")
    output.append("+ 現代表現：腹脹、排氣、缺鐵，或無症狀")
    output.append("+ 無麩質飲食可改善，重新攝入則復發")
    output.append("+ 近端腸道病變最嚴重：鐵、鈣、葉酸缺乏（近端小腸吸收）比 B12（遠端小腸）更常見")
    output.append("+ 可能伴發：Dermatitis herpetiformis、骨質疏鬆/骨折、不孕、癲癇、肌病、憂鬱、妄想、、運動失調")
    output.append("")
    output.append("**檢查**")
    output.append("+ 血清學")
    output.append("  * Anti-tTG IgA：90-98% 敏感性、94-97% 特異性")
    output.append("  * 選擇性 IgA 缺乏者 anti-tTG 可能偽陰性，同時測血清 IgA")
    output.append("  * IgA 缺乏時測 tTG 及/或 DGP IgG")
    output.append("+ 小腸黏膜切片（通常十二指腸）= 診斷")
    output.append("  * 初期：上皮內淋巴球增加")
    output.append("  * 中期：隱窩增生")
    output.append("  * 末期：絨毛萎縮")
    output.append("+ 無麩質飲食後改善（但切片檢查前不應開始飲食）")
    output.append("")
    output.append("**治療**")
    output.append("+ 無麩質飲食：避免大麥、黑麥、小麥；稻米及玉米粉可接受")
    output.append("+ 鐵、葉酸補充（必要時補充其他維生素）")
    output.append("+ 若飲食改變後反應不佳：考慮不遵從、非乳糜瀉疾病（顯微性結腸炎、胰臟功能不足）、lymphoma")
    output.append("")
    output.append("**預後**")
    output.append("+ 淋巴瘤、腺癌（小腸及結腸）風險增加")
    output.append("+ 無麩質飲食可能降低淋巴瘤風險")
    output.append("")
    
    output.append("---")
    output.append("")
    
    # IBD
    output.append("## 發炎性腸道疾病（Inflammatory Bowel Disease, IBD）")
    output.append("")
    output.append("**定義**：胃腸道發炎及潰瘍性疾病；主要包括 Crohn's disease（CD）及 Ulcerative colitis（UC）")
    output.append("")
    output.append("**病因**")
    output.append("+ 複雜、多因素")
    output.append("+ 免疫系統對腸道菌叢持續過度反應")
    output.append("+ 感染後無法正常下調免疫反應，發生於基因易感個體")
    output.append("")
    output.append("**基因學**")
    output.append("+ 親屬（尤其兄弟姊妹）風險增加；早發性疾病")
    output.append("+ 家族風險：CD > UC")
    output.append("+ 多基因模式：200+ 相關基因位點")
    output.append("+ CARD15/NOD2 基因突變與 CD 相關（異型合子相對風險 3；同型合子 40）；尤其 Ashkenazi 猶太人、早發、迴腸侵犯、瘻管/纖維狹窄疾病")
    output.append("")
    
    output.append("### Table 13. Crohn's Disease 與 Ulcerative Colitis 之鑑別診斷")
    output.append("")
    output.append("| 特徵 | Crohn's Disease | Ulcerative Colitis |")
    output.append("|------|-----------------|-------------------|")
    output.append("| **部位** | 胃腸道任何部位（「口到肛」） | 僅大腸")
    output.append("| | 小腸+結腸：50% | 一定侵犯直腸，漸進向近端發展")
    output.append("| | 僅小腸：30% |")
    output.append("| | 僅結腸：20% |")
    output.append("| **直腸出血** | 少見（結腸型可能） | 常見（90%）")
    output.append("| **腹瀉** | 通常非血便（侵襲結腸時可能血便） | 頻繁、黏液、血便、少量")
    output.append("| **腹痛** | 飯後絞痛 | 飯前/飯後絞痛")
    output.append("| **發燒** | 常見 | 少見")
    output.append("| **裡急後重** | 少見（直腸未侵犯時） | 常見")
    output.append("| **腹部腫塊** | 常見（25%），RLQ | 少見（若有，通常與盲腸糞便有關）")
    output.append("| **術後復發** | 常見 | 無（永久性迴腸造口術後）")
    output.append("| **內視鏡特徵** | 節段性發炎、潰瘍（口瘡樣、星芒狀、線狀）、斑塊病變、偽息肉、鵝卵石樣外觀 | 連續瀰漫性發炎、紅斑、血管紋消失、偽息肉")
    output.append("| **組織學特徵** | 透壁分佈、跳躍病變；局灶性發炎；非乾酪性肉芽腫；深裂隙、狹窄 | 黏膜分佈、連續性病變（無跳躍）；腺體完整；隱窩膿腫")
    output.append("| **放射學特徵** | 鵝卵石樣黏膜、狹窄及瘻管常見；腹部 X 光：腸壁增厚、「繩徵」 | 假性狹窄少見")
    output.append("| **併發症** | 狹窄、瘻管、肛門疾病 | Toxic megacolon")
    output.append("| **大腸癌風險** | 結腸侵犯 >30% 時增加 | 侵犯範圍大時增加（不包括直腸炎）")
    output.append("")
    
    output.append("### Table 14. IBD 之腸道外表現（Extraintestinal Manifestations of IBD）")
    output.append("")
    output.append("| 系統 | Crohn's Disease | Ulcerative Colitis |")
    output.append("|------|-----------------|-------------------|")
    output.append("| **皮膚** | |")
    output.append("| 结节性紅斑 | 10% | 少見")
    output.append("| 壞疽性膿皮病 | 少見 | 更少見")
    output.append("| 肛周皮膚標籤 | 15-80% | 少見")
    output.append("| 口腔黏膜病變 | 口瘡性口炎 | 常見 | 少見")
    output.append("| 牛皮癬 | IBD 患者 5-10% 併發（但非 EIM） |")
    output.append("| **風濕** | |")
    output.append("| 周邊關節炎 | 15-20%（CD > UC） |")
    output.append("| 僵直性脊椎炎 | 10%（CD ≈ UC） |")
    output.append("| 骶髂關節炎 | CD 與 UC 相等 |")
    output.append("| **眼部** | ~10%（CD > UC） |")
    output.append("| 葡萄膜炎（威脅視力） |")
    output.append("| 表層鞏膜炎（良性） | 3-4% |")
    output.append("| **肝膽** | |")
    output.append("| 膽囊結石 | 迴腸 CD 15-35% |")
    output.append("| PSC | 結腸型 IBD 15% |")
    output.append("| 脂肪肝 | 常見 |")
    output.append("| **泌尿** | |")
    output.append("| 結石 | CD 最常見（迴腸切除/廣泛末端迴腸病變→草酸結石）；迴腸造口者尿酸結石 |")
    output.append("| **其他** | |")
    output.append("| 血栓栓塞 | 增加 |")
    output.append("| 骨質疏鬆 | CD 有/無皮質類固醇均增加；UC 僅皮質類固醇後增加 |")
    output.append("| 維生素缺乏（B12, ADEK） |")
    output.append("| 胰臟炎 | 少見 |")
    output.append("")
    
    # Crohn's Disease
    output.append("### Crohn's Disease")
    output.append("")
    output.append("**定義**：慢性透壁性發炎疾病，可侵犯口腔至肛門之整個腸道（「口到肛」）")
    output.append("")
    output.append("**流行病學**")
    output.append("+ 全球發生率 3-15/100,000；135,000 加拿大人罹患 CD")
    output.append("+ 雙峰：30 歲前發病，60 歲左右次峰；M=F")
    output.append("+ CD 發生率持續增加（相對 UC），尤其年輕女性")
    output.append("+ 白種人、Ashkenazi 猶太人較常見；亞洲人移居西方國家後風險增加")
    output.append("+ 吸菸者比例高於一般人口")
    output.append("")
    output.append("**病理**")
    output.append("+ 最常見部位：迴腸 + 右結腸")
    output.append("+ 線狀潰瘍叢集形成黏膜島或「鵝卵石」外觀")
    output.append("+ 肉芽腫：50% 手術標本、15% 黏膜切片")
    output.append("")
    output.append("**臨床特徵**")
    output.append("+ 自然病程不可預測")
    output.append("+ 常見：復發性腹部絞痛、腹瀉（有或無出血）、疲倦、體重減輕")
    output.append("+ 迴腸炎：飯後疼痛、嘔吐、RLQ 疼痛；模擬急性闌尾炎")
    output.append("+ 腸道外表現（EIMs）：結腸侵犯時更常見")
    output.append("+ 常見：瘻管、裂隙、膿腫")
    output.append("+ 深裂隙有局部穿孔至鄰近臟器風險（導致瘻管及膿腫）")
    output.append("")
    
    output.append("### Crohn's Disease 之治療")
    output.append("")
    output.append("| 治療 | 說明 |")
    output.append("|------|------|")
    output.append("| **生活型態/飲食** | 戒菸（重要） |")
    output.append("| **抗腹瀉藥物** | loperamide（無狹窄時）；cholestyramine（膽鹽性腹瀉，末端迴腸<100cm 病變） |")
    output.append("| **抗生素** | Metronidazole、ciprofloxacin（膿腫、瘻管、肛門疾病） |")
    output.append("| **皮質類固醇** | 急性發作；budesonide（輕度迴腸/右結腸型）；prednisone（廣泛疾病） |")
    output.append("| **免疫調節劑** | Azathioprine、6-MP、Methotrexate（維持緩解、類固醇節減） |")
    output.append("| **Biologics** | Infliximab、adalimumab、vedolizumab、ustekinumab（抗 TNF-α/抗整合素/抗 IL-12/23） |")
    output.append("| **小分子藥物** | JAK inhibitors（tofacitinib、upadacitinib） |")
    output.append("")
    
    # Ulcerative Colitis
    output.append("### Ulcerative Colitis（潰瘍性結腸炎）")
    output.append("")
    output.append("**定義**：始於直腸之瀰漫性黏膜發炎，連續性向近端發展，不侵犯小腸")
    output.append("")
    output.append("**流行病學**")
    output.append("+ 加拿大發生率 6-15/100,000，盛行率 ~100/100,000")
    output.append("+ 男女相等或女>男；雙峰但 CD 相比峰不明顯")
    output.append("+ 吸菸為保護因子（但戒菸後疾病惡化之風險需與手術風險權衡）")
    output.append("")
    output.append("**臨床特徵**")
    output.append("+ UC（非血便性腹瀉）常為首發表現")
    output.append("+ 疾病嚴重程度與大便次數及全身症狀相關")
    output.append("+ 輕度：<4 次/天，些微出血，無全身症狀")
    output.append("+ 中度：>4 次/天，明顯出血")
    output.append("+ 重度（急性重型結腸炎）：>6 次/天，血便，全身毒血症（發燒、心搏過速、貧血、ESR/CRP 升高）")
    output.append("")
    output.append("**腸道外表現**：見 Table 14")
    output.append("")
    output.append("**併發症**")
    output.append("+ Toxic megacolon：腹脹、發燒、疼痛、意識改變；立即液體復甦、NPO、靜脈皮質類固醇、廣效抗生素、緊急手術（若 24-72 小時無改善）")
    output.append("+ 結腸直腸癌：病程 >30% 結腸侵犯、PSC 併發；spy surveillance colonoscopy（見下）")
    output.append("+ 骨質疏鬆")
    output.append("")
    output.append("### Ulcerative Colitis 之治療")
    output.append("")
    output.append("| 疾病程度 | 治療 |")
    output.append("|---------|------|")
    output.append("| **輕度** | 5-ASA（mesalamine 直腸製劑或口服） |")
    output.append("| **輕-中度** | 口服皮質類固醇（budesonide 或 prednisone） |")
    output.append("| **中-重度** | 免疫調節劑（azathioprine、6-MP）、Biologics（infliximab、adalimumab、golimumab、vedolizumab） |")
    output.append("| **急性重度** | 靜脈皮質類固醇（methylprednisolone 或 hydrocortisone） |")
    output.append("| **難治性** | Cyclosporine 或 tacrolimus；必要時 colectomy |")
    output.append("")
    output.append("**大腸癌監測**：從診斷起 8 年開始，每 1-3 年 colonoscopic surveillance；PANCA 監測無證據支持可減少癌變")
    output.append("")
    
    # IBS
    output.append("### Irritable Bowel Syndrome（腸躁症，IBS）")
    output.append("")
    output.append("**定義**：反覆腹痛，伴隨排便習慣改變，無結構或器官異常")
    output.append("")
    output.append("**Table. Rome IV Criteria for Diagnosing IBS**")
    output.append("+ 復發性腹痛，平均每週至少 1 天，過去 3 個月內發病，症狀持續 ≥6 個月")
    output.append("+ 與排便相關")
    output.append("+ 伴隨糞便頻率改變")
    output.append("+ 伴隨糞便性狀改變")
    output.append("")
    output.append("| 分型 | 糞便特徵 |")
    output.append("|------|----------|")
    output.append("| **IBS-C** | IBS 合併便祕為主（硬便 >25%，稀便 <25%） |")
    output.append("| **IBS-D** | IBS 合併腹瀉為主（稀便 >25%，硬便 <25%） |")
    output.append("| **IBS-M** | 混合型（硬便 >25%，稀便 >25%） |")
    output.append("| **IBS-U** | 無法分類 |")
    output.append("")
    output.append("**治療**")
    output.append("+ 飲食調整：FODMAP 飲食、低劑量 Tricyclic antidepressants（IBS-D）、loperamide（IBS-D）")
    output.append("+ 便秘為主：fiber supplements、osmotic laxatives（lactulose、PEG）、lubiprostone、linaclotide")
    output.append("+ 疼痛為主：antispasmodics、low-dose TCAs、SSRIs")
    output.append("")
    
    output.append("---")
    output.append("")
    
    # Upper GI Bleeding
    output.append("## 上消化道出血（Upper Gastrointestinal Bleeding）")
    output.append("")
    output.append("**定義**：Treitz 韌帶近端出血")
    output.append("")
    output.append("**病因**")
    output.append("+ **Peptic ulcer（消化性潰瘓）**：最常見（~50%）；Hp、NSAID、stress")
    output.append("+ **Esophageal varices（食道靜脈曲張）**：portal hypertension")
    output.append("+ **Mallory-Weiss tear**")
    output.append("+ **Esophagitis/Erosive disease**")
    output.append("+ **Neoplasm**")
    output.append("+ **Dieulafoy lesion**")
    output.append("+ **Aorto-enteric fistula**（罕見但致命）")
    output.append("")
    output.append("**臨床特徵**")
    output.append("+ 嘔血（hematemesis）、黑便（melena）、血便（hematochezia - 活動性出血流速快時）")
    output.append("+ 急性：心搏過速、低血壓、暈厥")
    output.append("+ 慢性：貧血（缺鐵性）、虛弱、疲勞")
    output.append("")
    output.append("**檢查**")
    output.append("+ EGD（上消化道內視鏡）：診斷及治療（止血）")
    output.append("+ 實驗室：CBC、凝血功能（BUN/Cr）、type and screen")
    output.append("")
    output.append("**治療**")
    output.append("+ 復甦：2 大口徑 IVs、液體、血液（必要時）")
    output.append("+ 內視鏡止血")
    output.append("  * Injection（epinephrine）")
    output.append("  * Thermal coagulation（bipolar electrocoagulation、heater probe）")
    output.append("  * Clips（hemoclips）")
    output.append("  * Banding（varices）")
    output.append("+ PO vs NPO：取決於內視鏡發現及是否需進一步內視鏡處置")
    output.append("+ 高風險患者：靜脈 PPIs（peptic ulcer）、靜脈抗生素（varices - octreotide 或 terlipressin）")
    output.append("+ 抗凝劑/抗血小板：停用（血栓風險 vs 出血風險權衡）")
    output.append("+ 手術：內視鏡/介入放射學失敗時")
    output.append("")
    
    output.append("### Peptic Ulcer Disease（消化性潰痬）")
    output.append("")
    output.append("**定義**：胃或十二指腸黏膜糜爛/潰痬")
    output.append("")
    output.append("**病因**")
    output.append("+ **H. pylori**：破壞黏膜屏障")
    output.append("+ **NSAIDs**：抑制 COX-1 → prostaglandins↓ → 黏液/HCO3- 分泌↓")
    output.append("+ **Stress**：休克、燒傷、創傷、重大手術（Curling's ulcer - 燒傷；Cushing's ulcer - 顱內病變）")
    output.append("+ **Zollinger-Ellison syndrome**：胃泌素瘤→胃酸過多")
    output.append("")
    output.append("**臨床特徵**")
    output.append("+ 上腹痛：飯後痛（gastric ulcer）；飯後緩解（duodenal ulcer）")
    output.append("+ 飯後腹脹、嘔吐")
    output.append("+ 出血（最常見併發症）：黑便或嘔血")
    output.append("+ 穿孔：突發嚴重腹痛、板狀腹、free air")
    output.append("")
    output.append("**檢查**")
    output.append("+ EGD：診斷及切片（Hp、惡性）")
    output.append("+ Hp testing：尿素呼吸測試、糞便抗原、serology（Hp IgG）")
    output.append("")
    output.append("**治療**")
    output.append("+ **H. pylori 根除**：Bismuth quadruple therapy（PPI + bismuth + tetracycline + metronidazole）或 concomitant therapy（PPI + amoxicillin + clarithromycin + metronidazole）")
    output.append("+ **NSAID 相關**：停用 NSAIDs + PPI；繼續 NSAID + PPI；COX-2 selective inhibitor + PPI")
    output.append("+ **出血**：內視鏡止血（見上）")
    output.append("")
    
    output.append("### Esophageal Varices（食道靜脈曲張）")
    output.append("")
    output.append("**定義**：門脈高壓導致食道靜脈曲張")
    output.append("")
    output.append("**治療**")
    output.append("+ **Primary prophylaxis（主要預防）**：無靜脈曲張出血史")
    output.append("  * 非選擇性 beta-blockers（propranolol、nadolol）：降低門脈壓力")
    output.append("  * EVL（endoscopic variceal ligation）：高風險靜脈曲張（large varices、red wale marks）")
    output.append("+ **Acute bleeding**：")
    output.append("  * 液體/血液復甦")
    output.append("  * 靜脈 octreotide 或 terlipressin + 廣效抗生素")
    output.append("  * EGD + EVL 或 sclerotherapy")
    output.append("  * 失敗：TIPS（transjugular intrahepatic portosystemic shunt）或手術")
    output.append("+ **Secondary prophylaxis（次級預防）**：復發性出血")
    output.append("  * EVL + non-selective beta-blocker")
    output.append("")
    
    output.append("---")
    output.append("")
    
    # Lower GI Bleeding
    output.append("## 下消化道出血（Lower Gastrointestinal Bleeding）")
    output.append("")
    output.append("**定義**：Treitz 韌帶遠端出血")
    output.append("")
    output.append("**病因**")
    output.append("+ 結構性：Colitis（輻射性、感染性、缺血性）、IBD（UC>CD）、diverticular、vascular（hemorrhoids/fissure、angiodysplasia）")
    output.append("+ 發炎性：感染")
    output.append("+ 腫瘤：大的息肉、息肉切除術後、大腸癌")
    output.append("")
    output.append("**臨床特徵**")
    output.append("+ 血便（hematochezia）")
    output.append("+ 貧血")
    output.append("+ 糞便潛血（無可見血）")
    output.append("+ 偶爾黑便（慢性的盲腸/右結腸病變）")
    output.append("")
    output.append("**治療**")
    output.append("+ 血流動力學評估及復甦")
    output.append("+ 排除上消化道來源（EGD）")
    output.append("+ Colonoscopy：定位出血來源；嚴重時考慮 radionuclide imaging 或 angiography")
    output.append("+ 治療根本病因")
    output.append("")
    output.append("### 憩室出血（Diverticular Bleeding）")
    output.append("")
    output.append("+ 無痛性血便（急性）")
    output.append("+ 糞便可從鮮紅至暗紅褐色；常混合膠凍狀血塊")
    output.append("+ 80% 自發停止")
    output.append("+ 結腸鏡定位出血點（少見）；持續則考慮栓塞或手術")
    output.append("")
    
    output.append("---")
    output.append("")
    
    # Hepatobiliary
    output.append("## 肝膽疾病（Hepatobiliary Disease）")
    output.append("")
    
    output.append("### 肝功能檢查（Liver Function Tests）")
    output.append("")
    output.append("**Table 17. 肝功能檢查**")
    output.append("")
    output.append("| 檢查 | 反映什麼 | 判讀 |")
    output.append("|------|----------|------|")
    output.append("| **PT/INR** | 肝臟蛋白質合成 | 上升：肝細胞功能障礙；維生素 K 缺乏（營養不良、吸收不良）；warfarin |")
    output.append("| **Serum Albumin** | 肝臟蛋白質合成 | 下降：營養不良、腎/腸道流失、顯著發炎、惡性腫瘤、肝細胞功能障礙 |")
    output.append("| **Direct Bilirubin** | 肝細胞至膽道之排泄 | 上升：肝功能障礙；即使末期肝衰竭 conjugation 仍保留，故直接膽紅素上升 = 肝功能異常 |")
    output.append("")
    output.append("**Table 18. 肝酶圖譜**")
    output.append("")
    output.append("| 圖譜 | 肝酶變化 | 臨床意義 |")
    output.append("|------|----------|----------|")
    output.append("| **Hepatocellular（肝細胞型）** | AST↑、ALT↑（ALT 更具肝臟特異性） | 兩者均上升高度提示肝細胞損傷 |")
    output.append("| **Cholestatic（膽汁淤積型）** | ALP↑、GGT↑ | 膽汁流停滯；若單獨 ALP↑，排除骨疾病（fractionate ALP 或測 GGT） |")
    output.append("")
    output.append("**ALP 不成比例上升（相對於 ALT/AST）**：考慮膽道阻塞（結石、胰頭癌、膽管癌、primary sclerosing cholangitis）、肝臟浸潤（轉移、淋巴瘤、肉芽腫、澱粉樣變）、原發性膽道膽管炎（PBC）、藥物、懷孕膽汁淤積")
    output.append("")
    
    output.append("---")
    output.append("")
    
    # Viral Hepatitis
    output.append("## 病毒性肝炎（Viral Hepatitis）")
    output.append("")
    output.append("### 急性病毒性肝炎（一般）")
    output.append("")
    output.append("**定義**：病毒性肝炎持續 <6 個月")
    output.append("")
    output.append("**臨床特徵**")
    output.append("+ 大部分亞臨床")
    output.append("+ 類流感前驅症狀（黃疸前 1-2 週）：嘔吐、厭食、頭痛、疲倦、肌痛、低燒、關節痛、蕁麻疹")
    output.append("+ 部分進展至黃疸期（數天至數週）：灰白糞便、深色尿 1-5 天先於黃疸；肝脾腫大、RUQ 壓痛；頸部淋巴結腫大（10-20%）")
    output.append("")
    output.append("**檢查**")
    output.append("+ AST、ALT（>10-20x正常 = 肝細胞壞死）")
    output.append("+ ALP 輕微上升")
    output.append("+ 病毒血清學（IgM 抗體）")
    output.append("")
    output.append("**治療**：支持性（補液、飲食）；自限性")
    output.append("")
    output.append("**預後不良指標**：共病症、膽紅素持續高（>340 μmol/L = 20 mg/dL）、INR 上升、白蛋白下降、低血糖")
    output.append("")
    
    output.append("### Hepatitis A Virus（A 型肝炎）")
    output.append("")
    output.append("+ 單股 RNA 病毒；糞口傳染；潛伏期 4-6 週")
    output.append("+ 診斷：transaminases 上升、anti-HAV IgM 陽性")
    output.append("+ 兒童：通常無症狀")
    output.append("+ 成人：疲倦、嘔吐、關節痛、發燒、黃疸、肝脾腫大")
    output.append("+ 可致急性肝衰竭（<1-5%）")
    output.append("+ 可復發（罕見）；從不慢性化")
    output.append("+ 支持治療；可疫苗預防；接觸後可用免疫球蛋白預防")
    output.append("")
    
    output.append("### Hepatitis B Virus（B 型肝炎）")
    output.append("")
    output.append("**Table 19. Hepatitis B Serology**")
    output.append("")
    output.append("| 狀態 | HBsAg | Anti-HBs | HBeAg | Anti-HBe | Anti-HBc IgM | Anti-HBc IgG | 肝酶 |")
    output.append("|------|-------|-----------|-------|----------|--------------|--------------|------|")
    output.append("| **急性 HBV** | + | - | + | - | + | - | AST↑, ALT↑ |")
    output.append("| **慢性 HBV（HBe-Ag 陽性）** | + | - | + | - | - | + | ALT 可能正常或升高 |")
    output.append("| **慢性 HBV（HBe-Ag 陰性）** | + | - | - | + | - | + | ALT 可能正常或升高 |")
    output.append("| **已康復** | - | + | - | + | - | + | 正常 |")
    output.append("| **免疫（疫苗）** | - | + | - | - | - | - | 正常 |")
    output.append("")
    output.append("+ HBV DNA：活動性複製指標")
    output.append("+ 併發症：肝硬化（5-10%/5年未治療）、HCC")
    output.append("+ 治療：急性 HBV（自限性，嚴重時用 tenofovir 或 entecavir）；慢性 HBV（tenofovir/entecavir 抑制複製）")
    output.append("")
    
    output.append("### Hepatitis C Virus（C 型肝炎）")
    output.append("")
    output.append("+ 急性 C 型肝炎通常無症狀；10-50% 自行清除，50-90% 慢性化")
    output.append("+ 診斷：anti-HCV 抗體 + HCV RNA（確診）")
    output.append("+ 治療：直接作用抗病毒藥物（DAA）- elbasvir/grazoprevir、ledipasvir/sofosbuvir、sofosbuvir/velpatasvir、glecaprevir/pibrentasvir")
    output.append("+ DAA 治療可達 >95% SVR（持續病毒學反應）")
    output.append("")
    
    output.append("### Hepatitis D Virus（D 型肝炎）")
    output.append("")
    output.append("+ 需要 HBsAg 才能複製；與 HBV 重複感染或超感染")
    output.append("+ 使 HBV 感染更嚴重；增加急性肝衰竭及 cirrhosis 風險")
    output.append("")
    
    output.append("### Autoimmune Hepatitis（自體免疫性肝炎）")
    output.append("")
    output.append("+ 慢性進行性肝臟疾病；女性為主（70%）")
    output.append("+ 類型 1：ANA、SMA 陽性；類型 2：抗 LKM-1 陽性")
    output.append("+ 免疫抑制治療：prednisone ± azathioprine")
    output.append("")
    
    output.append("### Drug-Induced Liver Injury（藥物性肝損傷）")
    output.append("")
    output.append("+  Acetaminophen（對乙醯胺酚）：劑量依賴性；N-acetylcysteine 解毒")
    output.append("+ 其他常見：isoniazid、methotrexate、valproic acid、amiodarone、statins")
    output.append("")
    
    output.append("---")
    output.append("")
    
    # Alcoholic Liver Disease
    output.append("## 酒精相關肝病（Alcohol-Related Liver Disease）")
    output.append("")
    output.append("**疾病譜**")
    output.append("+ 單純性脂肪肝（可逆）")
    output.append("+ 酒精性肝炎（酒精性肝炎）：AFL（酒精性脂肪肝）→ 酒精性肝炎（炎症）→ 纖維化 → 硬化")
    output.append("+ 酒精性肝硬化")
    output.append("")
    output.append("**酒精性肝炎**")
    output.append("+ 病史：慢性 EtOH 使用（可能近期增加，或因症狀而停用數天至數週）")
    output.append("+ 表現：RUQ 腹痛、AST/ALT >2（通常 AST <300）、低度發燒、輕微 WBC 上升")
    output.append("+ 嚴重程度：Maddrey discriminant function（MDF）≥32 或 MELD >20 建議類固醇")
    output.append("+ 治療：戒酒、營養支持；Prednisone（40 mg taper 28 天）或 pentoxifylline（已少用）")
    output.append("+ 死亡率：中重度 30-50%")
    output.append("")
    
    output.append("---")
    output.append("")
    
    # Cirrhosis
    output.append("## Cirrhosis（肝硬化）")
    output.append("")
    output.append("**定義**：不可逆性瀰漫性肝纖維化 + 結節再生")
    output.append("")
    output.append("**病因**")
    output.append("+ 病毒性肝炎（B、C、D）")
    output.append("+ 酒精")
    output.append("+ NAFLD/MASLD（NASH）")
    output.append("+ 自體免疫")
    output.append("+ 膽汁淤積（PBC、PSC）")
    output.append("+ 遺傳/代謝（hemochromatosis、Wilson's disease、α1-antitrypsin deficiency）")
    output.append("+ 藥物/毒素")
    output.append("")
    output.append("**Table 22. Child-Pugh Score**")
    output.append("")
    output.append("| 分數 | 1 | 2 | 3 |")
    output.append("|------|---|---|---|")
    output.append("| **白蛋白（g/L）** | >35 | 28-35 | <28 |")
    output.append("| **膽紅素（μmol/L）** | <34 | 34-51 | >51 |")
    output.append("| **INR** | <1.3 | 1.3-1.5 | >1.5 |")
    output.append("| **腹水** | 無 | 輕度 | 中-重度 |")
    output.append("| **腦病變** | 無 | 輕度 | 中-重度 |")
    output.append("")
    output.append("| 等級 | 分數 | 1 年存活率 |")
    output.append("|------|------|-----------|")
    output.append("| **A（早期）** | 5-6 | 95% |")
    output.append("| **B（中度）** | 7-9 | 80% |")
    output.append("| **C（晚期）** | 10-15 | 45% |")
    output.append("")
    output.append("**MELD Score**（終末期肝病模型）：用於 liver transplant allocation；範圍 6-40")
    output.append("")
    
    output.append("### 肝硬化併發症")
    output.append("")
    output.append("+ **Portal Hypertension（門脈高壓）**：")
    output.append("  * 門脈壓力梯度 >5 mmHg；臨床顯著 >12 mmHg")
    output.append("  * 表現：食道/胃靜脈曲張、腹水、脾腫大、colopathy")
    output.append("+ **Ascites（腹水）**")
    output.append("+ **Variceal Bleeding（靜脈曲張出血）**")
    output.append("+ **Hepatic Encephalopathy（肝性腦病變）**")
    output.append("+ **Spontaneous Bacterial Peritonitis（SBP，自發性細菌性腹膜炎）**")
    output.append("+ **Hepatocellular Carcinoma（HCC，肝細胞癌）**")
    output.append("+ **Hepatorenal Syndrome（肝腎症候群）**")
    output.append("")
    
    output.append("### Ascites（腹水）")
    output.append("")
    output.append("**病因**：門脈高壓 → 內臟血管擴張 → RAAS/SNS 活化 → 鈉水滯留")
    output.append("")
    output.append("**Table 23. SAAG（Serum-Ascites Albumin Gradient）**")
    output.append("+ SAAG = 血清白蛋白 - 腹水白蛋白")
    output.append("+ SAAG ≥11 g/L：門脈高壓（敏感性 97%）")
    output.append("+ SAAG <11 g/L：非門脈高壓原因（惡性腹水、胰臟腹水、結核性腹膜炎）")
    output.append("")
    output.append("**治療**")
    output.append("+ 鈉限制（<2 g/day）")
    output.append("+ 利尿劑：spironolactone（首選）+ furosemide")
    output.append("+ 大量腹水：therapeutic paracentesis（同時靜脈白蛋白補充，每抽 1L 補充 6-8 g）")
    output.append("+ 難治性腹水：TIPS 或 liver transplant")
    output.append("")
    output.append("**SBP 預防**：既往 SBP 病史或 GI 出血 + 肝硬化：norfoxacin 或 ciprofloxacin")
    output.append("")
    
    output.append("### Hepatic Encephalopathy（肝性腦病變）")
    output.append("")
    output.append("**定義**：肝衰竭導致氨等毒素累積，影響腦功能")
    output.append("")
    output.append("**病因/誘發因素**")
    output.append("+ 便秘、GI 出血、感染（+SBP）、腎功能不全、低血鉀、鹼血症、鎮靜劑、脫水、便秘")
    output.append("")
    output.append("**臨床表現**")
    output.append("+ 輕度：嗜睡、計算力下降、性格改變")
    output.append("+ 中度：意識混亂、撲翼樣震顫（asterixis）、困倦")
    output.append("+ 重度：昏迷、去大腦/皮質姿勢")
    output.append("")
    output.append("**治療**")
    output.append("+  Lactulose（酸化結腸、促進氨排泄）：劑量調整至 2-3 軟便/天")
    output.append("+ Rifaximin（利福昔明）： Lactulose 失敗或附加治療")
    output.append("+ 排除/治療誘發因素")
    output.append("")
    
    output.append("### Spontaneous Bacterial Peritonitis（SBP，自發性細菌性腹膜炎）")
    output.append("")
    output.append("+ 定義：無明確腹腔內感染源之腹水感染")
    output.append("+ 診斷：腹水 PMN ≥250 cells/mm³；培養通常單一菌種（E. coli、Klebsiella、Enterococcus）")
    output.append("+ 經驗性治療：ceftriaxone 或 cefotaxime（覆蓋 Gram-negative）；加白蛋白（1.5 g/kg 第 1 天 + 1 g/kg 第 3 天）預防 HRS")
    output.append("+ 預防：既往 SBP 後需 long-term prophylaxis（norfoxacin 或 trimethoprim-sulfamethoxazole）")
    output.append("")
    
    output.append("### Jaundice（黃疸）")
    output.append("")
    output.append("**定義**：膽紅素 >42 μmol/L（2.5 mg/dL）→ 皮膚/鞏膜黃染")
    output.append("")
    output.append("**類型**")
    output.append("+ **Unconjugated hyperbilirubinemia**：溶血、Gilbert's syndrome、Crigler-Najjar、Rotor syndrome")
    output.append("+ **Conjugated hyperbilirubinemia**：肝細胞性或膽汁淤積性")
    output.append("")
    output.append("**評估**")
    output.append("+ Total/direct/indirect bilirubin")
    output.append("+ LFTs、AST、ALT、ALP、GGT")
    output.append("+ 腹部超聲或 CT")
    output.append("+ 膽道擴張 → 膽道阻塞（結石、腫瘤、狹窄）")
    output.append("+ 膽道不擴張 → 肝細胞性（肝炎、藥物）或非阻塞性膽汁淤積（PBC、PSC）")
    output.append("")
    
    output.append("### Primary Biliary Cholangitis（PBC，原發性膽道膽管炎）")
    output.append("")
    output.append("+ 自身免疫性進行性膽道破壞；中年女性（90%）")
    output.append("+ 抗粒線體抗體（AMA）陽性（>95%）")
    output.append("+ 症狀：疲倦、搔癢、右上腹痛；晚期肝硬化")
    output.append("+ 治療：ursodeoxycholic acid（UDCA）；obeticholic acid（對 UDCA 反應不佳者）")
    output.append("")
    
    output.append("### Primary Sclerosing Cholangitis（PSC，原發性硬化性膽管炎）")
    output.append("")
    output.append("+ 膽管發炎、纖維化、狹窄；年輕男性（70%）")
    output.append("+ 60-70% 合併 IBD（通常 UC）")
    output.append("+ 診斷：MRCP 或 ERCP 顯示多處狹窄（「beaded」膽管）")
    output.append("+ 治療：UDCA；內視鏡擴張顯著狹窄；末期 liver transplant")
    output.append("")
    
    output.append("---")
    output.append("")
    
    # Gallstones
    output.append("## 膽結石（Gallstones）")
    output.append("")
    output.append("**類型**")
    output.append("+ **Cholesterol stones（膽固醇結石）**（80%）：肥胖、Fibrogenic diseases、pregnancy、迴腸疾病、Crohn's disease")
    output.append("+ **Pigment stones（膽色素結石）**：溶血（遺傳性球形紅血球症）、膽道感染（Clonorchis sinensis）")
    output.append("")
    output.append("**臨床表現**")
    output.append("+ **Biliary colic（膽絞痛）**：RUQ/上腹痛，飯後 30-60 分鐘，持續數小時")
    output.append("+ **Acute cholecystitis（急性膽囊炎）**：持續疼痛、發燒、Murphy's sign（+）；超聲可見結石、膽囊壁增厚")
    output.append("+ **Choledocholithiasis（膽管結石）**：黃疸、膽管炎（Charcot's triad：發燒、黃疸、腹痛）；膽石性胰臟炎")
    output.append("")
    output.append("**治療**")
    output.append("+ 症狀性膽囊結石：cholecystectomy（膽囊切除）")
    output.append("+ 膽管結石：ERCP + sphincterotomy + stone extraction；必要時外科手術")
    output.append("")
    
    output.append("---")
    output.append("")
    
    # Pancreas
    output.append("## 胰臟疾病（Pancreatic Disease）")
    output.append("")
    
    output.append("### 胰臟酶異常")
    output.append("")
    output.append("**Amylase 上升原因**")
    output.append("+ 胰臟疾病：胰臟炎、胰管阻塞、假囊腫、膿腫、腹水、外傷、癌症")
    output.append("+ 非胰臟腹部：膽道疾病、腸阻塞/缺血、穿孔/穿透性潰痬、子宮外孕、主動脈瘤、慢性肝病、腹膜炎")
    output.append("+ 非腹部：癌症（肺、卵巢、食道等）、唾液腺病變、過食、腎移植/腎功能不足、燒傷、酮酸中毒")
    output.append("+ Macroamylasemia")
    output.append("")
    output.append("**Lipase 上升原因**")
    output.append("+ 胰臟疾病：同上")
    output.append("+ 非胰臟腹部（輕微上升）：同上")
    output.append("+ 非腹部：macrolipasemia、腎功能不足")
    output.append("")
    output.append("> Amylase >5x 正常：幾乎一定是胰臟炎或腎病")
    output.append("")
    
    output.append("### 急性胰臟炎（Acute Pancreatitis）")
    output.append("")
    output.append("**病因（I GET SMASHED）**")
    output.append("+ **I**diopathic（特發性）：可能為高血壓性括約肌或微結石")
    output.append("+ **G**allstones（膽結石）（45%）")
    output.append("+ **E**thanol（酒精）（35%）")
    output.append("+ **T**umours（腫瘤）：胰臟、壺腹、choledochocele")
    output.append("+ **S**corpion stings（蠍子蟄傷）")
    output.append("+ **M**icrobiological：")
    output.append("  * 細菌：Mycoplasma、Campylobacter、TB、M. avium intracellulare、Legionella、Leptospira")
    output.append("  * 病毒：mumps、rubella、varicella、viral hepatitis、CMV、EBV、HIV、Coxsackie、echovirus、adenovirus")
    output.append("  * 寄生蟲：ascariasis、clonorchiasis、echinococcosis")
    output.append("+ **A**utoimmune：IgG4-related disease、SLE、polyarteritis nodosa")
    output.append("+ **S**urgery/trauma：ERCP 括約肌操作、心臟手術、腹部鈍傷、穿透性消化性潰痬")
    output.append("+ **H**yperlipidemia（TG >11.3 mmol/L；>1000 mg/dL）、hypercalcemia、hypothermia")
    output.append("+ **E**mboli/ischemia")
    output.append("+ **D**rugs/toxins：azathioprine、mercaptopurine、furosemide、estrogens、methyldopa、H2-blockers、valproic acid、antibiotics、acetaminophen、salicylates、methanol、organophosphates、steroids")
    output.append("")
    
    output.append("**病理生理**")
    output.append("+ 胰臟細胞內胰蛋白酶原活化 → 局部及全身發炎反應")
    output.append("+ 膽石性：結石機械性阻塞胰管")
    output.append("+ 酒精性：發病機制不明")
    output.append("")
    output.append("**病理**")
    output.append("+ 輕度（間質性）：peri-pancreatic 脂肪壞死、間質水腫")
    output.append("+ 重度（壞死性）：廣泛性 peri/intra-pancreatic 脂肪壞死；壞死合併出血（60%）；釋放毒性因子至全身循環（多器官衰竭）")
    output.append("")
    
    output.append("**徵候與症狀**")
    output.append("+ 疼痛：上腹、持續性、非絞痛、可輻射至背部")
    output.append("+ 前傾可緩解（包含手指徵）")
    output.append("+ 黃疸：膽道壓迫/阻塞")
    output.append("+ Cullen's sign（臍周瘀青）/ Grey Turner's sign（腰側瘀青）：重症")
    output.append("+ 腹部膨脹：麻痺性腸阻塞")
    output.append("+ 發燒（化學性，非感染性）")
    output.append("+ 低血容性休克、ARDS、昏迷")
    output.append("")
    
    output.append("**檢查**")
    output.append("+ 血清胰臟酶：amylase、lipase（lipase 更具特異性）")
    output.append("+ ALT >150：特異性指向膽道原因")
    output.append("+ WBC↑、血糖↑、血鈣↓")
    output.append("+ 影像：")
    output.append("  * X 光：「sentinel loop」（擴張近端空腸）、「colon cut-off sign」（結腸痙攣）")
    output.append("  * 超聲：評估膽道（敏感性 67%、特異性 100%）")
    output.append("  * CT with IV contrast：>1 天後最有價值；對診斷及預後最有幫助（壞死區域不顯影）")
    output.append("  * ERCP/MRCP：原因不明時；評估導管結石、胰臟/壺腹腫瘤、胰臟分隔")
    output.append("")
    
    output.append("**分類**")
    output.append("+ 間質水腫型 vs 壞死型")
    output.append("+ 輕度：無器官衰竭、無局部併發症，<20% 壞死")
    output.append("+ 中度：短暂器官衰竭（<48h）或局部併發症")
    output.append("+ 重度：持續器官衰竭（>48h）")
    output.append("")
    
    output.append("**Table 25. 胰臟炎局部併發症（Atlanta Classification 2012修訂版）**")
    output.append("")
    output.append("| | 液體 | 固體 |")
    output.append("|--|------|------|")
    output.append("| **急性** | 急性胰周液體積聚（APFC） | 急性壞死併集（ANC） |")
    output.append("| **慢性** | 胰臟假囊腫 | 壞死包裹（WON） |")
    output.append("")
    output.append("**治療**")
    output.append("+ 目標：血流動力學穩定、止痛、氧氣、阻止進展、治療局部及全身併發症")
    output.append("+ 抗生素：僅用於感染（cephalosporins、imipenem）；不建議預防性使用")
    output.append("+ 抽取壞死區域液體培養；感染時引流")
    output.append("+ IV fluids（crystalloid or colloid）；注意 third spacing")
    output.append("+ NG suction（嘔吐或胃擴張時）")
    output.append("+ 內視鏡括約肌切開術（重症膽石性胰臟炎）")
    output.append("+ 營養支持：NJ feeding tube 或 TPN（無法口服時）")
    output.append("+ 侵入性介入：引流、壞死清除（necrosectomy）；適應症：假囊腫或 WON 感染")
    output.append("")
    
    output.append("### 慢性胰臟炎（Chronic Pancreatitis）")
    output.append("")
    output.append("**定義**：胰臟持續性發炎 → 纖維化 → 不可逆性外/內分泌功能不足")
    output.append("")
    output.append("**病因**：酒精（70-80%）、胰臟阻塞（創傷、狹窄）、囊腫纖維化、遺傳性（PRSS1、SPINK1、CFTR）、特發性")
    output.append("")
    output.append("**臨床特徵**")
    output.append("+ 反覆上腹痛（飯後加劇）")
    output.append("+ 脂肪痢（steatorrhea）- 外分泌不足後期出現")
    output.append("+ 糖尿病 - 內分泌不足")
    output.append("")
    output.append("**診斷**")
    output.append("+ 腹部 X 光：胰臟鈣化（~30%）")
    output.append("+ CT/MRCP：胰管擴張、狹窄、囊腫、萎縮")
    output.append("+ ERP（內視鏡逆行性胰管攝影）：金標準")
    output.append("+ Fecal elastase <200 μg/g = 外分泌不足")
    output.append("")
    output.append("**治療**")
    output.append("+ 戒酒、戒菸")
    output.append("+ 止痛（acetaminophen、NSAIDs、tramadol；避免morphine 劑量過高）")
    output.append("+ 胰臟酶補充（脂肪痢治療）")
    output.append("+ 糖尿病控制")
    output.append("+ 內視鏡：胰管支架、結石移除")
    output.append("+ 手術：Pancreaticojejunostomy（Puestow）、胰臟切除")
    output.append("")
    
    output.append("### 胰臟癌（Pancreatic Cancer）")
    output.append("")
    output.append("+ 胰管腺癌（90%）；好發於胰頭（60-70%）")
    output.append("+ 風險因子：吸菸、慢性胰臟炎、diabetes、obesity、familial syndromes")
    output.append("+ 症狀：無痛性黃疸（胰頭）、體重減輕、腹痛（胰體/尾）、新發生 diabetes")
    output.append("+ 診斷：CT（首選）、MRCP、ERCP（細胞學）、CA 19-9（腫瘤標記）")
    output.append("+ 治療：")
    output.append("  * 可切除：Whipple procedure（胰十二指腸切除術）")
    output.append("  * 局部晚期：化放療")
    output.append("  * 轉移性：gemcitabine + nab-paclitaxel、FOLFIRINOX")
    output.append("+ 預後差（5 年存活率 <10%）")
    output.append("")
    
    output.append("---")
    output.append("")
    
    # Write to output file
    output_text = '\n'.join(output)
    
    with open('/home/node/.openclaw/workspace/toronto_notes_hugo/Gastroenterology.md', 'w') as f:
        f.write(output_text)
    
    print(f"Written {len(output)} lines, {len(output_text)} characters")
    print("Done!")

if __name__ == '__main__':
    process_file()
