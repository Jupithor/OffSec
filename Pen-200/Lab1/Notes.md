sqli (time attack) on WEB02(.121) ->
printspool privesc -> dump creads with mimikatz ->

SMB with joe creds(from mimi) to internal network FILES02(.11) ->
Log file contain NTML of users -> 

SMB to CLIENT01(.82) with Yoshi ->

evil-winrm to CLIENT02(.83) with wario ->
winpeas to privesc with service in unprotected location (msfvenom -f exe-service)

hydra bruteforce to vpn(.122) get creds for offsec ->
gtfobin for sudo -l  with openvpn

use ssh key from vpn(.122) to log in to mario on NTP(.14) ->

SSH to WEB01(.120), check history and see that the offsec user is also sudo (su - root) ->

enum known credentials against DEV04( .12), see that use yoshi has admin on RDP -> replace c:\temp\backup.exe with reverse shell ->
Find creds for WEB01(.120), offsec and for leon (hash from mimz)

crack hash for leon and psexec to DC01(.10) ->
add joe to domain admins and enterprise admins

psexec to PROD01 with jeo



