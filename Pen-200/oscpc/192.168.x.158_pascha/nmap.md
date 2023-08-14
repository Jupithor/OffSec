# Nmap 7.94 scan initiated Mon Aug 14 01:27:28 2023 as: nmap -sT -A -oN 192.168.x.158_pascha/nmap.md 192.168.228.155
Nmap scan report for 192.168.228.155
Host is up (0.045s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT     STATE SERVICE VERSION
80/tcp   open  http    Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows
9099/tcp open  unknown
| fingerprint-strings: 
|   FourOhFourRequest, GetRequest: 
|     HTTP/1.0 200 OK 
|     Server: Mobile Mouse Server 
|     Content-Type: text/html 
|     Content-Length: 321
|_    <HTML><HEAD><TITLE>Success!</TITLE><meta name="viewport" content="width=device-width,user-scalable=no" /></HEAD><BODY BGCOLOR=#000000><br><br><p style="font:12pt arial,geneva,sans-serif; text-align:center; color:green; font-weight:bold;" >The server running on "OSCP" was able to receive your request.</p></BODY></HTML>
9999/tcp open  abyss?
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port9099-TCP:V=7.94%I=7%D=8/14%Time=64D9BB64%P=x86_64-pc-linux-gnu%r(Ge
SF:tRequest,1A2,"HTTP/1\.0\x20200\x20OK\x20\r\nServer:\x20Mobile\x20Mouse\
SF:x20Server\x20\r\nContent-Type:\x20text/html\x20\r\nContent-Length:\x203
SF:21\r\n\r\n<HTML><HEAD><TITLE>Success!</TITLE><meta\x20name=\"viewport\"
SF:\x20content=\"width=device-width,user-scalable=no\"\x20/></HEAD><BODY\x
SF:20BGCOLOR=#000000><br><br><p\x20style=\"font:12pt\x20arial,geneva,sans-
SF:serif;\x20text-align:center;\x20color:green;\x20font-weight:bold;\"\x20
SF:>The\x20server\x20running\x20on\x20\"OSCP\"\x20was\x20able\x20to\x20rec
SF:eive\x20your\x20request\.</p></BODY></HTML>\r\n")%r(FourOhFourRequest,1
SF:A2,"HTTP/1\.0\x20200\x20OK\x20\r\nServer:\x20Mobile\x20Mouse\x20Server\
SF:x20\r\nContent-Type:\x20text/html\x20\r\nContent-Length:\x20321\r\n\r\n
SF:<HTML><HEAD><TITLE>Success!</TITLE><meta\x20name=\"viewport\"\x20conten
SF:t=\"width=device-width,user-scalable=no\"\x20/></HEAD><BODY\x20BGCOLOR=
SF:#000000><br><br><p\x20style=\"font:12pt\x20arial,geneva,sans-serif;\x20
SF:text-align:center;\x20color:green;\x20font-weight:bold;\"\x20>The\x20se
SF:rver\x20running\x20on\x20\"OSCP\"\x20was\x20able\x20to\x20receive\x20yo
SF:ur\x20request\.</p></BODY></HTML>\r\n");
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Aug 14 01:30:49 2023 -- 1 IP address (1 host up) scanned in 201.86 seconds
