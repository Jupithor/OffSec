# Nmap 7.94 scan initiated Sun Aug 20 07:29:04 2023 as: nmap -Pn -sT -A -oN 172.16.x.21/nmap.md 172.16.85.21
Nmap scan report for 172.16.85.21
Host is up (0.048s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT    STATE SERVICE       VERSION
135/tcp open  msrpc         Microsoft Windows RPC
139/tcp open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds?
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2023-08-20T11:29:18
|_  start_date: N/A
|_nbstat: NetBIOS name: FILES, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:ba:2b:ad (VMware)
|_clock-skew: -1s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Aug 20 07:29:58 2023 -- 1 IP address (1 host up) scanned in 54.53 seconds
