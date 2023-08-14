# Nmap 7.94 scan initiated Thu Aug 10 05:04:59 2023 as: nmap -sU -A -p161 -oN nmapUDP.md 192.168.218.145
Nmap scan report for 192.168.218.145
Host is up (0.042s latency).

PORT    STATE SERVICE VERSION
161/udp open  snmp    SNMPv1 server (public)
| snmp-sysdescr: Hardware: AMD64 Family 25 Model 1 Stepping 1 AT/AT COMPATIBLE - Software: Windows Version 6.3 (Build 19041 Multiprocessor Free)
|_  System uptime: 97d08h41m9.22s (841206922 timeticks)
| snmp-processes: 
|   1: 
|     Name: System Idle Process
|   4: 
|     Name: System
|   92: 
|     Name: Registry
|   356: 
|     Name: dwm.exe
|   372: 
|     Name: smss.exe
|   444: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k netsvcs -p -s DsmSvc
|   464: 
|     Name: csrss.exe
|   564: 
|     Name: wininit.exe
|   576: 
|     Name: csrss.exe
|   656: 
|     Name: winlogon.exe
|   684: 
|     Name: services.exe
|   708: 
|     Name: lsass.exe
|     Path: C:\WINDOWS\system32\
|   728: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k NetworkService -s TermService
|   804: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k DcomLaunch -p -s PlugPlay
|   828: 
|     Name: fontdrvhost.exe
|   856: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k DcomLaunch -p
|   900: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k LocalServiceNoNetwork -p
|   908: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k RPCSS -p
|   956: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k DcomLaunch -p -s LSM
|   1016: 
|     Name: fontdrvhost.exe
|   1084: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k netsvcs -p -s SENS
|   1148: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k LocalSystemNetworkRestricted -p -s NcbService
|   1156: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k LocalServiceNetworkRestricted -p -s TimeBrokerSvc
|   1208: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k LocalService -p -s DispBrokerDesktopSvc
|   1256: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k LocalServiceNetworkRestricted -p -s EventLog
|   1324: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k LocalService -p -s nsi
|   1344: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k LocalSystemNetworkRestricted -p -s UmRdpService
|   1384: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k LocalServiceNetworkRestricted -p -s Dhcp
|   1508: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k netsvcs -s CertPropSvc
|   1584: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k NetworkService -p -s NlaSvc
|   1628: 
|     Name: vm3dservice.exe
|     Path: C:\WINDOWS\system32\
|   1680: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k netsvcs -p -s Schedule
|   1752: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k NetworkService -p -s LanmanWorkstation
|   1792: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k LocalService -p
|   1824: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k netsvcs -p -s ProfSvc
|   1832: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k LocalService -p -s netprofm
|   1844: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k LocalService -p -s EventSystem
|   1856: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k LocalSystemNetworkRestricted -p -s SysMain
|   1876: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k netsvcs -p -s Themes
|   1988: 
|     Name: Memory Compression
|   1996: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k netsvcs -p -s SessionEnv
|   2068: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k LocalSystemNetworkRestricted -p -s AudioEndpointBuilder
|   2112: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k LocalService -p -s FontCache
|   2216: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k LocalServiceNetworkRestricted -p
|   2260: 
|     Name: MsMpEng.exe
|   2288: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k NetworkService -p -s Dnscache
|   2308: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k LocalServiceNetworkRestricted -p
|   2320: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k LocalServiceNetworkRestricted -p
|   2360: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k netsvcs -p -s UserManager
|   2404: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k netsvcs -p -s ShellHWDetection
|   2528: 
|     Name: spoolsv.exe
|     Path: C:\WINDOWS\System32\
|   2568: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k LocalServiceNetworkRestricted -p -s WinHttpAutoProxySvc
|   2612: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k LocalServiceNoNetworkFirewall -p
|   2812: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k appmodel -p -s StateRepository
|   2836: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k apphost -s AppHostSvc
|   2844: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k NetworkService -p -s CryptSvc
|   2852: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k utcsvc -p
|   2864: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k LocalServiceNoNetwork -p -s DPS
|   2888: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k ftpsvc -s ftpsvc
|   2912: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k netsvcs -p -s Winmgmt
|   2960: 
|     Name: msdtc.exe
|     Path: C:\WINDOWS\System32\
|   2984: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k netsvcs -p -s LanmanServer
|   3000: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k LocalService -p -s SstpSvc
|   3020: 
|     Name: snmp.exe
|     Path: C:\WINDOWS\System32\
|   3028: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k LocalSystemNetworkRestricted -p -s TrkWks
|   3036: 
|     Name: VGAuthService.exe
|     Path: C:\Program Files\VMware\VMware Tools\VMware VGAuth\
|   3052: 
|     Name: LicensingUI.exe
|     Path: C:\WINDOWS\system32\
|     Params:  /DesktopExperience
|   3056: 
|     Name: vmtoolsd.exe
|     Path: C:\Program Files\VMware\VMware Tools\
|   3068: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k iissvcs
|   3124: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k NetSvcs -p -s iphlpsvc
|   3132: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k netsvcs -p -s WpnService
|   3168: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k LocalService -p -s WdiServiceHost
|   3396: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k netsvcs
|   3532: 
|     Name: UserOOBEBroker.exe
|     Path: C:\Windows\System32\oobe\
|     Params: -Embedding
|   3748: 
|     Name: WmiPrvSE.exe
|     Path: C:\WINDOWS\system32\wbem\
|   3772: 
|     Name: RuntimeBroker.exe
|     Path: C:\Windows\System32\
|     Params: -Embedding
|   3844: 
|     Name: dllhost.exe
|     Path: C:\WINDOWS\system32\
|     Params: /Processid:{02D4B3F1-FD88-11D1-960D-00805FC79235}
|   3888: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k NetworkServiceNetworkRestricted -p -s PolicyAgent
|   4104: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k netsvcs -p -s UsoSvc
|   4252: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k LocalSystemNetworkRestricted -p -s WdiSystemHost
|   4620: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k LocalSystemNetworkRestricted -p -s StorSvc
|   4720: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k LocalServiceNetworkRestricted -s RmSvc
|   4884: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k LocalSystemNetworkRestricted -p -s PcaSvc
|   5196: 
|     Name: SearchIndexer.exe
|     Path: C:\WINDOWS\system32\
|     Params: /Embedding
|   5252: 
|     Name: sihost.exe
|   5272: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k UnistackSvcGroup -s CDPUserSvc
|   5284: 
|     Name: w3wp.exe
|     Path: c:\windows\system32\inetsrv\
|     Params: -ap "DefaultAppPool" -v "v4.0" -l "webengine4.dll" -a \\.\pipe\iisipmbd86b93b-1eb9-4ddf-bde7-ae404f8e521d -h "C:\inetpub\temp\ap
|   5304: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k UnistackSvcGroup -s WpnUserService
|   5420: 
|     Name: MicrosoftEdgeUpdate.exe
|     Path: C:\Users\offsec\AppData\Local\Microsoft\EdgeUpdate\
|     Params: /c
|   5428: 
|     Name: MouseServer.exe
|     Path: C:\Program Files (x86)\Mouse Server\
|   5456: 
|     Name: taskhostw.exe
|     Params: {222A245B-E637-4AE9-A93F-A59CA119A75E}
|   5472: 
|     Name: MicrosoftEdgeUpdate.exe
|     Path: C:\Program Files (x86)\Microsoft\EdgeUpdate\
|     Params:  /c
|   5512: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k netsvcs -p -s TokenBroker
|   5652: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k LocalSystemNetworkRestricted -p -s TabletInputService
|   5704: 
|     Name: ctfmon.exe
|   5792: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k LocalService -p -s CDPSvc
|   5924: 
|     Name: explorer.exe
|     Path: C:\WINDOWS\
|   6004: 
|     Name: SgrmBroker.exe
|   6032: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k ClipboardSvcGroup -p -s cbdhsvc
|   6184: 
|     Name: StartMenuExperienceHost.exe
|     Path: C:\Windows\SystemApps\Microsoft.Windows.StartMenuExperienceHost_cw5n1h2txyewy\
|     Params:  -ServerName:App.AppXywbrabmsek0gm3tkwpr5kwzbs55tkqay.mca
|   6248: 
|     Name: RuntimeBroker.exe
|     Path: C:\Windows\System32\
|     Params: -Embedding
|   6268: 
|     Name: RuntimeBroker.exe
|     Path: C:\Windows\System32\
|     Params: -Embedding
|   6376: 
|     Name: SearchApp.exe
|     Path: C:\Windows\SystemApps\Microsoft.Windows.Search_cw5n1h2txyewy\
|     Params:  -ServerName:CortanaUI.AppX8z9r6jm96hw4bsbneegw0kyxx296wr9t.mca
|   6632: 
|     Name: RuntimeBroker.exe
|     Path: C:\Windows\System32\
|     Params: -Embedding
|   6836: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k WbioSvcGroup -s WbioSrvc
|   7036: 
|     Name: Mouse Server Luminati.exe
|   7220: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k LocalServiceNetworkRestricted -p -s lmhosts
|   7316: 
|     Name: SecurityHealthService.exe
|   7404: 
|     Name: dllhost.exe
|     Path: C:\WINDOWS\system32\
|     Params: /Processid:{973D20D7-562D-44B9-B70B-5A0F49CCDF3F}
|   7468: 
|     Name: SecurityHealthSystray.exe
|     Path: C:\Windows\System32\
|     Params:  
|   7560: 
|     Name: vmtoolsd.exe
|     Path: C:\Program Files\VMware\VMware Tools\
|     Params:  -n vmusr
|   7604: 
|     Name: vm3dservice.exe
|     Path: C:\Windows\System32\
|     Params:  -u
|   7628: 
|     Name: OneDrive.exe
|     Path: C:\Users\offsec\AppData\Local\Microsoft\OneDrive\
|     Params:  /background
|   7644: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k LocalService -s W32Time
|   7804: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k netsvcs -p -s BITS
|   7820: 
|     Name: Microsoft.Photos.exe
|     Path: C:\Program Files\WindowsApps\Microsoft.Windows.Photos_2021.21090.10008.0_x64__8wekyb3d8bbwe\
|     Params:  -ServerName:App.AppXzst44mncqdg84v7sv6p7yznqwssy6f7f.mca
|   7868: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k LocalServiceAndNoImpersonation -p -s SSDPSRV
|   7956: 
|     Name: svchost.exe
|   8124: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k netsvcs -p
|   8156: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k LocalSystemNetworkRestricted -p -s DsSvc
|   8176: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -k UnistackSvcGroup
|   8408: 
|     Name: ApplicationFrameHost.exe
|     Path: C:\WINDOWS\system32\
|     Params: -Embedding
|   8436: 
|     Name: RuntimeBroker.exe
|     Path: C:\Windows\System32\
|     Params: -Embedding
|   8452: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k LocalService -p -s LicenseManager
|   8508: 
|     Name: svchost.exe
|     Path: C:\WINDOWS\System32\
|     Params: -k LocalSystemNetworkRestricted -p -s Netman
|   8556: 
|     Name: WinStore.App.exe
|     Path: C:\Program Files\WindowsApps\Microsoft.WindowsStore_12107.1001.15.0_x64__8wekyb3d8bbwe\
|_    Params:  -ServerName:App.AppXc75wvwned5vhz4xyxxecvgdjhdkgsdza.mca
| snmp-win32-software: 
|   Microsoft Edge; 2023-02-24T06:08:12
|   Microsoft Edge Update; 2023-03-02T01:34:30
|   Microsoft Edge WebView2 Runtime; 2023-02-24T06:08:48
|   Microsoft Update Health Tools; 2023-01-05T05:04:48
|   Microsoft Visual C++ 2015-2019 Redistributable (x64) - 14.24.281; 2023-01-05T05:04:50
|   Microsoft Visual C++ 2015-2019 Redistributable (x86) - 14.24.281; 2023-01-05T05:04:50
|   Microsoft Visual C++ 2019 X64 Additional Runtime - 14.24.28127; 2023-01-05T05:04:48
|   Microsoft Visual C++ 2019 X64 Minimum Runtime - 14.24.28127; 2023-01-05T05:04:48
|   Microsoft Visual C++ 2019 X86 Additional Runtime - 14.24.28127; 2023-01-05T05:04:50
|   Microsoft Visual C++ 2019 X86 Minimum Runtime - 14.24.28127; 2023-01-05T05:04:50
|   Mouse Server version 1.7.8.5; 2023-01-05T05:04:50
|   PuTTY release 0.76 (64-bit); 2023-01-05T05:04:48
|   Update for Windows 10 for x64-based Systems (KB5001716); 2023-01-05T05:04:48
|_  VMware Tools; 2023-01-05T05:04:48
| snmp-win32-services: 
|   Application Host Helper Service
|   Background Intelligent Transfer Service
|   Background Tasks Infrastructure Service
|   Base Filtering Engine
|   CNG Key Isolation
|   COM+ Event System
|   COM+ System Application
|   Certificate Propagation
|   Clipboard User Service_6b8d5
|   Connected Devices Platform Service
|   Connected Devices Platform User Service_6b8d5
|   Connected User Experiences and Telemetry
|   CoreMessaging
|   Credential Manager
|   Cryptographic Services
|   DCOM Server Process Launcher
|   DHCP Client
|   DNS Client
|   Data Sharing Service
|   Data Usage
|   Device Setup Manager
|   Diagnostic Policy Service
|   Diagnostic Service Host
|   Diagnostic System Host
|   Display Policy Service
|   Distributed Link Tracking Client
|   Distributed Transaction Coordinator
|   IP Helper
|   IPsec Policy Agent
|   Local Session Manager
|   Microsoft Defender Antivirus Service
|   Microsoft FTP Service
|   Microsoft Store Install Service
|   Network Connection Broker
|   Network Connections
|   Network List Service
|   Network Location Awareness
|   Network Store Interface Service
|   Payments and NFC/SE Manager
|   Plug and Play
|   Power
|   Print Spooler
|   Program Compatibility Assistant Service
|   RPC Endpoint Mapper
|   Radio Management Service
|   Remote Access Connection Manager
|   Remote Desktop Configuration
|   Remote Desktop Services
|   Remote Desktop Services UserMode Port Redirector
|   Remote Procedure Call (RPC)
|   SNMP Service
|   SSDP Discovery
|   Secure Socket Tunneling Protocol Service
|   Security Accounts Manager
|   Security Center
|   Server
|   Shell Hardware Detection
|   State Repository Service
|   Storage Service
|   Sync Host_6b8d5
|   SysMain
|   System Event Notification Service
|   System Events Broker
|   System Guard Runtime Monitor Broker
|   TCP/IP NetBIOS Helper
|   Task Scheduler
|   Themes
|   Time Broker
|   Touch Keyboard and Handwriting Panel Service
|   Update Orchestrator Service
|   User Manager
|   User Profile Service
|   VMware Alias Manager and Ticket Service
|   VMware SVGA Helper Service
|   VMware Tools
|   Web Account Manager
|   WinHTTP Web Proxy Auto-Discovery Service
|   Windows Audio
|   Windows Audio Endpoint Builder
|   Windows Biometric Service
|   Windows Connection Manager
|   Windows Defender Firewall
|   Windows Event Log
|   Windows Font Cache Service
|   Windows License Manager Service
|   Windows Management Instrumentation
|   Windows Process Activation Service
|   Windows Push Notifications System Service
|   Windows Push Notifications User Service_6b8d5
|   Windows Search
|   Windows Security Service
|   Windows Time
|   Workstation
|_  World Wide Web Publishing Service
| snmp-netstat: 
|   TCP  0.0.0.0:21           0.0.0.0:0
|   TCP  0.0.0.0:80           0.0.0.0:0
|   TCP  0.0.0.0:135          0.0.0.0:0
|   TCP  0.0.0.0:445          0.0.0.0:0
|   TCP  0.0.0.0:1978         0.0.0.0:0
|   TCP  0.0.0.0:3389         0.0.0.0:0
|   TCP  0.0.0.0:5040         0.0.0.0:0
|   TCP  0.0.0.0:49664        0.0.0.0:0
|   TCP  0.0.0.0:49665        0.0.0.0:0
|   TCP  0.0.0.0:49666        0.0.0.0:0
|   TCP  0.0.0.0:49667        0.0.0.0:0
|   TCP  0.0.0.0:49668        0.0.0.0:0
|   TCP  0.0.0.0:49669        0.0.0.0:0
|   TCP  0.0.0.0:49670        0.0.0.0:0
|   TCP  192.168.218.145:139  0.0.0.0:0
|   UDP  0.0.0.0:123          *:*
|   UDP  0.0.0.0:161          *:*
|   UDP  0.0.0.0:2007         *:*
|   UDP  0.0.0.0:3389         *:*
|   UDP  0.0.0.0:5050         *:*
|   UDP  0.0.0.0:5353         *:*
|   UDP  0.0.0.0:5355         *:*
|   UDP  127.0.0.1:1900       *:*
|   UDP  127.0.0.1:52926      *:*
|   UDP  127.0.0.1:60434      *:*
|   UDP  192.168.218.145:137  *:*
|   UDP  192.168.218.145:138  *:*
|   UDP  192.168.218.145:1900 *:*
|_  UDP  192.168.218.145:52925 *:*
| snmp-win32-users: 
|   Administrator
|   DefaultAccount
|   Guest
|   WDAGUtilityAccount
|   offsec
|_  zachary
| snmp-interfaces: 
|   Software Loopback Interface 1\x00
|     IP address: 127.0.0.1  Netmask: 255.0.0.0
|     Type: softwareLoopback  Speed: 1 Gbps
|     Traffic stats: 0.00 Kb sent, 0.00 Kb received
|   WAN Miniport (IPv6)\x00
|     Type: ethernetCsmacd  Speed: 0 Kbps
|     Traffic stats: 0.00 Kb sent, 0.00 Kb received
|   WAN Miniport (IP)\x00
|     Type: ethernetCsmacd  Speed: 0 Kbps
|     Traffic stats: 0.00 Kb sent, 0.00 Kb received
|   WAN Miniport (Network Monitor)\x00
|     Type: ethernetCsmacd  Speed: 0 Kbps
|     Traffic stats: 0.00 Kb sent, 0.00 Kb received
|   vmxnet3 Ethernet Adapter\x00
|     IP address: 192.168.218.145  Netmask: 255.255.255.0
|     MAC address: 00:50:56:ba:09:5e (VMware)
|     Type: ethernetCsmacd  Speed: 4 Gbps
|     Traffic stats: 1.04 Mb sent, 1.30 Mb received
|   vmxnet3 Ethernet Adapter-WFP Native MAC Layer LightWeight Filter-0000\x00
|     MAC address: 00:50:56:ba:09:5e (VMware)
|     Type: ethernetCsmacd  Speed: 4 Gbps
|     Traffic stats: 1.04 Mb sent, 1.30 Mb received
|   vmxnet3 Ethernet Adapter-QoS Packet Scheduler-0000\x00
|     MAC address: 00:50:56:ba:09:5e (VMware)
|     Type: ethernetCsmacd  Speed: 4 Gbps
|     Traffic stats: 1.04 Mb sent, 1.30 Mb received
|   vmxnet3 Ethernet Adapter-WFP 802.3 MAC Layer LightWeight Filter-0000\x00
|     MAC address: 00:50:56:ba:09:5e (VMware)
|     Type: ethernetCsmacd  Speed: 4 Gbps
|     Traffic stats: 1.04 Mb sent, 1.30 Mb received
|   WAN Miniport (IP)-WFP Native MAC Layer LightWeight Filter-0000\x00
|     Type: ethernetCsmacd  Speed: 0 Kbps
|     Traffic stats: 0.00 Kb sent, 0.00 Kb received
|   WAN Miniport (IP)-QoS Packet Scheduler-0000\x00
|     Type: ethernetCsmacd  Speed: 0 Kbps
|     Traffic stats: 0.00 Kb sent, 0.00 Kb received
|   WAN Miniport (IPv6)-WFP Native MAC Layer LightWeight Filter-0000\x00
|     Type: ethernetCsmacd  Speed: 0 Kbps
|     Traffic stats: 0.00 Kb sent, 0.00 Kb received
|   WAN Miniport (IPv6)-QoS Packet Scheduler-0000\x00
|     Type: ethernetCsmacd  Speed: 0 Kbps
|     Traffic stats: 0.00 Kb sent, 0.00 Kb received
|   WAN Miniport (Network Monitor)-WFP Native MAC Layer LightWeight Filter-0000\x00
|     Type: ethernetCsmacd  Speed: 0 Kbps
|     Traffic stats: 0.00 Kb sent, 0.00 Kb received
|   WAN Miniport (Network Monitor)-QoS Packet Scheduler-0000\x00
|     Type: ethernetCsmacd  Speed: 0 Kbps
|_    Traffic stats: 0.00 Kb sent, 0.00 Kb received
Too many fingerprints match this host to give specific OS details
Network Distance: 4 hops
Service Info: Host: oscp

TRACEROUTE (using port 161/udp)
HOP RTT      ADDRESS
1   42.10 ms 192.168.45.1
2   42.10 ms 192.168.45.254
3   42.13 ms 192.168.251.1
4   42.14 ms 192.168.218.145

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Aug 10 05:05:47 2023 -- 1 IP address (1 host up) scanned in 48.66 seconds
