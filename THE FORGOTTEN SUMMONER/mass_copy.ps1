$OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$backupBase = "C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\_Legacy_중립세력 (Backup)"
$liveBase = "C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 범대륙 초국가 및 중립 세력 (Supranational & Neutral)"

$mappings = @(
    @{ Backup="3. 첩보 (Intelligence)"; Live="6-7. 그림자 첩보 조직 (Shadow Intelligence)" },
    @{ Backup="2. 마법연구조직 (Magic Research)"; Live="6-6. 초국가 진리 연합 및 마탑 (Academia)" },
    @{ Backup="1. 용병단(Mercenaries)"; Live="6-3. 대륙 용병단 (Mercenaries)" }
)

foreach ($map in $mappings) {
    $bParent = Join-Path $backupBase $map.Backup
    $lParent = Join-Path $liveBase $map.Live
    
    if (Test-Path $bParent) {
        $legacyFolders = Get-ChildItem -Path $bParent -Directory
        foreach ($folder in $legacyFolders) {
            $legacyName = $folder.Name
            $legacyNum = ($legacyName -split '\.')[0]
            
            # Find matching Live folder
            $liveMatch = Get-ChildItem -Path $lParent -Directory | Where-Object { $_.Name -like "$legacyNum.*" } | Select-Object -First 1
            
            if ($liveMatch) {
                Write-Host "Copying $legacyName -> $($liveMatch.Name)"
                
                $srcUnits = Join-Path $folder.FullName "9. 예하 부대 및 기사단 (Military Units)"
                if (-not (Test-Path $srcUnits)) {
                    $srcUnits = Join-Path $folder.FullName "9. 예하 부대 (Military Units)"
                }
                
                $dstFaction = $liveMatch.FullName
                $dstUnits = Join-Path $dstFaction "9. 예하 부대 및 기사단 (Military Units)"
                
                if (Test-Path $srcUnits) {
                    if (Test-Path $dstUnits) {
                        Remove-Item -Path "$dstUnits\*" -Recurse -Force -ErrorAction SilentlyContinue
                        Remove-Item -Path $dstUnits -Recurse -Force -ErrorAction SilentlyContinue
                    }
                    Copy-Item -Path $srcUnits -Destination $dstFaction -Recurse -Force
                    Write-Host "Success for $legacyName"
                } else {
                    Write-Host "No military units folder found in $legacyName"
                }
            } else {
                Write-Host "Live folder for $legacyNum not found."
            }
        }
    } else {
        Write-Host "Backup parent not found: $bParent"
    }
}
Write-Host "ALL DONE"
