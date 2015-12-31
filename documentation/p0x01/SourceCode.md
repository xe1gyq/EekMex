# Source Code

We have a git repository

    user@board:~$
    user@board:/home/user# su
    Password: 
    user@board:/home/user# apt-get update
    user@board:/home/user# apt-get install git
    user@board:/home/user# exit
    user@board:~$ git clone https://github.com/xe1gyq/eekmex.git
    user@board:~$ cd eekmex
    user@board:~/eekmex$ ls
    documentation  LICENSE  README.md  sandbox  spacecraft  SUMMARY.md
    user@board:/home/user/eekmex# su
    Password: passwd
    user@board:/home/user/eekmex/spacecraft# python eekmex.py -c files
