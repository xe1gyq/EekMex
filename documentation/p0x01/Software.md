Software
==

## Ubilinux

### Installation

- [Loading Debian (Ubilinux) on the Edison ](https://learn.sparkfun.com/tutorials/loading-debian-ubilinux-on-the-edison)
  - Install 
  - Log into
    - user: edison
    - password: edison
  - Enable WiFi

## Packages

    root@ubilinux:~# apt-get install python-pip
    root@ubilinux:~# apt-get install git build-essential python-dev python-smbus
    root@ubilinux:~# git clone https://github.com/adafruit/Adafruit_Python_BMP.git
    root@ubilinux:~# cd Adafruit_Python_BMP
    root@ubilinux:~# python setup.py install
    root@ubilinux:~# 

    
