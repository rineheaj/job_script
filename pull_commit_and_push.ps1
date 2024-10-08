Set-Location
"C:\Users\josht\OneDrive\Desktop\Stuff\py\everything_rich\jobs"

git pull origin master --no-edit

$currentDateTime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

$changedFiles = git status --porcelain | 
ForEach-Object {
    $_.Substring(3)
} | Out-String

$commitMessage = "Automated commit on $currentDateTime`n" +
                    "Changed files:`n$changedFiles"

git add .

git commit -m $commitMessage

git push origin master

