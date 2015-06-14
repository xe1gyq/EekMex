GPSDEVICE=/dev/ttyUSB0
GPSBAUDRATE=38400

if -c "$GPSDEVICE"]; then
    stty -F $GPSDEVICE speed $GPSBAUDRATE
    gpsd -n $GPSDEVICE
    gpxlogger -d -f /tmp/gpslog.gpx
fi

