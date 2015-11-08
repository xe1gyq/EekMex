Operating System Abstraction Layer
==

    xe1gyq@jessie:~/Projects$ git clone https://github.com/nasa/osal.git
    Cloning into 'osal'...
    remote: Counting objects: 444, done.
    remote: Total 444 (delta 0), reused 0 (delta 0), pack-reused 444
    Receiving objects: 100% (444/444), 3.18 MiB | 466.00 KiB/s, done.
    Resolving deltas: 100% (197/197), done.
    Checking connectivity... done.
    xe1gyq@jessie:~/Projects$ cd osal
    xe1gyq@jessie:~/Projects/osal$ source setvars.sh
    xe1gyq@jessie:~/Projects/osal$ nano build/osal-config.mak
    BSP = pc-linux
    xe1gyq@jessie:~/Projects/osal$ export OSAL_SRC=/home/xe1gyq/Projects/osal/src
    

## Links

- [Operating System Abstraction Layer Github](https://github.com/nasa/osal)