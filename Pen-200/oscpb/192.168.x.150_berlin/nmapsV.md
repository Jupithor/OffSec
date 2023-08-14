# Nmap 7.94 scan initiated Sat Aug 12 08:45:31 2023 as: nmap -sV -oN nmapsV.md 192.168.228.150
Nmap scan report for 192.168.228.150
Host is up (0.047s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 8.9p1 Ubuntu 3 (Ubuntu Linux; protocol 2.0)
8080/tcp open  http-proxy
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8080-TCP:V=7.94%I=7%D=8/12%Time=64D77EF3%P=x86_64-pc-linux-gnu%r(Ge
SF:tRequest,98,"HTTP/1\.1\x20200\x20\r\nContent-Type:\x20text/plain;charse
SF:t=UTF-8\r\nContent-Length:\x2019\r\nDate:\x20Sat,\x2012\x20Aug\x202023\
SF:x2012:45:38\x20GMT\r\nConnection:\x20close\r\n\r\n{\"api-status\":\"up\
SF:"}")%r(HTTPOptions,75,"HTTP/1\.1\x20200\x20\r\nAllow:\x20GET,HEAD,OPTIO
SF:NS\r\nContent-Length:\x200\r\nDate:\x20Sat,\x2012\x20Aug\x202023\x2012:
SF:45:38\x20GMT\r\nConnection:\x20close\r\n\r\n")%r(RTSPRequest,3C6,"HTTP/
SF:1\.1\x20505\x20\r\nContent-Type:\x20text/html;charset=utf-8\r\nContent-
SF:Language:\x20en\r\nContent-Length:\x20830\r\nDate:\x20Sat,\x2012\x20Aug
SF:\x202023\x2012:45:38\x20GMT\r\n\r\n<!doctype\x20html><html\x20lang=\"en
SF:\"><head><title>HTTP\x20Status\x20505\x20\xe2\x80\x93\x20HTTP\x20Versio
SF:n\x20Not\x20Supported</title><style\x20type=\"text/css\">h1\x20{font-fa
SF:mily:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-
SF:size:22px;}\x20h2\x20{font-family:Tahoma,Arial,sans-serif;color:white;b
SF:ackground-color:#525D76;font-size:16px;}\x20h3\x20{font-family:Tahoma,A
SF:rial,sans-serif;color:white;background-color:#525D76;font-size:14px;}\x
SF:20body\x20{font-family:Tahoma,Arial,sans-serif;color:black;background-c
SF:olor:white;}\x20b\x20{font-family:Tahoma,Arial,sans-serif;color:white;b
SF:ackground-color:#525D76;}\x20p\x20{font-family:Tahoma,Arial,sans-serif;
SF:background:white;color:black;font-size:12px;}\x20a\x20{color:black;}\x2
SF:0a\.name\x20{color:black;}\x20\.line\x20{height:1px;background-color:#5
SF:25D76;border:none;}</style></head><body><h1")%r(FourOhFourRequest,113,"
SF:HTTP/1\.1\x20404\x20\r\nContent-Type:\x20application/json;charset=UTF-8
SF:\r\nDate:\x20Sat,\x2012\x20Aug\x202023\x2012:45:38\x20GMT\r\nConnection
SF::\x20close\r\n\r\n{\"timestamp\":\"2023-08-12T12:45:39\.138\+0000\",\"s
SF:tatus\":404,\"error\":\"Not\x20Found\",\"message\":\"No\x20message\x20a
SF:vailable\",\"path\":\"/nice%20ports%2C/Tri%6Eity\.txt%2ebak\"}")%r(Sock
SF:s5,3BB,"HTTP/1\.1\x20400\x20\r\nContent-Type:\x20text/html;charset=utf-
SF:8\r\nContent-Language:\x20en\r\nContent-Length:\x20800\r\nDate:\x20Sat,
SF:\x2012\x20Aug\x202023\x2012:45:38\x20GMT\r\nConnection:\x20close\r\n\r\
SF:n<!doctype\x20html><html\x20lang=\"en\"><head><title>HTTP\x20Status\x20
SF:400\x20\xe2\x80\x93\x20Bad\x20Request</title><style\x20type=\"text/css\
SF:">h1\x20{font-family:Tahoma,Arial,sans-serif;color:white;background-col
SF:or:#525D76;font-size:22px;}\x20h2\x20{font-family:Tahoma,Arial,sans-ser
SF:if;color:white;background-color:#525D76;font-size:16px;}\x20h3\x20{font
SF:-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;fo
SF:nt-size:14px;}\x20body\x20{font-family:Tahoma,Arial,sans-serif;color:bl
SF:ack;background-color:white;}\x20b\x20{font-family:Tahoma,Arial,sans-ser
SF:if;color:white;background-color:#525D76;}\x20p\x20{font-family:Tahoma,A
SF:rial,sans-serif;background:white;color:black;font-size:12px;}\x20a\x20{
SF:color:black;}\x20a\.name\x20{color:black;}\x20\.line\x20{height:1px;bac
SF:kground-color:#525D76;border:none;}</style></head><body");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Aug 12 08:45:47 2023 -- 1 IP address (1 host up) scanned in 16.00 seconds
