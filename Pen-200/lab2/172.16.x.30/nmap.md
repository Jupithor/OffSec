# Nmap 7.94 scan initiated Sun Aug 20 07:30:54 2023 as: nmap -Pn -sT -A -oN 172.16.x.30/nmap.md 172.16.85.30
Nmap scan report for 172.16.85.30
Host is up (0.081s latency).
Not shown: 995 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Anna Test Machine
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=WEBBY.relia.com
| Not valid before: 2023-07-23T00:10:39
|_Not valid after:  2024-01-22T00:10:39
| rdp-ntlm-info: 
|   Target_Name: RELIA
|   NetBIOS_Domain_Name: RELIA
|   NetBIOS_Computer_Name: WEBBY
|   DNS_Domain_Name: relia.com
|   DNS_Computer_Name: WEBBY.relia.com
|   DNS_Tree_Name: relia.com
|   Product_Version: 10.0.20348
|_  System_Time: 2023-08-20T11:31:11+00:00
|_ssl-date: 2023-08-20T11:31:51+00:00; 0s from scanner time.
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_nbstat: NetBIOS name: WEBBY, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:ba:dc:42 (VMware)
| smb2-time: 
|   date: 2023-08-20T11:31:11
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Aug 20 07:31:51 2023 -- 1 IP address (1 host up) scanned in 57.19 seconds
