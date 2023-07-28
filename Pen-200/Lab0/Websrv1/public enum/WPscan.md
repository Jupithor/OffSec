
kali@kali:~/beyond$ #wpscan --url http://192.168.50.244 --enumerate p --plugins-detection aggressive -o websrv1/wpscan

kali@kali:~/beyond$ cat websrv1/wpscan
...

[i] Plugin(s) Identified:

[+] akismet
 | Location: http://192.168.50.244/wp-content/plugins/akismet/
 | Latest Version: 5.0
 | Last Updated: 2022-07-26T16:13:00.000Z
 |
 | Found By: Known Locations (Aggressive Detection)
 |  - http://192.168.50.244/wp-content/plugins/akismet/, status: 500
 |
 | The version could not be determined.

[+] classic-editor
 | Location: http://192.168.50.244/wp-content/plugins/classic-editor/
 | Latest Version: 1.6.2 
 | Last Updated: 2021-07-21T22:08:00.000Z
...

[+] contact-form-7
 | Location: http://192.168.50.244/wp-content/plugins/contact-form-7/
 | Latest Version: 5.6.3 (up to date)
 | Last Updated: 2022-09-01T08:48:00.000Z
...

[+] duplicator
 | Location: http://192.168.50.244/wp-content/plugins/duplicator/
 | Last Updated: 2022-09-24T17:57:00.000Z
 | Readme: http://192.168.50.244/wp-content/plugins/duplicator/readme.txt
 | [!] The version is out of date, the latest version is 1.5.1
 |
 | Found By: Known Locations (Aggressive Detection)
 |  - http://192.168.50.244/wp-content/plugins/duplicator/, status: 403
 |
 | Version: ==1.3.26== (80% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://192.168.50.244/wp-content/plugins/duplicator/readme.txt

[+] elementor
 | Location: http://192.168.50.244/wp-content/plugins/elementor/
 | Latest Version: 3.7.7 (up to date)
 | Last Updated: 2022-09-20T14:51:00.000Z
...

[+] wordpress-seo
 | Location: http://192.168.50.244/wp-content/plugins/wordpress-seo/
 | Latest Version: 19.7.1 (up to date)
 | Last Updated: 2022-09-20T14:10:00.000Z




kali@kali:~/beyond$ #searchsploit #duplicator    
-------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                        |  Path
-------------------------------------------------------------------------------------- ---------------------------------
WordPress Plugin Duplicator - Cross-Site Scripting                                    | php/webapps/38676.txt
WordPress Plugin Duplicator 0.5.14 - SQL Injection / Cross-Site Request Forgery       | php/webapps/36735.txt
WordPress Plugin Duplicator 0.5.8 - Privilege Escalation                              | php/webapps/36112.txt
WordPress Plugin Duplicator 1.2.32 - Cross-Site Scripting                             | php/webapps/44288.txt
==Wordpress Plugin Duplicator 1.3.26 - Unauthenticated Arbitrary File Read              | php/webapps/50420.py
Wordpress Plugin Duplicator 1.3.26 - Unauthenticated Arbitrary File Read (Metasploit) | php/webapps/49288.rb==
WordPress Plugin Duplicator 1.4.6 - Unauthenticated Backup Download                   | php/webapps/50992.txt
WordPress Plugin Duplicator 1.4.7 - Information Disclosure                            | php/webapps/50993.txt
WordPress Plugin Multisite Post Duplicator 0.9.5.1 - Cross-Site Request Forgery       | php/webapps/40908.html
-------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
#websrv1
