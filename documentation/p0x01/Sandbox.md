# SandBox

## Creation

    root@jessie:~# easy_install python_boilerplate_template
    xe1gyq@jessie:~$ paster create -t python_boilerplate eekmex
    Selected and implied templates:
      python-boilerplate-template#python_boilerplate  A buildout/py.test/travis-enabled Python project with support for one or more setuptools-enabled packages.
    
    Variables:
      egg:      eekmex
      package:  eekmex
      project:  eekmex

### Frame

https://github.com/librecube-repos/LC-2102/tree/master/production/mechanical/stl

### Links

- https://pypi.python.org/pypi/python_boilerplate_template
- https://github.com/GomSpace/libcsp
- Link budget calculation Cubesat

## Subsystems, Questions

- Storage Subsystem
  - Means
  - Data amount
  - Free up time
- Communication Subsystems
  - Band, Frequency
  - Transmission timing
  - 

### Inertial Measurement Unit

    edison@ubilinux:~$ su
    Password: 
    root@ubilinux:/home/edison# i2cdetect -y -r 1
    ...
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- 1d -- -- 
    ...
    60: -- -- -- -- -- -- -- -- -- -- -- 6b -- -- -- -- 
    ...
    root@ubilinux:/home/edison# cd eekmex/eekmex
    root@ubilinux:/home/edison/eekmex/eekmex# python eekmex.py -d imu

## 

- pressure transducers
- load cells
- strain
- temperature gauges

- http://edsn.engr.scu.edu/
- http://www.nasa.gov/sites/default/files/atoms/files/edsn_fact_sheet-508-4may2015.pdf
- http://edsn.engr.scu.edu/doc/EDSN_Beacon_Decoding.pdf
- http://icubesat.org/archive/2015-2/icubesat-program-2015/
- https://www.sparkfun.com/tutorials/185