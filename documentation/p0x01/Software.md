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

## Packages Apt-Get Installation

    root@ubilinux:~# apt-get install python-pip
    root@ubilinux:~# apt-get install git build-essential python-dev python-smbus swig
    root@ubilinux:~# apt-get install gpsd gpsd-clients python-gps libxml2-dev libxslt1-dev

## Packages Pip Installation

    root@ubilinux:~# pip install numpy psutil XBee pyserial pykml

## Packages Manual Installation

### Adafruit BMP180 Python Library

    root@ubilinux:~# git clone https://github.com/adafruit/Adafruit_Python_BMP.git
    root@ubilinux:~# cd Adafruit_Python_BMP
    root@ubilinux:~# python setup.py install

### MRAA

    root@ubilinux:~$ git clone https://github.com/intel-iot-devkit/mraa.git
    root@ubilinux:~$ mkdir mraa/build && cd $_
    root@ubilinux:~$ cmake .. -DBUILDSWIGNODE=OFF
    root@ubilinux:~$ make
    root@ubilinux:~# make install
    root@ubilinux:~# cd
    root@ubilinux:~# nano /etc/ld.so.conf
    /usr/local/lib/i386-linux-gnu/
    root@ubilinux:~# ldconfig
    root@ubilinux:~# ldconfig -p | grep mraa
    root@ubilinux:~$ nano ~/.bashrc
    export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/site-packages/

### Cmake

    root@ubilinux:~$ wget http://www.cmake.org/files/v3.2/cmake-3.2.2.tar.gz
    root@ubilinux:~$ tar xvf cmake-3.2.2.tar.gz
    root@ubilinux:~$ cd cmake-3.2.2
    root@ubilinux:~$ ./bootstrap
    root@ubilinux:~$ make
    root@ubilinux:~# make install

### UPM
    
    root@ubilinux:~$ git clone https://github.com/intel-iot-devkit/upm.git
    root@ubilinux:~$ mkdir upm/build
    root@ubilinux:~$ cd upm/build
    root@ubilinux:~$ cmake .. -DBUILDSWIGNODE=OFF
    root@ubilinux:~$ make
    root@ubilinux:~# make install
    root@ubilinux:~$ nano ~/.bashrc
    export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/site-packages/

## RTIMULib

    root@ubilinux:~$ git clone https://github.com/richards-tech/RTIMULib.git
    root@ubilinux:~$ mkdir -p RTIMULib/RTIMULib/build
    root@ubilinux:~$ cd RTIMULib/RTIMULib/build
    root@ubilinux:~$ cmake ..
    root@ubilinux:~$ make -j4
    root@ubilinux:~# make install
    root@ubilinux:~# ldconfig
    root@ubilinux:~# nano /etc/ld.so.conf
    /usr/local/lib/
    root@ubilinux:~$ python setup.py build
    root@ubilinux:~# python setup.py install

## Testing GPS

    root@ubilinux:~# gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock
    root@ubilinux:~# cgps -s

## Testing SD Card

    root@ubilinux:~# mkdir /media/sdcard/
    root@ubilinux:~# mount -o umask=0,uid=nobody /dev/mmcblk1p1 /media/sdcard/
    
