# PowerShell script to fix unescaped underscores in .tex files

$cuDir = "D:\Proyectos\CDT-Analysis\cu"
$texFiles = Get-ChildItem -Path $cuDir -Filter "*.tex"

$fixedCount = 0

foreach ($file in $texFiles) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    $originalContent = $content
    
    # Replace unescaped underscores with escaped ones
    # Match _ that's not preceded by \
    $content = $content -replace '(?<!\\)_', '\_'
    
    if ($content -ne $originalContent) {
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8 -NoNewline
        Write-Host "Fixed: $($file.Name)"
        $fixedCount++
    }
}

Write-Host ""
Write-Host "✓ Processed $($texFiles.Count) files"
Write-Host "✓ Fixed $fixedCount files"
