# Nmap 7.94 scan initiated Tue Aug  1 09:26:26 2023 as: nmap -vvv -sT --top-ports=20 -Pn -oN 172.16.x.82/nmap.md 172.16.195.82
Nmap scan report for 172.16.195.82
Host is up, received user-set (1.8s latency).
Scanned at 2023-08-01 09:26:26 EDT for 35s

PORT     STATE  SERVICE       REASON
21/tcp   closed ftp           conn-refused
22/tcp   closed ssh           conn-refused
23/tcp   closed telnet        conn-refused
25/tcp   closed smtp          conn-refused
53/tcp   closed domain        conn-refused
80/tcp   closed http          conn-refused
110/tcp  closed pop3          conn-refused
111/tcp  closed rpcbind       conn-refused
135/tcp  open   msrpc         syn-ack
139/tcp  open   netbios-ssn   syn-ack
143/tcp  closed imap          conn-refused
443/tcp  closed https         conn-refused
445/tcp  open   microsoft-ds  syn-ack
993/tcp  closed imaps         conn-refused
995/tcp  closed pop3s         conn-refused
1723/tcp closed pptp          conn-refused
3306/tcp closed mysql         conn-refused
3389/tcp open   ms-wbt-server syn-ack
5900/tcp closed vnc           conn-refused
8080/tcp closed http-proxy    conn-refused

Read data files from: /usr/bin/../share/nmap
# Nmap done at Tue Aug  1 09:27:01 2023 -- 1 IP address (1 host up) scanned in 35.47 seconds
