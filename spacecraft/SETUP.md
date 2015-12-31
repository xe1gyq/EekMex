# Application Automatic Startup

root@edison:~# nano /lib/systemd/system/eekmex.service

 [Unit]
 Description=EekMex
 After=network.target

 [Service]
 ExecStart=/home/root/eekmex/eekmex.py
 Restart=always
 RestartSec=10s
 Environment=NODE_ENV=production

 [Install]
 WantedBy=multi-user.target

root@edison:~# systemctl daemon-reload
root@edison:~# systemcrl start eekmex.service
root@edison:~# systemcrl enable eekmex.service

root@ubilinux:/home/xe1gyq/Projects/eekmex# git push                                                                     
error: server certificate verification failed. CAfile: /etc/ssl/certs/ca-certificates.crt CRLfile: none while accessing h
ttps://github.com/xe1gyq/eekmex.git/info/refs                                                                            
root@ubilinux:/home/xe1gyq/Projects/eekmex# update-ca-certificates                                                       
Updating certificates in /etc/ssl/certs... 0 added, 0 removed; done.                                                     
Running hooks in /etc/ca-certificates/update.d....done. 

# AX25

apt-get install ax25-tools libax25 libax25-dev soundmodem


# End of File
