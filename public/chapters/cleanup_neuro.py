#!/usr/bin/env python3
"""
Clean up Toronto Notes Neurology.md for Hugo website.
Processes in chunks to handle the 7944-line file.
"""

import re
import sys

INPUT = "/home/node/.openclaw/workspace/toronto_notes_hugo/content/chapters/Neurology.md"
OUTPUT = "/home/node/.openclaw/workspace/toronto_notes_hugo/content/chapters/Neurology_clean.md"

def clean_text_block(text):
    """Clean a block of text: fix garbled chars, normalize whitespace."""
    # Fix common garbled OCR characters
    replacements = {
        '\xa0': ' ', '\u200b': '', '\u3000': ' ',
        '由...引起': '引起',
        '與...相關': '相關',
        '特別是': '特別是',
        '常見地': '常見地',
        '典型地': '典型地',
        '特別是': '特別是',
        '由於 ': '', '由於': '',
        '與 ': '', '與': '',
        '常見地': '常見地',
        '建議': '建議',
        '典型地': '典型地',
    }
    
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    # Remove broken table vertical text lines (single chars per line patterns)
    lines = text.split('\n')
    cleaned_lines = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip lines that are single Chinese characters (vertical table remnants)
        if len(line) <= 2 and len(line) > 0 and '\u4e00' <= line[0] <= '\u9fff':
            i += 1
            continue
        
        # Skip very short garbage lines
        if re.match(r'^[a-zA-Z0-9\s\-\+\.\,\(\)]{0,20}$', line) and len(line) < 5:
            i += 1
            continue
            
        cleaned_lines.append(lines[i])
        i += 1
    
    text = '\n'.join(cleaned_lines)
    
    # Normalize multiple blank lines to max 2
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    
    return text

def process_file():
    """Read, clean, and write the file."""
    with open(INPUT, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    lines = content.split('\n')
    print(f"Total lines read: {len(lines)}")
    
    # Process and clean
    cleaned_lines = []
    skip_until_next_header = False
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Skip OCR garbage lines
        if re.match(r'^[a-zA-Z]{1,3}\s*[0-9]{1,3}$', line.strip()):
            i += 1
            continue
        
        # Skip page numbers like "N1", "N2" etc at line start
        if re.match(r'^N\d+\s+\S', line.strip()):
            i += 1
            continue
        
        # Skip lines that are only numbers or single letters
        stripped = line.strip()
        if re.match(r'^[A-Z][0-9]{1,4}$', stripped):
            i += 1
            continue
        
        # Fix chapter numbering like "## 2.1" -> "##"
        line = re.sub(r'^#{1,6}\s*\d+(\.\d+)*\s*', lambda m: '#' * len(m.group().split()[0]) + ' ', line)
        
        cleaned_lines.append(line)
        i += 1
    
    result = '\n'.join(cleaned_lines)
    result = clean_text_block(result)
    
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write(result)
    
    print(f"Cleaned lines written: {len(cleaned_lines)}")
    return len(cleaned_lines)

if __name__ == '__main__':
    process_file()
