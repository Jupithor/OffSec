# Nmap 7.94 scan initiated Tue Aug  1 09:25:32 2023 as: nmap -vvv -sT --top-ports=20 -Pn -oN 172.16.x.14/nmap.md 172.16.195.14
Nmap scan report for 172.16.195.14
Host is up, received user-set (2.1s latency).
Scanned at 2023-08-01 09:25:32 EDT for 42s

PORT     STATE  SERVICE       REASON
21/tcp   closed ftp           conn-refused
22/tcp   open   ssh           syn-ack
23/tcp   closed telnet        conn-refused
25/tcp   closed smtp          conn-refused
53/tcp   closed domain        conn-refused
80/tcp   closed http          conn-refused
110/tcp  closed pop3          conn-refused
111/tcp  closed rpcbind       conn-refused
135/tcp  closed msrpc         conn-refused
139/tcp  closed netbios-ssn   conn-refused
143/tcp  closed imap          conn-refused
443/tcp  closed https         conn-refused
445/tcp  closed microsoft-ds  conn-refused
993/tcp  closed imaps         conn-refused
995/tcp  closed pop3s         conn-refused
1723/tcp closed pptp          conn-refused
3306/tcp closed mysql         conn-refused
3389/tcp closed ms-wbt-server conn-refused
5900/tcp closed vnc           conn-refused
8080/tcp closed http-proxy    conn-refused

Read data files from: /usr/bin/../share/nmap
# Nmap done at Tue Aug  1 09:26:14 2023 -- 1 IP address (1 host up) scanned in 41.71 seconds
