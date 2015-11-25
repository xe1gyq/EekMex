Protocols
==

## I2C

> I²C (Inter-Integrated Circuit), pronounced I-squared-C, is a multi-master, multi-slave, single-ended, serial computer bus invented by Philips Semiconductor (now NXP Semiconductors). It is typically used for attaching lower-speed peripheral ICs to processors and microcontrollers. Alternatively I²C is spelled I2C (pronounced I-two-C) or IIC (pronounced I-I-C).Wikipedia

    edison@ubilinux:~$ su
    Password: 
    root@ubilinux:/home/edison# cd
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
    root@ubilinux:~# i2cdump -y 1 0x6b
    No size specified (using byte-data access)
         0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f    0123456789abcdef
    00: b7 5b 08 fc 02 50 53 81 c1 c2 bb 8f 48 c5 00 d4    ?[???PS?????H?.?
    
    f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00    ................
    root@ubilinux:~# i2cset
    root@ubilinux:~# i2cget
    root@ubilinux:~# sensors-detect
    root@ubilinux:~# sensors
    

