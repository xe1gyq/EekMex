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

# End of File
