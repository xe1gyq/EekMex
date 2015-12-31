# Source Code

We have a git repository

    edison@ubilinux:~$
    edison@ubilinux:/home/edison# su
    Password: 
    root@ubilinux:/home/edison# apt-get update
    root@ubilinux:/home/edison# apt-get install git
    root@ubilinux:/home/edison# exit
    edison@ubilinux:~$ git clone https://github.com/xe1gyq/eekmex.git
    edison@ubilinux:~$ cd eekmex
    edison@ubilinux:~/eekmex$ ls
    documentation  eekmex  LICENSE  README.md  sandbox  simulator  SUMMARY.md  training
    root@ubilinux:/home/edison/eekmex# su
    Password: edison
    root@ubilinux:/home/edison/eekmex/eekmex# python eekmex.py -c files
    root@ubilinux:/home/edison/eekmex/eekmex# git config --global user.email "you@example.com"
    root@ubilinux:/home/edison/eekmex/eekmex# git config --global user.name "Your Name"
