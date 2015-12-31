Protocols
==

## I2C

> I²C (Inter-Integrated Circuit), pronounced I-squared-C, is a multi-master, multi-slave, single-ended, serial computer bus invented by Philips Semiconductor (now NXP Semiconductors). It is typically used for attaching lower-speed peripheral ICs to processors and microcontrollers. Alternatively I²C is spelled I2C (pronounced I-two-C) or IIC (pronounced I-I-C).Wikipedia

### i2c-tools

> A set of I²C programs that make it easy to debug I²C devices without having to write any code.

- [Elinux - Interfacing with I2C Devices](http://elinux.org/Interfacing_with_I2C_Devices)

```sh
    user@spacecraft:~$ su
    Password: 
    root@spacecraft:/home/user# cd
    root@spacecraft:~# i2cdetect -y -r 1
         0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- 1d -- -- 
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    60: -- -- -- -- -- -- -- -- -- -- -- 6b -- -- -- -- 
    70: -- -- -- -- -- -- -- 77
    user@spacecraft:~# i2cdump -y 1 0x6b
    No size specified (using byte-data access)
         0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f    0123456789abcdef
    00: b7 5b 08 fc 02 50 53 81 c1 c2 bb 8f 48 c5 00 d4    ?[???PS?????H?.?
    
    f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00    ................
    root@spacecraft:~# i2cset
    root@spacecraft:~# i2cget
    root@spacecraft:~# sensors-detect
    root@spacecraft:~# sensors
```

## Serial

> In telecommunication and computer science, serial communication is the process of sending data one bit at a time, sequentially, over a communication channel or computer bus. This is in contrast to parallel communication, where several bits are sent as a whole, on a link with several parallel channels. Wikipedia



## Gpsd Daemon

> gpsd is a service daemon that monitors one or more GPSes or AIS receivers attached to a host computer through serial or USB ports, making all data on the location/course/velocity of the sensors available

- [GPSD Homepage](http://www.catb.org/gpsd/)


    root@spacecraft:~# dmesg
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
    [  514.960259] usb 1-1.2: FTDI USB Serial Device conerverter now attached to ttyUSB0
    root@spacecraft:~# gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock
    root@spacecraft:~# cgps -s
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
