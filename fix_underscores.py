import os
import re
import glob

def fix_underscores_in_tex(file_path):
    """Fix unescaped underscores in tex files"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Pattern to find underscores that are NOT already escaped
    # This regex looks for _ that's not preceded by \ 
    # We need to be careful not to break already escaped underscores
    
    # Replace unescaped underscores with escaped ones
    # Negative lookbehind to avoid replacing already escaped underscores
    content = re.sub(r'(?<!\\)_', r'\\_', content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {file_path}")
        return True
    return False

# Process all .tex files in the cu directory
cu_dir = r'D:\Proyectos\CDT-Analysis\cu'
tex_files = glob.glob(os.path.join(cu_dir, '*.tex'))

fixed_count = 0
for tex_file in tex_files:
    if fix_underscores_in_tex(tex_file):
        fixed_count += 1

print(f"\n✓ Processed {len(tex_files)} files")
print(f"✓ Fixed {fixed_count} files")
