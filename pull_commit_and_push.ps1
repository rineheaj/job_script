
$config = Get-Content -Raw -Path "config.json" | ConvertFrom-Json

$jobPath = $config.absolute_job_path

Set-Location $jobPath

git pull origin master --no-edit

$currentDateTime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

$changedFiles = git status --porcelain | ForEach-Object { $_.Substring(3) } | Out-String

$commitMessage = "Automated commit on $currentDateTime`nChanged files:`n$changedFiles"

git add .

git commit -m $commitMessage

git push origin master

