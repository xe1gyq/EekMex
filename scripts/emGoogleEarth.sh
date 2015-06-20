#!/bin/sh

cp /media/sdcard/eekmexprekml.log scripts/
cd scripts
python kmlge.py
cp eekmex.kml /media/sdcard
cd ..
scp /media/sdcard/eekmex.kml xe1gyq@192.168.1.77:/home/xe1gyq/

# End of File
