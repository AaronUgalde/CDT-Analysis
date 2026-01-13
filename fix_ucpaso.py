import os
import re

def fix_ucpaso_specific(file_path):
    """Fix specific patterns where UCpaso command spans multiple lines"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix pattern: lines ending with incomplete sentence/command that continue on next line
    # starting with whitespace + non-command text
    # Match: (whitespace + non-\ char at start of line after UCpaso line)
    pattern = r'(\\UCpaso(?:\[\\UCactor\])?[^\n]+)\n(  [a-záéíóúñü])'
    
    modified = content
    while True:
        new_content = re.sub(pattern, r'\1 \2', modified, flags=re.IGNORECASE)
        if new_content == modified:
            break
        modified = new_content
    
    # Also fix pattern where BRref or other commands wrap
    pattern2 = r'(\\UCpaso[^\n]+)\n(  \\[^U])'
    while True:
        new_content = re.sub(pattern2, r'\1 \2', modified)
        if new_content == modified:
            break
        modified = new_content
    
    if modified != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(modified)
        return True
    return False

# Process all .tex files in cu directory
cu_dir = r'D:\Proyectos\CDT-Analysis\cu'
fixed_files = []

for filename in os.listdir(cu_dir):
    if filename.endswith('.tex'):
        file_path = os.path.join(cu_dir, filename)
        if fix_ucpaso_specific(file_path):
            fixed_files.append(filename)
            print(f"Fixed: {filename}")

if fixed_files:
    print(f"\nTotal files fixed: {len(fixed_files)}")
else:
    print("No files needed fixing")
