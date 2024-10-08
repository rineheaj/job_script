$ps1Files = Get-ChildItem -Path C:\ -Recurse -Filter *.ps1 -ErrorAction SilentlyContinue

$ps1Files
