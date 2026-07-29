#!/usr/bin/env python3
"""
Process Medical Imaging chapter: translate to Traditional Chinese,
apply Marino ICU formatting style.
"""
import re

# Read the source file
with open('Medical_Imaging_raw.md', 'r') as f:
    content = f.read()

# We'll process the Medical Imaging section (lines 1-2890 approximately)
lines = content.split('\n')

# Find the boundary: before "## Page 821" (Nephrology starts)
mi_lines = []
nephrology_start = None
for i, line in enumerate(lines):
    if '## Page 821' in line and 'NP' in line:
        nephrology_start = i
        break
    mi_lines.append(line)

print(f"Medical Imaging lines: {len(mi_lines)}")
print(f"Nephrology starts at line: {nephrology_start}")

# Save raw content for processing
with open('Medical_Imaging_raw_section.md', 'w') as f:
    f.write('\n'.join(mi_lines))

print("Saved raw section")
