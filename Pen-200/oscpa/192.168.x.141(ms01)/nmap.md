# Nmap 7.94 scan initiated Tue Aug  8 05:22:11 2023 as: nmap -sT -A -oN 192.168.x.141.md 192.168.235.141
Nmap scan report for 192.168.235.141
Host is up (0.055s latency).
Not shown: 993 closed tcp ports (conn-refused)
PORT     STATE SERVICE       VERSION
22/tcp   open  ssh           OpenSSH for_Windows_8.1 (protocol 2.0)
| ssh-hostkey: 
|   3072 e0:3a:63:4a:07:83:4d:0b:6f:4e:8a:4d:79:3d:6e:4c (RSA)
|   256 3f:16:ca:33:25:fd:a2:e6:bb:f6:b0:04:32:21:21:0b (ECDSA)
|_  256 fe:b0:7a:14:bf:77:84:9a:b3:26:59:8d:ff:7e:92:84 (ED25519)
80/tcp   open  http          Apache httpd 2.4.51 ((Win64) PHP/7.4.26)
|_http-generator: Nicepage 4.8.2, nicepage.com
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: Home
|_http-server-header: Apache/2.4.51 (Win64) PHP/7.4.26
81/tcp   open  http          Apache httpd 2.4.51 ((Win64) PHP/7.4.26)
|_http-title: Attendance and Payroll System
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.51 (Win64) PHP/7.4.26
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
3306/tcp open  mysql         MySQL (unauthorized)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2023-08-08T09:22:26
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Aug  8 05:22:32 2023 -- 1 IP address (1 host up) scanned in 20.42 seconds
