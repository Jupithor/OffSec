# Nmap 7.94 scan initiated Sun Aug 20 07:28:03 2023 as: nmap -Pn -sT -A -oN 172.16.x.7/nmap.md 172.16.85.7
Nmap scan report for 172.16.85.7
Host is up (0.063s latency).
Not shown: 993 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Apache httpd 2.4.53 ((Win64) OpenSSL/1.1.1n PHP/7.4.29)
|_http-server-header: Apache/2.4.53 (Win64) OpenSSL/1.1.1n PHP/7.4.29
| http-title: RELIA INTRANET &#8211; Just another WordPress site
|_Requested resource was http://172.16.85.7/wordpress/
|_http-generator: WordPress 6.0.3
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
443/tcp  open  ssl/http      Apache httpd 2.4.53 ((Win64) OpenSSL/1.1.1n PHP/7.4.29)
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10T23:48:47
|_Not valid after:  2019-11-08T23:48:47
| tls-alpn: 
|_  http/1.1
|_ssl-date: TLS randomness does not represent time
|_http-generator: WordPress 6.0.3
| http-title: RELIA INTRANET &#8211; Just another WordPress site
|_Requested resource was https://172.16.85.7/wordpress/
|_http-server-header: Apache/2.4.53 (Win64) OpenSSL/1.1.1n PHP/7.4.29
445/tcp  open  microsoft-ds?
3306/tcp open  mysql         MariaDB (unauthorized)
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=INTRANET.relia.com
| Not valid before: 2023-07-22T22:41:44
|_Not valid after:  2024-01-21T22:41:44
| rdp-ntlm-info: 
|   Target_Name: RELIA
|   NetBIOS_Domain_Name: RELIA
|   NetBIOS_Computer_Name: INTRANET
|   DNS_Domain_Name: relia.com
|   DNS_Computer_Name: INTRANET.relia.com
|   DNS_Tree_Name: relia.com
|   Product_Version: 10.0.20348
|_  System_Time: 2023-08-20T11:28:23+00:00
|_ssl-date: 2023-08-20T11:29:02+00:00; -1s from scanner time.
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2023-08-20T11:28:22
|_  start_date: N/A
|_nbstat: NetBIOS name: INTRANET, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:ba:f5:a3 (VMware)
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Aug 20 07:29:04 2023 -- 1 IP address (1 host up) scanned in 60.81 seconds
