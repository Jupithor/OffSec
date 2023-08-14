# Nmap 7.94 scan initiated Fri Aug 11 08:50:24 2023 as: nmap -vvv -sT --top-ports=50 -Pn -o 10.10.x.148_ms02/nmap.md 10.10.140.148
Nmap scan report for 10.10.140.148
Host is up, received user-set (0.086s latency).
Scanned at 2023-08-11 08:50:24 EDT for 2s

PORT      STATE    SERVICE          REASON

135/tcp   open     msrpc            syn-ack
139/tcp   open     netbios-ssn      syn-ack
445/tcp   open     microsoft-ds     syn-ack
1433/tcp  open     ms-sql-s         syn-ack

Read data files from: /usr/bin/../share/nmap
# Nmap done at Fri Aug 11 08:50:26 2023 -- 1 IP address (1 host up) scanned in 2.40 seconds
