# Nmap 7.94 scan initiated Thu Aug 17 07:37:47 2023 as: nmap -sT -A -oN 192.168.x.250/nmap.md 192.168.205.250
Nmap scan report for 192.168.205.250
Host is up (0.045s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE            VERSION
135/tcp  open  msrpc              Microsoft Windows RPC
139/tcp  open  netbios-ssn        Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
3389/tcp open  ssl/ms-wbt-server?
| ssl-cert: Subject: commonName=WINPREP
| Not valid before: 2023-08-05T18:29:02
|_Not valid after:  2024-02-04T18:29:02
|_ssl-date: 2023-08-17T11:39:07+00:00; 0s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: WINPREP
|   NetBIOS_Domain_Name: WINPREP
|   NetBIOS_Computer_Name: WINPREP
|   DNS_Domain_Name: WINPREP
|   DNS_Computer_Name: WINPREP
|   Product_Version: 10.0.22000
|_  System_Time: 2023-08-17T11:38:57+00:00
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2023-08-17T11:39:00
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Aug 17 07:39:07 2023 -- 1 IP address (1 host up) scanned in 80.77 seconds
