Software
==

## Ubilinux Installation

- [Loading Debian (Ubilinux) on the Edison ](https://learn.sparkfun.com/tutorials/loading-debian-ubilinux-on-the-edison)

## Boot Up

    Debian GNU/Linux 7 ubilinux ttyMFD2

    ubilinux login: edison
    Password: edison
    Last login: Sat Jan  1 00:01:37 UTC 2000 on ttyMFD2
    Linux ubilinux 3.10.17-yocto-standard-r2 #7 SMP PREEMPT Thu Feb 26 6

    The programs included with the Debian GNU/Linux system are free sof;
    the exact distribution terms for each program are described in the
    individual files in /usr/share/doc/*/copyright.

    Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
    permitted by applicable law.
    edison@ubilinux:~$ 

### WiFi

    edison@ubilinux:~$ su
    Password: edison
    root@ubilinux:/home/edison# cd 
    root@ubilinux:~# nano /etc/network/interfaces
    # interfaces(5) file used by ifup(8) and ifdown(8)
    auto lo
    iface lo inet loopback

    #auto usb0
    #iface usb0 inet static
    #    address 192.168.2.15
    #    netmask 255.255.255.0
    
    auto wlan0
    iface wlan0 inet dhcp
        # For WPA
        wpa-ssid INFINITUMxxxx
        wpa-psk yyyy
        # For WEP
        #wireless-essid itesm
        #wireless-mode Managed
        #wireless-key s:""
    
    root@ubilinux:~# ifup wlan0
    root@ubilinux:~# reboot

    <reboot your board, sign in and become root>

## Packages Apt-Get Installation

    edison@ubilinux:~$ su
    Password: edison
    root@ubilinux:/home/edison# cd 
    root@ubilinux:~# apt-get update
    root@ubilinux:~# apt-get install python-pip
    root@ubilinux:~# apt-get install git build-essential python-dev python-smbus swig
    root@ubilinux:~# apt-get install gpsd gpsd-clients python-gps libxml2-dev libxslt1-dev

## Packages Pip Installation

    root@ubilinux:~# pip install numpy psutil XBee pyserial pykml
    root@ubilinux:~# exit
    edison@ubilinux:~$ 

## Packages Manual Installation

### Adafruit BMP180 Python Library

    edison@ubilinux:~$ cd
    edison@ubilinux:~$ git clone https://github.com/adafruit/Adafruit_Python_BMP.git
    edison@ubilinux:~$ cd Adafruit_Python_BMP
    edison@ubilinux:~/Adafruit_Python_BMP$ su
    Password: edison
    root@ubilinux:/home/edison/Adafruit_Python_BMP# python setup.py install
    root@ubilinux:/home/edison/Adafruit_Python_BMP# exit
    edison@ubilinux:~/Adafruit_Python_BMP$ cd
    edison@ubilinux:~$

[Why not using UPM Library?](https://github.com/xe1gyq/eekmex/issues/1)

### Mraa
    
    edison@ubilinux:~$ su
    Password: 
    root@ubilinux:/home/edison# cd
    root@ubilinux:~# apt-get update
    root@ubilinux:~# apt-cache search pcre
    root@ubilinux:~# apt-get install libpcre3-dev git cmake python-dev swig
    root@ubilinux:~# exit
    edison@ubilinux:~$ cd
    edison@ubilinux:~$ git clone https://github.com/intel-iot-devkit/mraa.git
    edison@ubilinux:~$ mkdir mraa/build && cd $_
    edison@ubilinux:~/mraa/build$ cmake .. -DBUILDSWIGNODE=OFF
    edison@ubilinux:~/mraa/build$ make -j3
    edison@ubilinux:~/mraa/build$ su
    Password: edison
    root@ubilinux:/home/edison/mraa/build# make install
    root@ubilinux:/home/edison/mraa/build# nano /etc/ld.so.conf
    include /etc/ld.so.config.d/*.conf
    /usr/local/lib/i386-linux-gnu/
    root@ubilinux:/home/edison/mraa/build# ldconfig
    root@ubilinux:/home/edison/mraa/build# ldconfig -p | grep mraa
    root@ubilinux:/home/edison/mraa/build# nano ~/.bashrc
    export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/site-packages/
    root@ubilinux:/home/edison/mraa/build# exit
    edison@ubilinux:~/mraa/build# export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/site-packages/
    edison@ubilinux:~/mraa/build# nano ~/.bashrc
    export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/site-packages/
    edison@ubilinux:~/mraa/build# exit
    edison@ubilinux:~/mraa/build$ cd
    edison@ubilinux:~$ 

### Cmake

    ubilinux@ubilinux:~$ cd
    ubilinux@ubilinux:~$ wget http://www.cmake.org/files/v3.2/cmake-3.2.2.tar.gz
    ubilinux@ubilinux:~$ tar xvf cmake-3.2.2.tar.gz
    ubilinux@ubilinux:~$ cd cmake-3.2.2
    ubilinux@ubilinux:~/cmake-3.2.2$ ./bootstrap
    ubilinux@ubilinux:~/cmake-3.2.2$ make
    ubilinux@ubilinux:~/cmake-3.2.2$ su
    root@ubilinux:~/cmake-3.2.2# make install
    root@ubilinux:~/cmake-3.2.2# cp /usr/local/bin/cmake /usr/bin/cmake
    root@ubilinux:~/cmake-3.2.2# exit 
    ubilinux@ubilinux:~/cmake-3.2.2$ cd

### Upm

    edison@ubilinux:~$ cd
    edison@ubilinux:~$ git clone https://github.com/intel-iot-devkit/upm.git
    edison@ubilinux:~$ cd upm
    edison@ubilinux:~/upm$ mkdir build
    edison@ubilinux:~/upm$ cd build
    edison@ubilinux:~/upm$ export CMAKE_ROOT=/usr/local/share/cmake-3.2
    edison@ubilinux:~/upm/build$ cmake .. -DBUILDSWIGNODE=OFF
    edison@ubilinux:~/upm/build$ make
    edison@ubilinux:~/upm/build$ su
    Password: 
    root@ubilinux:~/upm/build# make install
    root@ubilinux:~/upm/build# export PYTHONPATH=$PYTHONPATH:/usr/lib/i386-linux-gnu/python2.7/site-packages/
    root@ubilinux:~/upm/build# nano ~/.bashrc
    export PYTHONPATH=$PYTHONPATH:/usr/lib/i386-linux-gnu/python2.7/site-packages/
    root@ubilinux:~/upm/build# exit
    edison@ubilinux:~/upm/build$ cd 
    edison@ubilinux:~$ 

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


### Intel.IoT.Roadshow Git Repository

    root@ubilinux:/home/edison# su
    Password: 
    root@ubilinux:/home/edison# apt-get update
    root@ubilinux:/home/edison# apt-get install git
    root@ubilinux:/home/edison# exit
    edison@ubilinux:~$ git clone https://github.com/xe1gyq/Intel.IoT.Roadshow.git
    edison@ubilinux:~$ cd Intel.IoT.Roadshow/2015
    edison@ubilinux:~/Intel.IoT.Roadshow$ python main.py -m hello
    Hello Edison!
    edison@ubilinux:~/Intel.IoT.Roadshow$ git config --global user.email "you@example.com"
    edison@ubilinux:~/Intel.IoT.Roadshow$ git config --global user.name "Your Name"
    edison@ubilinux:~/Intel.IoT.Roadshow$ cd
    
## Testing

### I2C

    root@ubilinux:~# i2cdetect -y -r 1
         0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- 1d -- -- 
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    60: -- -- -- -- -- -- -- -- -- -- -- 6b -- -- -- -- 
    70: -- -- -- -- -- -- -- 77                         

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
    
