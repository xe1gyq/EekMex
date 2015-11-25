Host Development
==

## Simulator Base Code

    eekmex@eekmex:~$ 
    eekmex@eekmex:/home/eekmex# apt-get update
    eekmex@eekmex:/home/eekmex# apt-get install git
    eekmex@eekmex:/home/eekmex# exit
    eekmex@eekmex:~$ git clone https://github.com/xe1gyq/eekmex.git
    Cloning into 'eekmex'...
    remote: Counting objects: 3542, done.
    remote: Compressing objects: 100% (88/88), done.
    remote: Total 3542 (delta 52), reused 0 (delta 0), pack-reused 3451
    Receiving objects: 100% (3542/3542), 325.81 KiB | 377.00 KiB/s, done.
    Resolving deltas: 100% (2404/2404), done.
    Checking connectivity... done.
    eekmex@eekmex:~$ cd eekmex
    eekmex@eekmex:~/eekmex$ ls
    documentation  eekmex  LICENSE  README.md  sandbox  simulator  SUMMARY.md  training
    eekmex@eekmex:~/eekmex$ cd simulator

## Simulator Clean

    eekmex@eekmex:~/eekmex/simulator$ python eekmex.py -c files
    root: eekmex     INFO EekMex, Aerospace Learning Platform
    root: eekmex     INFO Mode Clean Up, Remove Files

## Simulator Demo Sensors

    eekmex@eekmex:~/eekmex/simulator$ python eekmex.py -d sensors
    root: eekmex     INFO EekMex, Aerospace Learning Platform
    root: eekmex     INFO Mode Demo
    root: emdemo     INFO Demo
    root: emaltitude INFO Altitude 2020
    root: empressure INFO Pressure 1484
    root: emsealevelpressure INFO Sea Level Pressure 1900
    root: emtemperature INFO Temperature 40
    root: emdemo     INFO Sensors: 2020,1484,1900,40
    ...
    ^C
    eekmex@eekmex:~/eekmex/simulator$ 

## Simulator Demo IMU

    eekmex@eekmex:~/eekmex/simulator$ 

## Simulator Demo GPS

    eekmex@eekmex:~/eekmex/simulator$ 
