# Source Code

We have a git repository

```sh
    user@spacecraft:~$
    user@spacecraft:/home/user# su
    Password: 
    root@spacecraft:/home/user# apt-get update
    root@spacecraft:/home/user# apt-get install git
    root@spacecraft:/home/user# exit
    user@spacecraft:~$ git clone https://github.com/xe1gyq/eekmex.git
    user@spacecraft:~$ cd eekmex
    user@spacecraft:~/eekmex$ ls
    documentation  LICENSE  README.md  sandbox  spacecraft  SUMMARY.md
    user@spacecraft:/home/user/eekmex$ su
    Password: passwd
    root@spacecraft:/home/user/eekmex/spacecraft# python eekmex.py -c files
```