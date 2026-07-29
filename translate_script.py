#!/usr/bin/env python3
"""
Translation script for Medical Imaging chapter.
Applies OCR corrections + medical terminology translation.
"""
import re

TRANSLATIONS = {
    # ==== HEADER / FRONTMATTER ====
    "MIS 'Medical Imaging Toronto Notes 2025": "MIS 'Medical Imaging Toronto Notes 2025",
    
    # ==== CXR SECTION ====
    "Approach to CXR": "CXR 判讀方法",
    "Chest X-Ray Interpretation": "胸部 X 光判讀",
    "Basics": "基本原則",
    "Analysis": "分析",
    "ABCDEF": "ABCDEF",
    "AP.PA or other view": "AP/PA 或其他視角",
    "Body position/rotation": "身體位置/旋轉",
    "Confirm name": "確認姓名",
    "Films for comparison": "可供比較的舊片",
    "Internal": "內部",
    "Bones and Breast shadows": "骨骼與乳房陰影",
    "Cardiac silhouette and": "心臟輪廓與",
    "Costophrenic angle": "Costophrenic angle",
    "Lung fields": "肺野",
    "Anatomy": "解剖學",
    "Legend": "圖例",
    "PA view": "PA 視角",
    "Lateral view": "側視圖",
    
    # ==== CT CHEST ====
    "Approach to CT Chest": "CT Chest 判讀方法",
    
    # ==== LUNG ABNORMALITIES ====
    "Lung Abnormalities": "肺部異常",
    "Atelectasis": "肺葉塌陷",
    "Consolidation": "肺實質浸潤",
    "Interstitial Disease": "間質性肺病",
    "Pulmonary Nodule": "肺結節",
    "Pulmonary Vascular Abnormalities": "肺血管異常",
    "Pulmonary Edema": "肺水腫",
    "Pulmonary Embolism": "肺栓塞",
    "Localizing Lesions for Parenchymal Lung Disease": "肺實質病灶定位",
    
    # ==== PLEURAL / MEDIASTINAL ====
    "Pleural Abnormalities": "肋膜異常",
    "Pleural Effusion": "肋膜積液",
    "Pneumothorax": "氣胸",
    "Asbestos": "石棉相關疾病",
    "Mediastinal Abnormalities": "縱膈腔異常",
    "Mediastinal Mass": "縱膈腔腫塊",
    "Enlarged Cardiac Silhouette": "心臟輪廓擴大",
    
    # ==== TUBES/LINES ====
    "Tubes, Lines, and Catheters": "管路與導管",
    "Central Venous Catheter": "中央靜脈導管",
    "Endotracheal Tube": "氣管內管",
    "Nasogastric Tube": "鼻胃管",
    "Swan-Ganz Catheter": "肺動脈導管",
    "Chest Tube": "胸管",
    
    # ==== ABDOMINAL ====
    "Abdominal Imaging": "腹部影像學",
    "Abdominal X-Ray": "腹部 X 光",
    "Approach to Abdominal X-Ray": "腹部 X 光判讀方法",
    "Indications": "適應症",
    "3 Views of AXR": "腹部 X 光 3 種視角",
    "ErectiUpright": "站立正向",
    "Supine": "仰臥",
    "Left lateral decubitus": "左側躺",
    "3-6-9 Rule of Dilation": "3-6-9 擴張法則",
    "'Small bowel 3 cm)": "小腸 >3 cm)",
    "Large bowel >6 cm)": "大腸 >6 cm)",
    "Cecum (>9 cm)": "盲腸 (>9 cm)",
    "Anatomy": "解剖學",
    
    # ==== GI TRACT ====
    "Gastrointestinal Tract": "胃腸道",
    "Biliary vs. Portal Venous Air": "膽道 vs. 門靜脈空氣",
    
    # ==== CT ABDOMEN ====
    "Abdominal Computed Tomography": "腹部 CT",
    "Approach to Abdominal Computed Tomography": "腹部 CT 判讀方法",
    "CT and Bowel Obstruction": "CT 與腸阻塞",
    "CT Colonography (Virtual Colonoscopy)": "CT 大腸攝影（虛擬大腸鏡）",
    "Contrast Studies": "對比劑檢查",
    "Specific Visceral Organ Imaging": "特定臟器影像學",
    "Liver": "肝臟",
    "Spleen": "脾臟",
    "Pancreas": "胰臟",
    "Biliary Tree": "膽道樹",
    "Acute Cholecystitis": "急性膽囊炎",
    "Acute Appendicitis": "急性闌尾炎",
    "Acute Diverticulitis": "急性憩室炎",
    "Acute Pancreatitis": "急性胰臟炎",
    "Chronic Pancreatitis": "慢性胰臟炎",
    "Angiography of Gastrointestinal Tract": "胃腸道血管攝影",
    
    # ==== UROLOGY ====
    "Urological Imaging": "泌尿系統影像學",
    "Kidney, Ureter, and Bladder (KUB) X-Ray": "腎、輸尿管、膀胱 X 光",
    "Abdominal CT": "腹部 CT",
    "Renal Masses": "腎臟腫瘤",
    "Renal Cell Carcinoma": "腎細胞癌",
    "Ultrasound": "超音波",
    "Retrograde Pyelography": "逆行性腎盂攝影",
    "Voiding Cystourethrogram": "排尿性膀胱尿道攝影",
    "Retrograde Urethrogram": "逆行性尿道攝影",
    "MRI": "MRI",
    "Renal Nuclear Scan": "腎臟核醫掃描",
    
    # ==== GYNECOLOGY ====
    "Gynecological Imaging": "婦科影像學",
    "Adrenal Mass": "腎上腺腫塊",
    "Skull Films": "顱骨 X 光",
    "Myelography": "脊髓造影",
    "Cerebral Angiography/CT Angiography/MR Angiography": "腦血管攝影/CT 血管攝影/MR 血管攝影",
    "Nuclear Medicine": "核醫學",
    
    # ==== NEURO ====
    "Approach to Head Computed Tomography": "Head CT 判讀方法",
    "Selected Pathology": "精選病理",
    "Cerebrovascular Disease": "腦血管疾病",
    "Multiple Sclerosis": "多發性硬化症",
    "CNS Infections": "中樞神經系統感染",
    
    # ==== MSK ====
    "Musculoskeletal System": "肌肉骨骼系統",
    "Modalities": "成像模態",
    "Plain Film/X-Ray": "平面 X 光",
    "Fracture/Dislocation": "骨折/脫臼",
    "Arthritis": "關節炎",
    "Bone and Soft Tissue Tumours": "骨骼與軟組織腫瘤",
    "Bone Tumours": "骨腫瘤",
    "Soft Tissue Tumours": "軟組織腫瘤",
    "Infection": "感染",
    "Osteomyelitis": "骨髓炎",
    "Septic Arthritis": "化膿性關節炎",
    "Necrotizing Fasciitis": "壞死性筋膜炎",
    "Metabolic Bone Disease": "代謝性骨病",
    "Osteoporosis": "骨質疏鬆症",
    "Osteomalacia": "軟骨病",
    "Hyperparathyroidism": "副甲狀腺功能亢進",
    "Paget's Disease": "Paget 氏病",
    
    # ==== NUCLEAR MED ====
    "Respiratory": "呼吸系統",
    "V/Q Scan": "V/Q 掃描",
    "Cardiac": "心臟",
    "Myocardial Perfusion Scan/Nuclear Stress Test": "心肌灌流掃描/核醫 stress test",
    "Radionuclide Ventriculography": "放射性核醫心室造影",
    "Abdomen and Genitourinary System": "腹部與泌尿生殖系統",
    "HIDA Scan (Cholescintigraphy)": "HIDA 掃描（膽道閃爍造影）",
    "RBC Scan": "紅血球掃描",
    "Urea Breath Test": "尿素呼吸試驗",
    "Functional Renal Imaging": "功能性腎臟影像學",
    
    # ==== INTERVENTIONAL ====
    "Interventional Radiology": "介入性放射學",
    "Vascular Procedures": "血管處置",
    "Angiography": "血管攝影",
    "Percutaneous Transluminal Angioplasty and Stents": "經皮穿腔血管整形術與支架",
    "Thrombolytic Therapy": "血栓溶解療法",
    "Embolization": "栓塞術",
    "Inferior Vena Cava Filter": "下腔靜脈過濾器",
    "Central Venous Access": "中央靜脈通路",
    
    # ==== BREAST ====
    "Breast Imaging": "乳房影像學",
    "Modalities": "成像模態",
    "Mammography": "乳房攝影",
    "Breast Ultrasound": "乳房超音波",
    "Breast MRI": "乳房 MRI",
    "Breast Diagnostic and Interventional Procedures": "乳房診斷與介入處置",
    "Breast Findings": "乳房發現",
    "Breast Masses": "乳房腫塊",
    
    # ==== LANDMARK TRIALS ====
    "Landmark Radiology Trials": "重要放射學試驗",
    
    # ==== REFERENCES ====
    "References": "參考文獻",
    
    # ==== FINDINGS / PATHOGENESIS ====
    "findings": "發現",
    "pathogenesis": "致病機制",
    "differential diagnosis": "鑑別診斷",
    "management": "治療",
    "etiology": "病因",
    "complications": "併發症",
    "description": "說明",
    "procedure": "步驟",
    "Symptoms": "症狀",
    "Signs": "徵象",
    "Diagnosis": "診斷",
    "Treatment": "治療",
    "Prognosis": "預後",
    
    # ==== TABLE HEADERS ====
    "Advantage": "優點",
    "Disadvantage": "缺點",
    "Contrast": "對比劑",
    "Indication": "適應症",
    "Indication": "適應症",
    "Sensitivity": "敏感度",
    "Specificity": "特異度",
    "Feature": "特徵",
    "Property": "性質",
    "Class": "類別",
    "Definition": "定義",
    "Type": "類型",
    "Uses": "用途",
    "Radionuclide": "放射性核種",
    "Finding": "發現",
    "Typical": "典型",
    "Atypical": "非典型",
    
    # ==== ANATOMY LABELS (English) ====
    "anterior strib": "anterior rib",
    "anterior 2ndrib": "anterior 2nd rib",
    "aorticarch": "aortic arch",
    "aorto-pulmonary window": "aortopulmonary window",
    "anteriorairspace": "anterior airspace",
    "coracoid process": "coracoid process",
    "costophrenic angle": "costophrenic angle",
    "gastric bubble": "gastric bubble",
    "inferiorvenacava": "inferior vena cava",
    "leftatrium": "left atrium",
    "left mainstem bronchus": "left mainstem bronchus",
    "left pulmonary artery": "left pulmonary artery",
    "leftventricle": "left ventricle",
    "majortissure": "major fissure",
    "minortissure": "minor fissure",
    "main pulmonary artery": "main pulmonary artery",
    "rightatrium": "right atrium",
    "right mainstem bronchus": "right mainstem bronchus",
    "right pulmonary artery": "right pulmonary artery",
    "rightventricle": "right ventricle",
    "spinousprocess": "spinous process",
    "superior venacava": "superior vena cava",
    "vertebral body": "vertebral body",
    "posterior 3rd rb": "posterior 3rd rib",
    "posterior ath rib": "posterior 4th rib",
    
    # ==== LUNG LOBE LABELS ====
    "RUL": "RUL (右肺上葉)",
    "RML": "RML (右肺中葉)",
    "RLL": "RLL (右肺下葉)",
    "LUL": "LUL (左肺上葉)",
    "LLL": "LLL (左肺下葉)",
    "Right Upper Lobe": "右肺上葉",
    "Right Middle Lobe": "右肺中葉",
    "Right Lower Lobe": "右肺下葉",
    "Left Upper Lobe": "左肺上葉",
    "Left Lower Lobe": "左肺下葉",
    
    # ==== GENERAL MEDICAL ====
    "right": "右",
    "left": "左",
    "anterior": "前",
    "posterior": "後",
    "superior": "上",
    "inferior": "下",
    "medial": "內側",
    "lateral": "外側",
    "upper": "上",
    "lower": "下",
    "front": "前",
    "back": "後",
    
    # Common findings
    "increased opacity": " opacity 增加",
    "volume loss": "容積流失",
    "air bronchograms": "空氣支氣管徵",
    "silhouette sign": "輪廓徵",
    "wedge-shaped": "楔形",
    
    # Disease-related
    "Elevated Hemidiaphragm Suggests": "橫膈升高可能原因",
    "Depressed Hemidiaphragm Suggests": "橫膈下降可能原因",
    "Dx Anterior Mediastinal Mass": "前縱膈腔腫塊診斷",
    "Dx of Interstitial Lung Disease": "間質性肺病診斷",
    "Dx for Cavitating Lung Nodule": "空洞性肺結節診斷",
    "Biliary vs. Portal Venous Air": "膽道 vs. 門靜脈空氣",
    
    # OCR Fixes
    "FlSons": "Felson's",
    "flsons": "Felson's",
    "Flson": "Felson",
    " FlSons": " Felson's",
    " Flson": " Felson",
    "Flson’s": "Felson's",
    
    # Table-related
    "Types of CT Chest": "CT Chest 類型",
    "Types of Contrast Studies": "對比劑檢查類型",
    
    # Modality descriptions
    "Assessment": "評估",
    "Procedure Description": "步驟說明",
    "Study": "檢查",
    "Organ": "器官",
}

def translate_line(line):
    """Apply translations to a single line."""
    result = line
    for eng, chn in sorted(TRANSLATIONS.items(), key=lambda x: -len(x[0])):
        if eng in result:
            result = result.replace(eng, chn)
    return result

def translate_file(input_path, output_path):
    with open(input_path) as f:
        content = f.read()
    
    lines = content.split('\n')
    translated = [translate_line(line) for line in lines]
    
    with open(output_path, 'w') as f:
        f.write('\n'.join(translated))
    
    return len(lines), len('\n'.join(translated))

if __name__ == '__main__':
    lines, chars = translate_file('Medical_Imaging_cleaned.txt', 'Medical_Imaging_translated_v1.txt')
    print(f'Translated {lines} lines, {chars} chars')
