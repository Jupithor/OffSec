# Nmap 7.94 scan initiated Sun Aug 20 07:29:59 2023 as: nmap -Pn -sT -A -oN 172.16.x.15/nmap.md 172.16.85.15
Nmap scan report for 172.16.85.15
Host is up (0.057s latency).
Not shown: 996 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=WK02.relia.com
| Not valid before: 2023-07-23T00:39:50
|_Not valid after:  2024-01-22T00:39:50
| rdp-ntlm-info: 
|   Target_Name: RELIA
|   NetBIOS_Domain_Name: RELIA
|   NetBIOS_Computer_Name: WK02
|   DNS_Domain_Name: relia.com
|   DNS_Computer_Name: WK02.relia.com
|   DNS_Tree_Name: relia.com
|   Product_Version: 10.0.22000
|_  System_Time: 2023-08-20T11:30:14+00:00
|_ssl-date: 2023-08-20T11:30:54+00:00; 0s from scanner time.
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2023-08-20T11:30:14
|_  start_date: N/A
|_nbstat: NetBIOS name: WK02, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:ba:95:a3 (VMware)
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Aug 20 07:30:54 2023 -- 1 IP address (1 host up) scanned in 55.56 seconds
