@echo off

REG ADD “HKCU\SOFTWARE\Classes\Local Settings\Software\Microsoft\Windows\Shell\Bags\AllFolders\Shell” /V FolderType /T REG_SZ /D NotSpecified /F

taskkill /f /im explorer.exe

start explorer.exe