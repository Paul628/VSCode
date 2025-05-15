$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
Invoke-WebRequest "paste link here" -OutFile C:\Users\paull\Documents\file.txt `
-WebSession $session `
-Headers @{
    "authority"="domain here"
    "method"="GET"
    "path"="paste path here"
    "referer"="https://www.patreon.com/"
}
