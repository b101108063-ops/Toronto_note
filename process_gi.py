#!/usr/bin/env python3
"""Process Gastroenterology.md into Traditional Chinese markdown."""

import re

def clean_text(text):
    """Clean OCR artifacts."""
    text = text.replace('\x00', '')
    # Remove page markers
    text = re.sub(r'\n+## Page \d+\n+', '\n\n', text)
    # Remove footer artifacts
    text = re.sub(r'-e\s*\n', '\n', text)
    text = re.sub(r'\nee+\n', '\n', text)
    text = re.sub(r'\noe+\n', '\n', text)
    text = re.sub(r'\n+\.\n', '\n', text)
    # Remove leading page numbers like G16, G17, etc.
    text = re.sub(r'\nG\d+\s+Gastroenterology', '\nGastroenterology', text)
    text = re.sub(r'\nGis\s+Gastroenterology', '\nGastroenterology', text)
    text = re.sub(r'\nGu\s+Gastroenterology', '\nGastroenterology', text)
    text = re.sub(r'\nG\d+\s*\n', '\n', text)
    # Fix double newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def translate_keywords(text):
    """Translate common English medical terms to Chinese."""
    # Key translations (medical terms keep English)
    pairs = [
        # Section headers
        ("Gastroenterology", "胃腸學"),
        ("Toronto Notes 2025", "Toronto Notes 2025"),
        # Major section names
        ("Acute Diarrhea", "急性腹瀉"),
        ("Chronic Diarrhea", "慢性腹瀉"),
        ("Traveller's Diarrhea", "旅客腹瀉"),
        ("Maldigestion and Malabsorption", "消化不良與吸收不良"),
        ("Celiac Disease", "Celiac Disease（乳糜瀉）"),
        ("Inflammatory Bowel Disease", "發炎性腸道疾病"),
        ("Crohn's Disease", "Crohn's Disease"),
        ("Ulcerative Colitis", "Ulcerative Colitis（潰瘍性結腸炎）"),
        ("Irritable Bowel Syndrome", "Irritable Bowel Syndrome（腸躁症）"),
        ("Upper Gastrointestinal Bleeding", "上消化道出血"),
        ("Liver Disease", "肝臟疾病"),
        ("Viral Hepatitis", "病毒性肝炎"),
        ("Hepatitis A Virus", "Hepatitis A Virus（A型肝炎）"),
        ("Hepatitis B Virus", "Hepatitis B Virus（B型肝炎）"),
        ("Hepatitis C Virus", "Hepatitis C Virus（C型肝炎）"),
        ("Alcoholic Liver Disease", "酒精性肝病"),
        ("Cirrhosis", "Cirrhosis（肝硬化）"),
        ("Ascites", "腹水"),
        ("Portal Hypertension", "門脈高壓"),
        ("Jaundice", "黃疸"),
        ("Hepatic Encephalopathy", "肝性腦病變"),
        ("Spontaneous Bacterial Peritonitis", "自發性細菌性腹膜炎"),
        ("Primary Sclerosing Cholangitis", "原發性硬化性膽管炎"),
        ("Primary Biliary Cholangitis", "原發性膽道膽管炎"),
        ("Pancreatic Disease", "胰臟疾病"),
        ("Acute Pancreatitis", "急性胰臟炎"),
        ("Chronic Pancreatitis", "慢性胰臟炎"),
        ("Pancreatic Cancer", "胰臟癌"),
        ("Gallstones", "膽結石"),
        ("Benign Anorectal Disease", "良性肛門直腸疾病"),
        # Common terms
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
        ("Associated with", "與...相關"),
        ("characterized by", "特徵為"),
        ("most common", "最常見"),
        ("less common", "較少見"),
        ("rare", "罕見"),
        ("usually", "通常"),
        ("may", "可能"),
        ("should", "應"),
        ("contraindicated", "禁忌"),
        ("indications", "適應症"),
        ("side effects", "副作用"),
        ("adverse effects", "不良反應"),
        ("onset", "發病"),
        ("presentation", "表現"),
        ("history", "病史"),
        ("physical examination", "理學檢查"),
        ("laboratory", "實驗室"),
        ("imaging", "影像學"),
        ("endoscopy", "內視鏡"),
        ("biopsy", "切片檢查"),
        ("blood", "血液"),
        ("stool", "糞便"),
        ("urine", "尿液"),
        ("serum", "血清"),
        ("increased", "上升"),
        ("decreased", "下降"),
        ("elevated", "升高"),
        ("reduced", "降低"),
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
        ("prognosis", "預後"),
        ("outcome", "結局"),
        ("recurrence", "復發"),
        ("remission", "緩解"),
        ("relapse", "復發"),
        ("response", "反應"),
        ("resistant", "抗藥性"),
        ("sensitive", "敏感"),
        ("exacerbation", "惡化"),
        ("improve", "改善"),
        ("worsen", "惡化"),
        ("resolve", "緩解"),
        ("occur", "發生"),
        ("develop", "發生"),
        ("present", "表現"),
        ("absent", "缺席"),
        ("associated", "相關"),
        ("due to", "由於"),
        ("caused by", "因...引起"),
        ("secondary to", "次發於"),
        ("include", "包括"),
        ("such as", "例如"),
        ("especially", "特別是"),
        ("particularly", "特別是"),
        ("typically", "典型地"),
        ("approximately", "約"),
        ("about", "約"),
        ("range", "範圍"),
        ("between", "介於"),
        ("including", "包含"),
        ("without", "無"),
        ("with", "有"),
        ("and/or", "及/或"),
        ("or", "或"),
        ("and", "及"),
        ("but", "但是"),
        ("however", "然而"),
        ("although", "雖然"),
        ("despite", "儘管"),
        ("therefore", "因此"),
        ("thus", "因此"),
        ("hence", "故"),
        ("consequently", "結果"),
        ("in addition", "此外"),
        ("furthermore", "此外"),
        ("moreover", "再者"),
        ("finally", "最後"),
        ("first", "第一"),
        ("second", "第二"),
        ("third", "第三"),
        ("initial", "初始"),
        ("subsequent", "後續"),
        ("early", "早期"),
        ("late", "晚期"),
        ("prior to", "在...之前"),
        ("after", "之後"),
        ("before", "之前"),
        ("during", "期間"),
        ("following", "後"),
        ("regardless of", "不論"),
        ("according to", "根據"),
        ("associated with", "與...相關"),
        ("related to", "與...相關"),
        ("similar to", "類似"),
        ("different from", "不同於"),
        ("unlike", "不同於"),
        ("compared to", "相比"),
        ("in contrast", "相反地"),
        ("Importantly", "重要的是"),
        ("Note:", "注意："),
        ("Clinical Pearl:", "臨床要點："),
        ("Remember:", "請記住："),
        ("High-Yield:", "高頻考點："),
    ]
    
    result = text
    for eng, chn in pairs:
        result = result.replace(eng, chn)
    return result

with open('/home/node/.openclaw/workspace/toronto_notes_hugo/Gastroenterology.md') as f:
    raw = f.read()

cleaned = clean_text(raw)
translated = translate_keywords(cleaned)

with open('/home/node/.openclaw/workspace/toronto_notes_hugo/Gastroenterology_processed.md', 'w') as f:
    f.write(translated)

print(f"Processed text length: {len(translated)}")
print("Done!")
