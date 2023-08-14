# Nmap 7.94 scan initiated Thu Aug 10 07:10:40 2023 as: nmap -sT -A -oN 192.168.x.151_gust/nmap.md 192.168.218.151
Nmap scan report for 192.168.218.151
Host is up (0.045s latency).
Not shown: 993 filtered tcp ports (no-response)
PORT     STATE SERVICE          VERSION
80/tcp   open  http             Microsoft IIS httpd 10.0
|_http-title: IIS Windows
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|_  Potentially risky methods: TRACE
3389/tcp open  ms-wbt-server    Microsoft Terminal Services
| ssl-cert: Subject: commonName=OSCP
| Not valid before: 2023-05-09T08:52:26
|_Not valid after:  2023-11-08T08:52:26
| rdp-ntlm-info: 
|   Target_Name: OSCP
|   NetBIOS_Domain_Name: OSCP
|   NetBIOS_Computer_Name: OSCP
|   DNS_Domain_Name: OSCP
|   DNS_Computer_Name: OSCP
|   Product_Version: 10.0.19041
|_  System_Time: 2023-08-10T11:12:28+00:00
|_ssl-date: 2023-08-10T11:12:33+00:00; 0s from scanner time.
5060/tcp open  sip-proxy        FreeSWITCH mod_sofia 1.10.1~64bit
|_sip-methods: INVITE, ACK, BYE, CANCEL, OPTIONS, MESSAGE, INFO, UPDATE, REGISTER, REFER, NOTIFY, PUBLISH, SUBSCRIBE
5080/tcp open  sip-proxy        FreeSWITCH mod_sofia 1.10.1~64bit
7443/tcp open  ssl/websocket    (WebSocket version: 13)
| ssl-cert: Subject: commonName=FreeSWITCH/countryName=US
| Not valid before: 2022-10-28T14:47:12
|_Not valid after:  1986-09-04T08:18:56
|_ssl-date: TLS randomness does not represent time
8021/tcp open  freeswitch-event FreeSWITCH mod_event_socket
8082/tcp open  ssl/websocket    (WebSocket version: 13)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=FreeSWITCH/countryName=US
| Not valid before: 2022-10-28T14:47:12
|_Not valid after:  1986-09-04T08:18:56
| fingerprint-strings: 
|   GenericLines, GetRequest, HTTPOptions: 
|     HTTP/1.1 400 Bad Request
|_    Sec-WebSocket-Version: 13
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8082-TCP:V=7.94%T=SSL%I=7%D=8/10%Time=64D4C5D2%P=x86_64-pc-linux-gn
SF:u%r(GenericLines,37,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nSec-WebSocke
SF:t-Version:\x2013\r\n\r\n")%r(GetRequest,37,"HTTP/1\.1\x20400\x20Bad\x20
SF:Request\r\nSec-WebSocket-Version:\x2013\r\n\r\n")%r(HTTPOptions,37,"HTT
SF:P/1\.1\x20400\x20Bad\x20Request\r\nSec-WebSocket-Version:\x2013\r\n\r\n
SF:");
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Aug 10 07:12:33 2023 -- 1 IP address (1 host up) scanned in 113.35 seconds
