# Source Code

We have a git repository

    user@board:~$
    user@board:/home/edison# su
    Password: 
    user@board:/home/edison# apt-get update
    user@board:/home/edison# apt-get install git
    user@board:/home/edison# exit
    user@board:~$ git clone https://github.com/xe1gyq/eekmex.git
    user@board:~$ cd eekmex
    edison@ubilinux:~/eekmex$ ls
    documentation  eekmex  LICENSE  README.md  sandbox  simulator  SUMMARY.md  training
    root@ubilinux:/home/edison/eekmex# su
    Password: edison
    root@ubilinux:/home/edison/eekmex/spacecraft# python eekmex.py -c files
    root@ubilinux:/home/edison/eekmex/spacecraft# git config --global user.email "you@example.com"
    root@ubilinux:/home/edison/eekmex/spacecraft# git config --global user.name "Your Name"
