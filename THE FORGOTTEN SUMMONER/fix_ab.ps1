$dir = "C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 백과 (Hero Archive)\01-14-2. 현존 영웅\6. 중립세력 (Neutral)"
$files = Get-ChildItem -Path $dir -Filter "*.md" -Recurse
$pattern = "\s*\(" + [char]96 + "A-[A-Za-z]" + [char]96 + " 연계\)\.*"
$count = 0
foreach ($f in $files) {
    $text = [IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)
    $newText = [regex]::Replace($text, $pattern, "")
    if ($text -ne $newText) {
        [IO.File]::WriteAllText($f.FullName, $newText, [System.Text.Encoding]::UTF8)
        Write-Host "Replaced in $($f.Name)"
        $count++
    }
}
Write-Host "Total fixed: $count"
