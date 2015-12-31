# Payload

## Simulator

> Simulator Definition

## PreRequisites

```sh
    Debian GNU/Linux 8 eekmex tty1

    eekmex login: eekmex
    Password: eekmex
    ...
    eekmex@eekmex:~$ su
    Password: edison
    eekmex@eekmex:/home/eekmex# cd
    root@eekmex:~# apt-get update
    root@eekmex:~# apt-get install python-pip
    root@eekmex:~# apt-get install git build-essential python-dev swig libtool zlib1g-dev
    root@eekmex:~# apt-get install python-smbus lm-sensors
    root@eekmex:~# apt-get install gpsd gpsd-clients python-gps libxml2-dev libxslt1-dev
    root@eekmex:~# pip install dweepy RandomWords LoremIpsum
```

## General Sensors

  - Temperature
  - Pressure
  - Sea Level Pressure
  - Altitude

```sh
    root@ubilinux:/home/edison# cd eekmex/spacecraft
    root@ubilinux:/home/edison/eekmex/spacecraft# python eekmex.py -d all
    root: eekmex     INFO EekMex, Aerospace Learning Platform
    root: eekmex     INFO Mode Demo
    root: emdemo     INFO Demo
    root: emsensors  INFO Sensors
    root: emsensors  INFO Sensors: 2839,1586,1603,29
    ...
```

## Position (Global Positioning System)

  - Latitude
  - Longitude
  - Altitude

```sh
    root@eekmex:/home/eekmex/eekmex/spacecraft# python eekmex.py -d all
    root: eekmex     INFO EekMex, Aerospace Learning Platform
    root: eekmex     INFO Mode Demo
    root: emdemo     INFO Demo
    root: emgps      INFO Global Positioning System
    root: emgps      INFO Gps: 21.1640478895,-101.613045967,1828
    ...
```

## Inertial Measurement Unit

> LSM9DS0 9DOF IMU for full-range motion sensing. This chip combines a 3-axis accelerometer, a 3-axis gyroscope, and a 3-axis magnetometer.

- Roll
- Pitch
- Yaw

```sh
    root@eekmex:/home/eekmex# cd eekmex/eekmex
    root@eekmex:/home/eekmex/eekmex/spacecraft# python eekmex.py -d all
    root: eekmex     INFO EekMex, Aerospace Learning Platform
    root: eekmex     INFO Mode Demo
    root: emdemo     INFO Demo
    root: emimu      INFO Inertial Measurement Unit
    root: emimu      INFO Imu: -153,64,39,
    ...
```