# Nmap 7.94 scan initiated Sun Aug 20 07:27:07 2023 as: nmap -Pn -sT -A -oN 172.16.x.6/nmap.md 172.16.85.6
Nmap scan report for 172.16.85.6
Host is up (0.080s latency).
Not shown: 988 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2023-08-20 11:27:19Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: relia.com0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: relia.com0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: RELIA
|   NetBIOS_Domain_Name: RELIA
|   NetBIOS_Computer_Name: DC02
|   DNS_Domain_Name: relia.com
|   DNS_Computer_Name: DC02.relia.com
|   DNS_Tree_Name: relia.com
|   Product_Version: 10.0.20348
|_  System_Time: 2023-08-20T11:27:22+00:00
| ssl-cert: Subject: commonName=DC02.relia.com
| Not valid before: 2023-07-22T17:47:36
|_Not valid after:  2024-01-21T17:47:36
|_ssl-date: 2023-08-20T11:28:02+00:00; 0s from scanner time.
Service Info: Host: DC02; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_nbstat: NetBIOS name: DC02, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:ba:e4:5b (VMware)
| smb2-time: 
|   date: 2023-08-20T11:27:22
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Aug 20 07:28:03 2023 -- 1 IP address (1 host up) scanned in 56.38 seconds
