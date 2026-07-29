#!/usr/bin/env python3
"""Split Medical Imaging raw section into manageable chunks."""
import os

os.chdir('/home/node/.openclaw/workspace/toronto_notes_hugo')

with open('Medical_Imaging_raw_section.md', 'r') as f:
    content = f.read()

lines = content.split('\n')

# Define chunk boundaries (by page number sections)
# We want content without the "## Page XXX" headers and page separators
chunks = {
    '00_frontmatter': (0, 109),   # Up to "## Page 796"
    '01_cxr_basics': (110, 189),
    '02_ct_chest': (190, 275),
    '03_lung_abnormalities': (276, 400),
    '04_pleural_mediastinal': (401, 495),
    '05_abdominal_xray': (496, 613),
    '06_gi_ct_liver': (614, 748),
    '07_pancreas_biliary_appendix': (749, 855),
    '08_gu_gynecology': (856, 1067),
    '09_neuro_imaging': (1068, 1352),
    '10_msk_imaging': (1353, 1605),
    '11_nuclear_med': (1606, 1819),
    '12_interventional': (1820, 1918),
    '13_breast_imaging': (1919, 2252),
    '14_landmark_trials': (2253, 2351),
    '15_references': (2352, 2890),
}

# The actual content starts at line ~2 (after header line), first real content is line 4
# Let's be more precise - find ## Page 796
start_line = None
for i, line in enumerate(lines):
    if '## Page 796' in line:
        start_line = i
        break

print(f"First '## Page 796' at line {start_line}")

# Save chunks with page markers removed
for name, (start, end) in chunks.items():
    chunk_lines = lines[start:end]
    # Remove page header lines and footers
    cleaned = []
    skip_next = False
    for i, line in enumerate(chunk_lines):
        stripped = line.strip()
        if stripped.startswith('## Page ') or stripped == '-e':
            continue
        if stripped.startswith('Toronto Notes 2025') or stripped.startswith('MI'):
            continue
        if 'Page 796' in stripped or 'MI6' in stripped or 'MI7' in stripped:
            continue
        cleaned.append(line)
    
    chunk_text = '\n'.join(cleaned)
    fname = f'chunk_{name}.txt'
    with open(fname, 'w') as f:
        f.write(chunk_text)
    print(f"  {name}: {len(cleaned)} lines, {len(chunk_text)} chars")
