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

## Packages Apt-Get

    root@ubilinux:~# apt-get install python-pip
    root@ubilinux:~# apt-get install git build-essential python-dev python-smbus
    root@ubilinux:~# apt-get install gpsd gpsd-clients python-gps libxml2-dev libxslt1-dev

## Packages Pip

    root@ubilinux:~# pip install numpy psutil XBee pyserial pykml

## Packages Manual Installation

    root@ubilinux:~# git clone https://github.com/adafruit/Adafruit_Python_BMP.git
    root@ubilinux:~# cd Adafruit_Python_BMP
    root@ubilinux:~# python setup.py install

## Testing GPS    

    root@ubilinux:~# gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock
    root@ubilinux:~# cgps -s

    
