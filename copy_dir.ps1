
$sourceDir = $PSScriptRoot
$backupDir = Join-Path -Path $PSScriptRoot -ChildPath "backup"

if (-Not (Test-Path -Path $backupDir)) {
    New-Item -ItemType Directory -Path $backupDir
    Write-Output "Backup directory created at '$backupDir'"
} else {
    Write-Output "Backup directory already exists at '$backupDir'"
}

Get-ChildItem -Path $sourceDir -Exclude "backup" | ForEach-Object {
    Copy-Item -Path $_.FullName -Destination $backupDir -Recurse -Force
}

Write-Output "Files copied successfully from $sourceDir to $backupDir"
