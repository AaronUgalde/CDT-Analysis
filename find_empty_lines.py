import os
import re

def find_empty_lines_in_trayectoria(file_path):
    """Find empty lines within UCtrayectoria environments"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    in_trayectoria = False
    empty_line_issues = []
    
    for i, line in enumerate(lines, 1):
        if r'\begin{UCtrayectoria}' in line:
            in_trayectoria = True
        elif r'\end{UCtrayectoria}' in line:
            in_trayectoria = False
        elif in_trayectoria:
            # Check if line is empty or only whitespace (not a comment)
            stripped = line.strip()
            if stripped == '' or (stripped and not stripped.startswith('%') and not stripped.startswith('\\')):
                empty_line_issues.append((i, line))
    
    return empty_line_issues

# Process all .tex files in cu directory
cu_dir = r'D:\Proyectos\CDT-Analysis\cu'
problematic_files = {}

for filename in os.listdir(cu_dir):
    if filename.endswith('.tex'):
        file_path = os.path.join(cu_dir, filename)
        issues = find_empty_lines_in_trayectoria(file_path)
        if issues:
            problematic_files[filename] = issues

if problematic_files:
    for filename, issues in problematic_files.items():
        print(f"\n{filename}:")
        for line_no, line_content in issues[:3]:  # Show first 3 issues
            print(f"  Line {line_no}: {repr(line_content)}")
else:
    print("No empty lines found in UCtrayectoria environments")
