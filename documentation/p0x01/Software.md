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
    
[Why not using UPM Library?](https://github.com/xe1gyq/eekmex/issues/1)

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
    root@ubilinux:~# cmake .. -DBUILDSWIGNODE=OFF
    root@ubilinux:~# make
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

## Testing

### GPS

    root@ubilinux:~# dmesg
    [  514.492900] usb 1-1: reset full-speed USB device number 2 using dwc3-host
    [  514.513505] dwc3-host dwc3-host.2: xHCI xhci_drop_endpoint called with disabled ep f5626500
    [  514.513566] usb 1-1: ep 0x81 - rounding interval to 1024 microframes, ep desc says 2040 microframes
    [  514.922543] usb 1-1.2: new full-speed USB device number 3 using dwc3-host
    [  514.953097] usb 1-1.2: New USB device found, idVendor=0403, idProduct=6001
    [  514.953128] usb 1-1.2: New USB device strings: Mfr=1, Product=2, SerialNumber=3
    [  514.953149] usb 1-1.2: Product: FT232R USB UART
    [  514.953168] usb 1-1.2: Manufacturer: FTDI
    [  514.953186] usb 1-1.2: SerialNumber: A60442H3
    [  514.959035] ftdi_sio 1-1.2:1.0: FTDI USB Serial Device converter detected
    [  514.959298] usb 1-1.2: Detected FT232RL
    [  514.959322] usb 1-1.2: Number of endpoints 2
    [  514.959341] usb 1-1.2: Endpoint 1 MaxPacketSize 64
    [  514.959360] usb 1-1.2: Endpoint 2 MaxPacketSize 64
    [  514.959378] usb 1-1.2: Setting MaxPacketSize 64
    [  514.960259] usb 1-1.2: FTDI USB Serial Device converter now attached to ttyUSB0
    root@ubilinux:~# gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock
    root@ubilinux:~# cgps -s
    lqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqklqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqk
    x    Time:       2011-11-13T00:00:39.090Z   xxPRN:   Elev:  Azim:  SNR:  Used: x
    x    Latitude:   n/a                        xx                                 x
    x    Longitude:  n/a                        xx                                 x
    x    Altitude:   n/a                        xx                                 x
    x    Speed:      n/a                        xx                                 x
    x    Heading:    n/a                        xx                                 x
    x    Climb:      n/a                        xx                                 x
    x    Status:     NO FIX (15 secs)           xx                                 x
    x    Longitude Err:   n/a                   xx                                 x
    x    Latitude Err:    n/a                   xx                                 x
    x    Altitude Err:    n/a                   xx                                 x
    x    Course Err:      n/a                   xx                                 x
    x    Speed Err:       n/a                   xx                                 x
    x    Time offset:     124046999.723         xx                                 x
    x    Grid Square:     n/a                   xx                                 x
    mqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqjmqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqj


### SD Card

    root@ubilinux:~# mkdir /media/sdcard/
    root@ubilinux:~# mount -o umask=0,uid=nobody /dev/mmcblk1p1 /media/sdcard/
    
