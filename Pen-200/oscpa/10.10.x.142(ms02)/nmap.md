# Nmap 7.94 scan initiated Wed Aug  9 06:03:00 2023 as: nmap -vvv -sT --top-ports=50 -Pn -o 10.10.x.142/nmap.md 10.10.98.142
Nmap scan report for 10.10.98.142
Host is up, received user-set (2.1s latency).
Scanned at 2023-08-09 06:03:00 EDT for 101s

PORT      STATE  SERVICE          REASON
21/tcp    closed ftp              conn-refused
22/tcp    closed ssh              conn-refused
23/tcp    closed telnet           conn-refused
25/tcp    closed smtp             conn-refused
26/tcp    closed rsftp            conn-refused
53/tcp    closed domain           conn-refused
80/tcp    closed http             conn-refused
81/tcp    closed hosts2-ns        conn-refused
110/tcp   closed pop3             conn-refused
111/tcp   closed rpcbind          conn-refused
113/tcp   closed ident            conn-refused
135/tcp   open   msrpc            syn-ack
139/tcp   open   netbios-ssn      syn-ack
143/tcp   closed imap             conn-refused
179/tcp   closed bgp              conn-refused
199/tcp   closed smux             conn-refused
443/tcp   closed https            conn-refused
445/tcp   open   microsoft-ds     syn-ack
465/tcp   closed smtps            conn-refused
514/tcp   closed shell            conn-refused
515/tcp   closed printer          conn-refused
548/tcp   closed afp              conn-refused
554/tcp   closed rtsp             conn-refused
587/tcp   closed submission       conn-refused
646/tcp   closed ldp              conn-refused
993/tcp   closed imaps            conn-refused
995/tcp   closed pop3s            conn-refused
1025/tcp  closed NFS-or-IIS       conn-refused
1026/tcp  closed LSA-or-nterm     conn-refused
1027/tcp  closed IIS              conn-refused
1433/tcp  open   ms-sql-s         syn-ack
1720/tcp  closed h323q931         conn-refused
1723/tcp  closed pptp             conn-refused
2000/tcp  closed cisco-sccp       conn-refused
2001/tcp  closed dc               conn-refused
3306/tcp  closed mysql            conn-refused
3389/tcp  closed ms-wbt-server    conn-refused
5060/tcp  closed sip              conn-refused
5666/tcp  closed nrpe             conn-refused
5900/tcp  closed vnc              conn-refused
6001/tcp  closed X11:1            conn-refused
8000/tcp  closed http-alt         conn-refused
8008/tcp  closed http             conn-refused
8080/tcp  closed http-proxy       conn-refused
8443/tcp  closed https-alt        conn-refused
8888/tcp  closed sun-answerbook   conn-refused
10000/tcp closed snet-sensor-mgmt conn-refused
32768/tcp closed filenet-tms      conn-refused
49152/tcp closed unknown          conn-refused
49154/tcp closed unknown          conn-refused

Read data files from: /usr/bin/../share/nmap
# Nmap done at Wed Aug  9 06:04:41 2023 -- 1 IP address (1 host up) scanned in 100.94 seconds
