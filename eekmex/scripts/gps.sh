GPSDEVICE=/dev/ttyUSB0
GPSBAUDRATE=4800

if [ -c "$GPSDEVICE" ]; then
    stty -F $GPSDEVICE speed $GPSBAUDRATE
    gpsd -n $GPSDEVICE
    gpxlogger -d -f /tmp/gpslog.gpx
fi

